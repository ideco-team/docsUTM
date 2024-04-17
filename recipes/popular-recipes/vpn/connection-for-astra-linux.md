# Инструкция по созданию подключения в Astra Linux

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

Перед созданием подключения в Astra Linux, настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключение -> Основное**.

2\. Установите флаг в строке с нужным подключением и, если требуется, заполните дополнительные поля или скопируйте **PSK**-ключ.

<details>

<summary>Протокол L2TP/IPsec</summary>

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 и выполните три команды:

    sudo apt update
    sudo apt install network-manager-l2tp-gnome
    sudo reboot

2\. В трее (в настройках сети) выберите **Соединение VPN -> Добавить VPN-соединение**:

![](/.gitbook/assets/tray.png)

3\. Выберите тип соединения **Layer 2 Tunneling Protocol (L2TP)** и нажмите **Создать**:

![](/.gitbook/assets/tray2.png)

4\. В разделе **VPN** заполните поля:

* **Шлюз** - IP-адрес внешнего интерфейса Ideco NGFW или домен;
* **Имя пользователя** - например, *test*;
* **Пароль** .
  
![](/.gitbook/assets/tray3.png)

5\. Нажмите **Настройки IPsec**.

6\. Заполните поля:

* **Pre-shared key** - PSK-ключ из настроек Ideco NGFW (**Пользователи -&gt; VPN-подключение -&gt; Основное**);
* **Phase1** - алгоритм aes256-sha512-modp2048,aes256-sha512-modp1024,aes256-sha1-ecp256,aes256-sha1-modp2048,aes256-sha1-modp1024! \*;
* **Phase2** - алгоритмы aes256-sha512-modp2048,aes256-sha256-modp2048,aes256-sha1-modp2048,aes128-sha1-modp2048,aes256-sha512-modp1024,aes256-sha256-modp1024,aes256-sha1-modp1024,aes128-sha1-modp1024,aes256-sha512,aes256-sha256,aes256-sha1,aes128-sha1! \* 
  
    \* Обязательно поставьте восклицательный знак в конце строки.

Так как Astra Linux по умолчанию запрашивает не самые защищенные алгоритмы, рекомендуем заполнить их самостоятельно.

7\. Нажмите **OК**, затем **Сохранить**.

Далее в трее (в настройках сети) **Соединение VPN** появится VPN-подключение. Для активации установите галку **VPN-соединение**:

![](/.gitbook/assets/tray6.png)

</details>

<details>

<summary>Протокол IKEv2/IPsec</summary>

Перед настройкой подключения по протоколу IKEv2 установите корневой сертификат NGFW на устройство пользователя. Скачать сертификат можно одним из способов:

*   В личном кабинете, введя логин/пароль пользователя:

    <img align="left" src="/.gitbook/assets/ubuntu16.png" alt="" data-size="original">
    
*   В разделе **Сервисы -> Сертификаты**:

    <img align="left" src="/.gitbook/assets/certificates3.png" alt="" data-size="original">

**Создание подключения в Astra Linux**

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 и выполните две команды:
    
    sudo apt install libcharon-extra-plugins
    sudo apt install -y network-manager-strongswan libcharon-extra-plugins libstrongswan-extra-plugins

2\. После окончания установки перезагрузите компьютер:

    sudo reboot

3\. В трее (в настройках сети) выберите **Соединение VPN -> Добавить VPN-соединение**:

![](/.gitbook/assets/tray.png)

4\. Выберите тип соединения **IPsec/IKEv2(strongswan)** и нажмите **Создать**:

![](/.gitbook/assets/tray7.png)

5\. В разделе **VPN** и заполните следующие поля:

* **Имя соединения** - имя подключения;
* **Address** - введите домен, который указан в настройках **Пользователи -&gt; VPN-подключение -&gt; Основное -&gt; Подключение по IKEv2/IPsec**;
* **Certificate** - выберите ранее сохраненный корневой сертификат (если он не был выдан Let`s Encrypt);
* **Authentication** - рекомендуем выбрать EAP;
* **Username** - имя пользователя, которому разрешено подключение по VPN;
* **Password** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения.

Установите флаг **Request an inner IP address** и нажмите **Добавить:**

![](/.gitbook/assets/tray8.png)

6\. В трее (в настройках сети) выберите **Соединение VPN** и установите флаг в строке с созданным соединением.

</details>

{% hint style="info" %}
Перепроверить способы шифрования можно в конфигурации NGFW: \
откройте терминал NGFW и проверьте командой:  
**`cat /etc/strongswan/swanctl/conf.d/road_warriors.conf`**
* для Phase1 Algorithm ищите значения “proposals=”;
* для Phase2 Algorithms ищите значения “esp_proposals=”.
{% endhint %}