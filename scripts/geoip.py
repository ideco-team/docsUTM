import logging
from sys import argv, stdout
from ideco_atomic import AtomicPath
from gettext import textdomain
from gettext import gettext as _
from system_backend.geoip_db_status_updater import GeoIpStatusUpdater
from system_lib.geoip import GEOIP_MMDB, UpdateStatus

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stdout))


def main():
    textdomain('ideco-system-geoip-updater')
    AtomicPath(argv[1]).replace(GEOIP_MMDB)
    GeoIpStatusUpdater().set_status(UpdateStatus.UP_TO_DATE, _('GeoIP DB successfully updated.'))
    log.info('GeoIP DB successfully updated.')


if __name__ == '__main__':
    main()
