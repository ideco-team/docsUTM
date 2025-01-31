# Подключение по IKEv2/IPsec

{% hint style="success" %}
Данный протокол VPN является предпочтительным и рекомендованным для всех сценариев использования.
{% endhint %}

IKEv2/IPsec — протокол который используется для создания защищенного соединения между двумя устройствами в сети.

Протокол использует корневой сертификат для проверки подлинности участников соединения. Если для VPN-подключения используется сертификат, выданный Let`s Encrypt, то установка корневого сертификата на устройство пользователя не требуется.

Для аутентификации применяется связка логин/пароль пользователя Ideco NGFW или пользователя из Active Directory.

{% hint style="info" %}
Не рекомендуем использовать для VPN-подключений кириллические логины. А так же указывать в качестве логина IP-адрес.
{% endhint %}

## Настройка Ideco NGFW

### Основные настройки

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**:

![](/.gitbook/assets/vpn-authorization8.png)

2\. Включите опцию **Подключение по IKEv2/IPsec**.

3\. В соответствующем поле укажите доменное имя или IP-адрес и нажмите **Сохранить**. \
Важно: в разделе **Сервисы -> Сертификаты -> Загруженные сертификаты** загрузите сертификат с указанием полного доменного имени в расширении SAN. Wildcard-сертификат не может быть использован.

4\. В поле **Индекс интерфейса для Netflow** введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

5\. Передача клиентам маршрутов до ваших локальных сетей происходит автоматически. Для управления доступом к сетям используйте [Файрвол](/settings/access-rules/firewall.md).

### Настройка доступа по VPN

Разрешите пользователю подключение по VPN из интернета, создав в разделе **Пользователи -> VPN-подключения -> Доступ по VPN** разрешающее правило. Подробнее в статье [VPN-подключения](/settings/users/authorization/vpn-connection\README.md#dostup-po-vpn).

## Поддержка IPsec IKEv2 в клиентских ОС

* Microsoft **Windows 10**. Требует установки корневого сертификата Let's Encrypt. [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-windows10.md);
* Apple **MacOS X 10.11** "El Capitan" (2015 г.). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-high-sierra-macos.md);
* Linux [NetworkManager plugin](https://wiki.strongswan.org/projects/strongswan/wiki/NetworkManager) (c 2008 г.). Инструкция по настройке [Alt Linux](/recipes/popular-recipes/vpn/connection-for-alt-linux.md), [Ubuntu](/recipes/popular-recipes/vpn/connection-for-ubuntu.md), [Astra Linux](/recipes/popular-recipes/vpn/connection-for-astra-linux.md) и [Fedora](/recipes/popular-recipes/vpn/connection-for-fedora.md);
* Google **Android 11** (2020 г.). На более старых версиях можно использовать приложение [StrongSwan](https://play.google.com/store/apps/details?id=org.strongswan.android). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-android);
* Apple **iOS 9** (iPhone 4S) (2015 г.). [Инструкция по настройке](/recipes/popular-recipes/vpn/connection-for-mobile-devices.md#podklyuchenie-na-ios);
* **KeeneticOS 3.5.** [Инструкция по настройке](/recipes/popular-recipes/vpn/sstp-connecting-keenetic-wi-fi-routers.md);
* MikroTik;
* Cisco routers.
