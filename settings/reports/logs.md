---
description: В разделе представлена информация о логах работы служб.
---

# Журнал событий

{% hint style="info" %}
Время хранения логов в разделе **Журналы** - три месяца. После этого логи доступны в разделе **Управление сервером -> Терминал**.
{% endhint %}

Для просмотра логов определенной службы воспользуйтесь строкой поиска или фильтром. 
Для фильтрации логов по нескольким параметрам нажмите **Добавить фильтр** и выберите соответствующий критерий, значение и оператор в форме.

Фильтрация по нескольким критериям:

![](/.gitbook/assets/logs.png)

{% hint style="info" %}
По кнопке **Скачать CSV** сохраняются те строки логов, которые заданны фильтрацией.
{% endhint %}

<details>

<summary>Список служб, доступных в разделе</summary>

* **Файрвол** - ideco-firewall-backend, ideco-nflog;
* **Контроль приложений** - ideco-app-backend, ideco-app-control@Leth<номер локального интерфейса>;
* **Контент-фильтр** - ideco-content-filter-backend;
* **Ограничение скорости** - ideco-shaper-backend;
* **Антивирусы веб-трафика** - ideco-av-backend, ideco-clamd;
* **Предотвращение вторжений** - ideco-suricata-backend, ideco-suricata, ideco-suricata-event-syncer, ideco-suricata-event-to-syslog;
* **Объекты** - ideco-alias-backend;
* **Квоты** - ideco-quotas-backend, systemd-quotacheck;
* **Сетевые интерфейсы** - ideco-network-backend, ideco-network-nic;
* **Балансировка и резервирование**, **Маршрутизация** - ideco-routing-backend;
* **BGP**, **OSPF** - ideco-routing-backend;
* **Прокси** - ideco-proxy-backend, squid;
* **Обратный прокси** - ideco-reverse-backend;
* **DNS** - ideco-dns-backend, unbound;
* **DDNS** - ideco-dns-backend;
* **DHCP** - ideco-dnsmasq;
* **IPsec** - ideco-ipsec-backend, strongswan;
* **Центральная консоль** - ideco-central-console-backend;
* **Кластеризация** - ideco-cluster-backend, ideco-cluster-backup-pusher;
* **Автоматическое обновление** - ideco-sysupdate-backend;
* **Резервное копирование** - ideco-backup-backend, ideco-backup-create, ideco-backup-restore, ideco-backup-rotate;
* **Лицензия** - ideco-license-backend;
* **VPN-подключения** - ideco-accel-l2tp, ideco-accel-pptp, ideco-accel-sstp, ideco-vpn-servers-backend, ideco-vpn-authd;
* **Авторизация** - ideco-auth-backend;
* **Двухфакторная аутентификация** - ideco-web-authd;
* **Active Directory** - ideco-ad-backend, ideco-ad-log-collector@<имя домена>;
* **ALD Pro** - ideco-ald-rest, ideco-ald-backend;
* **Ideco Client** - ideco-agent-backend, ideco-agent-websocket;
* **Syslog** - ideco-monitor-backend;
* **Обнаружение устройств** - ideco-netscan-backend;
* **Web Application Firewall** - ideco-waf-backend, ideco-waf-event-syncer;
* **IGMP Proxy** - igmpproxy.

</details>

## Защита от брутфорс-атак
{% hint style="info" %}
Защита от брутфорс-атак (brute force - атака полным перебором) работает только для NGFW.
{% endhint %}

После 6 неудачных попыток ввода пароля в течение 15 минут IP-адрес подбирающего блокируется на 45 минут.

Логи службы `fail2ban` можно увидеть:

* В веб-интерфейсе в разделе **Отчеты и журналы -> Журнал Событий**, задав фильтр `fail2ban`.
* В разделе **Управление сервером -> Терминал**, введя команду `journalctl -u fail2ban`.

Для разблокировки через терминал используйте команды:

* `fail2ban-client unban --all` - команда используется для снятия всех блокировок;
* `fail2ban-client unban <IP-адрес>` - команда используется для разблокировки конкретного IP-адреса, указав нужный IP-адрес в качестве аргумента.

Также можно сбросить блокировки из локального меню шлюза, выбрав опцию **Сбросить блокировки по IP**:

![](/.gitbook/assets/bruteforce.png)
