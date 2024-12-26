---
description: >-
    USB-токен - это аппаратное устройство для безопасного хранения цифровых сертификатов и работы с приватными ключами.
---

# USB-токены

В таблице USB-токенов представлена информация о серийном номере, модели, метке ключа и корректности настройки USB-токена:

![](/.gitbook/assets/usb_tokens1.png)

<table><thead><tr><th width="144" align="center">Статус USB-токена</th><th>Описание</th></tr></thead><tbody><tr><td align="center"><img src="/.gitbook/assets/icon-tokens-green.png" alt="icon-tokens-green.png" data-size="line"></td><td>Токен подключен в USB-разъем сервера</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-tokens-grey.png" alt="icon-tokens-grey.png" data-size="line"></td><td>Токен не подключен в USB-разъем сервера</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-tokens-error.png" alt="icon-tokens-error.png" data-size="line"></td><td>Возникла ошибка или токен заблокирован</td></tr></tbody></table>

<table><thead><tr><th width="144" align="center">Статус PIN-кода</th><th>Описание</th></tr></thead><tbody><tr><td align="center"><img src="/.gitbook/assets/icon-pin-green.png" alt="icon-pin-green.png" data-size="line"></td><td>Верный PIN-код</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-pin-grey.png" alt="icon-pin-grey.png" data-size="line"></td><td>Неизвестеный статус PIN-кода. PIN-код был введен, но USB-токен не был установлен в USB-разъем сервера. USB-токен с верным PIN-кодом был извлечен из USB-разъема сервера</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-pin-error.png" alt="icon-pin-error.png" data-size="line"></td><td>Неверный PIN-код</td></tr></tbody></table>

Чтобы проверить содержимое USB-токенов и убедиться, что на них загружены все необходимые сертификаты, нажмите на ![](/.gitbook/assets/icon-tokens-certs.png) у соответствующего USB-токена. Откроется список всех загруженных сертификатов с подробной информацией.

## Настройка USB-токена на Ideco NGFW

Для работы Ideco NGFW с USB-токеном необходимо ввести корректный PIN-код. После этого сервисы NGFW смогут использовать токен для выполнения криптографических операций.

{% hint style="warning" %}
**Важно!** При превышении лимита попыток неправильного ввода PIN-кода устройство будет заблокировано. Лимит устанавливается производителем и считается до правильного ввода PIN-кода.
{% endhint %}

{% hint style="info" %}
**Ideco NGFW** поддерживает только USB-токен модели **Рутокен ЭЦП 3.0**. USB-токены других моделей могут не отображаться в веб-интерфейсе **Ideco NGFW**.
{% endhint %}

Чтобы добавить новый USB-токен, выполните действия:

1\. Подготовьте USB-токен в соответствии с инструкцией, представленной в [статье]().

2\. Подключите его к USB-разъему вашего сервера. Нажмите **Добавить** и заполните необходимые поля:

![](/.gitbook/assets/usb_tokens.png)

* **Серийный номер** - укажите серийный номер USB-токена;
* **PIN-код** - введите PIN-код;
* **Комментарий** - необязательное поле.

3\. Нажмите **Добавить**.