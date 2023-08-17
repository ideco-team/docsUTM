#!/usr/bin/env python3
import logging
import os
import re
import sys
from argparse import ArgumentParser
from configparser import RawConfigParser
from contextlib import closing
from html.parser import HTMLParser
from http.client import HTTPResponse
from json import dumps as json_dumps
from ssl import create_default_context
from time import sleep
from typing import Callable, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse, urlsplit, urlunsplit
from urllib.request import HTTPErrorProcessor, HTTPRedirectHandler, HTTPSHandler, OpenerDirector, Request, build_opener

log = logging.getLogger(__name__)


class MyHTTPErrorProcessor(HTTPErrorProcessor):
    def http_response(self, request, response):
        return response

    https_response = http_response


class MyHTTPRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise NotImplementedError

    def http_error_302(self, req, fp, code, msg, headers):
        pass

    http_error_301 = http_error_303 = http_error_307 = http_error_302


class MyHTMLParser(HTMLParser):
    def __init__(self, on_redirect_url: Callable[[str], None]):
        self.__on_redirect_url = on_redirect_url
        super().__init__()

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]):
        # Находим тег `meta http-equiv="refresh"` и выдираем URL веб-авторизации.
        # <meta http-equiv="refresh" content="0; url=https://192.168.0.1/web_authd/auth?user_ip=192.168.0.2&origin=https://yandex.ru/">
        if tag != 'meta':
            return
        attr_dict = dict(attrs)
        if attr_dict.get('http-equiv') != 'refresh':
            return
        match = re.match(r'^\s*\d+;\s*url=([^;\s]+)', attr_dict['content'], flags=re.IGNORECASE)
        if match is None:
            return
        self.__on_redirect_url(match.group(1))


def parse_auth(html: str) -> Optional[str]:
    url = None  # type: Optional[str]

    def on_redirect_url(parsed_url: str) -> None:
        nonlocal url
        url = parsed_url

    with closing(MyHTMLParser(on_redirect_url)) as parser:
        parser.feed(html)

    return url


def authorize(opener: OpenerDirector, login: str, password: str) -> None:
    # Обязательно HTTPS, чтобы кто-то недоверенный не перенаправил нас неизвестно куда
    ext_url = 'https://yandex.ru/'
    log.debug('Checking inet: doing "GET %s".', ext_url)
    with opener.open(ext_url) as response:  # type: HTTPResponse
        if response.getcode() != 511:
            return
        auth_html = response.read().decode()
    auth_url_orig = parse_auth(auth_html)
    if auth_url_orig is None:
        raise RuntimeError('Auth url parsing error.')
    log.debug('Got auth url: %r.', auth_url_orig)

    # Обязательно HTTPS, чтобы кто-то недоверенный не перенаправил нас неизвестно куда
    auth_url_normalized = urlparse(auth_url_orig)._replace(scheme='https').geturl()

    log.debug('Going to auth: doing "GET %s".', auth_url_normalized)
    with opener.open(auth_url_normalized) as response:  # type: HTTPResponse
        code = response.getcode()
        if not 300 <= code < 400:
            raise RuntimeError('"GET %s" unexpected code: %d' % (auth_url_normalized, code))
        webauth_url_orig = response.getheader('Location')
    log.debug('Got webauth url: %r.', webauth_url_orig)

    unused_scheme, location, path, query, unused_fragment = urlsplit(webauth_url_orig)
    # Обязательно HTTPS, чтобы не передавать данные в открытом виде
    webauth_url_normalized = urlunsplit(('https', location, path, '', ''))
    webauth_query_params = parse_qs(query)
    user_ip, = webauth_query_params['user_ip']
    webauth_origin, = webauth_query_params['webauth_origin']
    token, = webauth_query_params['token']
    webauth_data = {
        'login': login,
        'password': password,
        'user_ip': user_ip,
        'webauth_origin': webauth_origin,
        'token': token,  # на самом деле никак не проверяется
    }
    webauth_req = Request(
        webauth_url_normalized,
        headers={'Content-Type': 'application/json'},
        data=json_dumps(webauth_data).encode('ascii'),
    )

    webauth_data_for_log = json_dumps({key: value if key != 'password' else '****' for key, value in webauth_data.items()})
    log.debug('Going to webauth: doing "POST %s" with data: %s.', auth_url_normalized, webauth_data_for_log)
    with opener.open(webauth_req) as response:  # type: HTTPResponse
        code = response.getcode()
        if code == 403:
            raise RuntimeError('Wrong login or password')
        if not 100 <= code < 400:
            raise RuntimeError('"POST %s" unexpected code: %d' % (webauth_url_normalized, code))


def authorize_loop(opener: OpenerDirector, login: str, password: str, attempts: int, timeout: int) -> None:
    attempt_counter = 1
    # Именно так, чтобы одним и тем же кодом реализовать случай когда attempts == -1, т.е. число попыток не ограничено.
    while attempts == -1 or attempt_counter <= attempts:
        if attempt_counter > 1:
            sleep(timeout)
        log.debug('Auth attempt #%d.', attempt_counter)
        try:
            authorize(opener, login, password)
        except Exception as ex:
            log.error('Auth attempt #%d failed: %r.', attempt_counter, ex)
        else:
            log.debug('Successfully authorized.')
            return
        attempt_counter += 1
    raise RuntimeError('All authorisation attempts failed')


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode.',
    )
    parser.add_argument(
        '--root-ca',
        default=os.path.expanduser('~/.config/ideco-utm/root_ca.crt'),
        metavar='PATH',
        help='Path to UTM root CA certificate.',
    )
    parser.add_argument(
        '--config',
        default=os.path.expanduser('~/.config/ideco-utm/auth.conf'),
        metavar='PATH',
        help='Path to config with login and password, "-" means stdin.'
    )
    parser.add_argument(
        '--attempts',
        type=int,
        default=10,
        metavar='COUNT',
        help='Number of authorization attempts, "-1" means infinity.',
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=5,
        metavar='SEC',
        help='Timeout between authorization attempts.',
    )
    parser.add_argument(
        '--check-timeout',
        type=int,
        metavar='SEC',
        help='Timeout between internet availability checks.',
    )
    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG if args.debug else logging.INFO)

    context = create_default_context()
    context.load_verify_locations(cafile=args.root_ca)
    opener = build_opener(
        HTTPSHandler(context=context),
        MyHTTPErrorProcessor(),
        MyHTTPRedirectHandler(),
    )

    if args.config == '-':
        config_data = sys.stdin.read()
    else:
        try:
            with open(args.config) as fd:
                config_data = fd.read()
        except FileNotFoundError:
            raise RuntimeError('Config file %r does not exist' % args.config) from None

    config = RawConfigParser()
    config.read_string('[dummysection]\n' + config_data)
    login = config.get('dummysection', 'login')
    password = config.get('dummysection', 'password')

    if args.check_timeout is None:
        authorize_loop(opener, login, password, args.attempts, args.timeout)
        return

    try:
        while True:
            try:
                authorize_loop(opener, login, password, args.attempts, args.timeout)
            except Exception as ex:
                log.error('Error: %r.', ex)
            sleep(args.check_timeout)
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()