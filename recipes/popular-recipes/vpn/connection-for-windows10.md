# Инструкция по созданию подключения в Windows 10

{% hint style="info" %}
Перед настройкой VPN-подключения, в дереве пользователей откройте карточку нужного пользователя и установите флаг **Разрешить удаленный доступ через VPN**. Для этого перейдите в раздел **Пользователи -> Учетные записи**.

Перед настройкой подключения по протоколу IKEv2 установите корневой сертификат UTM на устройство пользователя. Скачать сертификат можно одним из способов:

*   В личном кабинете, введя логин/пароль пользователя:

    <img align="left" src="../../../.gitbook/assets/ubuntu16.png" alt="" data-size="original">
    
*   В разделе **Сервисы -> Сертификаты**:

    <img align="left" src="../../../.gitbook/assets/certificates2.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

## Создание VPN-подключения в Windows 10

1\. Кликните на иконке сетевого подключения в системном трее, и в появившемся окне выберите **Параметры сети и Интернет**:

<img src="../../../../.gitbook/assets/vpn-windows.png" alt="" data-size="original">

2\. Перейдите в раздел **VPN** и нажмите **Добавить VPN-подключение**:

<img src="../../../../.gitbook/assets/vpn-windows1.png" alt="" data-size="original">

3\. Заполните соответствующие поля и нажмите **Сохранить**:

<details>

<summary>Для PPTP</summary>

* Имя подключения - название создаваемого подключения;
* Имя или адрес сервера - адрес VPN-сервера;
* Тип VPN - Протокол PPTP;
* Тип данных для входа - Имя пользователя и пароль;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="../../../../.gitbook/assets/vpn-windows2.png" alt="" data-size="original">

При настройке подключения по VPN из сети Интернет, в свойствах VPN-подключения нужно указать следующие параметры:

* Перейдите в **Настройки параметров адаптера**;
* Нажмите на созданное подключение правой кнопкой мыши и выберите **Свойства**;
* Перейдите во вкладку **Безопасность** и установите:
  * **Шифрование данных** - обязательное (отключиться, если нет шифрования)
  * **Протокол расширенной проверки подлинности (EAP)** - Microsoft защищенный пароль (EAP MSCHAPV2)

</details>

<details>

<summary>Для L2TP/IPsec с общим ключом</summary>

**Важно:** L2TP IPsec клиенты, находящиеся за одним NAT'ом, могут испытывать проблемы подключения если их более одного. Решить проблему может помочь [инструкция](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-l2tp-ipsec-server-behind-nat-t-device). Рекомендуем вместо L2TP IPsec использовать IKEv2 IPsec.

Имя подключения - название создаваемого подключения;
* Имя или адрес сервера - адрес VPN-сервера;
* Тип VPN - Протокол L2TP/IPsec с общим ключом;
* Общий ключ - значение строки **PSK** в разделе **Пользователи -> VPN-подключение -> Основное -> Подключение по L2TP/IPsec**;
* Тип данных для входа - Имя пользователя и пароль;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="../../../../.gitbook/assets/vpn-windows3.png" alt="" data-size="original">

При настройке подключения по VPN из сети Интернет, в свойствах VPN-подключения нужно указать следующие параметры:

* Перейдите в **Настройки параметров адаптера**;
* Нажмите на созданное подключение правой кнопкой мыши и выберите **Свойства**;
* Перейдите во вкладку **Безопасность** и установите:
  * **Шифрование данных** - обязательное (отключиться, если нет шифрования)
  * **Протокол расширенной проверки подлинности (EAP)** - Microsoft защищенный пароль (EAP MSCHAPV2)

Если создается VPN-подключение к UTM через проброс портов, рекомендуем выполнить следующие действия:

1. Откройте **Редактор реестра**;
2. Перейдите в `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PolicyAgent` и создайте DWORD-параметр с именем AssumeUDPEncapsulationContextOnSendRule и значением `2`;
3. Перезагрузите Windows.

Возможные неполадки

1. Неправильно указан логин или пароль пользователя. Часто при повторном соединении предлагается указать домен. Старайтесь создавать цифро-буквенные пароли, желательно на латинице для учетных записей. Если есть сомнения в этом пункте, то временно установите логин и пароль пользователю «user» и «123456».
2. Для того, чтобы пакеты пошли через VPN-туннель, надо убедиться, что в настройках этого подключения стоит чекбокс **Использовать основной шлюз в удалённой сети** в разделе **Настройка параметров адаптера -> Правой кнопкой мыши по подключению -> Свойства -> Сеть -> Свойства опции «Протокол Интернета версии 4 (TCP/IPv4)» ->Дополнительно**. Если же маршрутизировать все пакеты в этот интерфейс не обязательно, то маршрут надо писать вручную.
3. Подключение происходит через DNAT, т.е. внешний интерфейс Ideco UTM не имеет «белого» IP-адреса, а необходимые для работы порты (500 и 4500) «проброшены» на внешний интерфейс устройства, расположенного перед Ideco UTM и имеющего «белый» IP-адрес. В данном случае VPN-подключение либо вообще не будет устанавливаться, либо будут периодические обрывы. Решение - исключить устройство перед Ideco UTM и указать на внешнем интерфейсе Ideco UTM «белый» IP-адрес, к которому в итоге и будут осуществляться L2TP/IPsec-подключения. Либо используйте протокол SSTP, потому что его проще опубликовать с помощью проброса портов.
4. Если в OC Windows 10 повторно подключиться по L2TP, но при этом использовать **невалидный** ключ PSK (введя его в дополнительных параметрах (скриншот ниже)), подключение все равно будет установлено успешно. Это связано с особенностями работы ОС.

Убедитесь, что локальная сеть (или адрес на сетевой карте) на удалённой машине не пересекается с локальной сетью организации. Если пересекается, то доступа к сети организации не будет (трафик по таблице маршрутизации пойдёт в физический интерфейс, а не в VPN). Адресацию необходимо менять.

</details>

<details>

<summary>Для SSTP</summary>

* Имя подключения - название создаваемого подключения;
* Имя или адрес сервера - адрес VPN-сервера в формате _адрес\_VPN\_сервера:порт_;
* Тип VPN - Протокол SSTP;
* Тип данных для входа - Имя пользователя и пароль;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="../../../../.gitbook/assets/vpn-windows4.png" alt="" data-size="original">

</details>

<details>

<summary>Для IKEv2</summary>



* Имя подключения - название создаваемого подключения;
* Имя или адрес сервера - адрес VPN-сервера;
* Тип VPN - Протокол IKEv2;
* Тип данных для входа - Имя пользователя и пароль;
* Имя пользователя - имя пользователя, которому разрешено подключение по VPN;
* Пароль - пароль пользователя.

<img src="../../../../.gitbook/assets/vpn-windows5.png" alt="" data-size="original">

При настройке подключения по VPN из сети Интернет, в свойствах VPN-подключения нужно указать следующие параметры:

* Перейдите в **Настройки параметров адаптера**;
* Нажмите на созданное подключение правой кнопкой мыши и выберите **Свойства**;
* Перейдите во вкладку **Безопасность** и установите:
  * **Шифрование данных** - обязательное (отключиться, если нет шифрования);
  * **Протокол расширенной проверки подлинности (EAP)** - Microsoft защищенный пароль (EAP MSCHAPV2).

</details>

4\. Активируйте подключение, нажав правой кнопкой мыши по созданному подключению и выбрав **Подключиться**:

<img src="../../../../.gitbook/assets/vpn-windows6.png" alt="" data-size="original">

5\. Для разрыва подключения нажмите **Отключиться**. Если нужно внести изменение в созданное подключение, нажмите **Дополнительные параметры -> Изменить**

<img src="../../../../.gitbook/assets/vpn-windows7.png" alt="" data-size="original">



## Ошибки работы VPN-подключений

<details>

<summary>Если VPN-подключение по протоколам IPSeс в Windows автоматически разрывается через 7 часов 45 минут и при подключении по IKEv2 возникает ошибка "Ошибка сопоставления групповой политики" или ошибка с кодом "13868"</summary>

Для восстановления связи подойдут следующие действия:

1\. Переподключите соединение. В данном случае соединение восстановится, но через 7 часов 45 минут вновь будет автоматически разорвано. Если требуется, чтобы подключение не разрывалось автоматически, то выполните действия из следующего пункта.

2\. Внесите изменения в реестр:

* Откройте **Редактор реестра**;
* Перейдите по пути `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RasMan\Parameters`;
* Нажмите правой кнопкой мыши по параметру именем **NegotiateDH2048\_AES256** и нажмите **Изменить**;
* В строке **Значение** укажите значение `1`:

<img src="../../../../.gitbook/assets/windows-vpn.png" alt="" data-size="original">

* Нажмите **OK**;
* Перезагрузите Windows.

    Если параметра именем **NegotiateDH2048\_AES256** нет, то создайте его. Для этого:
* Нажмите правой кнопкой мыши по свободному месту реестра в **Parameters** и выберите **Создать -> DWORD**:

<img src="../../../../.gitbook/assets/windows-vpn2.png" alt="" data-size="original">

* Задайте имя **NegotiateDH2048\_AES256**;
* Нажмите правой кнопкой мыши по созданному файлу и выберите **Изменить**:

<img src="../../../../.gitbook/assets/windows-vpn3.png" alt="" data-size="original">

* В строке **Значение** укажите значение `1`:

<img src="../../../../.gitbook/assets/windows-vpn4.png" alt="" data-size="original">

* Нажмите **OK**.

3\. Перезагрузите Windows.

</details>

{% hint style="info" %}
Если не хотите, чтобы после подключения по VPN интернет-трафик до внешних ресурсов ходил через Ideco UTM, то в свойствах VPN-подключения **Сеть/Протокол интернета TCP/IP версии 4/Дополнительно** уберите галочку **Использовать основной шлюз в удаленной сети**. Далее, чтобы получить доступ к компьютерам за Ideco UTM, вручную пропишите маршруты.
{% endhint %}