# Создание самоподписанного сертификата c помощью openssl

{% hint style="info" %}
Используйте эту статью, если вы пользуетесь операционной системой с ядром Linux.
При использовании операционной системы Windows воспользуйтесь статьей [Создание самоподписанного сертификата c помощью Powershell](creating-ssl-sert-powershell.md)
{% endhint %}

Для создания самоподписанного сертификата выполните действия:

1\. Создайте закрытый ключ для сертификата:

```
openssl genrsa -out ca.key 2048
```

   * ca.key - Файл с приватным ключом.

2\. Создайте запрос на подпись сертификата:

```
openssl req -key ca.key -new -out cert.csr
```
   * ca.key - Файл с приватным ключом;
   * cert.csr - Файл с запросом на подпись.

3\. Cоздайте файл с именем test.txt:

```
cat >> ./test.txt << EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:TRUE
keyUsage = digitalSignature, keyCertSign, cRLSign
subjectAltName=DNS:test.com
EOF
```
   * test.txt - Файл с расширениями сертификата;
   * test.com - Доменное имя сервера.

4\. Сгенерируйте самоподписанный сертификат:
   
```
openssl x509 -extfile ./test.txt -signkey ca.key -in cert.csr -req -days 365 -out ca.crt
```

   * test.txt - Файл, cозданный в 3 пункте;
   * ca.key - Файл с приватным ключом;
   * cert.csr - Файл с запросом на подпись сертификата;
   * ca.crt - Файл со сгенерированным сертификатом.

5\. Добавьте к сертификату приватный ключ:

```
cat ca.key ca.crt > server.pem
```

   * server.pem - Самоподписанный сертификат для загрузки на сервер.

{% hint style="info" %}
Для загрузки сертификата на сервер воспользуйтесь статьей [Загрузка SSL-сертификата на сервер](/settings/services/certificates/upload-own-ssl.md)
{% endhint %}