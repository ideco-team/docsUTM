---
description: >-
  Помогает централизованно управлять серверами UTM
---

# Центральная консоль

Ideco Center - это центральная консоль, разработанная для помощи в администрировании нескольких серверов Ideco UTM. Позволяет создавать правила файрвола и объекты, которые переносятся в подключенные сервера Ideco UTM. Подробнее о работе правил файрвола и объектов в статье [Политики и объекты](policies-and-objects.md).

Файл для установки центральной консоли доступен для скачивания в [личном кабинете](https://my.ideco.ru/#/utm/download). Процесс установки Ideco Center аналогичен [процессу установки Ideco UTM](../../../installation/installation-process.md).

## Подключение Ideco UTM к центральной консоли

Для подключения Ideco UTM к Ideco Center:
* Перейдите в раздел **Управление сервером -> Центральная консоль**;
* Введите IP адрес или доменное имя в строке **Сервер центральной консоли** и нажмите **Подключить**:

  ![](../../.gitbook/assets/central-console1.png)

* В интерфейсе Ideco Center перейдите в раздел **Серверы** и подтвердите подключение кнопкой ![](../../../.gitbook/assets/icon-yes.png).

  ![](../../.gitbook/assets/central-console.png)

{% hint style="info" %}
Если сервер Ideco Center находится за NAT, то требуется указать IP-адрес или доменное имя в разделе **Управление сервером -> Дополнительно -> Адрес центральной консоли**.
{% endhint %}

Удаление сервера Ideco UTM из Ideco Center разорвет привязку в интерфейсе Ideco UTM:

![](../../.gitbook/assets/central-console.gif)

Подробное описание функциональностей Ideco Center смотрите в соответствующих разделах.

{% content-ref url="policies-and-objects.md" %}
[policies-and-objects.md](policies-and-objects.md)
{% endcontent-ref %}

{% content-ref url="services.md" %}
[services.md](services.md)
{% endcontent-ref %}

{% content-ref url="server-management.md" %}
[server-management.md](server-management.md)
{% endcontent-ref %}