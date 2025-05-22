# Подключение MikroTik и Ideco NGFW по L2TP/IPsec

## Подключение MikroTik к Ideco NGFW по L2TP/IPsec

* Настройте VPN-сервер на Ideco NGFW в разделе **Пользователи -> VPN-подключения**. Подробная инструкция по настройке - в статье [Подключение по L2TP/IPsec](/settings/users/authorization/vpn-connection/l2tp-ipsec.md);

* Настройте подключение на MikroTik:

{% tabs %}

{% tab title="Веб-интерфейс" %}

1\. Перейдите в раздел **IP -> IPsec -> Profiles**, выберите профиль **default** и заполните поля:

![](/.gitbook/assets/mikrotik.png)

* **Hash Algorithms** - `sha1`.
* **Encryption Algorithm** - `aes-256`.
* **DH Group** - `modp2048`.

2\. Нажмите **OK**.

3\. Перейдите в раздел **IP -> IPsec -> Proposals**, выберите профиль **default** и заполните поля:

![](/.gitbook/assets/mikrotik1.png)

* **Auth. Algorithms** - `sha1`.
* **Encr. Algorithms** - `aes-256-cbc`, `aes-192-cbc`, `aes-128-cbc`.
* **PFS Group** - `modp2048`.

4\. Нажмите **OK**.

5\. Перейдите в раздел **Interfaces**, нажмите **New** и выберите **L2TP Client**.

6\. Заполните поля:

![](/.gitbook/assets/mikrotik2.png)

<details>
<summary>Расшифровка полей</summary>

* **Dial Out**:
  * **Connect To** - IP-адрес Ideco NGFW.
  * **User** - логин пользователя, которому разрешено подключение по VPN.
  * **Password** - пароль пользователя.
  * **Use IPsec** - включите опцию.
  * **IPsec Secret** - ключ, скопированный по пути **Пользователи -> VPN-подключения -> Основное** из поля **PSK**.
* **Advanced**:
  * **Allow** - `mschap2`.

</details>

7\. Нажмите **OK**.

8\. Перейдите в раздел **IP -> Routes** и проверьте, что маршрут создан:

![](/.gitbook/assets/mikrotik3.png)

{% endtab %}

{% tab title="Терминал" %}

1\. Отредактируйте IPsec profile:

{% code overflow="wrap" %}
```
ip ipsec profile set default hash-algorithm=sha1 enc-algorithm=aes-256 dh-group=modp2048
```
{% endcode %}

2\. Отредактируйте IPsec proposals:

{% code overflow="wrap" %}
```
ip ipsec proposal set default auth-algorithms=sha1 enc-algorithms=aes-256-cbc,aes-192-cbc,aes-128-cbc pfs-group=modp2048
```
{% endcode %}

3\. Создайте подключение к Ideco NGFW:

{% code overflow="wrap" %}
```
interface l2tp-client add connect-to=<server> profile=default disabled=no name=<interface_name> password="<password>" user="<login>" use-ipsec="yes" ipsec-secret="<psk>"
```
{% endcode %}

4\. Добавьте маршрут до первого адреса VPN-cети NGFW (remote VPN subnet):

{% code overflow="wrap" %}
```
ip route add dst-address=<remote VPN subnet> gateway=l2tp-out1
```
{% endcode %}

{% endtab %}

{% endtabs %}