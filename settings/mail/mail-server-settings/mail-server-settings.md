---
description: 
  Основные настройки почтового сервера.
---

# Настройка почтового сервера

1\. Перейдите в раздел **Почтовый релей -> Основные настройки**, заполните поля **Основной почтовый домен** и **Имя хоста почтового сервера**.

2\. Заполните дополнительные почтовые домены, которые почтовый сервер будет считать своими. Корреспонденция, отправляемая с ящиков в этих почтовых доменах, будет обрабатываться сервером при условии правильной установки MX-записей.

3\. Включите опции IMAP(S) и POP(S).

4\. Подключите дополнительный жесткий диск к серверу, если Ideco NGFW планируется использовать, как полноценный сервер с хранением почты.

![](../../../.gitbook/assets/mail-server-settings.png)

## SSL-сертификат для почтового домена

После сохранения настроек основного почтового домена и имени хоста почтового сервера Ideco NGFW создает локальный сертификат, подписанный корневым (самоподписанным) сертификатом. Параллельно с созданием локального сертификата отправляется запрос на выпуск сертификата Let’s Encrypt.

* Если сертификат Let’s Encrypt успешно выписался, то он заместит собой локальный сертификат.
* Если выпуск сертификата Let’s Encrypt завершился неудачей, то будет использоваться локальный сертификат.

{% hint style="info" %}
Для замены автоматически выпушенного сертификата перейдите в раздел **Сервисы -> Сертификаты -> Загруженные сертификаты** и загрузите собственную цепочку сертификатов. **CN (Общее имя)** последнего сертификата в цепочке должно соответствовать домену, для которого сертификат загружается. Подробнее в [инструкции](../services/certificates/upload-ssl-certificate-to-server.md).
{% endhint %}

## Проверка настроек почтового сервера

Рекомендуется проверить корректность всех настроек DNS и почтового сервера с помощью сервиса [mail-tester.com](https://www.mail-tester.com/).

При правильной настройке почтовый сервер на Ideco NGFW должен получить 10 баллов из 10.