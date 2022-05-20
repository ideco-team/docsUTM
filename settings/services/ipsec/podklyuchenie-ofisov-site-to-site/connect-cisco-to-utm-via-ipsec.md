---
description: >-
  По шагам данной статьи можно объединить сети Cisco и Ideco UTM по IPsec с
  использованием PSK.
---

# Входящее подключение Cisco IOS к Ideco UTM по IPSec

Рассмотрим настройку подключения по схеме, представленной на рисунке ниже:

![](<../../../../.gitbook/assets/DIA1 (1).png>)

## Шаг 1. Первоначальная настройка Ideco UTM

Настройте на Ideco UTM локальный и внешний интерфейсы. Подробная информация находится в статье [Первоначальная настройка](../../../../installation/initial-setup.md).

## Шаг 2. Первоначальная настройка Cisco IOS EX

Настройку Cisco можно осуществить несколькими способами - через консоль устройства (настройка описана ниже) или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://cisco.ideco.ru/](https://cisco.ideco.ru).

1\. Настройка локального интерфейса:

```
enable
conf t
interface GigabitEthernet2
ip address {локальный IP Cisco} {маска подсети}
no shutdown
ip nat inside
exit
```

2\. Настройка внешнего интерфейса:

```
interface GigabitEthernet1
ip address {внешний IP Cisco} {маска подсети}
no shutdown
ip nat outside
exit
```

3\. Проверьте наличие связи между внешними интерфейсами Ideco UTM и Cisco. Для этого в консоли Cisco используйте команду `ping {внешний IP UTM}` . Результат вывода команды - наличие ICMP-ответов.

4\. Создание access-list с адресацией локальной сети (подробную информацию по созданию access-list вы можете прочитать в [статье](https://www.cisco.com/c/ru\_ru/support/docs/security/ios-firewall/23602-confaccesslists.html) на официальном сайте Cisco):

```
ip access-list extended NAT
permit ip {локальная подсеть Cisco} {обратная маска подсети} any
exit
```

5\. Настройка NAT (подробную информацию по настройке данного пункта вы можете прочитать в [статье](https://www.cisco.com/c/ru\_ru/support/docs/ip/network-address-translation-nat/13772-12.html) на официальном сайте Cisco):

```
ip nat inside source list NAT interface GigabitEthernet1 overload
exit
```

6\. Сохранение настроек конфигурации:

```
write memory
```

7\. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в сеть Интернет.** Для этого перейдите на какой-нибудь сайт (например: [https://www.cisco.com/](https://www.cisco.com)) с устройства в локальной сети Cisco.

## Шаг 3. Настройка IKEv2+IPSec на Cisco

1\. Создание proposal (подробную информацию по настройке данного пункта вы можете прочитать в [статье ](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec\_conn\_ike2vpn/configuration/xe-16-8/sec-flex-vpn-xe-16-8-book/sec-cfg-ikev2-flex.html#GUID-6F6D8166-508A-4669-9DDC-4FE7AE9B9939\_\_GUID-A5DB59F5-70A0-421E-86AE-AE983B283E6F)на официальном сайте Cisco):

```
conf t
crypto ikev2 proposal ikev2proposal 
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2\. Создание policy (подробную информацию по настройке данного пункта вы можете прочитать в [статье ](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec\_conn\_ike2vpn/configuration/xe-16-8/sec-flex-vpn-xe-16-8-book/sec-cfg-ikev2-flex.html#GUID-B5C198FE-97D9-4F74-88C6-6B5802195772\_\_GUID-613A19C3-C5D6-456A-8D8A-4693F3553ED3)на официальном сайте Cisco):

```
crypto ikev2 policy ikev2policy 
match fvrf any
proposal ikev2proposal
exit
```

3\. Создание peer (key\_id - идентификатор удаленной стороны, т.е. Ideco UTM). Подробную информацию по настройке данного пункта вы можете прочитать в [статье ](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec\_conn\_ike2vpn/configuration/xe-16-8/sec-flex-vpn-xe-16-8-book/sec-cfg-ikev2-flex.html#GUID-D6AC9B42-1F22-4F60-A06A-A72575181659\_\_GUID-A1CB9A0A-6098-475C-99BE-5D41009CD9A9)на официальном сайте Cisco.

```
crypto ikev2 keyring key
peer strongswan
address {внешний IP UTM}
identity key-id {key_id}
pre-shared-key local {psk}
pre-shared-key remote {psk}
exit
exit
```

4\. Создание IKEv2 profile (подробную информацию по настройке данного пункта вы можете прочитать в [статье ](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec\_conn\_ike2vpn/configuration/xe-16-8/sec-flex-vpn-xe-16-8-book/sec-cfg-ikev2-flex.html#task\_20288C58E8B1416897A763FABA8B0885\_\_GUID-B31A2B1F-E07A-4DA9-8CEA-45D92E283D14)на официальном сайте Cisco):

```
crypto ikev2 profile ikev2profile
match identity remote address {внешний IP UTM} 255.255.255.255 
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
set peer {внешний IP UTM}
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

8\. Создание access-list для трафика между локальными сетями Cisco и UTM:

```
ip access-list extended cryptoacl
permit ip {локальная подсеть Cisco} {обратная маска подсети} {локальная подсеть UTM} {обратная маска подсети}
exit
```

9\. Добавление в access-list NAT исключения трафика между локальными сетями Cisco и UTM (правило `deny` должно оказаться выше чем `permit`):

```
ip access-list extended NAT 
no permit ip {локальная подсеть Cisco} {обратная маска подсети} any
deny ip {локальная подсеть Cisco} {обратная маска подсети} {локальная подсеть UTM} {обратная маска подсети}
permit ip {локальная подсеть Cisco} {обратная маска подсети} any
exit

end
```

10\. Сохранение настроек конфигурации:

```
write memory
```

## Шаг 4. Создание входящего IPSec подключения на UTM

1\. В веб-интерфейсе Ideco UTM откройте вкладку **Сервисы -> IPsec -> Устройства**.

2\. Добавьте новое подключение:

* **Название** – любое;
* **Тип** – входящее;
* **Тип аутентификации** – PSK;
* **PSK** – укажите PSK-ключ, который вы вводили в [Шаг 3](connect-cisco-to-utm-via-ipsec.md#shag-3-nastroika-ikev-2-ipsec-na-cisco) пункт 3;
* **Идентификатор удаленной стороны** – вставьте идентификатор Cisco (параметр Key ID в [Шаг 3](connect-cisco-to-utm-via-ipsec.md#shag-3-nastroika-ikev-2-ipsec-na-cisco) пункт 3;
* **Домашние локальные сети** – укажите локальную сеть Ideco UTM;
* **Удалённые локальные сети** – укажите локальную сеть Cisco.

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено (в списке подключений появится ваше подключение, в столбце **Статусы** зеленым цветом будет подсвечена надпись **Установлено**).

5\. Проверьте наличие трафика между локальными сетями (TCP и web).

## Итоговая конфигурация Cisco IOS

Итоговая конфигурация IKEv2 IPSec на Cisco IOS должна выглядеть следующим образом:

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
