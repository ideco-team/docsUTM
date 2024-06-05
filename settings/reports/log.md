---
description: Для просмотра логов работы служб перейдите в веб-интерфейсе в раздел Отчеты и журналы -> Журнал событий.
---
# Журнал событий

{% hint style="info" %}
Время хранения логов в разделе **Журнал событий** 3 месяца. Далее просматривать логи можно в разделе **Управление сервером -> Терминал**.
{% endhint %}

Для просмотра логов в веб-интерфейсе перейдите в раздел **Отчеты и журналы-> Журнал событий**.

В разделе можно просматривать логи работы служб таблицы:

| Раздел                                        | Имя службы   |
| :-------------------------------------------- | :------------------------- |
| Файрвол                                       | ideco-firewall-backend; ideco-nflog |
| Предотвращение вторжений                      | ideco-suricata-backend; ideco-suricata; ideco-suricata-event-syncer; ideco-suricata-event-to-syslog |
| Объекты                                       | ideco-alias-backend |
| Сетевые интерфейсы                            | ideco-network-backend; ideco-network-nic |
| Балансировка и резервирование, Маршрутизация  | ideco-routing-backend |
| DNS                                 	        | ideco-dns-backend; unbound |
| Центральная консоль	                          | ideco-central-console-backend |
| Автоматическое обновление	                    | ideco-sysupdate-backend |
| Бекапы                         | ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate |
| Лицензия	                                    | ideco-license-backend |
| Авторизация	                                  | ideco-auth-backend|
| Active Directory	                            | ideco-ad-backend; ideco-ad-log-collector@<имя домена> |
| ALD Pro                                       | ideco-ald-rest; ideco-ald-backend |
| Syslog	                                      | ideco-monitor-backend |

Чтобы посмотреть логи конкретной службы, воспользуйтесь строкой поиска или фильтром. 
Для фильтрации логов по нескольким критериям нажмите **Добавить фильтр** и выберите соответствующий критерий, значение и оператор в форме.

Пример фильтрации по нескольким критериям:

![](/.gitbook/assets/log1.png)

