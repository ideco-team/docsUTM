import os
import json
import logging
from typing import Any
from locale import getlocale
from sys import argv, stdout
from ideco_subprocess import run_process
from suricata_backend.storage.rulesets import RuleSetsUpdater
from tarfile import TarFile
from ideco_atomic import AtomicPath

_METAINFO_JSON = 'metainfo.json'
_RULES_FILE_PATH = AtomicPath('/var/cache/ideco/suricata-backend/rules.tar.gz')
_DISABLED_BY_DEFAULT: set[str] = {
    # Данные группы должны быть ОТКЛЮЧЕНЫ как только они ПОЯВИЛИСЬ в базе.
    'ideco-geoip-region-east-europa',
    'ideco-geoip-region-sea',
    "ideco-geoip-region-africa",
    'ideco-geoip-region-south-america',
    'ideco-geoip-remote',
}

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stdout))


def main():
    AtomicPath(argv[1]).replace(_RULES_FILE_PATH)
    _RULES_FILE_PATH.chmod(0o444)
    new_rules_idents: list[str] = []
    translations: dict[str, dict[str, str]] = {}
    with _RULES_FILE_PATH.open('rb') as fileobj:
        with TarFile.open(mode='r:gz', fileobj=fileobj, encoding='utf-8') as tar_file:
            for tar_info in tar_file:
                if not tar_info.isreg():  # пропускаем все что не файл
                    continue
                file_name, file_ext = os.path.splitext(os.path.basename(tar_info.name))
                if file_ext == '.rules':
                    new_rules_idents.append(file_name)
                elif os.path.basename(tar_info.name) == _METAINFO_JSON:
                    file_obj = tar_file.extractfile(tar_info)
                    assert file_obj is not None  # we checked the type earlier
                    last_update = json.load(file_obj)['last_update']
                elif os.path.basename(tar_info.name) == 'translations.json':
                    translations = json.load(tar_file.extractfile(tar_info))

    new_rules_idents.sort()
    lang, unused_encoding = getlocale()
    langpack: dict[str, str] = translations.get(lang, translations['en_US'])
    def mutator(old_rulesets: dict[str, Any]) -> dict[str, Any]:
        return {
            ident: [
                langpack.get(ident, ident),
                old_rulesets.get(ident, ['unused-string', ident not in _DISABLED_BY_DEFAULT])[1],
            ]
            for ident in new_rules_idents
        }

    RuleSetsUpdater().update_with_mutator(mutator)
    log.debug('Collection updated.')
    run_process(['systemctl', 'restart', 'ideco-suricata-backend.service'])
    log.debug('Backend restart.')
    log.info('Rules set successfully updated.')


if __name__ == '__main__':
    main()
