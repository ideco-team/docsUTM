# Терминал

{% hint style="warning" %}
Используйте терминал только для диагностики и воздержитесь от команд, изменяющих файлы.\
Система рассчитана на настройку только через веб-интерфейс.\
Компания «Айдеко» не несёт ответственности за негативные последствия работы с Ideco NGFW VPP из терминала.\
Техническая поддержка вправе отказать в обслуживании, если окажется, что работа системы была нарушена из-за действий пользователя в терминале.
{% endhint %}

## Команды для диагностики СontrolPlane интерфейса

* **Утилиты сетевой диагностики:** `ping`, `host`, `nslookup`, `tracepath`, `tcpdump`, `arping`, `ss` (аналог `netstat`);
* **Проверка скорости интернета:** `speedtest-cli`;
* **Просмотр ARP-таблицы**: `ip neigh show`.

## Команды для работы с логами и файловой системой

* **Файловый редактор:** `nano`, `vi`;
* **Просмотр логов:** `journalctl -u <название службы>` (например, `journalctl -u ideco-firewall-backend`).

## Команды для диагностики DataPlane интерфейсов

{% hint style="info" %}
Для просмотра подсказки по всем коммандам введите : `ideco-vppctl ?`
{% endhint %}

* **Просмотр списка всеx физических интерфейсов, соответствующих сетевой карте:** `ideco-vppctl show hardware-interface brief`;
* **Просмотр списка всех сетевых интерфейсов, через которые проходит трафик:** `ideco-vppctl show interface`;
* **Просмотр списка всех IP-адресов интерфейсов:** `ideco-vppctl show interface addr`;
* **Просмотр таблицы маршрутизации:** `ideco-vppctl show ip fib`;
* **Просмотр ARP таблицы:** `ideco-vppctl show ip neighbors`;
* **Утилиты сетевой диагностики:** `ideco-vppctl ping`.
* **Запись последних 100 сетевых пакетов, прошедших через шлюз:** `ideco-vppctl pcap trace rx tx intfc any file capture.pcap`

## Таблица служб

| Раздел                                        | Имя службы   |
| :-------------------------------------------- | :------------------------- |
| Учетные записи                                | ideco-user-backend |
| Авторизация                                   | ideco-auth-backend |
| Active Directory	                            | ideco-ad-backend |
| ALD Pro                                       | ideco-ald-rest; ideco-ald-backend |
| Файрвол                                       | ideco-firewall-backend; ideco-firewall-rest; ideco-cfw-backend; ideco-cfw-rest; |
| Ограничение скорости                          | ideco-shaper-backend-vpp |
| Предотвращение вторжений                      | ideco-suricata-backend; ideco-suricata-event-syncer; ideco-suricata-profiles-syncer-backend |
| Объекты                                       | ideco-alias-backend |
| Контроль приложений                           | ideco-app-backend-vpp, ideco-app-stats |
| Контент-фильтр                                | ideco-content-filter-backend; ideco-content-filter-backend-vpp |
| Сетевые интерфейсы                            | ideco-network-backend; ideco-vpp-backend; ideco-vpp-nic-syncer |
| Маршрутизация                                 | ideco-routing-backend; ideco-routing-backend-vpp; ideco-routing-rest |
| DNS                                 	        | ideco-dns-backend; nsd; unbound; unbound-anchor; unbound-keygen |
| NTP-сервер                                	| chronyd |
| Сертификаты                               	| ideco-cert-backend |
| Действия администраторов                      | ideco-audit-backend |
| Авторизация администраторов                   | ideco-web-backend |
| Отчеты и журналы                              | ideco-logs-backend; ideco-logs-syncer; ideco-reports-backend |
| Syslog	                                    | ideco-monitor-backend |
| Кластеризация           	                    | ideco-cluster-backend |
| Обновления            	                    | ideco-sysupdate-backend |
| Бэкапы                                        | ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate |
| Лицензия	                                    | ideco-license-backend |
| Дополнительно	                                | ideco-system-backend |