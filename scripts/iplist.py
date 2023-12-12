import logging
from sys import argv, stdout
from ideco_atomic import AtomicPath
from tarfile import TarFile
from tempfile import TemporaryDirectory
from alias_backend.iplist import IpListUpdater


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stdout))

_IPLIST_DIR = AtomicPath('/var/cache/ideco/alias-backend/iplist')


def main():
    _IPLIST_DIR.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=_IPLIST_DIR.parent) as tmp_dir:
        tmp_iplist_path = AtomicPath(tmp_dir) / 'iplist_update'
        tmp_iplist_path.mkdir()
        with TarFile.open(argv[1], mode='r:gz', encoding='utf-8') as tar_file:
            tar_file.extractall(tmp_iplist_path)
        tmp_iplist_path.sync_fs()
        # Можно удалить старые каталог и переместить.
        tmp_iplist_path.atomic_swap(_IPLIST_DIR)

    IpListUpdater().update_metadata()
    log.info('IPList DB successfully updated.')


if __name__ == '__main__':
    main()
