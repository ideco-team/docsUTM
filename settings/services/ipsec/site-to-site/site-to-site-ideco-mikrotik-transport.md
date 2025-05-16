# Подключение Ideco NGFW и MikroTik по IPsec в транспортном режиме

{% hint style="info" %}
При объединении сетей с помощью VPN локальные сети в разных офисах не должны пересекаться.

Для корректной работы подключений по сертификатам синхронизируйте время на MikroTik по NTP (например, предоставьте доступ в интернет).

IPsec-подключения от Ideco NGFW к MikroTik по сертификатам к MikroTik версии 6.45 и ниже не работают, так как нельзя использовать современные криптоалгоритмы.
{% endhint %}

{% hint style="success" %}
GRE over IPsec поддерживает мультикаст-трафик, что позволяет использовать более сложные механизмы маршрутизации, включая динамическую маршрутизацию через OSPF.

Также в GRE over IPsec не требуется задавать **Домашние локальные сети** и **Удаленные локальные сети**. Транспортный режим IPsec шифрует только то, что выше уровня IP, а заголовок IP оставляет без изменений.
{% endhint %}

Рассмотрим настройку подключения по схеме:

![](/.gitbook/assets/site-to-site-ideco-mikrotik5.png)

* `172.16.50.3/24` - внешний IP-адрес NGFW.
* `192.168.100.2/24` - локальный IP-адрес NGFW.
* `10.100.0.1/16` - IP-адрес GRE-тунеля NGFW.
* `172.16.50.4/24` - внешний IP-адрес MikroTik.
* `192.168.50.2/24` - локальный IP-адрес MikroTik.
* `10.100.0.2/16` - IP-адрес GRE-тунеля MikroTik.

Для настройки подключения MikroTik и Ideco NGFW следуйте инструкции в каждом из пунктов.

{% hint style="warning" %}
Перед настройкой подключения убедитесь, что удаленный и локальный IP-адрес GRE-туннеля не используются другим, уже действующим GRE-туннелем в разделе [Туннельные](/settings/services/connection-to-provider/README.md) или [IPsec](/settings/services/ipsec/README.md). Рекомендуем отключать такой GRE-туннель на время подключения к удаленному серверу через GRE over IPSec, либо использовать разные адреса для настроек GRE и GRE over IPSec.
{% endhint %}

## Подключение от Ideco NGFW к MikroTik

<details>

<summary>Предварительная настройка MikroTik</summary>

1\. Настройте на MikroTik IP-адреса:

```
/ip address add address=172.16.50.4/24 interface=ether1 network=172.16.50.0
/ip address add address=192.168.50.2/24 interface=ether2 network=192.168.50.0
```

2\. Создайте GRE-интерфейс и назначьте ему IP-адрес:

```
/interface gre add allow-fast-path=no local-address=172.16.50.4 name=gre-tunnel1 remote-address=172.16.50.3
/ip address add address=10.100.0.2/16 interface=gre-tunnel1 network=10.100.0.0
```

</details>

### Тип аутентификации PSK

<details>

<summary>Настройка исходящего IPsec-подключения на Ideco NGFW</summary>

1\. Заполните поля:

![](/.gitbook/assets/ipsec.png)

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.
* **Зона** - укажите зону для добавления IPSec-подключения.
* **Режим работы** - выберите **Транспортный** режим.
* **Адрес удаленного устройства** - укажите внешний IP-адрес устройства MikroTik.
* **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
* **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля MikroTik. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере. **IP-адрес интерфейса туннеля** и **Удаленный IP-адрес туннеля** должны находиться в одной подсети.
* **Интерфейс** - выберите внешний интерфейс NGFW.
* **Тип аутентификации** - выберите **PSK**.
* **PSK-ключ** - будет сгенерирован случайный PSK-ключ. Он потребуется для настройки подключения в MikroTik.
* **Тип идентификатора** - выберите **keyid**.
* **NGFW идентификатор** - введенный ключ (**key-id**) будет использоваться для идентификации входящего подключения в MikroTik.
* **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

2\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного MikroTik.

</details>

<details>

<summary>Настройка входящего IPsec-подключения на MikroTik</summary>

1\. Настройте IPsec-подключение со стороны MikroTik:

```
/ip ipsec profile add dh-group=modp4096 enc-algorithm=aes-256 hash-algorithm=sha256 name=from_192.168.100.0/24

/ip ipsec proposal add auth-algorithms=sha256 comment=from_192.168.100.0/24 enc-algorithms=aes-256-cbc name=172.16.50.3 pfs-group=modp4096

/ip ipsec peer add address=172.16.50.3/32 comment=from_192.168.100.0/24 exchange-mode=ike2 name=from_192.168.100.0/24 passive=yes profile=from_192.168.100.0/24

/ip ipsec identity add comment=from_192.168.100.0/24 peer=from_192.168.100.0/24 secret="<Сгенерированный NGFW PSK-ключ>"

/ip ipsec policy add dst-address=172.16.50.3/32 peer=from_192.168.100.0/24 proposal=172.16.50.3 protocol=gre src-address=172.16.50.4/32
```

2\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного NGFW.
</details>

### Тип аутентификации Сертификат

<details>

<summary>Настройка исходящего IPsec-подключения на Ideco NGFW</summary>

1\. Перейдите в раздел **IPsec -> Исходящие подключения** и нажмите **Добавить**.

2\. Заполните поля:

  ![](/.gitbook/assets/ipsec3.png)

  * **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.
  * **Зона** - укажите зону для добавления IPSec-подключения.
  * **Режим работы** - выберите **Транспортный** режим.
  * **Адрес удаленного устройства** - укажите внешний IP-адрес устройства MikroTik.
  * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
  * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля MikroTik. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере. **IP-адрес интерфейса туннеля** и **Удаленный IP-адрес туннеля** должны находиться в одной подсети.
  * **Интерфейс** - выберите интерфейс NGFW.
  * **Тип аутентификации** - выберите **Сертификат**.
  * **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

3\. Скачайте **Запрос на подпись сертификата**.

4\. Не закрывая форму создания исходящего подключения NGFW, перейдите к настройке Mikrotik.

</details>

<details>

<summary>Настройка входящего IPsec-подключения на MikroTik</summary>

1\. Загрузите скачанный ранее файл с **Запросом на подпись сертификата** (`NGFW.crt`) на MikroTik через WinBox или по SSH.

2\. Создайте корневой сертификат MikroTik:

```
/certificate add common-name=mk_ca name=mk_ca_template key-usage=key-cert-sign,crl-sign,digital-signature,content-commitment
/certificate sign mk_ca_template ca-crl-host=172.16.50.4 name=mk_ca
```

3\. Подпишите сертификат Ideco NGFW и сделайте его доверенным:

```
/certificate sign-certificate-request file-name=NGFW.csr ca=mk_ca
/certificate set [find name~"^device_.+\\.ipsec\$"] trusted=yes
```

4\. Экспортируйте корневой сертификат MikroTik и подписанный сертификат NGFW в формат `.pem`:

```
/certificate export-certificate mk_ca type=pem
/certificate export-certificate [find name~"^device_.+\\.ipsec\$"] type=pem
```

5\. Загрузите с MikroTik корневой сертификат MikroTik и подписанный сертификат NGFW через WinBox или по SSH. Названия файлов содержат `cert_export`.

6\. Настройте входящее IPsec-соединение на MikroTik:

```
/ip ipsec profile add name=from_192.168.100.0/24 hash-algorithm=sha256 enc-algorithm=aes-256 dh-group=modp4096 dpd-interval=120s dpd-maximum-failures=5

/ip ipsec peer add name=from_192.168.100.0/24 address=172.16.50.3/32 profile=from_192.168.100.0/24 exchange-mode=ike2 passive=yes comment=from_192.168.100.0/24

/ip ipsec identity add peer=from_192.168.100.0/24 auth-method=digital-signature certificate=mk_ca remote-certificate=[: put [/certificate get [/certificate find name~"^device_.+\\.ipsec\$"] name]] comment=from_192.168.100.0/24

/ip ipsec proposal add name=172.16.50.3 enc-algorithms=aes-256-cbc auth-algorithms=sha256 pfs-group=modp4096 comment=from_192.168.100.0/24

/ip ipsec policy add dst-address=172.16.50.3/32 peer=from_192.168.100.0/24 proposal=172.16.50.3 protocol=gre src-address=172.16.50.4/32
```

7\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного NGFW.

</details>

<details>

<summary>Донастройка исходящего IPsec-подключение на Ideco NGFW</summary>

Вернитесь к форме создания исходящего IPsec-соединения на Ideco NGFW.

1\. Загрузите скачанные ранее **Корневой сертификат MikroTik** (`cert_export_mk_ca.crt`) и **Подписанный сертификат NGFW** (`cert_export_device_<случайный набор символов>.ipsec.crt`) в соответствующие поля.

2\. Нажмите **Добавить подключение**.

3\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного MikroTik.

</details>

## Подключение от MikroTik к Ideco NGFW  

### Тип аутентификации PSK

<details>

<summary>Настройка исходящего IPsec-подключения на MikroTik</summary>

1\. Настройте на MikroTik IP-адреса:

```
/ip address add address=172.16.50.4/24 interface=ether1 network=172.16.50.0
/ip address add address=192.168.50.2/24 interface=ether2 network=192.168.50.0
```

2\. Создайте GRE-интерфейс и назначьте ему IP-адрес:

```
/interface gre add allow-fast-path=no local-address=172.16.50.4 name=gre-tunnel1 remote-address=172.16.50.3
/ip address add address=10.100.0.2/16 interface=gre-tunnel1 network=10.100.0.0
```

3\. Настройте IPsec-подключение со стороны MikroTik:

```
/ip ipsec profile add dh-group=modp4096 enc-algorithm=aes-256 hash-algorithm=sha256 name=to_192.168.100.0/24

/ip ipsec proposal add auth-algorithms=sha256 comment=to_192.168.100.0/24 enc-algorithms=aes-256-cbc name=172.16.50.3 pfs-group=modp4096

/ip ipsec peer add address=172.16.50.3/32 comment=to_192.168.100.0/24 exchange-mode=ike2 name=to_192.168.100.0/24 profile=to_192.168.100.0/24

/ip ipsec identity add comment=to_192.168.100.0/24 peer=to_192.168.100.0/24 my-id=key-id:"test_psk" secret="<PSK-ключ>"

/ip ipsec policy add dst-address=172.16.50.3/32 peer=to_192.168.100.0/24 proposal=172.16.50.3 protocol=gre src-address=172.16.50.4/32
```

4\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного NGFW.

</details>

<details>

<summary>Настройка входящего IPsec-подключения на Ideco NGFW</summary>

1\. Заполните поля:

![](/.gitbook/assets/ipsec1.png)

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.
* **Зона** - укажите зону для добавления IPSec-подключения.
* **Режим работы** - выберите **Транспортный** режим.
* **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
* **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля MikroTik. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере. **IP-адрес интерфейса туннеля** и **Удаленный IP-адрес туннеля** должны находиться в одной подсети.
* **Тип аутентификации** - выберите **PSK**.
* **PSK-ключ** - введите PSK-ключ, указанный при настройке исходящего IPsec-подключения в MikroTik.
* **Тип идентификатора** - выберите **keyid**.
* **NGFW идентификатор** - введите **key-id**, использованный при настройке исходящего IPsec-подключения в MikroTik.
* **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

2\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного MikroTik.

</details>

### Тип аутентификации Сертификат

<details>

<summary>Предварительная настройка MikroTik</summary>

1\. Настройте на MikroTik IP-адреса:

```
/ip address add address=172.16.50.4/24 interface=ether1 network=172.16.50.0
/ip address add address=192.168.50.2/24 interface=ether2 network=192.168.50.0
```

2\. Создайте GRE-интерфейс и назначьте ему IP-адрес:

```
/interface gre add allow-fast-path=no local-address=172.16.50.4 name=gre-tunnel1 remote-address=172.16.50.3
/ip address add address=10.100.0.2/16 interface=gre-tunnel1 network=10.100.0.0
```

3\. Сгенерируйте запрос на подпись сертификата:

```
/certificate add name=mk_ca common-name=mk_ca key-usage=digital-signature,content-commitment
/certificate create-certificate-request key-passphrase="" template=mk_ca
```

4\. Загрузите файл `certificate-request.pem` c MikroTik через WinBox или по SHH.

</details>

<details>

<summary>Настройка входящего IPsec-подключения на Ideco NGFW</summary>

1\. Перейдите в раздел **IPsec -> Входящие подключения** и нажмите **Добавить**.

2\. Заполните поля:

  ![](/.gitbook/assets/ipsec2.png)

  * **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.
  * **Зона** - укажите зону для добавления IPSec-подключения.
  * **Режим работы** - выберите **Транспортный** режим.
  * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
  * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля MikroTik. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере. **IP-адрес интерфейса туннеля** и **Удаленный IP-адрес туннеля** должны находиться в одной подсети.
  * **Тип аутентификации** - выберите **Сертификат**.
  * **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

3\. Загрузите скачанный ранее с MikroTik файл `certificate-request.pem` в поле **Запрос на подпись сертификата**.

4\. Нажмите **Добавить подключение**.

5\. Откройте созданное IPsec-соединение, нажав на ![](/.gitbook/assets/icon-edit.png), и загрузите файлы **Корневого сертификата NGFW** (`NGFW.crt`) и **Подписанного сертификата устройства** (`device.crt`).

6\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного MikroTik.

</details>

<details>

<summary>Настройка исходящего IPsec-подключение на MikroTik</summary>

1\. Загрузите на MikroTik скачанные ранее файлы **Корневого сертификата NGFW** (`NGFW.crt`) и **Подписанного сертификата устройства** (`device.crt`) через WinBox или по SSH.

2\. Импортируйте сертификаты:

```
/certificate import file-name=NGFW.crt passphrase=""
/certificate import file-name=device.crt passphrase=""
/certificate import file-name=certificate-request_key.pem passphrase=""
```

3\. Настройте IPsec-соединение:

```
/ip ipsec profile add dh-group=modp4096 enc-algorithm=aes-256 hash-algorithm=sha256 name=to_192.168.100.0/24 dpd-interval=120s dpd-maximum-failures=5

/ip ipsec peer add address=172.16.50.3/32 comment=to_192.168.100.0/24 exchange-mode=ike2 name=to_192.168.100.0/24 profile=to_192.168.100.0/24

/ip ipsec identity add comment=to_192.168.100.0/24 peer=to_192.168.100.0/24 auth-method=digital-signature certificate=device.crt_0 remote-certificate=NGFW.crt_0

/ip ipsec proposal add auth-algorithms=sha256 comment=to_192.168.100.0/24 enc-algorithms=aes-256-cbc name=172.16.50.3 pfs-group=modp4096

/ip ipsec policy add dst-address=172.16.50.3/32 peer=to_192.168.100.0/24 proposal=172.16.50.3 protocol=gre src-address=172.16.50.4/32
```

4\. Настройте статическую или динамическую маршрутизацию до локальных сетей удаленного NGFW.

</details>

## Настройка динамической маршрутизации

### OSPF 

<details>

<summary>Настройка на Ideco NGFW</summary>

1\. Перейдите в раздел **Сервисы -> OSPF** и нажмите **Добавить**.

2\. Заполните поля:

![](/.gitbook/assets/ospf9.png)

* **Интерфейс** - выберите GRE-over-Ipsec интерфейс Ideco NGFW, настроенный ранее.
* **Название зоны** - введите номер зоны (значение `area`, должно совпадать на NGFW и Mikrotik). Можно ввести в виде числа или IP-адреса, нажав иконку ![](/.gitbook/assets/icon-ospf.png).
* **Вес** - введите стоимость маршрута.

3\. Нажмите **Сохранить**.

4\. Включите модуль **OSPF**.

</details>

<details>

<summary>Настройка на MikroTik (RouterOS 6.48.6)</summary>

1\. Настройте область (значение `area`, должно совпадать на NGFW и Mikrotik):

```
/routing ospf area 
add name=backbone area-id=0.0.0.0 type=default default-cost=1 inject-summary-lsa=no
```

3\. Объявите сети, участвующие в OSPF:
```
/routing ospf network
add network=192.168.50.0/24 area=backbone
add network=10.100.0.0/16 area=backbone
```

</details>

<details>

<summary>Настройка на MikroTik (RouterOS 7.18.2)</summary>

1\. Настройте OSPF Instance (процесс OSPF, управляющий определенной группой маршрутов и интерфейсов):

```
/routing ospf instance 
add name=<Название Instance> router-id=<Router-ID Mikrotik> redistribute=connected in-filter-chain=ospf-in out-filter-chain=ospf-out
```

2\. Настройте магистральную зону (значение `area`, должно совпадать на NGFW и Mikrotik):

```
/routing ospf area 
add name=backbone area-id=0.0.0.0 instance=<Название Instance>
```

3\. Настройте интерфейсы:

```
/routing ospf interface-template
add interfaces=<Название GRE-интерфейса> area=backbone type=ptp network=10.100.0.0/16 cost=10
add interfaces=<Название интерфейса локальной сети> area=backbone type=broadcast network=192.168.50.0/24 cost=1
```

4\. Настройте фильтрацию:

```
/routing filter rule
add chain=ospf-in rule="accept" disabled=no comment="Разрешаем все входящие маршруты"
add chain=ospf-out rule="accept" disabled=no comment="Разрешаем все исходящие маршруты"
```

{% hint style="info" %}
Разрешение всех маршрутов без фильтрации допустимо в тестовых средах, простых или полностью контролируемых топологиях. В распределенных сетях рекомендуем применять фильтрацию OSPF-маршрутов.
{% endhint %}

</details>

### BGP

<details>

<summary>Настройка на Ideco NGFW</summary>

1\. Перейдите в раздел **Сервисы -> BGP** и нажмите **Добавить**.

2\. Введите номер автономной системы в строку **Номер AS** и нажмите **Сохранить**.

3\. Заполните поля:

![](/.gitbook/assets/bgp4.png)

* **Исходящий интерфейс** - выберите **Любой**.
* **Название** - любое значение.
* **IP-адрес** - укажите IP-адрес интерфейса туннеля MikroTik.
* **Номер AS** - номер автономной системы MikroTik.
* **Входящие сети** - укажите локальные сети MikroTik.
* **Анонсируемые сети** - укажите локальные сети Ideco NGFW.

4\. Заполните **Дополнительные настройки** [BGP](/settings/services/bgp.md) и нажмите **Сохранить**.

5\. Включите модуль **BGP**.

</details>

<details>

<summary>Настройка на MikroTik</summary>

1\. Настройте общий шаблон BGP:

{% code overflow="wrap" %}

```
/routing bgp template set default address-families=ip disabled=no output.default-originate=always router-id=<Router-ID Mikrotik> routing-table=main 
```

{% endcode %}

2\. Добавьте BGP-сессию с Ideco NGFW:

{% code overflow="wrap" %}

```
/routing bgp connection add address-families=ip as=<AS MikroTik> disabled=no local.role=ebgp-peer name=<Имя подключения> output.default-originate=always .redistribute=\ connected,static,vpn,dhcp,modem remote.address=<IP-адрес NGFW> .as=<AS NGFW> router-id=<Router-ID NGFW> routing-table=main templates=default \ use-bfd=no
```

{% endcode %}

</details>

## Возможные проблемы

<details>

<summary>Соединение не устанавливается при повторной активации</summary>

Если подключение было отключено и при попытке включения соединение не установилось, удаленное устройство попало в fail2ban. Для установки соединения сбросьте блокировки по IP на Ideco NGFW. О сбросе блокировки читайте в статье [Защита от брутфорс-атак](/settings/reports/logs.md#защита-от-брутфорс-атак).

Fail2ban отслеживает в log-файлах попытки обратиться к сервисам, и, если находит повторяющиеся неудачные попытки авторизации с одного и того же IP-адреса или хоста, блокирует IP-адрес.

</details>

<details>

<summary>Соединение периодически разрывается</summary>

При работе туннеля между Ideco NGFW и MikroTik может происходить обрыв соединения. Чтобы восстановить соединение, необходимо отправить какой-либо трафик с MikroTik в сторону Ideco NGFW.

Для автоматизации процесса поддержания соединения, создайте на MikroTik скрипт, который будет отправлять ping-запросы по расписанию планировщика к Ideco NGFW:

1\. Откройте веб-интерфейс MikroTik или подключитесь через WinBox.

2\. Перейдите в раздел **System** -> **Scripts**.

3\. Нажмите кнопку **+** для создания нового скрипта и заполните поля:

<img src="/.gitbook/assets/ipsec-mikrotik.png" alt="IPSec MikroTik" width="350" />

* **Name** - название скрипта (не поддерживаются пробелы и нижние подчеркивания).
* **Policy** - оставьте флаги на **read** и **test**.
* **Source** - введите команду `ping <ID-адрес Ideco NGFW> count=3`.

4\. Нажмите **Apply**, затем **Ok**.

Далее настройте запуск скрипта по расписанию в планировщике заданий:

1\. Перейдите в раздел **System** → **Scheduler**.

2\. Нажмите кнопку **+** для создания нового скрипта и заполните поля:

<img src="/.gitbook/assets/ipsec-mikrotik2.png" alt="IPSec MikroTik" width="350" />

* **Name** - название задания (не поддерживаются пробелы и нижние подчеркивания).
* **Interval** - интервал 00:00:15 (каждые 15 секунд).
* **Policy** - оставьте флаги на **read** и **test**.
* **On Event** - введите название созданного ранее скрипта.

3\. Нажмите **Apply**, затем **Ok**.

По завершению настройки MikroTik каждые 15 секунд будет отправлять три ICMP-запроса на адрес Ideco NGFW. Это позволит автоматически восстанавливать туннельное соединение в случае обрыва.

</details>