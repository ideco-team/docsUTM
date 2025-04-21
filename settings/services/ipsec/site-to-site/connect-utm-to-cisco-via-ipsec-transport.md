---
description: >-
  В статье описано, как объединить сети Cisco и Ideco NGFW по GRE over IPsec с использованием PSK.
---

# Подключение Cisco IOS и Ideco NGFW по IPsec в транспортном режиме

GRE over IPsec поддерживает мультикаст-трафик, что позволяет использовать более сложные механизмы маршрутизации, включая динамическую маршрутизацию через OSPF.

В GRE over IPsec не требуется задавать **Домашние локальные сети** и **Удаленные локальные сети**. Транспортный режим IPsec шифрует только то, что выше уровня IP, а заголовок IP оставляет без изменений.

{% hint style="info" %}
Для доступности локальных сетей NGFW и Cisco с удаленного устройства при подключении по GRE over IPsec настройте на обоих устройствах статические маршруты или динамическую маршрутизацию через [BGP](/settings/services/bgp.md) или [OSPF](/settings/services/ospf.md).
{% endhint %}

Рассмотрим настройку подключения по схеме ниже:

![](/.gitbook/assets/connect-utm-to-cisco-via-ipsec.png)

Адресация:

* `172.16.2.172/24` - внешний IP-адрес NGFW.
* `192.168.18.18/24` - локальный IP-адрес NGFW.
* `172.16.2.171/24` - внешний IP-адрес Cisco.
* `192.168.17.17/24` - локальный IP-адрес Cisco.
* `10.100.0.1/30` - IP-адрес интерфейса туннеля NGFW.
* `10.100.0.2/30` - IP-адрес интерфейса туннеля Cisco.


Для настройки подключения Cisco IOS к Ideco NGFW следуйте инструкции ниже.

<details>

<summary>Первоначальная настройка Ideco NGFW и Cisco IOS</summary>

## Настройка Ideco NGFW

Настройте на Ideco NGFW локальный и внешний интерфейсы. Инструкция по настройке - в [статье](/installation/initial-setup.md).

## Настройка Cisco IOS через консоль

1\. Настройте локальный интерфейс:

```
enable
conf t
interface GigabitEthernet2
ip address <локальный IP Cisco> <маска подсети>
no shutdown
ip nat inside
exit
```

2\. Настройте внешний интерфейс:

```
interface GigabitEthernet1
ip address <внешний IP Cisco> <маска подсети>
no shutdown
ip nat outside
exit
```

3\. Проверьте наличие связи между внешними интерфейсами Ideco NGFW и Cisco. Для этого в консоли Cisco используйте команду `ping <внешний IP NGFW>`. Результат вывода команды - наличие ICMP-ответов.

4\. Создайте access-list и NAT для доступа из локальной сети в интернет:

```
ip access-list extended NAT
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit
ip nat inside source list NAT interface gigabitEthernet 1 overload
``` 

5\. Сохраните настройки конфигурации:

```
write memory
```

5\. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в интернет.**\
   Для этого перейдите на какой-нибудь сайт (например: [https://www.cisco.com/](https://www.cisco.com)) с устройства в локальной сети Cisco.

</details>

{% hint style="danger" %}
В некоторых версиях Cisco передает внешний IP-адрес вместо **KeyID** (проверьте, включив расширенный лог IPsec на Cisco). При настройке подключения от таких роутеров к Ideco NGFW в качестве **Идентификатора удаленной стороны** укажите внешний IP-адрес Cisco, в качестве **Типа идентификатора** - auto.
{% endhint %}

## Подключение от Ideco NGFW к Cisco

<details>

<summary>Настройка IKEv2+GRE-over-IPsec на Cisco</summary>

1\. Создайте proposal:

```
conf t
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создайте policy:

```
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
exit
```

3\. Создайте peer (key-id - идентификатор удаленной стороны, т. е. Ideco NGFW):

* Для подключения от Ideco NGFW к Cisco:

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP-адрес NGFW>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

* Для подключения от Cisco к Ideco NGFW:

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP NGFW>
identity key-id <key-id> # Если Cisco передает IP вместо key-id, то identity address <внешний IP-адрес Cisco>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создайте IKEv2 profile (key-id - идентификатор удаленной стороны, т. е. Ideco NGFW):

* Для подключения от Ideco NGFW к Cisco:

```
crypto ikev2 profile ikev2profile
match identity remote key-id <key-id>
authentication remote pre-share
authentication local pre-share
keyring local key
dpd 10 3 periodic
exit
```

* Для подключения от Cisco к Ideco NGFW:

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP NGFW> 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local key
dpd 10 3 periodic
exit
```

5\. Настройте шифрование в ESP:

```
crypto ipsec transform-set TS esp-gcm 256
mode transport
exit
```

6\. Настройте профиль IPsec:

```
crypto ipsec profile ikev2TSprofile
set transform-set TS
set pfs group19
set ikev2-profile ikev2profile
exit
```

7\. Создайте туннельный интерфейс:

```
interface Tunnel0
ip address <IP-адрес интерфейса туннеля Cisco> <маска подсети>
ip mtu 1400
tunnel source GigabitEthernet 1
tunnel destination <внешний IP-адрес NGFW>
tunnel protection ipsec profile ikev2TSprofile
exit
```

8\. Настройте динамическую маршрутизацию (BGP или OSPF) или статический маршрут до локальных сетей Ideco NGFW:

```
ip route <локальная подсеть за NGFW> <маска подсети> <IP интерфейса туннеля NGFW>
```

9\. Сохраните настройки конфигурации:

```
write memory
```

</details>


<details>

<summary>Настройка исходящего подключения на Ideco NGFW</summary>

Для настройки исходящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Исходящие подключения**.

2\. Добавьте новое подключение:

![](/.gitbook/assets/ipsec27.png)

   * **Название** - любое.
   * **Зона** - укажите зону для добавления IPSec подключения.
   * **Режим работы** - выберите **Транспортный**.
   * **Адрес удаленного устройства** - введите IP-адрес Cisco.
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля Cisco. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере.
   * **Тип аутентификации** - PSK.
   * **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется, чтобы настроить подключение в Cisco.
   * **NGFW идентификатор** - введенный ключ будет использоваться для идентификации исходящего подключения. Введите также этот идентификатор в Cisco.

3\. Проверьте, что подключение установилось (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

4\. Проверьте наличие трафика между туннельными интерфейсами NGFW и Cisco. Для этого в консоли Cisco или терминале NGFW используйте утилиту `ping`.

</details>

Итоговая конфигурация IKEv2 GRE over IPsec на Cisco IOS должна выглядеть следующим образом:

<details>

<summary>Для подключения от Ideco NGFW к Cisco</summary>

```
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 2

!
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
!
!
crypto ikev2 keyring key
 peer strongswan
  address <внешний IP-адрес NGFW>
  pre-shared-key local <psk>
  pre-shared-key remote <psk>
!
!
crypto ikev2 profile ikev2profile
 match identity remote key-id <key-id>
 authentication remote pre-share
 authentication local pre-share
 keyring local key
 dpd 10 3 periodic
!
!
crypto ipsec transform-set TS esp-gcm 256
 mode transport
!
!
crypto ipsec profile ikev2TSprofile
 set transform-set TS
 set pfs group2
 set ikev2-profile ikev2profile
!
!
interface Tunnel0
 ip address <IP-адрес интерфейса туннеля Cisco> <маска подсети>
 ip mtu 1400
 tunnel source GigabitEthernet 1
 tunnel destination <внешний IP-адрес NGFW>
 tunnel protection ipsec profile ikev2TSprofile
!
interface GigabitEthernet1
! внешний интерфейс
 ip address <внешний IP Cisco> <маска подсети>
 ip nat outside
 negotiation auto
 no mop enabled
 no mop sysid

interface GigabitEthernet2
! локальный интерфейс
 ip address <локальный IP Cisco> <маска подсети>
 ip nat inside
 negotiation auto
 no mop enabled
 no mop sysid
!
ip nat inside source list NAT interface GigabitEthernet1 overload
ip route <локальная подсеть за NGFW> <маска подсети> <IP интерфейса туннеля NGFW>
!
ip access-list extended NAT
 permit ip <локальная подсеть Cisco> <обратная маска подсети> any
```

</details>

## Подключение от Cisco к Ideco NGFW

<details>

<summary>Настройка IKEv2+GRE-over-IPsec на Cisco</summary>

1\. Создайте proposal:

```
conf t
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создайте policy:

```
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
exit
```

3\. Создайте peer (key-id - идентификатор удаленной стороны, т. е. Ideco NGFW):

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP NGFW>
identity key-id <key-id> # Если Cisco передает IP вместо key-id, то identity address <внешний IP-адрес Cisco>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создайте IKEv2 profile (key-id - идентификатор удаленной стороны, т. е. Ideco NGFW):

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP NGFW> 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local key
dpd 10 3 periodic
exit
```

5\. Настройте шифрование в ESP:

```
crypto ipsec transform-set TS esp-gcm 256
mode transport
exit
```

6\. Настройте профиль IPsec:

```
crypto ipsec profile ikev2TSprofile
set transform-set TS
set pfs group19
set ikev2-profile ikev2profile
exit
```

7\. Создайте туннельный интерфейс:

```
interface Tunnel0
ip address <IP-адрес интерфейса туннеля Cisco> <маска подсети>
ip mtu 1400
tunnel source GigabitEthernet 1
tunnel destination <внешний IP-адрес NGFW>
tunnel protection ipsec profile ikev2TSprofile
exit
```

8\. Настройте динамическую маршрутизацию (BGP или OSPF) или статический маршрут до локальных сетей Ideco NGFW:

```
ip route <локальная подсеть за NGFW> <маска подсети> <IP интерфейса туннеля NGFW>
```

9\. Сохраните настройки конфигурации:

```
write memory
```

</details>

<details>

<summary>Настройка входящего подключения на Ideco NGFW</summary>

Для настройки входящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Устройства(входящие подключения)**.

2\. Добавьте новое подключение:

![](/.gitbook/assets/ipsec28.png)

   * **Название** - любое.
   * **Зона** - укажите зону для добавления IPsec-подключения.
   * **Режим работы** - выберите **Транспортный**.
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW.
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля Cisco. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере.
   * **Тип аутентификации** - PSK.
   * **PSK** - укажите PSK-ключ.
   * **Тип идентификатора** - keyid или auto, если Cisco передает IP-адрес вместо key-id.
   * **Идентификатор удаленной стороны** - вставьте идентификатор Cisco (параметр Key ID) или IP-адрес Cisco, если Cisco передает IP-адрес вместо key-id.

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

5\. Проверьте наличие трафика между туннельными интерфейсами NGFW и Cisco. Для этого в консоли Cisco или терминале NGFW используйте утилиту `ping`.

</details>

Итоговая конфигурация IKEv2 GRE over IPsec на Cisco IOS должна выглядеть следующим образом:

<details>

<summary>Для подключения от Cisco к Ideco NGFW</summary>

```
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 2

!
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
!
!
crypto ikev2 keyring key
 peer strongswan
  address <внешний IP NGFW>
  identity key-id <key-id> # Если Cisco передает IP вместо key-id, то identity address <внешний IP-адрес Cisco>
  pre-shared-key local <psk>
  pre-shared-key remote <psk>
!
!
crypto ikev2 profile ikev2profile
 match identity remote address <внешний IP NGFW> 255.255.255.255
 authentication remote pre-share
 authentication local pre-share
 keyring local key
!
!
crypto ipsec transform-set TS esp-gcm 256
 mode transport
!
!
crypto ipsec profile ikev2TSprofile
 set transform-set TS
 set pfs group2
 set ikev2-profile ikev2profile
!
!
interface Tunnel0
 ip address <IP-адрес интерфейса туннеля Cisco> <маска подсети>
 ip mtu 1400
 tunnel source GigabitEthernet 1
 tunnel destination <внешний IP-адрес NGFW>
 tunnel protection ipsec profile ikev2TSprofile
!
interface GigabitEthernet1
! внешний интерфейс
 ip address <внешний IP Cisco> <маска подсети>
 ip nat outside
 negotiation auto
 no mop enabled
 no mop sysid

interface GigabitEthernet2
! локальный интерфейс
 ip address <локальный IP Cisco> <маска подсети>
 ip nat inside
 negotiation auto
 no mop enabled
 no mop sysid
!
ip nat inside source list NAT interface GigabitEthernet1 overload
ip route <локальная подсеть за NGFW> <маска подсети> <IP интерфейса туннеля NGFW>
!
ip access-list extended NAT
 permit ip <локальная подсеть Cisco> <обратная маска подсети> any
```

</details>

## Настройка динамической маршрутизации

### OSPF

<details>

<summary>Настройка на Cisco</summary>

Настройте процесс OSPF на роутере (значение `area` должно совпадать на Cisco и NGFW):

```
conf t
router ospf 1
passive-interface default
 no passive-interface Tunnel0
 network <подсеть туннельного интерфейса Cisco> <обратная маска> area 0
 network <локальная подсеть Cisco> <обратная маска> area 0
exit
```

</details>

<details>

<summary>Настройка на Ideco NGFW</summary>

1\. Перейдите в раздел **Сервисы -> OSPF** и нажмите **Добавить**.

2\. Заполните поля:

![](/.gitbook/assets/ospf9.png)

* **Интерфейс** - выберите GRE-over-Ipsec интерфейс Ideco NGFW, настроенный ранее.
* **Название зоны** - введите номер зоны (значение `area`, должно совпадать на NGFW и Cisco). Можно ввести в виде числа или IP-адреса, нажав иконку ![](/.gitbook/assets/icon-ospf.png).
* **Вес** - введите стоимость маршрута.

3\. Нажмите **Сохранить**. 

4\. Включите модуль **OSPF**.

</details>

{% hint style="success" %}
Для подключения нескольких устройств Cisco к одному Ideco NGFW и передачи маршрутов между всеми устройствами:

1\. Создайте для каждого Cisco Gre-over-IPsec подключение к Ideco NGFW.

2\. Подключите каждое устройство Cisco по OSPF.

При такой конфигурации локальные сети каждого Cisco будут доступны с Ideco NGFW и других устройств Cisco.
{% endhint %}

### BGP

<details>

<summary>Настройка на Cisco</summary>

Настройте процесс BGP на роутере:

```
conf t
router bgp 3500
 neighbor <IP интерфейса туннеля NGFW> remote-as 3501
 neighbor <IP интерфейса туннеля NGFW> ebgp-multihop 2
 neighbor <IP интерфейса туннеля NGFW> update-source Tunnel0
 !
 address-family ipv4
  network <локальная подсеть Cisco> mask <маска подсети>
  neighbor <IP интерфейса туннеля NGFW> activate
 exit-address-family
```

</details>

<details>

<summary>Настройка на Ideco NGFW</summary>

1\. Перейдите в раздел **Сервисы -> BGP** и нажмите **Добавить**.

2\. В **Настройках** введите номер автономной системы в строку **Номер AS** и нажмите **Сохранить**.

3\. Заполните поля:

![](/.gitbook/assets/bgp3.png)

* **Исходящий интерфейс** - выберите **Любой**.
* **IP-адрес** - укажите IP-адрес интерфейса туннеля Cisco.
* **Номер AS** - номер AS Cisco (указанный в команде `router bgp 3500`).
* **Входящие сети** - укажите локальные сети Cisco.
* **Анонсируемые сети** - укажите локальные сети Ideco NGFW.

4\. Заполните **Дополнительные настройки** [BGP](/settings/services/bgp.md) и нажмите **Сохранить**.

5\. Включите модуль **BGP**.

</details>

