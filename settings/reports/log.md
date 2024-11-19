---
description: В разделе представлена информация о логах работы служб.
---
# Системный журнал

{% hint style="info" %}
Время хранения логов в разделе **Системный журнал** - три месяца. После этого логи доступны в разделе **Управление сервером -> Терминал**.
{% endhint %}

Для просмотра логов определенной службы воспользуйтесь строкой поиска или фильтром. Для фильтрации логов по нескольким критериям нажмите **Добавить фильтр** и выберите соответствующий критерий, значение и оператор в форме.

Пример фильтрации по нескольким критериям:

![](/.gitbook/assets/log1.png)

<details>

<summary>Список служб, доступных в разделе</summary>

* **Авторизация** - `ideco-auth-backend`;
* **Авторизация администраторов** - `ideco-web-backend`;
* **Бэкапы** - `ideco-backup-backend`, `ideco-backup-create`, `ideco-backup-restore`, `ideco-backup-rotate`;
* **Действия администраторов** - `ideco-audit-backend`;
* **Дополнительно: язык, часовой пояс, включение особых режимов работы** - `ideco-system-backend`;
* **Доступ по SSH** - `sshd`;
* **Защита от повторяющихся подозрительных действий, в т.ч. от брутфорс-атак (brute force - атака полным перебором)** - `fail2ban`;
* **Кластеризация** - `ideco-cluster-backend`;
* **Контент-фильтр** - `ideco-content-filter-backend`, `ideco-content-filter-backend-vpp`;
* **Контроль приложений** - `ideco-app-backend-vpp`, `ideco-app-stats`;
* **Лицензия** - `ideco-license-backend`;
* **Локальное меню** - `ideco-local-menu`;
* **Маршрутизация** - `ideco-routing-backend`, `ideco-routing-backend-vpp`, `ideco-routing-rest`;
* **Обнаружение устройств** - `ideco-netscan-backend`;
* **Обновления** - `ideco-sysupdate-backend`;
* **Объекты** - `ideco-alias-backend`;
* **Ограничение скорости** - `ideco-shaper-backend-vpp`;
* **Отправка оповещений через телеграм-бота** - `ideco-mir-alerts`;
* **Отчеты и журналы** - `ideco-logs-backend`, `ideco-logs-syncer`, `ideco-reports-backend`;
* **Предотвращение вторжений** - `ideco-suricata-backend`, `ideco-suricata-event-syncer`, `ideco-suricata-profiles-syncer-backend`;
* **Сбор анонимной статистики о работе сервера** - `ideco-gatherstat-backend`;
* **Сертификаты** - `ideco-cert-backend`;
* **Сетевые интерфейсы** - `ideco-network-backend`, `ideco-vpp-backend`, `ideco-vpp-nic-syncer`;
* **Учетные записи** - `ideco-user-backend`;
* **Файрвол** - `ideco-firewall-backend`, `ideco-firewall-rest`, `ideco-cfw-backend`, `ideco-cfw-rest`;
* **Active Directory** - `ideco-ad-backend`;
* **ALD Pro** - `ideco-ald-rest`, `ideco-ald-backend`;
* **DNS** - `ideco-dns-backend`, `nsd`, `unbound`, `unbound-anchor`, `unbound-keygen`;
* **NTP-сервер** - `chronyd`;
* **REST API NGFW** - `ideco-rest-api-backend`;
* **Syslog** - `ideco-monitor-backend`.

**Служебное:**

* `clickhouse-server` - сервер базы данных;
* `ideco-apply-manual-blocklist` - блокировка источников и назначений из файла;
* `ideco-conndrop` - сервис для очистки невалидных подключений;
* `ideco-etcd-permanent`, `ideco-etcd-runtime` - локальная база данных;
* `ideco-vpp` - процесс обработки трафика;
* `ideco-vpp-prometheus-exporter`, `prometheus`, `prometheus-node-exporter` - сбор метрик и статистики.

</details>