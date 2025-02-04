# Настройка Device VPN

На Ideco NGFW необходимо загрузить доверенный сертификат, который будет использоваться для подписи сертификата авторизации устройства. Если для авторизации будет использоваться самоподписанный сертификат, его также можно загрузить в качестве доверенного.

Если для проверки подлинности используется промежуточный сертификат, то на Ideco NGFW нужно загрузить файл, содержащий всю цепочку сертификатов, начиная с корневого. Структура этого файла похожа на [структуру](/settings/services/certificates/upload-ssl-certificate-to-server.md) файла для загрузки SSL-сертификата на сервер.

Чтобы подключить устройство к Ideco NGFW в режиме Device VPN, выполните действия:

1\. В веб-интерфейсе Ideco NGFW перейдите в раздел **Пользователи -> Ideco Client**.

2\. Введите домен или IP-адрес Ideco NGFW, включите настройку **Создавать туннель при подключении из локальной сети** (если устройства пользователей находятся в локальной сети).

3\. Включите настройку **Принимать подключения в режиме Device VPN**.

4\. Загрузите доверенный сертификат в формате `.pem` и нажмите **Сохранить**. Процесс создания сертификата описан в статье [Создание сертификатов для Device VPN](/settings/users/ideco-client/device-vpn-cert.md):

![](/.gitbook/assets/ideco-client6.png)

5\. Перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте правило, разрешающее учетным записям Ideco Device VPN подключение по протоколу Wireguard:

![](/.gitbook/assets/vpn-authorization18.png)

{% hint style="info" %}
Если в таблице **Доступ по VPN** устройству из группы Device VPN запрещен доступ, на короткое время подключение из внешней сети будет установлено. За это время может пройти определенный объем трафика.
Позже подключение будет разорвано. Это связано с тем, что проверка по таблице доступа VPN для Device VPN происходит не в момент подключения, а позже.
{% endhint %}

6\. Установите Ideco Client на устройство пользователя ([Windows](/settings/users/ideco-client/ideco-client-windows.md), [Linux](/settings/users/ideco-client/ideco-client-linux.md), [MacOS](/settings/users/ideco-client/ideco-client-macos.md)).

7\. Загрузите на устройство пользователя сертификат с расширением .pem, который содержит приватный ключ и подписан доверенным сертификатом. Процесс создания сертификата описан в статье [Создание сертификатов для Device VPN](/settings/users/ideco-client/device-vpn-cert.md).

{% hint style="danger" %}
Рекомендуем для безопасности хранить сертификаты в директориях, к которым есть доступ только у администратора. Например:
* Для Linux - это home-каталог `/root`, в который имеет доступ только администратор;
* Для Windows нужно создать новую папку. В свойствах папки в разделе **Безопасность** нужно разрешить доступ только для пользователя Система/System.
{% endhint %}

8\. Запустите установленный Ideco Client:

<details>
<summary>Для Windows</summary>

Откройте командную строку от имени администратора и введите:

{% code overflow="wrap" %}
```
<абсолютный путь до IdecoClient>\IdecoClient.exe --set-devicevpn-cert-path=<абсолютный путь до файла сертификата> --set-devicevpn-host=<адрес NGFW> --set-enable-devicevpn=True
```
{% endcode %}

</details>

<details>
<summary>Для Linux</summary>

Откройте терминал и введите:

{% code overflow="wrap" %}
```
sudo <абсолютный путь до IdecoClient>/ld.so --argv0 IdecoClient --library-path <абсолютный путь до IdecoClient>/lib <абсолютный путь до IdecoClient>/IdecoClient --set-devicevpn-cert-path=<абсолютный путь до файла сертификата> --set-devicevpn-host=<адрес NGFW> --set-enable-devicevpn=True
```
{% endcode %}

Для вывода заданных параметров в консоль воспользуйтесь командой:

{% code overflow="wrap" %}
```
sudo <абсолютный путь до IdecoClient>/ld.so --argv0 IdecoClient --library-path <абсолютный путь до IdecoClient>/lib <абсолютный путь до IdecoClient>/IdecoClient --print-devicevpn-config=True
```
{% endcode %}

</details>

<details>
<summary>Для MacOS</summary>

Откройте терминал и введите:

{% code overflow="wrap" %}
```
sudo <абсолютный путь до IdecoClient>/IdecoClient --set-devicevpn-cert-path=<абсолютный путь до файла сертификата> --set-devicevpn-host=<адрес NGFW> --set-enable-devicevpn=True
```
{% endcode %}

Для вывода заданных параметров в консоль воспользуйтесь командой:

{% code overflow="wrap" %}
```
(sudo) <абсолютный путь до IdecoClient>/IdecoClient --print-devicevpn-config=True
```
{% endcode %}

</details>

{% hint style="warning" %}
При неудачном подключении Device VPN попытка соединения будет бесконечной, даже если закрыть Ideco Client или перезапустить службу.

Для решения проблемы необходимо:

* Выключить Device VPN: выполнить команду по настройке Device VPN с единственным параметром `--set-enable-devicevpn=False`;
* Исправить проблему подключения (загрузить правильный сертификат, определить корректность пути до него);
* Настроить и активировать Device VPN: выполнить команду по настройке Device VPN и параметром `--set-enable-devicevpn=True`.
* В интерфейсе Ideco NGFW убедиться, что подключение Device VPN выполнено.
{% endhint %}