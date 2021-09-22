---
description: >-
  По шагам данной статьи можно объединить сети Cisco и Ideco UTM по IPsec с
  использованием PSK.
---

# Входящее подключение Cisco IOS к Ideco UTM по IPSec

Рассмотрим настройку подключения по схеме, представленной на рисунке ниже:

![](../../../../.gitbook/assets/dia1.png)

## Шаг 1. Первоначальная настройка Ideco UTM 

Настройте UTM в режиме роутера \(наличие локального и [внешнего](../../../connection-to-provider/ethernet-connection.md) интерфейсов\).

## Шаг 2. Первоначальная настройка Cisco IOS EX

1. Настройка локального интерфейса:

```text
enable
conf t
interface GigabitEthernet2
ip address 10.80.211.100 255.255.255.0
no shutdown
ip nat inside
exit
```

2. Настройка внешнего интерфейса:

```text
interface GigabitEthernet1
ip address 172.16.200.100 255.255.255.0
no shutdown
ip nat outside
exit
```

3. **Проверьте наличие связи между внешними интерфейсами Ideco UTM и Cisco**.

4. Создание access-list с адресацией локальной сети:

```text
ip access-list extended NAT
permit ip 10.80.211.0 0.0.0.255 any
exit
```

4. Настройка NAT:

```text
ip nat inside source list NAT interface GigabitEthernet1 overload
exit
```

5. Сохранение настроек конфигурации:

```text
write memory
```

6. **После сохранения настроек проверьте, что из локальной сети Cisco присутствует доступ в сеть Интернет**.

## Шаг 3. Настройка IKEv2+IPSec на Cisco

1. Создание proposal:

```text
conf t
crypto ikev2 proposal ikev2proposal 
encryption aes-cbc-256
integrity sha256
group 19
exit
```

2. Создание policy:

```text
crypto ikev2 policy ikev2policy 
match fvrf any
proposal ikev2proposal
exit
```

3. Создание peer \(key\_id - идентификатор удаленной стороны, т.е. Ideco UTM\):

```text
crypto ikev2 keyring key
peer strongswan
address {внешний IP UTM-a}
identity key-id {key_id}
pre-shared-key local {psk}
pre-shared-key remote {psk}
exit
exit
```

4. Создание IKEv2 профиля:

```text
crypto ikev2 profile ikev2profile
match identity remote address {внешний IP UTM-a} 255.255.255.255 
authentication remote pre-share
authentication local pre-share
keyring local key 
exit
```

5. Настройка шифрования в esp:

```text
crypto ipsec transform-set TS esp-gcm 256 
mode tunnel
exit
```

6. Создание ipsec-isakmp:

```text
crypto map cmap 10 ipsec-isakmp 
set peer {внешний IP UTM-a}
set transform-set TS 
set ikev2-profile ikev2profile
match address cryptoacl
exit
```

7. Настройка crypto map на внешнем интерфейсе:

```text
interface GigabitEthernet1
crypto map cmap
exit
```

8. Создание access-list для трафика между локальными сетями Cisco и UTM:

```text
ip access-list extended cryptoacl
permit ip 10.80.211.0 0.0.0.255 192.168.211.0 0.0.0.255
exit
```

9. Добавление в access-list NAT исключения трафика между локальными сетями Cisco и UTM \(правило `deny` должно оказаться выше чем `permit`\):

```text
ip access-list extended NAT 
no permit ip 10.80.211.0 0.0.0.255 any
deny ip 10.80.211.0 0.0.0.255 192.168.211.0 0.0.0.255
permit ip 10.80.211.0 0.0.0.255 any
exit

end
```

10. Сохранение настроек конфигурации:

```text
write memory
```

## Шаг 4. Создание входящего IPSec подключения на UTM

1. В веб-интерфейсе Ideco UTM откройте вкладку **Сервисы -&gt; IPsec -&gt; Устройства**.

2. Добавьте новое подключение:

* **Название** – любое;
* **Тип** – входящее;
* **Тип аутентификации** – PSK;
* **PSK** – укажите PSK-ключ, который будет использоваться для подключения \(см. Шаг 3 пункт 3\);
* **Идентификатор ключа** – см. Шаг 3 пункт 3;
* **Домашние локальные сети** – укажите локальную сеть Ideco UTM;
* **Удалённые локальные сети** – укажите локальную сеть Cisco.

3. Сохраните созданное подключение, затем нажмите на кнопку **Включить**.

4. Проверьте, что подключение установлено.

5. Проверьте наличие трафика между локальными сетями \(TCP и web\).



