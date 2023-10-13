# Загрузка своего SSL-сертификата на сервер

## Подготовка SSL сертификата для загрузки на UTM VPP
Для загрузки доверенного SSL сертификата, купленного у Certificate Authority или Центра сертификации, выполните действия:

1. Создайте текстовый файл вида:

```
-----BEGIN PRIVATE KEY-----
.....
.....
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
```

{% hint style="info" %}
Если Центр сертификации выдал приватный ключ в зашифрованном виде, расшифруйте ключ с помощью passphrase (фразы-пароля) перед добавлением в файл. 
{% endhint %}

2. Добавьте в блок (**BEGIN PRIVATE KEY**) расшифрованный приватный ключ.

3. Добавьте сертификат на домен, сертификаты из бандла vendor-сертификатов, корневой сертификат в каждый из блоков (**BEGIN CERTIFICATE**).

4. Проверьте, что файл имеет такую структуру:

```
Приватный ключ
Сертификат на домен
Сертификат из состава бандла vendor-сертификатов
Сертификат из состава бандла vendor-сертификатов
...
Основной (корневой) сертификат
```

5. Сохраните файл с расширением **.pem** и воспользуйтесь [инструкцией по загрузке сертификата на UTM VPP](#zagruzka-ssl-sertifikata-na-utm-vpp).

{% hint style="info" %}
С общепринятым стандартом создания файла-цепочки сертификатов можно также ознакомиться здесь: [https://www.digicert.com/ssl-support/pem-ssl-creation.htm](https://www.digicert.com/ssl-support/pem-ssl-creation.htm).
{% endhint %}

## Создание самоподписанного сертификата c помощью Powershell

1. Запустите PowerShell от имени администратора.

2. Сгенерируйте сертификат, выполнив команду:

```
New-SelfSignedCertificate -DnsName test.ideco.com -TextExtension @("2.5.29.19={text}CA=true") -CertStoreLocation cert:\LocalMachine\My
```

* `test.ideco.com` - домен.

![](../../.gitbook/assets/upload-ssl-certificate-to-server.png)

Для просмотра сгенерированного сертификата выполните команду `certlm.msc`.

3. Сформируйте пароль для сертификата:

```
$CertPassword = ConvertTo-SecureString -String “12345” -Force –AsPlainText
```

* `12345` - пароль.

4. Экспортируйте сертификат выполнив команду:

```
Export-PfxCertificate -Cert cert:\LocalMachine\My\2284919151C5C624341D7B75FE034B00DF6A44FA -FilePath C:\Users\pende\ssl\test.ideco.pfx -Password $CertPassword
```

* `2284919151C5C624341D7B75FE034B00DF6A44FA` - идентификатор сертификата полученный на шаге 2.

5. Конвертируйте сертификат в расширение .pem ([пример конвертора](https://www.leaderssl.ru/tools/ssl_converter)).


## Конвертация сертификата из формата pkcs12 в формат pem с помощью openssl

{% hint style="info" %}
Для конвертации сертификата с помощью openssl на Windows воспользуйтесь ссылкой для [загрузки openssl на компьютер](http://slproweb.com/products/Win32OpenSSL.html) и для[установки openssl на компьютер](http://iljin-oleg.blogspot.com/2012/12/openssl-openssl-ssl-secure-socket-layer.html).
{% endhint %}

Для конвертации сертификата из формата **pkcs12** в формат **pem** выполните действия:
1. Откройте командную строку.
2. Введите команду `openssl pkcs12 -in certificate.pkcs12 -out certificate.pem` (сконвертируется сертификат в нужный формат).

* **certificate.pkcs12** - исходный сертификат который был получен у центра сертификации.
* **certificate.pem** - результат конвертации;

3. Откройте полученный файл и убедитесь, что он имеет структуру:

```
    -----BEGIN CERTIFICATE-----
    ..............
    ..............
    -----END CERTIFICATE-----
    -----BEGIN PRIVATE KEY-----
    ..............
    ..............
    -----END PRIVATE KEY-----
   ```

Если в сертификате написано `--BEGIN ENCRYPTED PRIVATE KEY--`, то расшифруйте его с помощью утилиты openssl.\
**Команда для расшифровки:** `openssl rsa -in certificate.pem -out certificate_decoded.pem`. 

* **certificate.pem** - файл который был получен после конвертации;
* **certificate\_decode.pem** - результат расшифровки.

4. Для подготовки сертификата к загрузке воспользуйтесь статьей [Подготовка SSL сертификата для загрузки на UTM VPP](#podgotovka-ssl-sertifikata-dlya-zagruzki-na-utm-vpp).
5. Для загрузки сертификата на UTM VPP воспользуйтесь статьей [Загрузка SSL сертификата на UTM VPP](#zagruzka-ssl-sertifikata-na-utm-vpp).

## Загрузка SSL сертификата на UTM VPP

Для загрузки подготовленного сертификата на Ideco UTM VPP выполните действия:
1. Перейдите в раздел **Сервисы -> Сертификаты -> Загруженные сертификаты**.
2. Нажмите **Загрузить корневой сертификат**.
3. Выберите сертификат вида: 

```
-----BEGIN PRIVATE KEY-----
.....
.....
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
.....
.....
-----END CERTIFICATE-----
```
