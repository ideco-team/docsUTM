# Терминал

{% hint style="warning" %}
Используйте терминал только для диагностики. Воздержитесь от команд, изменяющих файлы. Система рассчитана на настройку только через веб-интерфейс. Компания "Айдеко" не несет ответственности за негативные последствия работы с Ideco NGFW из терминала. Техническая поддержка вправе отказать в обслуживании, если окажется, что работа системы была нарушена из-за действий пользователя в терминале.
{% endhint %}

## Основные команды

* **Утилиты сетевой диагностики:** `ping`, `host`, `nslookup`, `tracepath`, `tcpdump`, `arping`, `ss` (аналог `netstat`);
* **Файловый редактор:** `nano`;
* **Просмотр логов:** `journalctl -u <название службы>` (например, `journalctl -u ideco-routing-backend`);
* **Проверка скорости интернета:** `speedtest-cli`;
* **Просмотр ARP-таблицы**: `ip neigh show`.
* **Просмотр конфигурации FRR**: `vtysh`

## Таблица служб

<table><thead><tr><th width="329">Раздел</th><th>Имя службы</th></tr></thead><tbody><tr><td>Файрвол</td><td>ideco-nflog;ideco-firewall-backend</td></tr><tr><td>Профили контроля приложений</td><td>ideco-app-backend; ideco-app-control-nfq</td></tr><tr><td>Контент-фильтр</td><td>ideco-content-filter-backend</td></tr><tr><td>Ограничение скорости</td><td>ideco-shaper-backend</td></tr><tr><td>Антивирусы веб-трафика</td><td>ideco-av-backend;</td></tr><tr><td>Предотвращение вторжений</td><td>ideco-suricata-backend; ideco-suricata; ideco-suricata-event-syncer; ideco-suricata-profiles-syncer;</td></tr><tr><td>Объекты</td><td>ideco-alias-backend</td></tr><tr><td>Квоты</td><td>ideco-quotas-backend; systemd-quotacheck</td></tr><tr><td>Сетевые интерфейсы</td><td>ideco-network-backend; ideco-network-nic</td></tr><tr><td>Балансировка и резервирование, Маршрутизация</td><td>ideco-routing-backend</td></tr><tr><td>BGP, OSPF</td><td>ideco-routing-backend</td></tr><tr><td>Прокси</td><td>ideco-proxy-backend; squid</td></tr><tr><td>Обратный прокси</td><td>ideco-reverse-backend</td></tr><tr><td>DNS</td><td>ideco-dns-backend; unbound</td></tr><tr><td>DDNS</td><td>ideco-dns-backend</td></tr><tr><td>DHCP</td><td>ideco-dnsmasq</td></tr><tr><td>IPsec</td><td>ideco-ipsec-backend; strongswan</td></tr><tr><td>Центральная консоль</td><td>ideco-central-console-backend</td></tr><tr><td>Кластеризация</td><td>ideco-cluster-backend; ideco-cluster-backup-pusher</td></tr><tr><td>Автоматическое обновление</td><td>ideco-sysupdate-backend</td></tr><tr><td>Бэкапы</td><td>ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate</td></tr><tr><td>Лицензия</td><td>ideco-license-backend</td></tr><tr><td>VPN-подключения</td><td>ideco-accel-l2tp; ideco-accel-pptp; ideco-accel-sstp; ideco-vpn-servers-backend; ideco-vpn-authd</td></tr><tr><td>Авторизация</td><td>ideco-auth-backend</td></tr><tr><td>Веб-аутентификация, Двухфакторная аутентификация</td><td>ideco-web-authd</td></tr><tr><td>Active Directory</td><td>ideco-ad-backend; ideco-ad-log-collector@&#x3C;имя домена></td></tr><tr><td>ALD Pro</td><td>ideco-ald-rest; ideco-ald-backend</td></tr><tr><td>Ideco Client</td><td>ideco-agent-backend; ideco-agent-websocket</td></tr><tr><td>Syslog</td><td>ideco-monitor-backend</td></tr><tr><td>Обнаружение устройств</td><td>ideco-netscan-backend</td></tr><tr><td>Web Application Firewall</td><td>ideco-waf-backend; ideco-waf-event-syncer</td></tr><tr><td>IGMP Proxy</td><td>ideco-igmpproxy-backend; ideco-igmpproxy</td></tr></tbody></table>
