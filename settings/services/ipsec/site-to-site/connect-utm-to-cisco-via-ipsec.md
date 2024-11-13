---
description: >-
  По шагам статьи можно объединить сети Cisco и Ideco NGFW по IPsec или GRE over IPsec с
  использованием PSK.
---

# Подключение Cisco IOS и Ideco NGFW по IPsec

## Настройка подключения в туннельном режиме

Рассмотрим настройку подключения по схеме ниже:

![](/.gitbook/assets/connect-utm-to-cisco-via-ipsec1.png)

Для настройки подключения Cisco IOS к Ideco NGFW нужно следовать инструкции в каждом из пунктов.

<details>

<summary>Первоначальная настройка Ideco NGFW и Cisco IOS</summary>

### Настройка Ideco NGFW

Настройте на Ideco NGFW локальный и внешний интерфейсы. Подробная информация находится в статье [Первоначальная настройка](/installation/initial-setup.md).

### Настройка Cisco IOS XE

Настройку Cisco можно осуществить через консоль устройства или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://cisco.ideco.ru/](https://cisco.ideco.ru).

#### Настройка Cisco через консоль

1\. Настройка локального интерфейса:

```
enable
conf t
interface GigabitEthernet2
ip address <локальный IP Cisco> <маска подсети>
no shutdown
ip nat inside
exit
```

2\. Настройка внешнего интерфейса:

```
interface GigabitEthernet1
ip address <внешний IP Cisco> <маска подсети>
no shutdown
ip nat outside
exit
```

3\. Проверьте наличие связи между внешними интерфейсами Ideco NGFW и Cisco. Для этого в консоли Cisco используйте команду `ping <внешний IP NGFW>`. Результат вывода команды - наличие ICMP-ответов.

4\. Создание access-list с адресацией локальной сети:

```
ip access-list extended NAT
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit
```

5\. Настройка NAT:

```
ip nat inside source list NAT interface GigabitEthernet1 overload
exit
```

6\. Сохранение настроек конфигурации:

```
write memory
```

7\. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в сеть интернет.**\
   Для этого перейдите на какой-нибудь сайт (например: [https://www.cisco.com/](https://www.cisco.com)) с устройства в локальной сети Cisco.

### Настройка IKEv2+IPsec на Cisco

1\. Создание proposal:

```
conf t
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создание policy:

```
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
exit
```

3\. Создание peer (key\_id - идентификатор удаленной стороны, т. е. Ideco NGFW):

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP NGFW>
identity key-id <key_id>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создание IKEv2 profile:

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP NGFW> 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local key
exit
```

5\. Настройка шифрования в esp:

```
crypto ipsec transform-set TS esp-gcm 256
mode tunnel
exit
```

6\. Создание ipsec-isakmp:

```
crypto map cmap 10 ipsec-isakmp
set peer <внешний IP NGFW>
set transform-set TS
set ikev2-profile ikev2profile
match address cryptoacl
exit
```

7\. Настройка crypto map на внешнем интерфейсе:

```
interface GigabitEthernet1
crypto map cmap
exit
```

8\. Создание access-list для трафика между локальными сетями Cisco и NGFW:

```
ip access-list extended cryptoacl
permit ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
exit
```

9\. Добавление в access-list NAT исключения трафика между локальными сетями Cisco и NGFW (правило `deny` должно оказаться выше чем `permit`):

```
ip access-list extended NAT
no permit ip <локальная подсеть Cisco> <обратная маска подсети> any
deny ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit

end
```

10\. Сохранение настроек конфигурации:

```
write memory
```

</details>

<details>

<summary>Настройка исходящего подключения на Ideco NGFW</summary>

Для настройки исходящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Исходящие подключения**.

2\. Добавьте новое подключение:

   * **Название** - любое;
   * **Зона** - укажите зону для добавления IPSec подключения;
   * **Режим работы** - выберите **Туннельный**;
   * **Адрес удаленного устройства** - введите IP-адрес Cisco;
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса туннеля. Поле необязательное, заполняется при настройке BGP-соседства для динамической маршрутизации и для получения статистики обмена пакетами;
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса туннеля Cisco. Поле необязательное. Для получения статистики о потере пакетов, средней задержке и джиттере заполните поля **IP-адрес интрефейса туннеля** и **Удаленный IP-адрес туннеля**. Они должны находиться в одной подсети.
   * **Домашние локальные сети** - укажите локальную сеть Ideco NGFW;
   * **Удаленные локальные сети** - укажите локальную сеть Cisco;
   * **Тип аутентификации** - PSK;
   * **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется, чтобы настроить подключение в Cisco;
   * **Идентификатор NGFW** - введенный вами ключ будет использоваться для идентификации исходящего подключения. Введите также этот идентификатор в Cisco.

3\. Проверьте, что подключение установилось (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

4\. Проверьте наличие трафика между локальными сетями (TCP и web).

</details>

{% hint style="info" %}
Если Cisco передает внешний IP-адрес вместо **KeyID** (проверьте, включив расширенный лог IPsec на Cisco), укажите в качестве **Идентификатора удаленной стороны** внешний IP-адрес Cisco.
{% endhint %}

<details>

<summary>Настройка входящего подключения на Ideco NGFW</summary>

Для настройки входящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Устройства (входящие подключения)**.

2\. Добавьте новое подключение:

   * **Название** - любое;
   * **Зона** - укажите зону для добавления IPSec-подключения;
   * **Режим работы** - выберите **Туннельный**;
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса туннеля. Поле необязательное, заполняется при настройке BGP-соседства для динамической маршрутизации и для получения статистики обмена пакетами;
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса туннеля Cisco. Поле необязательное. Для получения статистики о потере пакетов, средней задержке и джиттере заполните поля **IP-адрес интрефейса туннеля** и **Удаленный IP-адрес туннеля**. Они должны находиться в одной подсети. заполняется для получения статистики обмена пакетами; 
   * **Домашние локальные сети** - укажите локальную сеть Ideco NGFW;
   * **Удаленные локальные сети** - укажите локальную сеть Cisco;
   * **Тип аутентификации** - PSK;
   * **PSK** - укажите PSK-ключ;
   * **Идентификатор удаленной стороны** - вставьте идентификатор Cisco (параметр Key ID).

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

5\. Проверьте наличие трафика между локальными сетями (TCP и web).

</details>

Итоговая конфигурация IKEv2 IPsec на Cisco IOS должна выглядеть следующим образом:

```
crypto ikev2 proposal ikev2proposal
 encryption aes-cbc-256
 integrity sha256
 group 19

crypto ikev2 policy ikev2policy
 match fvrf any
 proposal ikev2proposal

crypto ikev2 keyring key
 peer strongswan
  address 5.5.5.5
  pre-shared-key local QWEqwe1234567890
  pre-shared-key remote QWEqwe1234567890

crypto ikev2 profile ikev2profile
 match identity remote key-id key-id
 authentication remote pre-share
 authentication local pre-share
 keyring local key

crypto ipsec transform-set TS esp-gcm 256
 mode tunnel

crypto map cmap 10 ipsec-isakmp
 set peer 5.5.5.5
 set transform-set TS
 set ikev2-profile ikev2profile
 match address cryptoacl

interface GigabitEthernet1
! внешний интерфейс
 ip address 1.1.1.1 255.255.255.0
 ip nat outside
 negotiation auto
 no mop enabled
 no mop sysid
 crypto map cmap

interface GigabitEthernet2
! локальный интерфейс
 ip address 2.2.2.2 255.255.255.0
 ip nat inside
 negotiation auto
 no mop enabled
 no mop sysid

ip nat inside source list NAT interface GigabitEthernet1 overload

ip access-list extended NAT
 deny   ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
 permit ip 2.2.2.0 0.0.0.255 any
ip access-list extended cryptoacl
 permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
```

## Настройка подключения в транспортном режиме

{% hint style="success" %}
GRE over IPsec поддерживает мультикаст-трафик, что позволяет использовать более сложные механизмы маршрутизации, включая динамическую маршрутизацию через OSPF.

Также в GRE over IPsec не требуется задавать **Домашние локальные сети** и **Удаленные локальные сети**. Транспортный режим IPsec шифрует только то, что выше уровня IP, а заголовок IP оставляет без изменений.
{% endhint %}

Рассмотрим настройку подключения по схеме ниже:

![](/.gitbook/assets/connect-utm-to-cisco-via-ipsec.png)

Для настройки подключения Cisco IOS к Ideco NGFW нужно следовать инструкции в каждом из пунктов.

<details>

<summary>Первоначальная настройка Ideco NGFW и Cisco IOS</summary>

### Настройка Ideco NGFW

Настройте на Ideco NGFW локальный и внешний интерфейсы. Подробная информация находится в статье [Первоначальная настройка](/installation/initial-setup.md).

### Настройка Cisco IOS через консоль

1\. Настройка локального интерфейса:

```
enable
conf t
interface GigabitEthernet2
ip address <локальный IP Cisco> <маска подсети>
no shutdown
exit
```

2\. Настройка внешнего интерфейса:

```
interface GigabitEthernet1
ip address <внешний IP Cisco> <маска подсети>
no shutdown
exit
```

3\. Проверьте наличие связи между внешними интерфейсами Ideco NGFW и Cisco. Для этого в консоли Cisco используйте команду `ping <внешний IP NGFW>`. Результат вывода команды - наличие ICMP-ответов.

4\. Сохранение настроек конфигурации:

```
write memory
```

5\. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в сеть интернет.**\
   Для этого перейдите на какой-нибудь сайт (например: [https://www.cisco.com/](https://www.cisco.com)) с устройства в локальной сети Cisco.

### Настройка IKEv2+GRE-over-IPsec на Cisco

1\. Создание proposal:

```
conf t
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создание policy:

```
crypto ikev2 policy ikev2policy
match fvrf any
proposal ikev2proposal
exit
```

3\. Создание peer (key\_id - идентификатор удаленной стороны, т. е. Ideco NGFW):

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP NGFW>
identity key-id <key_id>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создание IKEv2 profile:

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP NGFW> 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local key
exit
```

5\. Настройка шифрования в esp:

```
crypto ipsec transform-set TS esp-gcm 256
mode transport
exit
```

6\. Настройка профиля IPsec:

```
crypto ipsec profile SECURE-P
set transform-set SECURE-TS 
set pfs group2
```

7\. Настройка GRE-over-IPsec-туннеля:

```
interface Tunnel1
description to_NGFW
ip address <IP GRE-over-IPsec-интерфейса Cisco> <маска подсети>
tunnel source <внешний IP Cisco> 
tunnel destination <внешний IP NGFW>
tunnel mode ipsec ipv4
tunnel protection ipsec profile SECURE-P
```

8\. Настройка маршрута:

```
ip route <локальная подсеть за NGFW> <маска подсети> <IP GRE-over-IPsec-интерфейса NGFW>
```

9\. Сохранение настроек конфигурации:

```
write memory
```

</details>

<details>

<summary>Настройка исходящего подключения на Ideco NGFW</summary>

Для настройки исходящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Исходящие подключения**.

2\. Добавьте новое подключение:

   * **Название** - любое;
   * **Зона** - укажите зону для добавления IPSec подключения;
   * **Режим работы** - выберите **Транспортный**;
   * **Адрес удаленного устройства** - введите IP-адрес Cisco;
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW;
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля Cisco. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере.
   * **Тип аутентификации** - PSK;
   * **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется, чтобы настроить подключение в Cisco;
   * **NGFW идентификатор** - введенный вами ключ будет использоваться для идентификации исходящего подключения. Введите также этот идентификатор в Cisco.

3\. Проверьте, что подключение установилось (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

4\. Проверьте наличие трафика между локальными сетями (TCP и web).

</details>

<details>

<summary>Настройка входящего подключения на Ideco NGFW</summary>

Для настройки входящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Устройства(входящие подключения)**.

2\. Добавьте новое подключение:

   * **Название** - любое;
   * **Зона** - укажите зону для добавления IPsec-подключения;
   * **Режим работы** - выберите **Транспортный**;
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса GRE-туннеля NGFW;
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса GRE-туннеля Cisco. Поле необязательное и заполняется для получения статистики о потере пакетов, средней задержке и джиттере.
   * **Тип аутентификации** - PSK;
   * **PSK** - укажите PSK-ключ;
   * **Идентификатор удаленной стороны** - вставьте идентификатор Cisco (параметр Key ID).

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

5\. Проверьте наличие трафика между локальными сетями (TCP и web).

</details>

Итоговая конфигурация IKEv2 GRE over IPsec на Cisco IOS должна выглядеть следующим образом:

```
crypto ikev2 proposal ikev2proposal
 encryption aes-cbc-256
 integrity sha256
 group 19

crypto ikev2 policy ikev2policy
 match fvrf any
 proposal ikev2proposal

crypto ikev2 keyring key
 peer strongswan
  address 172.168.10.25
  pre-shared-key local QWEqwe1234567890
  pre-shared-key remote QWEqwe1234567890

crypto ikev2 profile ikev2profile
 match identity remote key-id key-id
 authentication remote pre-share
 authentication local pre-share
 keyring local key

crypto ipsec transform-set TS esp-gcm 256
 mode transport

crypto ipsec profile SECURE-P
 set transform-set SECURE-TS 
 set pfs group2
!
interface Tunnel1
 description to_NGFW
 ip address 192.168.200.1 255.255.255.0
 tunnel source 192.168.233.204 # <внешний IP Cisco>
 tunnel destination 172.168.10.25 # <внешний IP NGFW>
 tunnel protection ipsec profile SECURE-P
!
ip route 192.168.0.0 255.255.255.0 192.168.200.2

interface GigabitEthernet1
! внешний интерфейс
 ip address 192.168.233.204 255.255.255.0
 crypto map cmap

interface GigabitEthernet2
! локальный интерфейс
 ip address 192.168.10.1 255.255.255.0

```