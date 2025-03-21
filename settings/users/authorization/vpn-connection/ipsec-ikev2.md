# IPSec IKEv2

{% hint style="success" %}
Данный протокол VPN является предпочтительным и рекомендованным для всех сценариев использования.

Инструкции по настройке VPN-подключений на разных ОС, доступны по [ссылке](../../../../recipes/popular-recipes/vpn/README.md).
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

## Настройка VPN-сервера в Ideco UTM

1\. Для включения авторизации по IKEv2 установите соответствующий флаг **Подключение по IKEv2/IPSec** в разделе веб-интерфейса **Пользователи -> Авторизация пользователей -> VPN-подключение**.

2\. Передача маршрутов клиентам до ваших локальных сетей происходит автоматически. Для управления доступом к сетям используйте [Файрвол](../../../access-rules/firewall.md).

3\. Подключение возможно только по доменному имени (не по IP-адресу), поэтому необходимо иметь доменное имя, которое резолвится в IP-адрес внешнего интерфейса Ideco UTM. В поле **Домен** необходимо указать это DNS-имя. Оно необходимо для выписки сертификата Let’s Encrypt.

![](/.gitbook/assets/domain.png)

4\. У пользователей, которым необходимо подключаться извне по VPN установите флаг **Разрешить удаленный доступ через VPN** в дереве пользователей. Указанный там логин и пароль будут использоваться для подключения.

## Поддержка IPSec IKEv2 в клиентских ОС

* Microsoft **Windows 7** (2009 г.). Требует установки корневого сертификата Let's Encrypt;
* Apple **MacOS X 10.11** "El Capitan" (2015 г.);
* Linux [NetworkManager plugin](https://wiki.strongswan.org/projects/strongswan/wiki/NetworkManager) (c 2008 г.);
* Google **Android 11** (2020 г.). На более старых версиях можно использовать приложение [StrongSwan](https://play.google.com/store/apps/details?id=org.strongswan.android);
* Apple **iOS 9** (iPhone 4S) (2015 г.);
* **KeeneticOS 3.5;**
* Mikrotik;
* Cisco routers.