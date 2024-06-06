# Подключение MikroTik и Ideco NGFW по L2TP/IPsec и IKev2/IPsec

## Подключение MikroTik к Ideco NGFW по L2TP/IPsec

Настройте подключение, выполнив команды:

1\. Отредактируйте IPsec profile:

```
ip ipsec profile set default hash-algorithm=sha1 enc-algorithm=aes-256 dh-group=modp2048
```

2\. Отредактируйте IPsec proposals:

```
ip ipsec proposal set default auth-algorithms=sha1 enc-algorithms=aes-256-cbc,aes-192-cbc,aes-128-cbc pfs-group=modp2048
```

3\. Создайте подключение к Ideco NGFW:

```
interface l2tp-client add connect-to=<server> profile=default disabled=no name=<interface_name> password="<password>" user="<login>" use-ipsec="yes" ipsec-secret="<psk>"
```

4\. Добавьте маршрут до первого адреса VPN-cети NGFW (remote VPN subnet):

```
ip route add dst-address=<remote VPN subnet> gateway=l2tp-out1
```

{% hint style="info" %}
Для работы удаленных сетей на NGFW и на MikroTik нужно создавать маршруты на обоих устройствах.
{% endhint %}

{% hint style="info" %}
Если у вас в разделе **Правила трафика -> Файрвол -> SNAT** отключен **Автоматический SNAT локальных сетей**, то может понадобиться прописать маршрут до сети VPN, где шлюзом является NGFW.

Пример:

* Aдрес NGFW = `169.254.1.5`
* Первый адрес VPN = `10.128.0.1`

`ip route add dst-address=169.254.1.5 gateway==10.128.0.1`
{% endhint %}

## Подключение Mikrotik к Ideco NGFW по IKev2/IPsec

1\. Откройте WinBox.

2\. Перейдите в терминал, нажав `new terminal`:

![](/.gitbook/assets/utm-to-mikrotik-vpn.png)

3\. Загрузите сертификат выполнив команды:

```
/tool fetch url="https://letsencrypt.org/certs/letsencryptauthorityx1.pem" dst-path=letsencryptauthorityx1.pem
/tool fetch url="https://letsencrypt.org/certs/lets-encrypt-r3.pem" dst-path=lets-encrypt-r3.pem
```

4\. Импортируйте сертификат выполнив команды:

```
/certificate import file-name=isrgrootx1.pem passphrase="" name=lisrgrootx1.pem
/certificate import file-name=lets-encrypt-r3.pem passphrase="" name=lets-encrypt-r3
```

5\. Настройте алгоритмы шифрования для IPsec step 1 (IKE):

```
/ip ipsec profile add dh-group=modp4096,modp2048,modp1024 dpd-interval=2m dpd-maximum-failures=5 enc-algorithm=aes-256,aes-192,aes-128 hash-algorithm=sha256 lifetime=1d name=IKEv2_TO_NGFW nat-traversal=yes proposal-check=obey
```

6\. Настройте алгоритмы шифрования для IPsec step 2 (ESP):

```
/ip ipsec proposal add auth-algorithms=sha512,sha256,sha1 disabled=no enc-algorithms="aes-256-cbc,aes-256-ctr,aes-256-gcm,aes-192-cbc,aes-192-gcm,aes-128-cbc,aes-128-ctr,aes-128-gcm" lifetime=30m name=IKev2_to_NGFW pfs-group=modp1024
```

7\. Настройте одноранговый узел. В качестве `address` укажите доменное имя, которое используется для IKev2 подключения:

```
/ip ipsec peer add address={ideco.test.ru} disabled=no exchange-mode=ike2 name=IKEV2_TO_NGFW profile=IKEv2_TO_NGFW send-initial-contact=yes
```

8\. Создайте группу, которая будет использоваться для автоматического NAT:

```
/ip ipsec policy group add name=IKEv2_TO_NGFW
```

9\. Создайте address-list в котором находятся Удаленные сети NGFW. Если за NGFW несколько подсетей, то нужно создавать несколько элементов в списке: 

```
/ip firewall address-list add address={1.2.3.0/24} disabled=no list=Behind_NGFW_Gateway
```

10\. Создайте новую запись конфигурации режима с ответчиком `= no`, которая будет запрашивать параметры конфигурации с сервера:

```
/ip ipsec mode-config add connection-mark=no-mark name=IKEv2_TO_NGFW responder=no src-address-list=Behind_NGFW_Gateway use-responder-dns=yes
```

11\. Создайте политику, которая придет с NGFW (в виде шаблона):

```
/ip ipsec policy add disabled=no dst-address=0.0.0.0/0 group=IKEv2_TO_NGFW proposal=IKEv2_TO_NGFW protocol=all src-address=0.0.0.0/0 template=yes
```

12\. Создайте профиль идентификации пользователя:

```
/ip ipsec identity add auth-method=eap certificate="" disabled=no eap-methods=eap-mschapv2 generate-policy=port-strict mode-config=IKEv2_TO_NGFW peer=IKEV2_TO_NGFW policy-template-group=IKEv2_TO_NGFW username=<'login'> password=<'password'> 
```

13\. Перейдите в веб-интерфейс NGFW в раздел **Пользователи —> VPN подключения** и в строке **Сеть для VPN-подключений** добавьте первый адрес сети VPN:

![](/.gitbook/assets/utm-to-mikrotik-vpn1.png)

14\. Создайте маршрут до удаленных сетей NGFW через интерфейс, который смотрит в интернет.

```
/ip route add disabled=no dst-address={10.128.0.0/16} gateway=ether1 routing-table=main
```

* где в качестве gateway={ether1} - интерфейс, который выходит в интернет.