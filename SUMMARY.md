# Table of contents

* [Об Ideco NGFW VPP](README.md)

## Общая информация <a href="#general" id="general"></a>

* [Виды и состав лицензий](general/license.md)
* [Системные требования и источники обновления данных](general/data-update-source-utm-vpp.md)
* [Техническая поддержка](general/technical-support.md)

## Быстрый старт <a href="#initial-setup" id="initial-setup"></a>

* [Рекомендации при первоначальной настройке](initial-setup/tips-for-initial-setup.md)
* [MY.IDECO](initial-setup/my-ideco.md)
* [Подготовка к установке на устройство](initial-setup/preparation-install.md)
  * [Настройка гипервизора](initial-setup/setup-hypervisor.md)
  * [Подготовка загрузочного диска](initial-setup/preparation-boot-disk.md)
* [Установка](initial-setup/setup.md)
* [Первоначальная настройка](initial-setup/initial-setup-web.md)

## Расширенная настройка <a href="#advanced-setting" id="advanced-setting"></a>

* [Настройка пользователей и интеграция с контроллерами домена](advanced-setting/users/README.md)
  * [Дерево пользователей и управление учетными записями](advanced-setting/users/user-tree.md)
  * [Настройка авторизации пользователей](advanced-setting/users/authorization/README.md)
    * [Авторизация через журнал безопасности Active Directory](advanced-setting/users/authorization/ad-auth-logs.md)
    * [IP и MAC авторизация](advanced-setting/users/authorization/ip-mac-authorization.md)
    * [Авторизация по подсетям](advanced-setting/users/authorization/authorization-by-subnet.md)
  * [Настройка интеграции с Active Directory](advanced-setting/users/active-directory.md)
  * [Настройка интеграции с ALD Pro](advanced-setting/users/ald.md)
* [Управление трафиком](advanced-setting/control-blocking/README.md)
  * [Профили безопасности](advanced-setting/control-blocking/security-profiles/README.MD)
    * [Профили TLS/SSL-инспекций](advanced-setting/control-blocking/security-profiles/tls-inspection-security-profiles.md)
    * [Профили контроля приложений](advanced-setting/control-blocking/security-profiles/application-control-profiles.md)
    * [Профили контент-фильтра](advanced-setting/control-blocking/security-profiles/content-filter-profiles.md)
  * [Файрвол](advanced-setting/control-blocking/firewall.md)
  * [Предотвращения вторжений](advanced-setting/control-blocking/ips.md)
  * [Маршрутизация](advanced-setting/control-blocking/routing.md)
  * [BGP](advanced-setting/control-blocking/bgp.md)
* [Управление сервером и его настройка](advanced-setting/server-management/README.md)
  * [Управление сетевыми интерфейсами](advanced-setting/server-management/server-configuration-management.md)
  * [Сертификаты](advanced-setting/server-management/certificates.md)
  * [Загрузка своего SSL-сертификата](advanced-setting/server-management/upload-own-ssl.md)
  * [Терминал](advanced-setting/server-management/terminal.md)
  * [Управление лицензиями](advanced-setting/server-management/binding-license.md)
  * [Управление администраторами](advanced-setting/server-management/management-admins.md)
  * [Настройка доступа к серверу по SSH](advanced-setting/server-management/SSH-access.md)
  * [Объекты: создание, редактирование и удаление](advanced-setting/server-management/aliases.md)
  * [Резервное копирование](advanced-setting/server-management/backup.md)
  * [Автоматическое обновление](advanced-setting/server-management/server-update.md)
  * [NTP-сервер: принцип работы и настройка](advanced-setting/server-management/ntp.md)
  * [DNS](advanced-setting/server-management/dns.md)
  * [Настройка часового пояса и языка](advanced-setting/server-management/language-time-management.md)
* [Журналирование и мониторинг](advanced-setting/logging-monitoring/README.md)
  * [Панель мониторинга](advanced-setting/logging-monitoring/monitor-panel.md)
  * [Логирование: логи работы модулей и их отправка на удаленный сервера](advanced-setting/logging-monitoring/log.md)
  * [Действия администраторов](advanced-setting/logging-monitoring/admins-actions.md)
  * [Статистика и журнал событий безопасности](advanced-setting/logging-monitoring/security-events.md)
  * [История авторизации пользователей](advanced-setting/logging-monitoring/authorization-log.md)
  * [Отчеты: создание шаблонов и отправка на почту](advanced-setting/logging-monitoring/report-designer.md)
  * [Информация об активных сессиях пользователей](advanced-setting/logging-monitoring/authorization-info.md)
  * [Информация о загруженности системы](advanced-setting/logging-monitoring/workload-schedule.md)
  * [Telegram, Ideco Monitoring Bot и Zabbix агент](advanced-setting/logging-monitoring/connection-external-services.md)
* [Настройка клиентских машин](advanced-setting/setup-client/README.md)
  * [Настройка соединения c NGFW VPP](advanced-setting/setup-client/setup-connection.md)
  * [Настройка клиентских машин для фильтрации трафика](advanced-setting/setup-client/sertificate-setup.md)

## Диагностика проблем <a href="#problem-diagnosis" id="problem-diagnosis"></a>

* [Проблемы при авторизации пользователей](problem-diagnosis/authorization.md)
* [Восстановление пароля администратора](problem-diagnosis/recovery-password-admin.md)
* [Примеры диагностики через терминал](problem-diagnosis/diagnose-console.md)

## changelog

* [Ideco NGFW VPP 17.X](changelog/vpp/README.md)
* [ФСТЭК Ideco UTM 16.X](changelog/fstek/README.md)
* [Ideco Center 16.Х](changelog/cc/README.md)
