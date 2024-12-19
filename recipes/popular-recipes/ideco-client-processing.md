# Как Ideco Client обрабатывает запросы с редиректом на сервер Ideco NGFW

**Ideco Client** может обрабатывать запросы с перенаправлением (код ответа 302). Получив ответ от сервера, **Ideco Client** выполняет шаги для подключения к **Ideco NGFW**:

1. Отправляет запрос на адрес https://host:14765/connect.

2. Если сервер отвечает статусом 302 с редиректом, **Ideco Client** использует информацию из этого ответа для установления соединения.

3. **Ideco Client** подключается к NGFW, используя имя сервера или IP-адрес, указанный в поле Location.

{% hint style="warning" %}
**Важно**:

* Адрес обязательно должен включать порт `14765`;

* В заголовке Location в ответе 302 должен быть указан полный URL-адрес, из которого будет извлечено только имя сервера или IP-адрес;

* Полученное имя сервера или IP-адрес используются для создания адреса в формате `wss://host_from_location:14765/connect`, к которому будет подключаться **Ideco Client**;

* Если ответа со статусом 302 от адреса `https://host:14765/connect` нет, то **Ideco Client** подключится к NGFW по адресу `wss://host:14765/connect`.
{% endhint %}

Пример правильного редиректа, полученный с помощью утилиты **сurl**:

1\. **Запрос**: `curl -il https://host.dev:14765/connect`.

2\. **Ответ**:

```
HTTP/1.1 302 Found
Server: SERVERNAME
Date: Fri, 15 Nov 2024 04:22:46 GMT
Content-Length: 0
Connection: keep-alive
Keep-Alive: timeout=15
Location: https://ngfw-host.dev/
cache-control: no-cache
```

Из заголовка `Location: https://ngfw-host.dev/` будет извлечен новый хост `ngfw-host.dev`, и **Ideco Client** будет подключаться к NGFW по адресу `wss://ngfw-host.dev:14765/connect`.

3\. Если при попытке доступа к URL-адресу `https://host.dev:14765/connect` не будет получен ответ с кодом 302, то **Ideco Client** подключится к NGFW по адресу `wss://host.dev:14765/connect`.