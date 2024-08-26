# Создание самоподписанного сертификата c помощью openssl

{% hint style="info" %}
Используйте эту статью, если вы пользуетесь операционной системой с ядром Linux.
При использовании операционной системы Windows воспользуйтесь статьей [Создание самоподписанного сертификата c помощью PowerShell](creating-ssl-sert-powershell.md).
{% endhint %}

Для создания самоподписанного сертификата выполните действия:

1\. Создайте закрытый ключ для сертификата:

```
openssl genrsa -out ca.key 2048
```

Где `ca.key` - файл с приватным ключом.

2\. Создайте запрос на подпись сертификата:

```
openssl req -key ca.key -new -out cert.csr
```
   * `ca.key` - файл с приватным ключом;
   * `cert.csr` - файл с запросом на подпись.

3\. Cоздайте файл с именем test.txt:

```
cat >> ./test.txt << EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:TRUE
keyUsage = digitalSignature, keyCertSign, cRLSign
subjectAltName=DNS:test.com
EOF
```
   * `test.txt` - файл с расширениями сертификата;
   * `test.com` - доменное имя сервера.

4\. Сгенерируйте самоподписанный сертификат:
   
```
openssl x509 -extfile ./test.txt -signkey ca.key -in cert.csr -req -days 365 -out ca.crt
```

   * `test.txt` - файл, cозданный в 3 пункте;
   * `ca.key` - файл с приватным ключом;
   * `cert.csr` - файл с запросом на подпись сертификата;
   * `ca.crt` - файл со сгенерированным сертификатом.

5\. Добавьте к сертификату приватный ключ:

```
cat ca.key ca.crt > server.pem
```

   Где `server.pem` - cамоподписанный сертификат для загрузки на сервер.

{% hint style="info" %}
Для загрузки сертификата на сервер воспользуйтесь статьей [Загрузка SSL-сертификата на сервер](/settings/services/certificates/upload-ssl-certificate-to-server.md)
{% endhint %}