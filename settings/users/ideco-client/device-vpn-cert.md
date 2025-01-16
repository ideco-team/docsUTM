# Создание сертификатов для Device VPN

В статье описан процесс создания сертификатов с использованием OpenSSL для подключения по [Device VPN](/settings/users/ideco-client/README.md#device-vpn) между Ideco NGFW и Ideco Client. Процесс включает в себя два этапа:

1\. Создание корневого сертификата с защищенным приватным ключом.

2\. Создание сертификатов для пользовательских устройств на основе этого корневого сертификата.

## Создание корневого сертификата

1\. Сгенерируйте приватный ключ корневого сертификата, защищенный _passphrase_:

{% code overflow="wrap" %}
```
openssl genrsa -des3 -out ideco-dvpn_root-ca.key 4096
```
{% endcode %}

* `-des3` - приватный ключ зашифрован алгоритмом Triple DES (3DES);
* `ideco-dvpn_root-ca.key` - файл, содержащий приватный ключ.

2\. Сгенерируйте корневой сертификат, используя приватный ключ корневого сертификата:

{% code overflow="wrap" %}
```
openssl req -x509 -new -sha256 -days 1825 -key ideco-dvpn_root-ca.key -nodes -out ideco-dvpn_root-ca.pem
```
{% endcode %}

* `-nodes` - не шифровать приватный ключ сертификата;
* `-sha256` - использовать алгоритм SHA256 при создании сертификата;
* `-days 1825` - срок действия сертификата в днях;
* `ideco-dvpn_root-ca.key` - файл, содержащий приватный ключ корневого сертификата;
* `ideco-dvpn_root-ca.pem` - файл, содержащий корневой сертификат.

3\. Проверьте, что сертификат был успешно создан командой:

{% code overflow="wrap" %}
```
openssl x509 -text -noout -in ideco-dvpn_root-ca.pem
```
{% endcode %}

* Корневой сертификат должен иметь атрибут `CA:TRUE`;
* `ideco-dvpn_root-ca.pem` - файл, содержащий корневой сертификат.

4\. В разделе **Пользователи -> Ideco Client** в поле **Доверенный сертификат** загрузите созданый сертификат `ideco-dvpn_root-ca.pem` без приватного ключа:

![](/.gitbook/assets/device-vpn.png)

После этого корневой сертификат будет необходим для создания пользовательских сертификатов.

## Создание пользовательского сертификата для конечного устройства

1\. Сгенерируйте приватный ключ без применения шифрования (в дальнейшем незашифрованный ключ размещается в пользовательском пространстве администратора, куда у пользователей не будет доступа):

{% code overflow="wrap" %}
```
openssl genrsa -out client1-dvpn.key 4096
```
{% endcode %}

* `client1-dvpn.key` - файл, содержащий приватный ключ.

2\. Сгенерируйте запрос на выпуск пользовательского сертификата с использованием приватного ключа:

{% code overflow="wrap" %}
```
openssl req -new -key client1-dvpn.key -out client1-dvpn.csr
```
{% endcode %}

* `client1-dvpn.key` - файл, содержащий приватный ключ;
* `client1-dvpn.csr` - файл, содержащий зашифрованный запрос на выпуск сертификата.

3\. Создайте файл расширений сертификата для использования в генерации сертификата:

{% code overflow="wrap" %}
```
File: client1-dvpn.ext
# client1 certificate
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = client1.lan1.ru
```
{% endcode %}

* В этом файле используется subjectAltName (SAN) и указывается DNS-имя пользовательского устройства. DNS-имя используется в качестве имени пользователя Device VPN на Ideco NGFW.

4\. Сгенерируйте сертификат пользовательского устройства от [корневого сертификата для Device VPN](/settings/users/ideco-client/device-vpn-cert.md#sozdanie-kornevogo-sertifikata). Это может сделать администратор, используя зашифрованный [приватный ключ](/settings/users/ideco-client/device-vpn-cert.md#sozdanie-kornevogo-sertifikata) от корневого сертификата для Device VPN:

{% code overflow="wrap" %}
```
openssl x509 -req -in client1-dvpn.csr -CA ideco-dvpn_root-ca.pem -CAkey ideco-dvpn_root-ca.key -CAcreateserial -out client1-dvpn.crt -days 825 -sha256 -extfile client1-dvpn.ext
```
{% endcode %}

* `client1-dvpn.csr` - файл, содержащий зашифрованный запрос на выпуск сертификата;
* `ideco-dvpn_root-ca.pem` - файл, содержащий корневой сертификат;
* `ideco-dvpn_root-ca.key` - файл, содержащий приватный ключ корневого сертификата;
* `client1-dvpn.crt` - файл, содержащий пользовательский сертификат.

5\. Проверьте, что сертификат был успешно создан командой:

{% code overflow="wrap" %}
```
openssl x509 -text -noout -in client1-dvpn.crt
```
{% endcode %}

* `client1-dvpn.crt` - файл, содержащий пользовательский сертификат;
* Cертификат должен иметь атрибут `CA:FALSE` и `Subject Key Identifier`.

6\. Объедините приватный ключ и сертификат пользовательского устройства:

{% code overflow="wrap" %}
```
cat client1-dvpn.key client1-dvpn.crt > client1-dvpn.pem
```
{% endcode %}

* `client1-dvpn.key` - файл, содержащий приватный ключ;
* `client1-dvpn.crt` - файл, содержащий пользовательский сертификат;
* `client1-dvpn.pem` - файл, содержащий пользовательский сертификат с приватным ключом внутри.


7\. Сертификат `client1-dvpn.pem` с приватным ключом внутри, полученный на этом этапе, устанавливается на пользовательском устройстве и используется в параметрах Ideco Client.