# Скрипты автоматической разавторизации

Разавторизация пользователей возможна в полностью автоматическом режиме.

Для этого нужно настроить скрипт, исполняемый при выходе пользователей из системы [logout](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753583(v=ws.11)?redirectedfrom=MSDN). Это можно сделать с помощью групповых политик домена (GPO).

{% hint style="info" %}
Для работы скрипта выполните все настройки политик безопасности домена и браузера, описанные в статье [Авторизация пользователей](active-directory-user-authorization.md).

Для авторизации по SSO используйте [Ideco Client](/settings/users/ideco-client/README.md).
{% endhint %}

## Разавторизация пользователя

Удобно применять скрипт, когда один компьютер используют разные пользователи. Скрипт можно скачать из веб-интерфейса, нажав кнопку **Скачать скрипт для разавторизации**. В разделе **Пользователи -> Авторизация** установите галку **Веб-аутентификация**:

![](/.gitbook/assets/auto-de-authorization-script.gif)

Для работы скрипта разавторизации пользователя установите сертификат сервера в качестве доверенного корневого центра сертификации на компьютеры пользователей. Можно сделать это локально или через групповые политики домена, как описано в [инструкции](/settings/access-rules/content-filter/filtering-https-traffic.md#dobavlenie-sertifikata-cherez-politiki-domena-microsoft-active-directory).

Также необходимо отключить предупреждение о несоответствии адреса сертификата в свойствах Internet Explorer:

![](/.gitbook/assets/auto-de-authorization-script1.png)

{% hint style="info" %}
Этот параметр также можно установить через GPO, изменив параметр реестра:

HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings параметр `WarnonBadCertRecving = 0`
{% endhint %}

### Добавления скрипта для разавторизации

Добавьте скрипт, выполняемый [при выходе пользователя из системы](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753583(v=ws.11)?redirectedfrom=MSDN):

1\. Откройте групповые политики (gpedit.msc) от имени администратора на устройстве пользователя;

2\. Перейдите в **Конфигурации пользователя**, далее в **Конфигурации Windows**:

![](/.gitbook/assets/auto-de-authorization-script2.png)

4\. Нажмите **Сценарии (вход/выход из системы)**;

5\. Откройте **Выход из системы** и перейдите на вкладку **Сценарии PowerShell**:

![](/.gitbook/assets/auto-de-authorization-script3.png)

6\. Нажмите **Добавить** и выберите скачанный файл **UTM_logout.ps1**, нажав на кнопку **Обзор**:

![](/.gitbook/assets/auto-de-authorization-script4.png)

7\. Обновите групповые политики, выполнив команду `gpupdate /force` в консоли.

{% hint style="info" %}

Если в Internet Explorer появляется окно с текстом **Для получения доступа требуется аутентификация** и авторизация происходит только при ручном переходе по ссылке, установите параметр **Активные сценарии** в Internet Explorer в значение **Включить**.

![](/.gitbook/assets/auto-de-authorization-script5.jpg)

Автоматически групповая политика обновляется не сразу после внесения изменений. Чтобы скрипты начали работать, обновите политику вручную командой `gpupdate /force` на рабочей станции.
{% endhint %}