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

В разделе можно просматривать логи работы служб таблицы:

| Раздел                                        | Имя службы   |
| :-------------------------------------------- | :------------------------- |
| Файрвол                                       | ideco-firewall-backend; ideco-nflog |
| Предотвращение вторжений                      | ideco-suricata-backend; ideco-suricata-event-syncer |
| Объекты                                       | ideco-alias-backend |
| Сетевые интерфейсы                            | ideco-network-backend |
| Балансировка и резервирование, Маршрутизация  | ideco-routing-backend |
| DNS                                 	        | ideco-dns-backend; unbound |
| Центральная консоль	                        | ideco-central-console-backend |
| Автоматическое обновление	                    | ideco-sysupdate-backend |
| Резервное копирование                         | ideco-backup-backend; ideco-backup-create; ideco-backup-restore; ideco-backup-rotate |
| Лицензия	                                    | ideco-license-backend |
| Авторизация	                                | ideco-auth-backend |
| Active Directory	                            | ideco-ad-backend; ideco-ad-log-collector@<имя домена> |
| ALD Pro                                       | ideco-ald-rest; ideco-ald-backend |
| Syslog	                                    | ideco-monitor-backend |


