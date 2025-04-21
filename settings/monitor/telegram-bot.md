---
description: >-
  Статья содержит настройку Telegram-бота для получения уведомлений о событиях в Ideco NGFW.
---

# Telegram-бот

**Ideco Monitoring Bot** — это Telegram-бот, который отправляет уведомления о событиях в Ideco NGFW (уведомления из колокольчика):

* В личные сообщения;
* В беседы, где 2 и более участников (groups).

Привязка бота и настройка оповещений Ideco Monitoring Bot осуществляется в [личном кабинете](https://my.ideco.ru/).

## Привязка Ideco Monitоring Bot

<details>

<summary>К личному аккаунту</summary>

1\. Откройте чат с ботом: [@ideco_monitor_bot](https://telegram.im/@ideco_monitor_bot).
2\. Напишите боту `/start`.
3\. Скопируйте код привязки к аккаунту.
4\. Перейдите в раздел **Ideco Monitoring Bot** в [личном кабинете](https://my.ideco.ru/#/ideco-monitoring-bot).
5\. Нажмите **Привязать аккаунт**.
6\. Введите код в поле **Токен Telegram-аккаунта** и нажмите **Привязать**:

![](/.gitbook/assets/telegram-bot.png)

{% hint style="success" %}
Уведомления начнут приходить в Telegram-аккаунт.
{% endhint %}

</details>

<details>

<summary>К беседе</summary>

{% hint style="info" %}
При подключении Ideco Monitoring Bot к беседе нельзя использовать подсказки для команд, поскольку требуется ввод команды `/start` вручную.
{% endhint %}

1\. Перейдите в группу в Telegram и добавьте бота: @ideco_monitor_bot.
2\. Напишите `/start` в группе.
3\. Скопируйте код привязки к аккаунту.
4\. Перейдите в раздел **Ideco Monitoring Bot** в [личном кабинете](https://my.ideco.ru/#/ideco-monitoring-bot).
5\. Нажмите **Привязать аккаунт**.
6\. Введите код в поле **Токен Telegram-аккаунта** и нажмите **Привязать**:

![](/.gitbook/assets/telegram-bot.png)

{% hint style="success" %}
Уведомления начнут приходить в Telegram-аккаунт.
{% endhint %}

</details>

## Настройка оповещений Ideco Monitоring Bot

В личном кабинете можно настроить оповещения от Ideco Monitoring Bot для каждого привязанного аккаунта или беседы.
Для настройки оповещений:

1\. Перейдите в раздел **Ideco Monitoring Bot** в [личном кабинете](https://my.ideco.ru/#/ideco-monitoring-bot).
2\. Выберите аккаунт или группу и нажмите ![](/.gitbook/assets/icon-bot-notifications.png).
3\. Выберите уведомления, которые хотели бы получать.

{% hint style="info" %}
Если требуется временно отключить отправку уведомлений, нажмите на ![](/.gitbook/assets/icon-bot-off.png). Оповещения перестанут приходить, пока снова не нажмете на эту иконку.
{% endhint %}