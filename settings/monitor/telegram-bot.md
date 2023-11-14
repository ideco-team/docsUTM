---
description: >-
  Ideco Monitoring Bot может прислать уведомления о событиях в Ideco UTM
  (уведомления из колокольчика).
---

# Telegram-бот

Бот может отправлять оповещения:

* в личные сообщения;
* в беседы, где 2 и более пользователей (groups).

Привязка бота и настройка оповещений Ideco Monitoring Bot осуществляется в [личном кабинете](https://my.ideco.ru/).
## Привязка Ideco Monitоring Bot

<details>
<summary>Настройка привязки Ideco Monitoring Bot к одному пользователю</summary>

1. Настроить Интернет на Ideco UTM.
2. [Привязать лицензию](../../service/license-management.md) к серверу.
3. Перейти к диалогу с ботом: [@ideco\_monitor\_bot](https://telegram.im/@ideco_monitor_bot).
4. Написать боту `/start`.
5. Скопировать код привязки к аккаунту.
6. Перейти в раздел **Ideco Monitoring Bot** в [личном кабинете](https://my.ideco.ru/#/ideco-monitoring-bot).
7. Нажать на кнопку **Привязать аккаунт**.
8. Ввести код в соответствующее поле и нажать на кнопку **Привязать**.

![](../../.gitbook/assets/monitoring\_bot\_link.png)

</details>

<details>

<summary>Настройка привязки Ideco Monitoring Bot к беседе</summary>

1. Настроить Интернет на Ideco NGFW.
2. [Привязать лицензию](broken-reference) к серверу.
3. Перейти в группу и добавить пользователя @ideco_monitoring_bot.
4. Написать `/start` в группе.
5. Скопировать код привязки к аккаунту.
6. Перейти в раздел **Ideco Monitoring Bot** в [личном кабинете](https://my.ideco.ru/#/ideco-monitoring-bot).
7. Нажать на кнопку **Привязать аккаунт**.
8. Ввести код в соответствующее поле и нажать на кнопку **Привязать**.

![](../../.gitbook/assets/monitoring\_bot\_link.png)

</details>

{% hint style="info" %}
При настройке подключения Ideco Monitoring Bot к беседе нельзя использовать подсказки для команд, поскольку требуется ввод команды `/start` вручную.
{% endhint %}

{% hint style="success" %}
Уведомления начнут приходить в Telegram аккаунт.
{% endhint %}

## Настройка оповещений Ideco Monitоring Bot

Настройте оповещения, которые приходят от Ideco Monitoring Bot, для каждой отдельной беседы.

Для настройки оповещений:
1. Перейдите в раздел настройки, нажав на иконку ![bot\_notification\_settings.svg](../../.gitbook/assets/bot\_notification\_settings.svg).
2. Проставьте галочки напротив тех уведомлений, которые хотели бы получать в выбранной беседе.

{% hint style="info" %}
Если требуется временно отключить отправку уведомлений, нажмите на иконку ![bot\_notification\_shutdown.svg](../../.gitbook/assets/bot\_notification\_shutdown.svg). Оповещение перестанут приходить, пока снова не нажмете на эту иконку.
{% endhint %}