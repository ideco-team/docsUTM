# Ошибка 400 Bad Request Request Header Or Cookie Too Large при авторизации в браузерах

Ошибка возникает на Windows 7, 8, 11, Windows Server 2008 R2, 2012, 2022 из-за большого количества групп безопасности и неспособности токена Kerberos вместить все данные.

По умолчанию размер токена Kerberos:

* **Windows 7 и Windows Server 2008R2** - 12000 байт;
* **Windows 8 и Windows Server 2012 (включая Windows Server 2022 и Windows 11)** - 48000 байт.

Для решения проблемы нужно увеличить размер токена на пользовательской ОС. Для этого:

1\. Откройте редактор реестра и перейдите в раздел **HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Kerberos\Parameters**.

2\. Создайте новый параметр типа **DWORD (32-bit)** с именем **MaxTokenSize**.

3\. Задайте максимальное значение размера буфера - 65535 байт в десятичной системе счисления:

![](/.gitbook/assets/maxtokensize.png)

4\. Перезагрузите компьютер.

{% hint style="info" %}
Чтобы узнать текущее значение параметра **MaxTokenSize**, выполните следующую команду в **PowerShell**:

```
Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters|select MaxTokenSize
```
{% endhint %}