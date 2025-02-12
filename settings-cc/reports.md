# Отчеты и журналы

## Системный журнал

{% hint style="info" %}
Время хранения логов в разделе **Журналы** - три месяца. После этого логи доступны в разделе **Управление сервером -> Терминал**.
{% endhint %}

В разделе доступен просмотр логов Ideco Center и подключенных к центральной консоли Ideco NGFW. Для отображения в таблице логов серверов необходимо в разделе **Управление сервером -> [Ideco Center](/settings/server-management/central-console.md)** каждого Ideco NGFW включить опцию **Отправлять журналы на Ideco Center**:

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
* **Файрвол** - `ideco-firewall-backend`;
* **Контроль приложений** - `ideco-app-backend`;
* **Контент-фильтр** - `ideco-content-filter-backend`;
* **Предотвращение вторжений** - `ideco-suricata-event-syncer`, `ideco-suricata-backend`;
* **Объекты** - `ideco-alias-backend`;
* **Сетевые интерфейсы** - `ideco-network-backend`, `ideco-network-nic`;
* **Маршрутизация** - `ideco-routing-backend`, `ideco-routing-rest`;
* **Обратный прокси** - `ideco-reverse-backend`;
* **DNS** - `ideco-dns-backend`, `unbound`, `nsd`, `unbound-anchor`, `unbound-keygen`;
* **NTP** - `chronyd`;
* **Кластеризация** - `ideco-cluster-backend`;
* **Обновления** - `ideco-sysupdate-backend`;
* **Бэкапы** - `ideco-backup-backend`;
* **Лицензия** - `ideco-license-backend`;
* **Syslog** - `ideco-logs-backend`;
* **Отчеты и журналы** - `ideco-logs-backend`, `ideco-logs-syncer`;
* **Действия администраторов** - `ideco-audit-backend`;
* **Сертификаты** - `ideco-cert-backend`;
* **Сбор анонимной статистики о работе сервера** - `ideco-gatherstat-backend`;
* **Локальное меню** - `ideco-local-menu`;
* **Дополнительно (язык, часовой пояс, включение особых режимов работы)** - `ideco-system-backend`;
* **Защита от повторяющихся зловредных или подозрительных действия, в т.ч. от брутфорс-атак (brute force - атака полным перебором)** - `fail2ban`;
* **Доступ по SSH** - `sshd`.

**Служебное:**

* `clickhouse-server` - сервер базы данных;
* `ideco-etcd-runtime`, `ideco-etcd-permanent` - локальная база данных;
* `prometheus`, `prometheus-node-exporter` - сбор метрик и статистики.

</details>

## Действия администраторов

Ideco Center логирует действия администраторов, которые вносят изменения в конфигурацию Ideco Center из веб-интерфейса, локального меню и терминала.

![](/.gitbook/assets/cc-admins.png)
