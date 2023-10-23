# Терминал

{% hint style="warning" %}
Используйте терминал только для диагностики. Воздержитесь от команд, изменяющих файлы. Система рассчитана на настройку только через веб-интерфейс. Компания «Айдеко» не несёт ответственности за негативные последствия работы с Ideco NGFW из терминала. Техническая поддержка вправе отказать в обслуживании, если окажется, что работа системы была нарушена из-за действий пользователя в терминале.
{% endhint %}

## Основные команды

* **Утилиты сетевой диагностики:** `ping`, `host`, `nslookup`, `tracepath`, `tcpdump`, `arping`, `ss` (аналог `netstat`);
* **Файловый редактор:** `nano`;
* **Просмотр логов:** `journalctl -u <название службы>` (например, `journalctl -u ideco-routing-backend`);
* **Проверка скорости интернета:** `speedtest-cli`;
* **Просмотр ARP-таблицы**: `ip neigh show`.

## Таблица служб

| Раздел                                        | Имя службы   |
| :-------------------------------------------- | :------------------------- |
| Файрвол                                       | ideco-av-backend; ideco-nflog |
| Контроль приложений                           | ideco-app-backend; ideco-app-control@Leth<номер локального интерфейса> |
| Контент-фильтр                                | ideco-content-filter-backend |
| Ограничение скорости                          | ideco-shaper-backend |
| Антивирусы веб-трафика                        | ideco-av-backend;|
| Предотвращение вторжений                      | ideco-suricata-backend; ideco-suricata; ideco-suricata-event-syncer; ideco-suricata-event-to-syslog |
| Объекты                                       | ideco-alias-backend |
| Квоты                                         | ideco-quotas-backend; systemd-quotacheck |
| Сетевые интерфейсы                            | ideco-network-backend; ideco-network-nic |
| Балансировка и резервирование, Маршрутизация  | ideco-routing-backend |
| BGP, OSPF	                                    | ideco-routing-backend |
| Прокси	                                    | ideco-proxy-backend; squid |
| Обратный прокси	                            | ideco-reverse-backend |
| DNS                                 	        | ideco-dns-backend; unbound |
| DDNS                                 	        | ideco-dns-backend |
| DHCP	                                        | ideco-dnsmasq |
| IPsec	                                        | ideco-ipsec-backend; strongswan |
| Центральная консоль	                        | ideco-central-console-backend |
| Кластеризация	                                | ideco-cluster-backend; ideco-cluster-backup-pusher |
| Автоматическое обновление	                    | ideco-sysupdate-backend |
| Резервное копирование                         | ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate |
| Лицензия	                                    | ideco-license-backend |
| VPN-подключения                          	    | ideco-accel-l2tp; ideco-accel-pptp; ideco-accel-sstp; ideco-vpn-servers-backend; ideco-vpn-authd |
| Авторизация	                                | ideco-auth-backend |
| Двухфакторная аутентификация	                | ideco-web-authd |
| Active Directory	                            | ideco-ad-backend; ideco-ad-log-collector@<имя домена> |
| ALD Pro                                       | ideco-ald-rest; ideco-ald-backend |
| Ideco Client                                  | ideco-agent-backend; ideco-agent-websocket |
| Syslog	                                    | ideco-monitor-backend |
| Обнаружение устройств	                        | ideco-netscan-backend |
| Web Application Firewall                      | ideco-waf-backend; ideco-waf-event-syncer |
| IGMP Proxy                                    | igmpproxy |