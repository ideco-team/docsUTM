---
title: Скрипты автоматической авторизации и разавторизации
description: null
published: true
date: '2021-05-18T11:28:58.840Z'
tags: ad
editor: markdown
dateCreated: '2021-04-02T07:27:01.956Z'
---

# Скрипты автоматической авторизации и разавторизации

Авторизация и разавторизация пользователей возможна в полностью автоматическом режиме.

Для этого нужно настроить скрипты, исполняемые при входе пользователей в систему [logon](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770908%28v=ws.11%29?redirectedfrom=MSDN) и выходе пользователей из системы [logout](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753583%28v=ws.11%29?redirectedfrom=MSDN). Это можно сделать, например, с помощью групповых политик домена \(GPO\).

{% hint style="info" %}
Для работы данных скриптов необходимо выполнить все настройки политик безопасности домена и браузера, описанные в статье [Авторизация пользователей](avtorizaciya-polzovatelei-active-directory.md).
{% endhint %}

## Авторизация пользователя

Необходимо добавить скрипт в сценарии, выполняемые [при входе в систему](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770908%28v=ws.11%29?redirectedfrom=MSDN).

**UTMLogon\_script.vbs**

```text
Dim IE
Set IE = CreateObject("InternetExplorer.Application")
IE.Visible = True
IE.Fullscreen = False
IE.Toolbar = False
IE.StatusBar = False
Wscript.Sleep(3000)
IE.Navigate2("http://ya.ru")
Wscript.Sleep(20000)
IE.Quit
```

## Разавторизация пользователя

Удобно применять этот скрипт, когда один компьютер используют разные пользователи для посещения ресурсов сети Интернет.

Для работы разавторизации пользователя необходима установка сертификата сервера в качестве доверенного корневого центра сертификации на компьютеры пользователей. Можно сделать это локально или через групповые политики домена, как описано в инструкции.

Также необходимо отключить предупреждение о несоответствии адреса сертификата в свойствах Internet Explorer:

![](../../.gitbook/assets/ie11.png)

Этот параметр также можно установить через GPO, изменив параметр реестра:

HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings параметр `WarnonBadCertRecving = 0`

Далее необходимо добавить скрипт, выполняемый [при выходе пользователя из системы](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753583%28v=ws.11%29?redirectedfrom=MSDN):

**UTMLogout\_script.vbs**

```text
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objWMIService = objLocator.ConnectServer(".", "root\cimv2")

Set HostNameSet = objWMIService.ExecQuery("Select * From Win32_NetworkAdapterConfiguration WHERE IPEnabled = True")
Set objHTTP = CreateObject("WinHttp.WinHttpRequest.5.1")
For Each objitem in HostNameSet
     If NOT IsNULL(objItem.IPAddress)Then
         For Each Ip in objItem.IpAddress
             Url = "https://IP-адрес UTM:8443/monitor_backend/sessions/logout/" & Ip
             objHTTP.Open "DELETE", Url, False
             On Error Resume Next
             objHTTP.send("")
        Next
     End If

Next
```

Вместо «IP-адрес UTM» укажите IP-адрес локального интерфейса Ideco UTM.

## Возможные ошибки при выполнении скриптов

* Если в Internet Explorer появляется окно с текстом **Для получения доступа требуется аутентификация**, и авторизация происходит только при ручном переходе по ссылке на авторизацию, то переход в браузере на страницу авторизации может не произойти \(он может быть ограничен настройками безопасности браузера\). В таком случае, установите параметр **Активные сценарии** в Internet Explorer в значение **Включить**.

![](../../.gitbook/assets/6586987.jpg)

* Автоматически групповая политика обновляется не сразу после внесения изменений. Чтобы скрипты начали работать, обновите политику вручную командой `gpupdate /force` на рабочей станции.

