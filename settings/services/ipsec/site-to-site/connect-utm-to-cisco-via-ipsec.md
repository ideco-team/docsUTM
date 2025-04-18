---
description: >-
  По шагам статьи можно объединить сети Cisco и Ideco NGFW по IPsec с использованием PSK.
---

# Подключение Cisco IOS и Ideco NGFW по IPsec в туннельном режиме

Рассмотрим настройку подключения по схеме ниже:

![](/.gitbook/assets/connect-utm-to-cisco-via-ipsec1.png)

Адресация:

* `172.16.2.172/24` - внешний IP-адрес NGFW.
* `192.168.18.18/24` - локальный IP-адрес NGFW.
* `172.16.2.171/24` - внешний IP-адрес Cisco.
* `192.168.17.17/24` - локальный IP-адрес Cisco.

Для настройки подключения Cisco IOS к Ideco NGFW следуйте инструкции ниже.

<details>

<summary>Первоначальная настройка Ideco NGFW и Cisco IOS</summary>

## Настройка Ideco NGFW

Настройте на Ideco NGFW локальный и внешний интерфейсы. Подробная информация находится в статье [Первоначальная настройка](/installation/initial-setup.md).

## Настройка Cisco IOS XE

Настроить Cisco можно, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://cisco.ideco.ru/](https://cisco.ideco.ru).

Для настройки Cisco через консоль выполните действия:

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

4\. Создайте access-list с адресацией локальной сети:

```
ip access-list extended NAT
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit
```

5\. Настройте NAT:

```
ip nat inside source list NAT interface GigabitEthernet1 overload
exit
```

6\. Сохраните настройки конфигурации:

```
write memory
```

7\. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в интернет.**

Для этого перейдите на какой-нибудь сайт (например: [https://www.cisco.com/](https://www.cisco.com)) с устройства в локальной сети Cisco.

</details>

{% hint style="danger" %}
В некоторых версиях Cisco передает внешний IP-адрес вместо **KeyID** (проверьте, включив расширенный лог IPsec на Cisco). При настройке подключения от таких роутеров к Ideco NGFW в качестве **Идентификатора удаленной стороны** укажите внешний IP-адрес Cisco, в качестве **Типа идентификатора** - auto.
{% endhint %}

## Подключение от Ideco NGFW к Cisco

<details>

<summary>Настройка IPsec на Cisco</summary>

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

3\. Создайте peer:

```
crypto ikev2 keyring key
peer strongswan
address <внешний IP NGFW>
pre-shared-key local <psk>
pre-shared-key remote <psk>
exit
exit
```

4\. Создайте IKEv2 profile:

```
crypto ikev2 profile ikev2profile
match identity remote key-id <key-id>
authentication remote pre-share
authentication local pre-share
keyring local key
exit
```

5\. Настройте шифрование в ESP:

```
crypto ipsec transform-set TS esp-gcm 256
mode tunnel
exit
```

6\. Создайте ipsec-isakmp:

```
crypto map cmap 10 ipsec-isakmp
set peer <внешний IP NGFW>
set transform-set TS
set ikev2-profile ikev2profile
match address cryptoacl
reverse-route
exit
```

7\. Настройте crypto map на внешнем интерфейсе:

```
interface GigabitEthernet1
crypto map cmap
exit
```

8\. Создайте access-list для трафика между локальными сетями Cisco и NGFW:

```
ip access-list extended cryptoacl
permit ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
exit
```

9\. Добавьте в access-list NAT исключения трафика между локальными сетями Cisco и NGFW (правило `deny` должно оказаться выше, чем `permit`):

```
ip access-list extended NAT
no permit ip <локальная подсеть Cisco> <обратная маска подсети> any
deny ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit

end
```

10\. Сохраните настройки конфигурации:

```
write memory
```

</details>

<details>

<summary>Настройка исходящего подключения на Ideco NGFW</summary>

Для настройки исходящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Исходящие подключения**.

2\. Добавьте новое подключение:

![](/.gitbook/assets/ipsec25.png)

   * **Название** - любое.
   * **Зона** - укажите зону для добавления IPSec подключения.
   * **Режим работы** - выберите **Туннельный**.
   * **Адрес удаленного устройства** - введите IP-адрес Cisco.
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса туннеля. Поле необязательное, заполняется при настройке BGP-соседства для динамической маршрутизации и для получения статистики обмена пакетами.
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса туннеля Cisco. Поле необязательное. Для получения статистики о потере пакетов, средней задержке и джиттере заполните поля **IP-адрес интрефейса туннеля** и **Удаленный IP-адрес туннеля**. Они должны находиться в одной подсети.
   * **Автоматическое создание маршрутов** - включите опцию.
   * **Домашние локальные сети** - укажите локальную сеть Ideco NGFW.
   * **Удаленные локальные сети** - укажите локальную сеть Cisco.
   * **Тип аутентификации** - PSK.
   * **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется, чтобы настроить подключение в Cisco.
   * **Идентификатор NGFW** - введенный ключ будет использоваться для идентификации исходящего подключения. Введите также этот идентификатор в Cisco.
   * **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено и используется (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Используется**).

5\. Проверьте наличие трафика между локальными сетями.

</details>

Итоговая конфигурация IKEv2 IPsec на Cisco IOS должна выглядеть следующим образом:

<details>

<summary>Для подключения от Ideco NGFW к Cisco</summary>

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
   address <внешний IP NGFW>
   pre-shared-key local <psk>
   pre-shared-key remote <psk>

crypto ikev2 profile ikev2profile
  match identity remote key-id <key-id>
  authentication remote pre-share
  authentication local pre-share
  keyring local key

crypto ipsec transform-set TS esp-gcm 256
 mode tunnel

crypto map cmap 10 ipsec-isakmp
 set peer <внешний IP NGFW>
 set transform-set TS
 set ikev2-profile ikev2profile
 match address cryptoacl
 reverse-route

interface GigabitEthernet1
! внешний интерфейс
 ip address <внешний IP Cisco> <маска подсети>
 ip nat outside
 negotiation auto
 no mop enabled
 no mop sysid
 crypto map cmap

interface GigabitEthernet2
! локальный интерфейс
 ip address <локальный IP Cisco> <маска подсети>
 ip nat inside
 negotiation auto
 no mop enabled
 no mop sysid

ip nat inside source list NAT interface GigabitEthernet1 overload

ip access-list extended NAT
 deny   ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
 permit ip <локальная подсеть Cisco> <обратная маска подсети> any
ip access-list extended cryptoacl
 permit ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
```

</details>

## Подключение от Cisco к Ideco NGFW

<details>

<summary>Настройка IPsec на Cisco</summary>

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

3\. Создайте peer:

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

4\. Создайте IKEv2 profile:

```
crypto ikev2 profile ikev2profile
match identity remote address <внешний IP NGFW> 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local key
exit
```

5\. Настройте шифрование в ESP:

```
crypto ipsec transform-set TS esp-gcm 256
mode tunnel
exit
```

6\. Создайте ipsec-isakmp:

```
crypto map cmap 10 ipsec-isakmp
set peer <внешний IP NGFW>
set transform-set TS
set ikev2-profile ikev2profile
match address cryptoacl
reverse-route
exit
```

7\. Настройте crypto map на внешнем интерфейсе:

```
interface GigabitEthernet1
crypto map cmap
exit
```

8\. Создайте access-list для трафика между локальными сетями Cisco и NGFW:

```
ip access-list extended cryptoacl
permit ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
exit
```

9\. Добавьте в access-list NAT исключения трафика между локальными сетями Cisco и NGFW (правило `deny` должно оказаться выше чем `permit`):

```
ip access-list extended NAT
no permit ip <локальная подсеть Cisco> <обратная маска подсети> any
deny ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
permit ip <локальная подсеть Cisco> <обратная маска подсети> any
exit

end
```

10\. Сохраните настройки конфигурации:

```
write memory
```

</details>

<details>

<summary>Настройка входящего подключения на Ideco NGFW</summary>

Для настройки входящего IPsec-подключения на Ideco NGFW выполните действия:

1\. В веб-интерфейсе Ideco NGFW откройте вкладку **Сервисы -> IPsec -> Устройства (входящие подключения)**.

2\. Добавьте новое подключение:

![](/.gitbook/assets/ipsec26.png)

   * **Название** - любое.
   * **Зона** - укажите зону для добавления IPSec-подключения.
   * **Режим работы** - выберите **Туннельный**.
   * **IP-адрес интерфейса туннеля** - укажите IP-адрес интерфейса туннеля. Поле необязательное, заполняется при настройке BGP-соседства для динамической маршрутизации и для получения статистики обмена пакетами.
   * **Удаленный IP-адрес туннеля** - укажите IP-адрес интерфейса туннеля Cisco. Поле необязательное. Для получения статистики о потере пакетов, средней задержке и джиттере заполните поля **IP-адрес интрефейса туннеля** и **Удаленный IP-адрес туннеля**. Они должны находиться в одной подсети. заполняется для получения статистики обмена пакетами.
   * **Автоматическое создание маршрутов** - включите опцию. 
   * **Домашние локальные сети** - укажите локальную сеть Ideco NGFW.
   * **Удаленные локальные сети** - укажите локальную сеть Cisco.
   * **Тип аутентификации** - PSK.
   * **PSK** - укажите PSK-ключ.
   * **Тип идентификатора** - keyid или auto, если Cisco передает IP-адрес вместо key-id.
   * **Идентификатор удаленной стороны** - вставьте идентификатор Cisco (параметр Key ID) или IP-адрес Cisco, если Cisco передает IP-адрес вместо key-id.
   * **Индекс интерфейса для Netflow** - введите индекс для идентификации интерфейса (целое число от 0 до 65535), если используете Netflow.

3\. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4\. Проверьте, что подключение установлено и используется (в столбце **Статусы** зеленым цветом будет подсвечена надпись **Используется**).

5\. Проверьте наличие трафика между локальными сетями.

</details>

Итоговая конфигурация IKEv2 IPsec на Cisco IOS должна выглядеть следующим образом:

<details>

<summary>Для подключения от Cisco к Ideco NGFW</summary>

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
   address <внешний IP NGFW>
   identity key-i <key-id> # Если Cisco передает IP вместо key-id, то identity address <внешний IP-адрес Cisco>
   pre-shared-key local <psk>
   pre-shared-key remote <psk>

crypto ikev2 profile ikev2profile
  match identity remote address <внешний IP NGFW> 255.255.255.255
  authentication remote pre-share
  authentication local pre-share
  keyring local key

crypto ipsec transform-set TS esp-gcm 256
 mode tunnel

crypto map cmap 10 ipsec-isakmp
 set peer <внешний IP NGFW>
 set transform-set TS
 set ikev2-profile ikev2profile
 match address cryptoacl
 reverse-route

interface GigabitEthernet1
! внешний интерфейс
 ip address <внешний IP Cisco> <маска подсети>
 ip nat outside
 negotiation auto
 no mop enabled
 no mop sysid
 crypto map cmap

interface GigabitEthernet2
! локальный интерфейс
 ip address <локальный IP Cisco> <маска подсети>
 ip nat inside
 negotiation auto
 no mop enabled
 no mop sysid

ip nat inside source list NAT interface GigabitEthernet1 overload

ip access-list extended NAT
 deny   ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
 permit ip <локальная подсеть Cisco> <обратная маска подсети> any
ip access-list extended cryptoacl
 permit ip <локальная подсеть Cisco> <обратная маска подсети> <локальная подсеть NGFW> <обратная маска подсети>
```

</details>
