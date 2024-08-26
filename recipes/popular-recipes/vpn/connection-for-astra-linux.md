# Инструкция по созданию подключения в Astra Linux

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

Перед созданием подключения в Astra Linux, настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг в строке c нужным подключением и, если требуется, заполните дополнительные поля или скопируйте **PSK**-ключ.

<details>

<summary>Протокол L2TP/IPsec</summary>

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 или через путь **Пуск -> Системные -> Терминал Fly** и выполните три команды:
```
sudo apt update
sudo apt install network-manager-l2tp-gnome
sudo reboot
```

2\. В трее (в настройках сети) выберите **Соединение VPN -> Добавить VPN-соединение**:

![](/.gitbook/assets/connection-for-astra-linux1.png)

3\. Выберите тип соединения **Layer 2 Tunneling Protocol (L2TP)** и нажмите **Создать**:

![](/.gitbook/assets/connection-for-astra-linux2.png)

4\. На вкладке **VPN** заполните поля:

![](/.gitbook/assets/connection-for-astra-linux3.png)

* **Шлюз** - IP-адрес внешнего интерфейса Ideco NGFW или домен;
* **Имя пользователя**;
* **Пароль**.

5\. Нажмите **Настройки IPsec**.

6\. Заполните поля:

![](/.gitbook/assets/astra3.png)

* **Gateway ID** - IP-адрес интерфейса, к которому осуществляется подключение;
* **Pre-shared key** -  PSK-ключ из настроек Ideco NGFW (**Пользователи -&gt; VPN-подключение -&gt; Основное**);
* **Phase1 Algorithm** - `aes256-sha512-modp2048,aes256-sha512-modp1024,aes256-sha1-ecp256,aes256-sha1-modp2048,aes256-sha1-modp1024!`; \*
* **Phase2 Algorithms** - `aes256-sha512-modp2048,aes256-sha256-modp2048,aes256-sha1-modp2048,aes128-sha1-modp2048,aes256-sha512-modp1024,aes256-sha256-modp1024,aes256-sha1-modp1024,aes128-sha1-modp1024,aes256-sha512,aes256-sha256,aes256-sha1,aes128-sha1!`.\*
  
    \* Обязательно поставьте восклицательный знак в конце строки.

Так как Astra Linux по умолчанию запрашивает не самые защищенные алгоритмы, рекомендуем заполнить их самостоятельно.

7\. При необходимости перейдите в Настройки РРР и настройте разделы **Аутентификация**, **Шифрование и сжатие**, **Прочее**:

![](/.gitbook/assets/astra4.png)

8\. Нажмите **OК**, затем **Сохранить**.

Далее в трее (в настройках сети) **Соединение VPN** появится VPN-подключение. Для активации установите галку **VPN-соединение**:

![](/.gitbook/assets/connection-for-astra-linux4.png)

</details>

{% hint style="info" %}
Проверить способы шифрования можно в конфигурации NGFW. Для этого включите в настройках VPN "Подключение по IKEv2/IPsec", откройте терминал NGFW и введите команду:  
**`cat /run/ideco-ipsec-backend/strongswan/swanctl/conf.d/rw_ikev2.conf`**
* для Phase1 Algorithm ищите значения “proposals=”;
* для Phase2 Algorithms ищите значения “esp_proposals=”.
{% endhint %}

<details>

<summary>Протокол IKEv2/IPsec</summary>

Перед настройкой подключения по протоколу IKEv2 установите корневой сертификат NGFW на устройство пользователя. Скачать сертификат можно одним из способов по [ссылке](/installation/initial-setup.md).

**Создание подключения в Astra Linux**

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 или через путь **Пуск -> Системные -> Терминал Fly** и выполните три команды:

``` 
sudo apt install libcharon-extra-plugins
sudo apt install -y network-manager-strongswan libcharon-extra-plugins libstrongswan-extra-plugins
sudo reboot
```

2\. В трее (в настройках сети) выберите **Соединение VPN -> Добавить VPN-соединение**:

![](/.gitbook/assets/connection-for-astra-linux1.png)

3\. Выберите тип соединения **IPsec/IKEv2 (strongswan)** и нажмите **Создать**:

![](/.gitbook/assets/connection-for-astra-linux5.png)

4\. На вкладке **VPN** заполните следующие поля:

![](/.gitbook/assets/astra1.png)

* **Имя соединения** - имя подключения;
* **Address** - введите домен, который указан в настройках **Пользователи -&gt; VPN-подключения -&gt; Основное -&gt; Подключение по IKEv2/IPsec**;
* **Certificate** - выберите ранее сохраненный корневой сертификат (если он не был выдан Let`s Encrypt);
* **Authentication** - рекомендуем выбрать EAP (Username/Password);
* **Username** - имя пользователя, которому разрешено подключение по VPN;
* **Password** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения.

Установите флаг **Request an inner IP address** и нажмите **Добавить**.

5\. В трее (в настройках сети) выберите **Соединение VPN** и установите флаг в строке с созданным соединением.

![](/.gitbook/assets/astra2.png)

</details>
