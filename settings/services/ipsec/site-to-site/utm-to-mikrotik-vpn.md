# Подключение MikroTik и Ideco NGFW по L2TP/IPsec 

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

