import logging
from sys import argv, stdout
from gettext import textdomain
from gettext import gettext as _
from ideco_atomic import AtomicPath
from ideco_subprocess import run_process_json
from content_filter_backend.sky_db_status_updater import SkyDBStatusUpdater, UpdateStatus


_CF_DATABASE_DIR = AtomicPath('/var/cache/ideco/content-filter-backend/db')

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(stdout))


def main():
    textdomain('ideco-content-filter-backend')
    output = run_process_json(['ideco-rocks-cf-tool', str(_CF_DATABASE_DIR), 'ingest', argv[1]])
    updater = SkyDBStatusUpdater()
    # Необходимо, тк на фронте все еще будет отображаться "Нет доступных обновлений". Перезагрузка бекенда не поможет.
    updater.set_status(UpdateStatus.UP_TO_DATE, _('No updates required'))
    updater.set_db_timestamp(output['timestamp'])
    log.info('Content filter DB successfully updated.')


if __name__ == '__main__':
    main()
