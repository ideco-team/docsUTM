---
description: >-
  В статье рассказывается, как настроить подключение IKEv2/IPsec.
---

# Подключение по IKEv2/IPsec

{% hint style="success" %}
Видеоинструкцию смотрите по ссылкам:
* [Rutube](https://rutube.ru/video/5ff5b898fe9b5b010074ac972548bf1f/);
* [Youtube](https://www.youtube.com/watch?v=1dQJsP2B2S8).
{% endhint %}

IKEv2/IPsec - протокол, который используется для создания защищенного соединения между двумя устройствами в сети.

{% hint style="success" %}
Данный протокол VPN является предпочтительным и рекомендованным для всех сценариев использования.
{% endhint %}

Протокол использует корневой сертификат для проверки подлинности участников соединения. Если для VPN-подключения используется сертификат, выданный Let`s Encrypt, то установка корневого сертификата на устройство пользователя не требуется.

Для аутентификации применяется связка логин и пароль пользователя Ideco NGFW или пользователя из Active Directory.

## Настройка Ideco NGFW

Не рекомендуем использовать для VPN-подключений кириллические логины и пароли, а так же указывать в качестве логина IP-адрес.

### Основные настройки

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**:

![](/.gitbook/assets/vpn-authorization8.png)

2\. Включите опцию **Подключение по IKEv2/IPsec**.

3\. В соответствующем поле укажите доменное имя или IP-адрес и нажмите **Сохранить**.

{% hint style="info" %}

* Если используется сертификат Let's Encrypt, то дополнительных действий не требуется.
* Если сертификат для VPN-подключений издан NGFW, появится уведомление о необходимости установить корневой сертификат Ideco NGFW у клиентов:

![](/.gitbook/assets/vpn-authorization29.png)

* Если используете сторонний сертификат (например, от коммерческих Certificate Authority), убедитесь, что домен указан в поле **Subject Alternative Name (SAN)**. Загрузите сертификат как пользовательский в разделе **Сервисы -> Сертификаты -> Загруженные сертификаты**.
{% endhint %}

4\. Если используете Netflow, то в поле **Индекс интерфейса для Netflow** введите целое число от 0 до 65535 для идентификации интерфейса.

5\. Передача клиентам маршрутов до ваших локальных сетей происходит автоматически. Для управления доступом к сетям используйте [Файрвол](/settings/access-rules/firewall.md).

### Настройка доступа по VPN

Разрешите пользователю подключение по VPN из интернета, создав в разделе **Пользователи -> VPN-подключения -> Доступ по VPN** разрешающее правило. Подробнее - в статье [VPN-подключение](/settings/users/authorization/vpn-connection/README.md).

## Поддержка IKEv2/IPsec в клиентских ОС

* Microsoft **Windows 10** и выше. Требует установки корневого сертификата Let's Encrypt. [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-windows10.md).
* Apple **MacOS X 10.11** "El Capitan" (2015 г.) и выше. [Инструкции по настройке](/recipes/popular-recipes/vpn/connection-for-high-sierra-macos.md).
* Linux [NetworkManager plugin](https://wiki.strongswan.org/projects/strongswan/wiki/NetworkManager) (c 2008 г.). Инструкция по настройке [Alt Linux](/recipes/popular-recipes/vpn/connection-for-alt-linux.md), [Ubuntu](/recipes/popular-recipes/vpn/connection-for-ubuntu.md), [Astra Linux](/recipes/popular-recipes/vpn/connection-for-astra-linux.md) и [Fedora](/recipes/popular-recipes/vpn/connection-for-fedora.md).
* Google **Android 11** (2020 г.) и выше. На более ранних версиях можно использовать приложение [StrongSwan](https://play.google.com/store/apps/details?id=org.strongswan.android). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-android).
* Apple **iOS 9** (iPhone 4S, 2015 г.) и выше. [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-ios).
* **KeeneticOS 3.5** и выше. [Инструкция по настройке](/recipes/popular-recipes/vpn/sstp-connecting-keenetic-wi-fi-routers.md).
* MikroTik.
* Cisco routers.
