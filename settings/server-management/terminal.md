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
| Файрвол                                       | ideco-firewall-backend; ideco-nflog |
| Предотвращение вторжений                      | ideco-suricata-backend; ideco-suricata; ideco-suricata-event-syncer; ideco-suricata-event-to-syslog |
| Ограничение скорости                                | ideco-shaper-backend|
| Контент-Фильтр                                | ideco-content-filter-backend|
| Объекты                                       | ideco-alias-backend |
| Сетевые интерфейсы                            | ideco-network-backend; ideco-network-nic |
| Балансировка и резервирование, Маршрутизация  | ideco-routing-backend |
| DNS                                 	        | ideco-dns-backend; unbound |
| Центральная консоль	                          | ideco-central-console-backend |
| Автоматическое обновление	                    | ideco-sysupdate-backend |
| Резервное копирование                         | ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate |
| Лицензия	                                    | ideco-license-backend |
| Авторизация	                                  | ideco-auth-backend|
| Active Directory	                            | ideco-ad-backend; ideco-ad-log-collector@<имя домена> |
| ALD Pro                                       | ideco-ald-rest; ideco-ald-backend |
| Syslog	                                      | ideco-monitor-backend |