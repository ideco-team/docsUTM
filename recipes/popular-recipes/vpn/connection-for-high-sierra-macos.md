# Инструкция по созданию подключения в Mac OS

{% hint style="info" %}
Перед настройкой VPN-подключения, перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.

Также установите корневой сертификат NGFW на устройство пользователя. Скачать сертификат можно одним из способов:

*   В личном кабинете, введя логин/пароль пользователя:

    <img align="left" src="/.gitbook/assets/user-personal-account6.png" alt="" data-size="original">
    
*   В разделе **Сервисы -> Сертификаты**:

    <img align="left" src="/.gitbook/assets/certs2.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

<details>

<summary>Протокол PPPoE</summary>

Для настройки Ideco NGFW перейдите в раздел **Пользователи -> VPN-подключения -> Основное** и установите флаг **Подключение по PPPoE**:

![](/.gitbook/assets/vpn-authorization1.png)

**Создание подключения в MacOS**

1\. Перейдите в раздел **Системные настройки -> Сеть**;

2\. Нажмите **Добавить** в левом нижнем углу (иконка ![](/.gitbook/assets/connection-for-high-sierra-macos1.png));

3\. В появившемся окне заполните поля:

<img src="/.gitbook/assets/connection-for-high-sierra-macos2.png" alt="" data-size="original">

* **Интерфейс** - PPPoE;
* **Ethernet** - например, Wi-Fi;
* **Имя службы** - имя подключения.

4\. Нажмите **Создать** и заполните:

<img src="/.gitbook/assets/connection-for-high-sierra-macos3.png" alt="" data-size="original">

* **Имя службы PPPoE** - имя службы;
* **Имя учетной записи** - логин;
* **Пароль** - пароль.

5\. Нажмите **Подключить**.

</details>

<details>

<summary>Протокол IKEv2/IPsec</summary>

Настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг **Подключение по IKEv2/IPsec** и заполните поля **Домен**:

<img src="/.gitbook/assets/vpn-authorization2.png" alt="" data-size="original">

**Создание подключения в MacOS**

1\. Перейдите в раздел **Системные настройки -> Сеть**:

2\. Нажмите **Добавить** в левом нижнем углу (иконка ![](/.gitbook/assets/connection-for-high-sierra-macos1.png));

3\. В появившемся окне заполните поля:

<img src="/.gitbook/assets/connection-for-high-sierra-macos4.png" alt="" data-size="original">

* **Интерфейс** - VPN;
* **Тип VPN** - IKEv2;
* **Имя службы** - имя подключения.

4\. Нажмите **Создать**;

5\. Установите параметры подключения:

<img src="/.gitbook/assets/connection-for-high-sierra-macos5.png" alt="" data-size="original">

* **Адрес сервера** - адрес VPN-сервера;
* **Удаленный ID** - продублируйте адрес VPN-сервера.

6\. Выберите **Настройки аутентификации**;

7\. Укажите идентификационные данные и нажмите **OK**:

<img src="/.gitbook/assets/connection-for-high-sierra-macos6.png" alt="" data-size="original">

* **Имя пользователя** - имя пользователя, которому разрешено подключение по VPN;
* **Пароль** - пароль пользователя.

8\. Нажмите **ОК**;

9\. Поставьте флаг в пункте **Показывать статус VPN в строке меню** и нажмите **Применить**.

</details>

<details>

<summary>Протокол L2TP/IPsec</summary>

**Важно:** L2TP IPsec-клиенты, находящиеся за одним NAT'ом, могут испытывать проблемы подключения, если их более одного. Рекомендуем вместо L2TP IPsec использовать IKEv2 IPsec.

Перед созданием подключения настройте Ideco NGFW:

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите флаг **Подключение по L2TP/IPsec** и скопируйте **PSK**-ключ:

<img src="/.gitbook/assets/vpn-authorization3.png" alt="" data-size="original">

**Создание подключения в MacOS**

1\. Перейдите в раздел **Системные настройки -> Сеть**:

<img src="/.gitbook/assets/connection-for-high-sierra-macos7.png" alt="" data-size="original">

2\. Нажмите **Добавить** в левом нижнем углу (иконка ![](/.gitbook/assets/connection-for-high-sierra-macos1.png));

3\. В появившемся окне заполните поля:

<img src="/.gitbook/assets/connection-for-high-sierra-macos8.png" alt="" data-size="original">

* **Интерфейс** - VPN;
* **Тип VPN** - L2TP через IPsec;
* **Имя службы** - имя подключения.

4\. Нажмите **Создать**;

5\. Заполните **Адрес сервера** и **Имя учетной записи**:

<img src="/.gitbook/assets/connection-for-high-sierra-macos9.png" alt="" data-size="original">

6\. Поставьте флаг на пункте **Показывать статус VPN в строке меню** и выберите **Настройки аутентификации**.

7\. В **Аутентификации пользователя** заполните **Пароль**, в **Аутентификации компьютера** - **Общий ключ (Shared Secret)**

<img src="/.gitbook/assets/connection-for-high-sierra-macos10.png" alt="" data-size="original">

8\. Нажмите **ОК -> Применить**.

Включите VPN-соединение:

* В левой верхней части экрана нажмите значок VPN-соединения (![](/.gitbook/assets/connection-for-high-sierra-macos12.png))
* Выберите _Подключить (имя службы, заданное в пункте 3)_:

    <img src="/.gitbook/assets/connection-for-high-sierra-macos11.png" alt="" data-size="original">

</details>
