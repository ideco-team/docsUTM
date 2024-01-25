# Создание самоподписанного сертификата c помощью PowerShell

Чтобы создать корневой (самоподписанный) сертификат с помощью PowerShell, выполните следующие действия:

1. Запустите PowerShell от имени администратора.

2. Сгенерируйте сертификат, выполнив команду:

```
New-SelfSignedCertificate -DnsName test.ideco.com -TextExtension @("2.5.29.19={text}CA=true") -CertStoreLocation cert:\LocalMachine\My
```

* `test.ideco.com` - домен.

![](../../../.gitbook/assets/upload-ssl-certificate-to-server.png)

Для просмотра сгенерированного сертификата выполните команду `certlm.msc`.

3. Сформируйте пароль для сертификата:

```
$CertPassword = ConvertTo-SecureString -String “12345” -Force -AsPlainText
```

* `12345` - пароль.

4. Экспортируйте сертификат выполнив команду:

```
Export-PfxCertificate -Cert cert:\LocalMachine\My\2284919151C5C624341D7B75FE034B00DF6A44FA -FilePath C:\Users\pende\ssl\test.ideco.pfx -Password $CertPassword
```

* `2284919151C5C624341D7B75FE034B00DF6A44FA` - идентификатор сертификата полученный на шаге 2;
* `C:\Users\pende\ssl\test.ideco.pfx` - путь до папки, в которую требуется сохранить сертификат (проверьте его корректность во избежание ошибок).

5. Конвертируйте сертификат в расширение .pem ([пример конвертора](https://www.leaderssl.ru/tools/ssl_converter)).

6. Воспользуйтесь [инструкцией по загрузке сертификата на NGFW](upload-ssl-certificate-to-server.md).