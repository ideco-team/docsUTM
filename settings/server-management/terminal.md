# Терминал

{% hint style="warning" %}
Используйте терминал только для диагностики. Воздержитесь от команд, изменяющих файлы. Система рассчитана на настройку только через веб-интерфейс. Компания «Айдеко» не несёт ответственности за негативные последствия работы с Ideco UTM из терминала. Техническая поддержка вправе отказать в обслуживании, если окажется, что работа системы была нарушена из-за действий пользователя в терминале.
{% endhint %}

## Основные команды

* **Утилиты сетевой диагностики:** `ping`, `host`, `nslookup`, `tracepath`, `tcpdump`, `arping`, `ss` (аналог `netstat`);
* **Файловый редактор:** `nano`;
* **Просмотр логов:** `journalctl -u <название службы>` (например, `journalctl -u ideco-routing-backend`);
* **Проверка скорости интернета:** `speedtest-cli`.

## Таблица служб

| Раздел                                        | Имя службы   |
| :-------------------------------------------- | :------------------------- |
| Файрвол                                       | ideco-firewall-backend.service |
| Контроль приложений                           | ideco-app-backend.service; ideco-app-control@Leth<номер локального интерфейса>.service |
| Контент-фильтр                                | ideco-content-filter-backend.service |
| Ограничение скорости                          | ideco-shaper-backend.service |
| Антивирусы веб-трафика                        | ideco-av-backend.service; clamav-freshclam.service; ideco-clamd.service; kav-scanner.service |
| Предотвращение вторжений                      | ideco-suricata-backend.service; ideco-suricata.service; ideco-suricata-event-syncer.service; ideco-suricata-event-to-syslog.service |
| Объекты                                       | ideco-alias-backend.service |
| Квоты                                         | ideco-quotas-backend.service; systemd-quotacheck.service |
| Сетевые интерфейсы                            | ideco-network-backend.service; ideco-network-nic.service |
| Балансировка и резервирование, Маршрутизация  | ideco-routing-backend.service |
| BGP, OSPF	                                    | frr.service; ideco-routing-backend.service |
| Прокси	                                    | ideco-proxy-backend.service; squid.service |
| Обратный прокси	                            | ideco-reverse-backend.service |
| DNS                                 	        | ideco-unbound.service; ideco-dns-backend.service; nsd.service |
| DDNS                                 	        | ideco-dns-backend.service |
| DHCP	                                        | ideco-dnsmasq.service |
| IPSec	                                        | ideco-ipsec-backend.service; strongswan.service |
| Центральная консоль	                        | ideco-central-console-backend.service |
| Кластеризация	                                | ideco-cluster-backend.service; ideco-cluster-backup-pusher.service |
| Автоматическое обновление	                    | ideco-sysupdate-backend.service |
| Резервное копирование                         | ideco-backup-backend.service; ideco-backup-create.service; ideco-backup-restore.service; ideco-backup-rotate.service |
| Лицензия	                                    | ideco-license-backend.service |
| VPN-подключения                          	    | ideco-accel-l2tp.service; ideco-accel-pptp.service; ideco-accel-sstp.service; ideco-vpn-servers-backend.service; ideco-vpn-authd.service |
| Авторизация	                                | ideco-auth-backend.service |
| Двухфакторная аутентификация	                | ideco-web-authd.service |
| Active Directory	                            | ideco-ad-backend.service; ideco-ad-log-collector@<имя домена>.service |
| Ideco агент	                                | ideco-agent-backend.service; ideco-agent-server.service; ideco-agent-websocket.service |
| Syslog	                                    | ideco-monitor-backend.service |
| Обнаружение устройств	                        | ideco-netscan-backend.service |
