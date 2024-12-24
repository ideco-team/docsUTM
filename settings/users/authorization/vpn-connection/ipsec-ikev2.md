# Подключение по IKEv2/IPsec

{% hint style="success" %}
Данный протокол VPN является предпочтительным и рекомендованным для всех сценариев использования.

Инструкции по настройке VPN-подключений на разных ОС доступны по [ссылке](/recipes/popular-recipes/vpn/README.md).
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины. А так же указывать в качестве логина IP-адрес.
{% endhint %}

## Настройка VPN-сервера в Ideco NGFW

Если корневой сертификат NGFW не находится в доверенных, то скачайте и установите его на компьютер пользователя. Скачать сертификат можно одним из способов:

* В личном кабинете, введя логин/пароль пользователя:

    ![](/.gitbook/assets/user-personal-account6.png)
* В разделе **Сервисы -> Сертификаты -> Загруженные сертификаты**:

    ![](/.gitbook/assets/certs1.png)

1\. Для включения авторизации по IKEv2 установите соответствующий флаг **Подключение по IKEv2/IPsec** в разделе веб-интерфейса **Пользователи -> VPN-подключения -> Основное**.

2\. В соответствующем поле укажите доменное имя или IP-адрес и нажмите **Сохранить**. \
Важно: в разделе **Сервисы -> Сертификаты -> Загруженные сертификаты** загрузите сертификат с указанием полного доменного имени в расширении SAN. Wildcard-сертификат не может быть использован.

![](/.gitbook/assets/vpn-authorization8.png)

3\. Создайте в разделе **Пользователи -> VPN-подключения -> Доступ по VPN** правило, разрешающее пользователю VPN-подключение для пользователей, которым необходимо подключаться извне по VPN. Указанный в карточке пользователя логин и пароль будут использоваться для подключения.

4\. Передача клиентам маршрутов до ваших локальных сетей происходит автоматически. Для управления доступом к сетям используйте [Файрвол](/settings/access-rules/firewall.md).

## Поддержка IPsec IKEv2 в клиентских ОС

* Microsoft **Windows 10**. Требует установки корневого сертификата Let's Encrypt. [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-windows10.md);
* Apple **MacOS X 10.11** "El Capitan" (2015 г.). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-high-sierra-macos.md);
* Linux [NetworkManager plugin](https://wiki.strongswan.org/projects/strongswan/wiki/NetworkManager) (c 2008 г.). Инструкция по настройке [Alt Linux](/recipes/popular-recipes/vpn/connection-for-alt-linux.md), [Ubuntu](/recipes/popular-recipes/vpn/connection-for-ubuntu.md), [Astra Linux](/recipes/popular-recipes/vpn/connection-for-astra-linux.md) и [Fedora](/recipes/popular-recipes/vpn/connection-for-fedora.md);
* Google **Android 11** (2020 г.). На более старых версиях можно использовать приложение [StrongSwan](https://play.google.com/store/apps/details?id=org.strongswan.android). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-android);
* Apple **iOS 9** (iPhone 4S) (2015 г.). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-ios);
* **KeeneticOS 3.5.** [Инструкция по настройке](/recipes/popular-recipes/vpn/sstp-connecting-keenetic-wi-fi-routers.md);
* MikroTik;
* Cisco routers.

{% hint style="info" %}
При проблемах с подключением на IOS требуется:

1\. Проверить, что в качестве VPN-сервера указано его доменное имя в разделе **Пользователи -> VPN-подключения**.

2\.  Проверить, что на доменное имя VPN-сервера выдан сертификат Let's Encrypt.
{% endhint %}