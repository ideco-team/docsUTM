---
description: >-
  Используется для удаленной работы пользователей с предоставлением каждому отдельного рабочего стола. 
---

# Авторизация пользователей терминальных серверов

{% hint style="info" %}
Особенности работы для пользователей терминальных серверов AD:

* Пользователи имеют один IP-адрес, поэтому правила **Файрвола** и **Контроля приложений**, примененные для одного пользователя, будут действовать на всех;
* **Контент-фильтр** распознает этих пользователей, поэтому его правила применяются для отдельных пользователей и групп;
* Сессии авторизации не создаются, так как пользователи терминальных серверов обращаются с одним IP-адресом;
* Работает только при прямых подключениях к прокси;
* В **Журнале веб-доступа** не отображаются события по терминальным пользователям.
{% endhint %}

Для авторизации пользователей терминальных серверов установите флаг **Авторизовать пользователей терминальных серверов** и укажите IP-адрес терминального сервера в одноименной строке. Пользователи, отправляющие запросы с этих IP-адресов, считаются пользователями терминальных серверов и авторизуются через SSO.

Обратите внимание, что при большом количестве пользователей на сервере терминалов может потребоваться [увеличить количество одновременных сессий](https://docs.microsoft.com/ru-ru/windows-server/remote/remote-desktop-services/troubleshoot/remote-desktop-service-currently-busy#check-the-connection-limit-policy) с одного адреса в дополнительных параметрах безопасности.

Возможна **раздельная авторизация пользователей** терминального сервера (работающего под управлением ОС Windows Server 2008 R2 и Windows Server 2012) с помощью авторизации через [Ideco Client](/settings/users/ideco-client.md) или по [SSO (NTLM)](/settings/users/active-directory/active-directory-user-authorization.md). При этом сам сервер по IP авторизовать не нужно.

Для раздельной авторизации пользователей терминального сервера: 

* На сервере терминалов настройте [**Remote Desktop IP Virtualization**](https://docs.microsoft.com/en-us/troubleshoot/windows-server/remote/remote-desktop-ip-virtualization); 
* На сервере Ideco NGFW настройте авторизацию пользователей через [Ideco Client](/settings/users/ideco-client.md) или [веб-аутентификацию (SSO или NTLM)](/settings/users/active-directory/active-directory-user-authorization.md). 

{% hint style="info" %}
Авторизация пользователей терминального сервера по логам контроллера домена AD пока не реализована.
{% endhint %}

## Настройка Remote Desktop IP Virtualization на Windows Server 2012

Для работы функции [Remote Desktop IP Virtualization](https://docs.microsoft.com/en-us/troubleshoot/windows-server/remote/remote-desktop-ip-virtualization) на одном из Windows-серверов должна быть добавлена роль DHCP-сервера (с другими DHCP-серверами эта функция может работать некорректно) и выделена область IP-адресов для пользователей терминального сервера.

В **Редакторе управления групповыми политиками** перейдите по пути: **Computer Configation –> Policies –> Administrative Templates –> Windows Components -> Remote Desktop Service –> Remote Desktop Session Host –> Application Compatibility**.

Путь для русскоязычной версии: **Конфигурация компьютера –> Административные шаблоны –> Компоненты Windows -> Служба удаленных рабочих столов –> Узел сеансов удаленных рабочих столов –> Совместимость приложений**. Включите опцию **Turn on Remote Desktop IP Virtualization (Включить IP-виртуализацию удаленных рабочих столов)** в групповой политике с параметром **Per Session (Для сеансов)**:

![](/.gitbook/assets/terminal-server.png)

Рекомендуется также включить опцию **Do not use Remote Desktop Session Host server IP address when virtual IP address is not available (Не использовать IP-адрес сервера узла сеансов удаленных рабочих столов, если виртуальный IP-адрес недоступен)**.

Командой `gpupdate /force` выполнить обновление всех политик.

Проверьте, что настройки изменились, командой в PowerShell:

`Get-WmiObject -Namespace root\cimv2\TerminalServices -query "select * from Win32_TSVirtualIP"`

Значения: 

* `VirtualIPActive = 1` - вкл. виртуализация;
* `VirtualIPMode=0` - для сессии.

## Настройка Remote Desktop IP Virtualization на Windows Server 2019/2022

### Условия

![](/.gitbook/assets/rdp1.png)

1\. Windows Server 2019/2022 с ролью контроллера домена;

2\. Windows Server 2019/2022 с ролью терминального сервера. Отдельный сервер опционален, можно добавить эту роль серверу с ролью контроллера домена;

3\. Ideco NGFW, введен в домен опционально;

4\. Клиентские Windows-машины, введенные в домен;

5\. (опционально) Windows Server 2019/2022 с ролью DHCP-сервера для динамической раздачи виртуальных IP-адресов. Конфликтует в ролью терминального сервера, поэтому DHCP-сервер и терминальный сервер должны быть разными машинами. DHCP-сервер используется на базе Windows Server. DHCP-сервер на Ideco NGFW, например, не подойдёт.

### Настройка

{% hint style="info" %}
Все настройки выполняются от имени администратора.
{% endhint %}

Установите все последние обновления Windows Server и перезагрузите серверы.

На сервере с ролью терминального сервера выполните следующие действия:

1\. Отключите WinSock2. Переместите (рекомендуется) или удалите раздел реестра по указанному пути с помощью **Редактора реестра** (regedit):

**Путь:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters\AppId_Catalog\2C69D9F1

2\. Включите компонент IPFilterBitmaps:

<details>

<summary>Добавление параметра через глобальную политику реестра с помощью Редактора реестра (regedit) (рекомендуется)</summary>

**Путь:** HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services

**Ключ:** IPFilterBitmaps

**Тип:** REG_DWORD

**Значение:** 1
</details>

<details>

<summary>Добавление параметра через групповую политику реестра с помощью Редактора реестра (regedit)</summary>

**Путь:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\TSAppSrv\VirtualIP

**Ключ:** IPFilterBitmaps

**Тип:** REG_DWORD

**Значение:** 1

</details>

3\. Перезагрузите сервер;

4\. Настройте IP-виртуализацию удалённых рабочих столов на сервере с ролью терминального сервера;

{% hint style="info" %}
Далее описана настройка для режима **Для сеансов**, который выдаёт виртуальный IP-адрес каждой пользовательской сессии.
{% endhint %}

<details>

<summary>Через редактирование объекта WMI-инфраструктуры (глобальную политику реестра) в Powershell (рекомендуется)</summary>

Значение для метода SelectNetworkAdapter - MAC-адрес сетевого интерфейса, который будет использоваться для IP-виртуализации. Выполните команду:
```
$obj = gwmi -namespace "Root/CIMV2/TerminalServices" Win32_TSVirtualIP
$obj.SelectNetworkAdapter('52-54-00-00-90-01')
$obj.SetVirtualMode(0)
$obj.SetVirtualIPActive(1)
```
После выполнения команды убедитесь, что все параметры выставлены правильно, введя `$obj`.

</details>

<details>

<summary>Через групповую политику с помощью Редактора локальной групповой политики (gpedit.msc)</summary>

1\. Перейдите в раздел **Политика Локальный компьютер –> Конфигурация компьютера –> Административные шаблоны –> Компоненты Windows –> Службы удалённых рабочих столов –> Узел сеансов удалённых рабочих столов –> Совместимость приложений**.

Путь для англоязычной версии: **Local Computer Policy –> Computer Configuration –> Administrative Templates –> Windows Components –> Remote Desktop Services –> Remote Desktop Session Host –> Application Compatibility**;

2\. Включите параметр политики **Включить IP-виртуализацию удаленных рабочих столов** с параметром **Для сеансов**.

Англоязычная версия: **Turn on Remote Desktop IP Virtualization** с параметром **Per Session**;

3\. Включите параметр политики **Выбрать сетевой адаптер, используемый для IP-виртуализации удалённых рабочих столов** в параметр **IP-адрес с маской сетевого интерфейса, который будет использоваться для IP-виртуализации** (например, 192.168.100.200/24).

Англоязычная версия: **Select the network adapter to be used for Remote Desktop IP Virtualization** в параметр **IP adress and network mask corresponding to the network adapter to be used for Remote Desktop IP Virtualization**;

4\. (опционально) Включите параметр политики **Не использовать IP-адрес сервера узла сеансов рабочих столов, если IP-адрес недоступен** (**Do not use Remote Desktop Session Host server IP address when virtual IP address is not available**).

![](/.gitbook/assets/rdp7.png)

</details>

5\. Повторно перезагрузите сервер.

Настройте выдачу виртуальных IP-адресов:

<details> 

<summary>Для статической выдачи виртуальных IP-адресов на сервере с ролью терминального сервера</summary>


Включите компонент IPPool. Через групповую политику реестра с помощью **Редактора реестра** (regedit) добавьте параметр:

**Путь:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\TSAPPSrv\VirtualIP

**Ключ:** IPPool

**Тип:** REG_SZ (строковый параметр)

**Значение:** `%SystemRoot%\system32\TSVIPool.dll`

Настройте статический диапазон IP-адресов:

1\. Создайте новый раздел IPPool по пути HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\TSAPPSrv\VirtualIP через групповую политику реестра с помощью **Редактора реестра** (regedit).

2\. Добавьте в новый раздел параметры типа REG_SZ (строковый параметр):

* Ключ Start, значение - начало диапазона IP-адресов (например, 192.168.100.200);

* Ключ End, значение - конец диапазона IP-адресов (например, 192.168.100.210);

* Ключ SubnetMask, значение - маска подсети (например, 255.255.255.0).

3\. Перезагрузите сервер с ролью терминального сервера.

</details>

<details>

<summary> Для динамической выдачи виртуальных IP-адресов на сервере с ролью DHCP-сервера </summary>

Выдайте DHCP-серверу необходимые привилегии через групповую политику реестра с помощью **Редактора реестра»** (regedit):

**Путь:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dhcp

**Ключ:** RequiredPrivileges

**Тип:** REG_MULTI_SZ (многострочный параметр)

**Значение:**
```
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeImpersonatePrivilege
```

Перезагрузите сервер с ролью DHCP-сервера.

</details>

В случае успешной настройки на интерфейс, выбранный для IP-виртуализации, при подключении клиентов будут выдаваться виртуальные IP-адреса, которые исходящие запросы будут использовать в качестве источника.

![](/.gitbook/assets/rdp2.png)

### Диагностика

#### Виртуальные IP-адреса не выдаются

На сервере с ролью терминального сервера проверьте работоспособность службы IP-виртуализации. Для этого перейдите в раздел **Просмотр событий (локальный компьютер) –> Журналы приложений и служб –> Microsoft –> Windows –> Terminal Services-TSAppSrv-TSVIP –> Администратор**. 

Путь для англоязычной версии: **Event Viewer (Local) –> Applications and Services Logs –> Misrosoft –> Windows –> Terminal Services-TSAppSrv-TSVIP –> Administrator**.

Успешно запущенная служба произведёт события 100 и 112 после запуска и 103, 104 при подключении/отключении клиента:

![](/.gitbook/assets/rdp3.png)

В объекте WMI-инфраструктуры (независимо от вида настройки самой IP-виртуализации) в Powershell выполните:
```
$obj = gwmi -namespace "Root/CIMV2/TerminalServices" Win32_TSVirtualIP
$obj
```
Убедитесь, что параметр IP.VirtualIPActive = 1.

![](/.gitbook/assets/rdp4.png)

Если что-то отличается, убедитесь, что все инструкции по настройке выполнены правильно, а DHCP-сервер работает исправно. При необходимости выполните настройку заново рекомендуемыми способами.

#### Подключения используют основной IP-адрес терминального сервера

Использовать IP-виртуализацию будут только Windows-приложения, работающие на WinSock, то есть приложения, использующие протоколы TCP или UDP. ICMP-приложения вроде ping не будут использовать IP-виртуализацию.

Подключения будут использовать основной IP-адрес терминального сервера также в случае, когда запрашиваемый адрес недоступен (например, Destination Unreachable).

IP-виртуализация работает только для пользователей, подключённых к терминальному серверу через службу mstsc (**Подключение к удалённому рабочему столу**).