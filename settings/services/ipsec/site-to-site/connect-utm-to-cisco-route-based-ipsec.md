---
description: >-
  В статье описана настройка route-based IPsec между NGFW и Cisco в туннельном режиме.
---

# Подключение Cisco IOS и Ideco NGFW по route-based IPsec

Рассмотрим процесс настройки подключения в туннельном режиме по следующей схеме:

![](/.gitbook/assets/connect-utm-to-cisco-route-based-ipsec.png)

Адресация:

* `192.168.26.125/30` - IP-адрес интерфейса туннеля NGFW.
* `192.168.26.126/30` - IP-адрес интерфейса туннеля Cisco.
* `172.16.50.3/24` - внешний IP-адрес NGFW.
* `192.168.100.2/24` - локальный IP-адрес NGFW.
* `172.16.50.4/24` - внешний IP-адрес Cisco.
* `192.168.105.2/24` - локальный IP-адрес Cisco.

<details>

<summary>Первоначальная настройка Ideco NGFW и Cisco IOS</summary>

### Настройка Ideco NGFW

Настройте на Ideco NGFW локальный и внешний интерфейсы. Подробная информация находится в статье [Первоначальная настройка](/installation/initial-setup.md).

### Настройка Cisco

Для настройки Cisco через консоль выполните действия:

1\. Настройка локального и внешнего интерфейса:

```
enable
configure terminal
interface gigabitEthernet 1
ip address <внешний IP-адрес Cisco> <маска подсети>
no shutdown
ip nat outside
exit

interface gigabitEthernet 2
ip address <локальный IP-адрес Cisco> <маска подсети>
no shutdown
ip nat inside
exit
```

2\. Настройка DNS и добавление маршрута по умолчанию для доступа в интернет:

```
configure terminal
ip name-server <IP-адрес DNS-сервера>
ip route 0.0.0.0 0.0.0.0 <IP-адрес провайдера>
```

3\. Создание access-list и NAT для доступа из локальной сети в интернет:

```
ip access-list extended NAT
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit
ip nat inside source list NAT interface gigabitEthernet 1 overload
``` 

4\. Добавление локального администратора и настройка доступа по SSH:

```
configure terminal
username admin privilege 15 secret <пароль>
hostname <имя роутера>
ip domain name <имя домена>
crypto key generate rsa 
ip ssh version 2
aaa new-model
line vty 0 4
transport input ssh
privilege level 15
exit
```

5\. Сохранение настроек конфигурации:

```
write 
```

</details>

<details>

<summary>Настройка route-based IPsec на Cisco</summary>

1\. Создание proposal:

```
configure terminal
crypto ikev2 proposal ikev2proposal
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создание policy:

```
crypto ikev2 policy ikev2policy
proposal ikev2proposal
exit 
```

3\. Создание peer:

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP-адрес NGFW>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создание IKEv2 profile:

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP-адрес NGFW> <маска подсети>
identity local address <внешний IP-адрес Cisco>
authentication remote pre-share
authentication local pre-share
keyring local key
no config-exchange set send
no config-exchange set accept
no config-exchange request
exit
```

5\. Настройка шифрования в esp:

```
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
mode tunnel
exit
```

6\. Создание ipsec profile:

```
crypto ipsec profile ikev2TSprofile
set transform-set TS
set pfs group19
set ikev2-profile ikev2profile
exit
```

7\. Создание туннельного интерфейса:

```
interface Tunnel3000
ip address <IP-адрес интерфейса туннеля Cisco> <маска подсети>
tunnel source gigabitEthernet 1
tunnel mode ipsec ipv4
tunnel destination <внешний IP-адрес NGFW>
tunnel protection ipsec profile ikev2TSprofile
exit
```

8\. Сохранение настроек конфигурации:

```
write 
```

</details>

<details>

<summary>Настройка исходящего подключения на Ideco NGFW</summary>

Для настройки исходящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Исходящие подключения**.

2\. Добавьте новое подключение:

![](/.gitbook/assets/connect-utm-to-cisco-route-based-ipsec1.png)

   * **Название** - любое;
   * **Зона** - укажите зону для добавления IPSec подключения;
   * **Режим работы** - выберите **Туннельный**;
   * **Адрес удаленного устройства** - введите IP-адрес Cisco;
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса туннеля NGFW;
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса туннеля Cisco. Они должны находиться в одной подсети;
   * **Домашние локальные сети** - укажите локальную сеть Ideco NGFW;
   * **Удаленные локальные сети** - укажите локальную сеть Cisco;
   * **Тип аутентификации** - PSK;
   * **PSK** - укажите PSK-ключ созданный на третьем этапе в разделе **Настройка route-based IPsec на Cisco**;
   * **NGFW идентификатор** - укажите внешний IP-адрес NGFW;
   * **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

3\. Проверьте, что подключение установилось (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

4\. Проверьте наличие трафика между локальными сетями (TCP и web).

</details>

Итоговая конфигурация route-based IPsec на Cisco должна выглядеть следующим образом:

<details>

<summary>Для подключения от Cisco к Ideco NGFW</summary>

```
crypto ikev2 proposal ikev2proposal 
 encryption aes-cbc-256
 integrity sha256
 group 19

crypto ikev2 policy ikev2policy 
 proposal ikev2proposal

crypto ikev2 keyring key
 peer strongswan
  address <внешний IP-адрес NGFW>
  pre-shared-key local <psk>
  pre-shared-key remote <psk>

crypto ikev2 profile ikev2profile
 match identity remote address <внешний IP-адрес NGFW> <маска подсети>
 identity local address <внешний IP-адрес Cisco>
 authentication remote pre-share
 authentication local pre-share
 keyring local key
 no config-exchange set send
 no config-exchange set accept
 no config-exchange request

crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac 
 mode tunnel

crypto ipsec profile ikev2TSprofile
 set transform-set TS 
 set pfs group19
 set ikev2-profile ikev2profile
```

</details>
