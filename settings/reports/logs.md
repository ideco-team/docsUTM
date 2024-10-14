---
description: В разделе представлена информация о логах работы служб.
---

# Системный журнал

{% hint style="info" %}
Время хранения логов в разделе **Журналы** - три месяца. После этого логи доступны в разделе **Управление сервером -> Терминал**.
{% endhint %}

Для просмотра логов определенной службы воспользуйтесь строкой поиска или фильтром. 
Для фильтрации логов по нескольким параметрам нажмите **Добавить фильтр** и выберите соответствующий критерий, значение и оператор в форме.

Фильтрация по нескольким критериям:

![](/.gitbook/assets/logs.png)

{% hint style="info" %}
По кнопке **Скачать CSV** сохраняются те строки логов, которые заданы фильтрацией.
{% endhint %}

<details>

<summary>Список служб, доступных в разделе</summary>

* **Учетные записи** - `ideco-user-backend`;
* **Личный кабинет пользователя** - `ideco-user-cabinet-backend`;
* **Файрвол** - `ideco-firewall-backend`;
* **Контроль приложений** - `ideco-app-backend`;
* **Контент-фильтр** - `ideco-content-filter-backend`;
* **Ограничение скорости** - `ideco-shaper-backend`;
* **Антивирусы веб-трафика** - `ideco-av-backend`;
* **Предотвращение вторжений** - `ideco-suricata-event-syncer`, `ideco-suricata-backend`;
* **Объекты** - `ideco-alias-backend`;
* **Квоты** - `ideco-quotas-backend`;
* **Сетевые интерфейсы** - `ideco-network-backend`, `ideco-network-nic`;
* **Маршрутизация** - `ideco-routing-backend`, `ideco-routing-rest`;
* **Прокси** - `ideco-proxy-backend`, `squid`;
* **Обратный прокси** - `ideco-reverse-backend`;
* **DNS** - `ideco-dns-backend`, `unbound`, `nsd`, `unbound-anchor`, `unbound-keygen`;
* **DDNS** - `ideco-dns-backend`;
* **DHCP** - `ideco-dhclient`, `ideco-dhcp-server-backend`;
* **NTP** - `chronyd`;
* **IPsec** - `ideco-ipsec-backend`;
* **Центральная консоль** - `ideco-central-console-backend`;
* **VCE** - `ideco-vce-backend`;
* **Кластеризация** - `ideco-cluster-backend`;
* **Обновления** - `ideco-sysupdate-backend`;
* **Бэкапы** - `ideco-backup-backend`;
* **Лицензия** - `ideco-license-backend`;
* **VPN-подключения** - `ideco-vpn-authd`, `ideco-vpn-dhcp-backend`, `ideco-vpn-dhcp-server`, `ideco-vpn-servers-backend`, `ideco-vpn-netns`, `ideco-vpn-sessions-sync`;
* **Авторизация** - `ideco-auth-backend`;
* **Веб-аутентификация, Двухфакторная аутентификация** - `ideco-web-authd`;
* **Active Directory** - `ideco-ad-backend`;
* **ALD Pro** - `ideco-ald-rest`, `ideco-ald-backend`;
* **Ideco Client** - `ideco-agent-websocket`, `ideco-agent-backend`, `ideco-app-stats`;
* **Syslog** - `ideco-monitor-backend`;
* **Отчеты и журналы** - `ideco-logs-backend`, `ideco-reports-backend`, `ideco-logs-syncer`;
* **Действия администраторов** - `ideco-audit-backend`;
* **Обнаружение устройств** - `ideco-netscan-backend`;
* **Web Application Firewall** - `ideco-waf-backend`, `ideco-waf-event-syncer`;
* **IGMP Proxy** - `ideco-igmpproxy-backend`;
* **Сертификаты** - `ideco-cert-backend`;
* **Почтовый релей** - `ideco-mail-backend`;
* **Сбор анонимной статистики о работе сервера** - `ideco-gatherstat-backend`;
* **Локальное меню** - `ideco-local-menu`;
* **Отправка оповещений через телеграм-бота** - `ideco-mir-alerts`; 
* **Проверка скорости** - `ideco-speedtest`;
* **Дополнительно (язык, часовой пояс, включение особых режимов работы)** - `ideco-system-backend`;
* **Защита от повторяющихся зловредных или подозрительных действия, в т.ч. от брутфорс-атак (brute force - атака полным перебором)** - `fail2ban`;
* **Доступ по SSH** - `sshd`.

**Служебное:**

* `clickhouse-server` - сервер базы данных;
* `ideco-etcd-runtime`, `ideco-etcd-permanent` - локальная база данных;
* `prometheus`, `prometheus-node-exporter` - сбор метрик и статистики.

</details>

## Защита от брутфорс-атак
{% hint style="info" %} 
Защита от брутфорс-атак (brute force - атака полным перебором) работает только для NGFW. 
{% endhint %}

После 6 неудачных попыток ввода пароля в течение 15 минут IP-адрес подбирающего блокируется на 45 минут.

Логи службы `fail2ban` можно увидеть:

* В веб-интерфейсе в разделе **Отчеты и журналы -> Системный журнал**, задав фильтр `fail2ban`.
* В разделе **Управление сервером -> Терминал**, введя команду `journalctl -u fail2ban`.

Сбросить блокировки можно из локального меню шлюза: **Сбросить блокировки по IP**.

![](/.gitbook/assets/local-menu2.png)
