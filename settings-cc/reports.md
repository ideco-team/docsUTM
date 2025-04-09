---
description: >-
  В статье представлена информация о логах работы служб.
---

# Отчеты и журналы

## Системный журнал

{% hint style="info" %}
Время хранения логов в разделе **Системный журнал** - три месяца. После этого логи доступны в разделе **Управление сервером -> Терминал**.
{% endhint %}

В разделе доступен просмотр логов Ideco Center и подключенных к центральной консоли Ideco NGFW. Для отображения в таблице логов серверов необходимо в разделе **Управление** \
**сервером -> [Ideco Center](/settings/server-management/central-console.md)** каждого Ideco NGFW включить опцию **Отправлять журналы на Ideco Center**:

![](/.gitbook/assets/cc-logs2.png)

Чтобы просмотреть логи определенной службы, воспользуйтесь строкой поиска или фильтром. Для фильтрации логов по нескольким параметрам нажмите **Добавить фильтр** и выберите соответствующий критерий, значение и оператор в форме:

![](/.gitbook/assets/cc-logs.png)

На вкладке **Журнал серверов** можно выбрать группу серверов для просмотра логов Ideco NGFW из веб-интерфейса Ideco Center:

![](/.gitbook/assets/cc-logs1.png)

{% hint style="info" %}
По кнопке **Скачать CSV** сохраняются те строки логов, которые заданы фильтрацией.
{% endhint %}

<details>

<summary>Список служб, доступных в разделе</summary>

* **Серверы** - `ideco-servers-backend`, `ideco-servers-websocket`;
* **Файрвол** - `ideco-firewall-backend`, `ideco-firewall-rest`;
* **Контент-фильтр** - `ideco-content-filter-backend`;
* **Предотвращение вторжений** - `ideco-suricata-backend`;
* **Объекты** - `ideco-alias-backend`;
* **Сетевые интерфейсы** - `ideco-network-backend`, `ideco-network-nic`;
* **Маршрутизация** - `ideco-routing-backend`, `ideco-routing-rest`;
* **Обратный прокси** - `ideco-reverse-backend`;
* **Защита и управление DNS** - `ideco-dns-backend`, `unbound`, `nsd`, `unbound-anchor`, `unbound-keygen`;
* **DHCP-сервер** - `ideco-dhclient`;
* **NTP-сервер** - `chronyd`;
* **Кластеризация** - `ideco-cluster-backend`;
* **Обновления** - `ideco-sysupdate-backend`;
* **Бэкапы** - `ideco-backup-backend`, `ideco-backup-create`;
* **Лицензия** - `ideco-license-backend`;
* **Syslog** - `ideco-logs-backend`, `ideco-monitor-backend`;
* **Отчеты и журналы** - `ideco-logs-backend`, `ideco-logs-syncer`;
* **Действия администраторов** - `ideco-audit-backend`;
* **Авторизация администраторов** - `ideco-web-backend`;
* **Сертификаты** - `ideco-cert-backend`;
* **Локальное меню** - `ideco-local-menu`;
* **Дополнительно** - `ideco-system-backend`;
* **Сбор анонимной статистики о работе сервера** - `ideco-gatherstat-backend`;
* **Защита от несанкционированного доступа, в т.ч. от брутфорс-атак (brute force - атака полным перебором)** - `fail2ban`;
* **REST API NGFW** - `ideco-rest-api-backend`;
* **Доступ по SSH** - `sshd`.

**Служебное:**

* `clickhouse-server` - сервер базы данных;
* `nginx-control-plane` - cервер управления nginx Ideco;
* `ideco-conndrop` - сервис для очистки невалидных подключений;
* `ideco-etcd-runtime`, `ideco-etcd-permanent` - локальная база данных;
* `ideco-apply-manual-blocklist` - блокировка источников и назначений из файла;
* `ideco-vk-cloud-license` - управление лицензиями в облачной среде;
* `ideco-check-sums` - проверка целостности файлов;
* `ideco-policy-backend` - проверка прав пользователей на перезапуск служб systemd;
* `ideco-system-swap` - управление SWAP-разделами;
* `prometheus`, `prometheus-node-exporter` - сбор метрик и статистики.

</details>

## Действия администраторов

Ideco Center логирует действия администраторов, которые вносят изменения в конфигурацию Ideco Center из веб-интерфейса, локального меню и терминала.

![](/.gitbook/assets/cc-admins.png)

## Syslog

Модуль позволяет отправлять все системные сообщения (syslog) с группы серверов Ideco NGFW в сторонние коллекторы (Syslog Collector) или в SIEM-системы.

Чтобы настроить пересылку системных сообщений, перейдите в раздел **Отчеты и журналы -> Syslog** и выполните действия:

![](/.gitbook/assets/cc-syslog.png)

1\. Выберите группу серверов NGFW, журналы с которых будут передаваться на Syslog Server.

{% hint style="info" %}

Опция **Направлять журналы Ideco Center в Syslog Server** позволяет отправлять журналы, генерируемые самой Ideco CC, на Syslog Server.

{% endhint %}

2\. Укажите IP-адрес сервера-коллектора (любой локальный или публичный IP-адрес).

3\. В поле **Порт** укажите порт, настроенный на сервере-коллекторе (в диапазоне от 1 до 65535).

4\. Выберите протокол для передачи системных логов: TCP или UDP.

5\. Выберите формат, в котором будут передаваться системные сообщения: Syslog или CEF.

6\. Нажмите **Сохранить** и включите опцию Syslog.

Примеры расшифровки передаваемых логов представлены в [статье](/settings/reports/syslog.md#rasshifrovka-peredavaemykh-logov).