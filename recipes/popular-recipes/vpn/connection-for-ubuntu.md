# Создание VPN-подключения в Ubuntu

{% hint style="info" %}
Перед настройкой VPN-подключения, перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

{% hint style="warning" %}
Инструкция актуальна для версии Ubuntu 24.04 LTS.
{% endhint %}

<details>

<summary>Протокол PPTP</summary>

Перед созданием подключения в Ubuntu перейдите в Ideco NGFW, в раздел **Пользователи -> VPN-подключения -> Основное** и установите флаг **Подключение по PPTP**:

<img src="/.gitbook/assets/vpn-authorization4.png" alt="" data-size="original">

**Создание подключения в Ubuntu**

1\. Перейдите **Настройки -> Сети** и в строке **VPN** нажмите ![](/.gitbook/assets/icon-add.png):

<img src="/.gitbook/assets/connection-for-ubuntu1.png" alt="" data-size="original">

2\. В окне создания подключений выберите пункт **Туннельный протокол типа точка-точка (PPTP)**:

<img src="/.gitbook/assets/connection-for-ubuntu2.png" alt="" data-size="original">

3\. В разделе **Идентификация** заполните следующие поля:

<img src="/.gitbook/assets/connection-for-ubuntu3.png" alt="" data-size="original">

* **Название** - имя подключения;
* **Шлюз** - доменное имя или IP-адрес интерфейса NGFW;
* **Имя пользователя** - имя пользователя, которому разрешено подключение по VPN;
* **Пароль** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения;
* **NT-домен** - оставьте поле пустым.

Рекомендуем нажать **Дополнительно** и установить флаги на пунктах:

<img src="/.gitbook/assets/connection-for-ubuntu4.png" alt="" data-size="original">

* **Разрешить следующие методы аутентификации** - установите флаг на пункте _MSCHAPv2_;
* **Использовать шифрование MPPE** - в строке _Шифрование_ выберите 128-бит (наиболее защищенное);
* **Использовать для данных сжатие BSD** - использование алгоритма BSD-compress;
* **Использовать для данных сжатие Deflate** - использование алгоритма Deflate;
* **Использовать сжатие заголовков TCP** - использование метода сжатия заголовков TCP/IP Вана Якобсона.

4\. Нажмите **ОК** и **Добавить**.

5\. Перевести опцию созданного VPN-подключения в положение включен:

<img src="/.gitbook/assets/connection-for-ubuntu5.png" alt="" data-size="original">

</details>

<details>

<summary>Протокол IKEv2/IPsec</summary>

Перед созданием подключения в Ubuntu настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг **Подключение по IKEv2/IPsec** и заполните поле **Домен и IP-адрес**:

<img src="/.gitbook/assets/vpn-authorization2.png" alt="" data-size="original">

3\. Скачайте корневой сертификат одним из способов:

* В личном кабинете, введя логин/пароль пользователя:

    <img src="/.gitbook/assets/user-personal-account6.png" alt="" data-size="original">
* В разделе **Сервисы -> Сертификаты -> Загруженные сертификаты**:

    <img src="/.gitbook/assets/certs3.png" alt="" data-size="original">

Корневой сертификат потребуется для настройки подключения рабочей станции пользователя, если не был получен корневой сертификат через Let\`s Encrypt. При необходимости перенесите файл сертификата на рабочую станцию.\
Если для VPN-подключения используется сертификат, выданный Let\`s Encrypt, то установка корневого сертификата на устройство не требуется.

**Создание подключения в Ubuntu**

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 и выполните команду:

```bash
sudo apt install -y network-manager-strongswan libcharon-extra-plugins libstrongswan-extra-plugins
```

2\. После окончания установки перезагрузите компьютер:

```bash
sudo reboot
```

3\. Перейдите в терминале в директорию с загруженным корневым сертификатом (если на доменное имя NGFW выпущен Let`s Encrypt сертификат, сразу перейдите к пункту 6).

4\. Установите корневой сертификат NGFW в доверенные сертификаты Ubuntu:

```bash
sudo cp ca.crt /usr/local/share/ca-certificates/ca.crt
```

* `ca.crt` - имя скачанного сертификата.

5\. Для обновления сертификатов устройства выполните команду:

```bash
sudo update-ca-certificates
```

6\. Перейдите в **Настройки -> Сети** и в строке **VPN** нажмите ![](/.gitbook/assets/icon-add.png):

<img src="/.gitbook/assets/connection-for-ubuntu1.png" alt="" data-size="original">

7\. В появившемся окне выберите **IPsec\IKEv2 (strongswan)**:

<img src="/.gitbook/assets/connection-for-ubuntu6.png" alt="" data-size="original">

8\. В разделе **Идентификация** и заполните следующие поля:

<img src="/.gitbook/assets/connection-for-ubuntu7.png" alt="" data-size="original">

* **Название** - имя подключения;
* **Address** - введите домен, который указан в настройках **Пользователи -> VPN-подключения -> Основное -> Подключение по IKEv2/IPsec**;
* **Authentication** - рекомендуем выбрать EAP;
* **Username** - имя пользователя, которому разрешено подключение по VPN;
* **Password** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения.

Установите флаг **Request an inner IP address** и нажмите **Добавить**.

9\. Включите созданное VPN-подключение.

</details>

<details>

<summary>Протокол SSTP</summary>

Перед созданием подключения в Ubuntu настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг **Подключение по SSTP** и заполните поля **Домен** и **Порт**:

<img src="/.gitbook/assets/vpn-authorization5.png" alt="" data-size="original">

**Создание подключения в Ubuntu**

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+F1 и выполните две команды:

```
sudo apt-add-repository ppa:eivnaes/network-manager-sstp
sudo apt install -y network-manager-sstp sstp-client 
```

2\. После окончания установки перезагрузите компьютер:

```
sudo reboot
```

3\. После окончания установки пакетов, перейдите в **Настройки -> Сети** и в строке **VPN** нажмите ![](/.gitbook/assets/icon-add.png):

<img src="/.gitbook/assets/connection-for-ubuntu1.png" alt="" data-size="original">

4\. В появившемся окне выберите **Туннельный протокол типа точка-точка (SSTP)**:

<img src="/.gitbook/assets/connection-for-ubuntu8.png" alt="" data-size="original">

5\. В разделе **Идентификация** и заполните следующие поля:

<img src="/.gitbook/assets/connection-for-ubuntu9.png" alt="" data-size="original">

* **Название** - имя подключения;
* **Шлюз** - укажите в формате _домен:\[порт, выбранный на NGFW]_;
* **Имя пользователя** - имя пользователя, которому разрешено подключение по VPN;
* **Пароль** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения;
* **NT-домен** - оставьте поле пустым.

Рекомендуем нажать **Advanced** и установить флаги на пунктах:

* **Разрешить следующие методы аутентификации** - установите флаг на пункте _MSCHAPv2_;
* **Использовать для данных сжатие BSD** - использование алгоритма BSD-compress;
* **Использовать для данных сжатие Deflate** - использование алгоритма Deflate;
* **Использовать сжатие заголовков TCP** - использование метода сжатия заголовков TCP/IP Вана Якобсона.

6\. Нажмите **Добавить** и переведите опцию созданного VPN-подключения в положение включен:

<img src="/.gitbook/assets/connection-for-ubuntu10.png" alt="" data-size="original">

</details>

<details>

<summary>Протокол L2TP/IPsec</summary>

**Важно:** L2TP IPsec клиенты, находящиеся за одним NAT'ом, могут испытывать проблемы подключения, если их более одного. Рекомендуем вместо L2TP IPsec использовать IKEv2 IPsec.

Перед созданием подключения настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг **Подключение по L2TP/IPsec** и скопируйте **PSK**-ключ:

<img src="/.gitbook/assets/vpn-authorization3.png" alt="" data-size="original">

**Создание подключения в Ubuntu**

1\. Подключите репозиторий, в котором находятся необходимые пакеты для создания L2TP VPN-соединения, а затем обновите информацию о репозиториях. Для этого выполните следующие команды:

```
sudo add-apt-repository ppa:nm-l2tp/network-manager-l2tp
sudo apt update
```

2\. Установите дополнение к стандартному NetworkManager с помощью двух пакетов:

```
sudo apt install -y network-manager-l2tp network-manager-l2tp-gnome
```

3\. После окончания установки перезагрузите компьютер:

```
sudo reboot
```

4\. После окончания установки пакетов перейдите в **Настройки -> Сети** и в строке **VPN** нажмите ![](/.gitbook/assets/icon-add.png):

<img src="/.gitbook/assets/connection-for-ubuntu1.png" alt="" data-size="original">

5\. В окне создания подключений по VPN выберите пункт **Layer 2 Tunneling Protocol (L2TP)**:

<img src="/.gitbook/assets/connection-for-ubuntu11.png" alt="" data-size="original">

6\. На вкладке **Идентификация** заполните следующие поля:

<img src="/.gitbook/assets/connection-for-ubuntu12.png" alt="" data-size="original">

* **Название** - имя подключения;
* **Шлюз** - доменное имя или IP-адрес интерфейса NGFW;
* **Тип** - Password-аутентификация по пользователю и паролю;
* **Имя пользователя** - имя пользователя, которому разрешено подключение по VPN;
* **Пароль** - пароль пользователя. В правой части поля необходимо выбрать вариант хранения для пароля от VPN-соединения;
* **NT-домен** - оставьте поле пустым.

7\. Перейдите в **Настройки IPsec** и включите опцию **Enable IPsec tunnel to L2TP host**, чтобы активировалась возможность настраивать остальные параметры:

<img src="/.gitbook/assets/connection-for-ubuntu13.png" alt="" data-size="original">

* **Type: Pre-shared key (PSK)** - аутентификация по общему ключу;
* **Pre-shared key** - ключ, который необходимо скопировать по пути **Пользователи -> VPN-подключения -> Основное** из поля **PSK**.

Раздел **Advanced** необязательный для заполнения.

После окончания настройки **L2TP IPsec Options** нажмите **ОК**.

8\. При необходимости перейдите в **Настройки РРР** и настройте раздел **Аутентификация**, **Шифрование и сжатие** и **Прочие**:

<img src="/.gitbook/assets/connection-for-ubuntu14.png" alt="" data-size="original">

После настройки **Параметры РРР** нажмите **ОК** и **Применить**.

9\. Переведите опцию созданного VPN-подключения в положение включен:

<img src="/.gitbook/assets/connection-for-ubuntu15.png" alt="" data-size="original">

</details>
