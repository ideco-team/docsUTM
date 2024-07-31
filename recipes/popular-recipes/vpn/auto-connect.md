# Автоматическое создание подключений

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило. 
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

<details>

<summary>Протокол L2TP/IPsec</summary>

**Важно:** L2TP IPsec клиенты, находящиеся за одним NAT'ом, могут испытывать проблемы подключения? если их более одного. Решить проблему может помочь [инструкция](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-l2tp-ipsec-server-behind-nat-t-device). Рекомендуем вместо L2TP IPsec использовать IKEv2 IPsec.

Запустите следующий скрипт PowerShell для автоматического создания подключения на компьютерах пользователей с Windows 8.1 и 10. Для этого скачайте готовые скрипты подключения сервера из раздела **Пользователи -> VPN-подключения -> Основное**.

Подключение будет создано со следующими параметрами:

1\. Протокол **L2TP/IPsec** с использованием PSK-ключа;

2\.  Параметр **Использовать основной шлюз в удаленной сети** выключен.

    Доступ к локальным сетям того же класса, что были получены для VPN-подключения по умолчанию в Windows 7 и 10, будет осуществляться через VPN-подключение, поэтому дополнительных маршрутов создавать не нужно (если не используются разные классы сетей в локальной сети офиса).

Создайте файл с именем **ideco\_ngfw\_l2tp.ps1** (в Блокноте или редакторе Windows PowerShell ISE) и скопируйте в него следующий текст:

```
### Ideco NGFW L2TP/IPsec connection ###
param([switch]$Elevated)
$currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
if (!$currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator))  {
  if (!$elevated) {
    Start-Process `
            powershell.exe `
            -Verb RunAs `
            -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ( $myinvocation.MyCommand.Definition ))
  }
  exit
}
Enable-NetFirewallRule -Group "@FirewallAPI.dll,-28502"
Add-VpnConnection `
    -Force `
    -Name "Ideco NGFW L2TP VPN" `
    -TunnelType L2TP `
    -ServerAddress my.domain.com `
    -L2tpPsk "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" `
    -EncryptionLevel "Required" `
    -AuthenticationMethod MSChapV2 `
    -SplitTunneling $False `
    -DnsSuffix activedirectory.domain `
    -RememberCredential
```

**Поменяйте в нем необходимые параметры на соответствующие вашим настройкам:**

* **Ideco NGFW L2TP VPN** - имя подключения в системе (может быть произвольным);
* **my.domain.com** - домен или IP-адрес основного внешнего интерфейса Ideco NGFW;
* **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX** - PSK-ключ вашего сервера;
* **activedirectory.domain** - ваш домен Active Directory (Если есть. Если его нет, нужно удалить эту строчку из скрипта).

**Запустить скрипт на компьютере пользователя можно из контекстного меню файла "Выполнить с помощью PowerShell". Нажмите "Ок" в диалоге повышения прав (они требуются для разрешения доступа к общим файлам и принтерам).**

После этого в системе будет создано подключение, а также включен общий доступ к файлам и принтерам для всех сетей (иначе доступ к файловым ресурсам в локальной сети может быть невозможен).

Пользователю при первой авторизации необходимо ввести свой логин/пароль.

**Возможные ошибки при выполнении скрипта**

* При появлении ошибки "Выполнение сценариев отключено в этой системе" нужно включить выполнение сценариев, выполнив команду в PowerShell: `Set-ExecutionPolicy Unrestricted`.

</details>

<details>

<summary>Протокол SSTP</summary>

Запустите следующий скрипт PowerShell для автоматического создания подключения на компьютерах пользователей с Windows 8.1 и 10. Для этого скачайте готовый скрипт из раздела **Пользователи -> VPN-подключения -> Основное**.

**Подключение будет создано со следующими параметрами:**

1\. Протокол **SSTP** с использованием PSK-ключа;

2\.  Параметр **Использовать основной шлюз в удаленной сети** выключен.

    Доступ к локальным сетям того же класса, что были получены для VPN-подключения по умолчанию в Windows 7 и 10, будет осуществляться через VPN-подключение, поэтому дополнительных маршрутов создавать не нужно (если не используются разные классы сетей в локальной сети офиса).

Создайте текстовый файл с именем **ideco\_ngfw\_sstp.ps1** (в Блокноте или редакторе Windows PowerShell ISE) и скопируйте туда следующий текст:

```
### Ideco NGFW SSTP connection ###
param([switch]$Elevated)
$currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
if (!$currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator))  {
  if (!$elevated) {
    Start-Process `
            powershell.exe `
            -Verb RunAs `
            -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ( $myinvocation.MyCommand.Definition ))
  }
  exit
}
Enable-NetFirewallRule -Group "@FirewallAPI.dll,-28502"
Add-VpnConnection `
    -Force `
    -Name "Ideco NGFW SSTP VPN" `
    -TunnelType SSTP `
    -ServerAddress my.domain.com:4443 `
    -EncryptionLevel "Required" `
    -AuthenticationMethod MSChapV2 `
    -SplitTunneling $False `
    -DnsSuffix activedirectory.domain `
    -RememberCredential
```

**Поменяйте в нем необходимые параметры на соответствующие вашим настройкам:**

1\. **Ideco NGFW SSTP VPN** - имя подключения в системе (может быть произвольным);

2\. **my.domain. com:4443** - домен внешнего интерфейса Ideco NGFW и порт, на котором включили SSTP;

3\. **activedirectory.domain** - ваш домен Active Directory (если домена нет, нужно удалить эту строчку из скрипта).

**Запустить скрипт на компьютере пользователя можно из контекстного меню файла "Выполнить с помощью PowerShell". Нажмите "Ок" в диалоге повышения прав (они требуются для разрешения доступа к общим файлам и принтерам).**

После этого подключение в системе будет создано, а также включен общий доступ к файлам и принтерам для всех сетей (иначе доступ к файловым ресурсам в локальной сети может быть невозможен).

Пользователю при первой авторизации необходимо ввести свой логин/пароль.

**Возможные ошибки при выполнении скрипта**

При ошибке "Выполнение сценариев отключено в этой системе", нужно включить выполнение сценариев, выполнив команду в PowerShell: `Set-ExecutionPolicy Unrestricted`.

</details>

<details>

<summary>Протокол IPsec IKEv2</summary>

Запустить скрипт PowerShell для автоматического создания подключения на компьютерах пользователей с Windows 8.1 и 10, скачав готовый скрипт из раздела **Пользователи -> VPN-подключения -> Основное**.

Перед настройкой подключения по протоколу IKEv2 установите корневой сертификат NGFW на устройство пользователя. Скачать сертификат можно в разделе **Сервисы -> Сертификаты -> Загруженные сертификаты** в веб-интерфейсе NGFW или в личном кабинете пользователя по кнопке **Скачать корневой сертификат**.

Корневой сертификат потребуется для настройки подключения рабочей станции пользователя, если не был получен корневой сертификат через Let\`s Encrypt. \
Если для VPN-подключения используется сертификат, выданный Let\`s Encrypt, установка корневого сертификата на устройство не требуется.

**Подключение с помощью скрипта будет создано со следующими параметрами:**

1\. Протокол IKEv2; \
2\. Параметр **Использовать основной шлюз в удаленной сети** выключен. Доступ к локальным сетям того же класса, что были получены для VPN-подключения по умолчанию в Windows 7 и 10, будет осуществляться через VPN-подключение, поэтому дополнительных маршрутов создавать не нужно (если не используются разные классы сетей в локальной сети офиса).

Создайте текстовый файл с именем **ideco\_ngfw\_ikev2.ps1** (в Блокноте или редакторе Windows PowerShell ISE) и скопируйте туда следующий текст:

```
### Ideco NGFW IKEv2 connection ###
param([switch]$Elevated)
$currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
if (!$currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator))  {
  if (!$elevated) {
    Start-Process \`
            powershell.exe `
            -Verb RunAs `
            -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ( $myinvocation.MyCommand.Definition ))
  }
  exit
}
Enable-NetFirewallRule -Group "@FirewallAPI.dll,-28502"
Add-VpnConnection `
    -Force `
    -Name "Ideco NGFW IKEv2 VPN" `
    -TunnelType IKEv2 `
    -ServerAddress my.domain.com `
    -EncryptionLevel "Required" `
    -AuthenticationMethod EAP `
    -SplitTunneling $False `
    -DnsSuffix activedirectory.domain `
    -RememberCredential
```

**Поменяйте в нем необходимые параметры на соответствующие вашим настройкам:**

1\. `Ideco NGFW IKEv2 VPN` - название подключения в системе (может быть произвольным);

2\. `my.domain.com` - домен внешнего интерфейса Ideco NGFW (А-запись для домена должна ссылаться на IP-адрес внешнего интерфейса Ideco NGFW);

3\. `activedirectory.domain` - ваш домен Active Directory (если его нет, нужно удалить эту строчку из скрипта).

Запустить скрипт на компьютере пользователя можно из контекстного меню файла "Выполнить с помощью PowerShell". Нажмите "Ок" в диалоге повышения прав (они требуются для разрешения доступа к общим файлам и принтерам).

После этого подключение в системе будет создано, а также включен общий доступ к файлам и принтерам для всех сетей (иначе доступ к общим папкам в локальной сети будет невозможен).

При первой авторизации необходимо ввести логин/пароль пользователя.

**Возможные ошибки при выполнении скрипта**

При появлении ошибки "Выполнение сценариев отключено в этой системе" нужно включить выполнение сценариев, выполнив команду в PowerShell: `Set-ExecutionPolicy Unrestricted`.

</details>

## Ошибки работы VPN-подключений

<details>

<summary>Если VPN-подключение по протоколам IPSeс в Windows автоматически разрывается через 7 часов 45 минут и при подключении по IKEv2 возникает ошибка "Ошибка сопоставления групповой политики" или ошибка с кодом "13868"</summary>

Для восстановления связи подойдут следующие действия:

1\. Переподключите соединение. Оно восстановится, но через 7 часов 45 минут вновь будет автоматически разорвано. Если требуется, чтобы подключение не разрывалось автоматически, то выполните действия из следующего пункта.

2\. Внесите изменения в реестр:

* Откройте **Редактор реестра**;
* Перейдите по пути `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RasMan\Parameters`;
* Нажмите правой кнопкой мыши по параметру с именем **NegotiateDH2048\_AES256** и нажмите **Изменить**;
* В строке **Значение** укажите значение `1`:

![](/.gitbook/assets/auto-connect1.png)

* Нажмите **OK**;
* Перезагрузите Windows;

    Если параметра с именем **NegotiateDH2048\_AES256** нет, то создайте его. Для этого:
* Нажмите правой кнопкой мыши по свободному месту реестра в **Parameters** и выберите **Создать -> DWORD**:

![](/.gitbook/assets/auto-connect2.png)

* Задайте имя **NegotiateDH2048\_AES256**;
* Нажмите правой кнопкой мыши по созданному файлу и выберите **Изменить**:

![](/.gitbook/assets/auto-connect3.png)

* В строке **Значение** укажите значение `1`:

![](/.gitbook/assets/auto-connect4.png)

* Нажмите **OK**.

3\. Перезагрузите Windows.

</details>
