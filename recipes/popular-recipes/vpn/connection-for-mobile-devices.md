# Инструкция по созданию VPN-подключения на мобильных устройствах

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.

Также установите корневой сертификат NGFW на устройство пользователя. Скачать сертификат можно одним из способов:

* В личном кабинете, введя логин/пароль пользователя:

    <img align="left" src="/.gitbook/assets/user-personal-account6.png" alt="" data-size="original">
    
* В разделе **Сервисы -> Сертификаты**:

    <img align="left" src="/.gitbook/assets/certs1.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

<details>

<summary>Подключение через приложение StrongSwan</summary>

1\. Нажмите **Добавить VPN профиль**:

<img src="/.gitbook/assets/connection-for-mobile-devices1.png" alt="" data-size="original">

2\. Заполните поля:

* Сервер - домен, указанный в Ideco NGFW в разделе **Пользователи -> VPN-подключения -> Основное -> Подключение по IKEv2/IPsec**;
* VPN тип - IKEv2 EAP (Логин/Пароль);
* Логин - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="/.gitbook/assets/connection-for-mobile-devices2.png" alt="" data-size="original">

3\. Нажмите **Сохранить** и кликните по созданному подключению:

<img src="/.gitbook/assets/connection-for-mobile-devices3.png" alt="" data-size="original">

</details>

<details>

<summary>Подключение на Android</summary>

1\. Перейдите в **VPN** в раздел **Настройки -> Подключения -> Другие настройки**. При необходимости воспользуйтесь строкой поиска по настройкам.

2\. Выберите тип подключения и заполните следующие поля:

**Для PPTP:**

* Имя - имя подключения;
* Адрес сервера - адрес VPN-сервера;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="/.gitbook/assets/connection-for-mobile-devices4.png" alt="" data-size="original">

**Для IKEv2/IPsec MSCHAPv2:**

* Имя - имя подключения;
* Адрес сервера - адрес VPN-сервера;
* Идентификатор IPsec - логин пользователя;
* Сертификат сервера - "Принято от сервера";
* Сертификат ЦС IPsec - "Не проверять сервер";
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="/.gitbook/assets/connection-for-mobile-devices5.png" alt="" data-size="original">

**Для L2TP/IPsec PSK:**

* Имя - имя подключения;
* Адрес сервера - адрес VPN-сервера;
* Общий ключ IPsec - значение строки **PSK** в разделе **Пользователи -> VPN-подключения -> Основное -> Подключение по L2TP/IPsec**.

<img src="/.gitbook/assets/connection-for-mobile-devices6.png" alt="" data-size="original">

4\. Нажмите **Сохранить** и активируйте подключение.

</details>

<details>

<summary>Подключение на iOS</summary>

1\. Перейдите в раздел **Настройки -> Основные -> VPN**:

<img src="/.gitbook/assets/connection-for-mobile-devices7.png" alt="" data-size="original">

2\. Нажмите **Добавить конфигурацию VPN**:

<img src="/.gitbook/assets/connection-for-mobile-devices8.png" alt="" data-size="original">

3\. Выберите **Тип** подключения и заполните соответствующие поля:

**Для PPTP:**

Начиная с версии iOS-10 компания Apple убрала поддержку протокола PPTP.

* Описание - название соединения;
* Сервер - адрес VPN-сервера;
* Учетная запись - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="/.gitbook/assets/connection-for-mobile-devices9.png" alt="" data-size="original">

**Для L2TP:**

* Описание - название соединения;
* Сервер - адрес VPN-сервера;
* Учетная запись - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя;
* Общий ключ - значение строки **PSK** в разделе **Пользователи -> VPN-подключения -> Основное -> Подключение по L2TP/IPsec**.

<img src="/.gitbook/assets/connection-for-mobile-devices10.png" alt="" data-size="original">

**Для IKEv2:**

* Описание - название соединения;
* Сервер - адрес VPN-сервера;
* Удаленный ID - адрес VPN-сервера;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="/.gitbook/assets/connection-for-mobile-devices11.png" alt="" data-size="original">

4\. Нажмите **Готово**;

5\. Переведите опцию **Статус** вправо:

<img src="/.gitbook/assets/connection-for-mobile-devices12.png" alt="" data-size="original">

</details>
