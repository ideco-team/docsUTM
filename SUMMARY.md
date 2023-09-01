# Table of contents

* [Об Ideco UTM VPP](README.md)

## Общая информация <a href="#general" id="general"></a>

* [Лицензирование](general/license.md)
* [Системные требования и источники обновления данных](general/data-update-source-utm-vpp.md)
* [Техническая поддержка](general/technical-support.md)

## Первоначальная настройка <a href="#initial-setup" id="initial-setup"></a>

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
  * [Настройка авторизации пользователей](advanced-setting/authorization/README.md)
    * [Авторизация через журнал безопасности Active Directory](advanced-setting/authorization/active-directory.md)
    * [IP и MAC авторизация](advanced-setting/authorization/ip-mac-authorization.md)
    * [Авторизация по подсетям](advanced-setting/authorization/authorization-by-subnet.md)
  * [Настройка интеграции с Active Directory](advanced-setting/users/active-directory.md)
  * [Настройка интеграции с ALD Pro](advanced-setting/users/ald.md)
* [Блокировка трафика](advanced-setting/traffic-blocking/traffic-blocking.md)
  * [Настройка файрвола](advanced-setting/traffic-blocking/firewall.md)
  * [Настройка службы предотвращения вторжений](advanced-setting/traffic-blocking/ips.md)
* [Управление сервером и его настройка](advanced-setting/server-management/server-management.md)
  * [Сертификаты](advanced-setting/server-management/certificates.md)
  * [Терминал](advanced-setting/server-management/terminal.md)
  * [Привязка лицензий к серверу на MY.IDECO](advanced-setting/server-management/binding-license.md)
* [Журналирование](advanced-setting/logging/monitoring-reporting-logging.md)
  * [Логирование](advanced-setting/logging/log.md)
  * [Cобытия и отчеты](advanced-setting/logging/events-reports.md)
* [Мониторинг](advanced-setting/monitoring/monitor.md)
  * [Информация об активных сессиях пользователей](advanced-setting/monitoring/authorization-info.md)
  * [Информация о загруженности системы](advanced-setting/monitoring/workload-schedule.md)
  * [Подключение сторонних сервисов для мониторинга](advanced-setting/monitoring/connection-external-services.md)
* [Настройка клиентских машин](advanced-setting/setup-client/setup-on-client-machines.md)
  * [Настройка соединения c UTM VPP](advanced-setting/setup-client/setup-connection.md) 

## Диагностика проблем <a href="problem-diagnosis" id="problem-diagnosis"></a>
* [Проблемы при авторизации пользователей](problem-diagnosis/authorization.md)
* [Примеры диагностики через терминал](problem-diagnosis/diagnose-console.md)
## changelog

* [Ideco UTM VPP](changelog/vpp/README.md)
* [Ideco UTM](changelog/ideco-utm/README.md)
  * [Версия Ideco UTM 15.X](changelog/ideco-utm/versiya-ideco-utm-15.x.md)
  * [Версия Ideco UTM 14.X](changelog/ideco-utm/versiya-ideco-utm-14.x.md)
  * [Версия Ideco UTM 13.X](changelog/ideco-utm/versiya-ideco-utm-13.x.md)
  * [Версия Ideco UTM 12.X](changelog/ideco-utm/versiya-ideco-utm-12.x.md)
  * [Версия Ideco UTM 11.X](changelog/ideco-utm/versiya-ideco-utm-11.x.md)
  * [Версия Ideco UTM 10.X](changelog/ideco-utm/version-10.x.md)
  * [Версия Ideco UTM 9.X](changelog/ideco-utm/version-9.x.md)
  * [Версия Ideco UTM 8.X](changelog/ideco-utm/version-8.x.md)
  * [Версия Ideco UTM 7.Х.Х](changelog/ideco-utm/version-7.x.x/README.md)
    * [Версия Ideco UTM 7.9.X](changelog/ideco-utm/version-7.x.x/version-7.9.x.md)
    * [Версия Ideco UTM 7.8.X](changelog/ideco-utm/version-7.x.x/version-7.8.x.md)
    * [Версия Ideco UTM 7.7.X](changelog/ideco-utm/version-7.x.x/version-7.7.x.md)
    * [Версия Ideco UTM 7.6.Х](changelog/ideco-utm/version-7.x.x/version-7.6.x.md)
    * [Версия Ideco UTM 7.5.Х](changelog/ideco-utm/version-7.x.x/version-7.5.x.md)
    * [Версия Ideco UTM 7.4.X](changelog/ideco-utm/version-7.x.x/version-7.4.x.md)
* [ФСТЭК Ideco UTM](changelog/fstek/README.md)
  * [ФСТЭК Ideco UTM 14.Х](changelog/fstek/fstek-ideco-utm-14.x.md)
  * [ФСТЭК Ideco UTM 11.Х](changelog/fstek/fstek-ideco-utm-11.x.md)
* [Ideco Center](changelog/cc/README.md)
  * [Версия Ideco Center 14.Х](changelog/cc/version-14.x.md)
  * [Версия Ideco Center 13.Х](changelog/cc/version-13.x.md)
