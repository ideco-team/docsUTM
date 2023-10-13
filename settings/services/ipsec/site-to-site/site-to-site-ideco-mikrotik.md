# Подключение Ideco UTM и Mikrotik

{% hint style="info" %}
При объединении сетей с помощью VPN локальные сети в разных офисах не должны пересекаться.

Для корректной работы подключений по сертификатам синхронизируйте время на MikroTIk по NTP (например, предоставьте доступ в Интернет).

Исходящие IPsec-подключения по сертификатам к MikroTik ниже версии 6.45 не работают из-за невозможности использования современных криптоалгоритмов.
{% endhint %}

**При использовании** [**нашего конфигуратора скриптов настроек MikroTik**](https://mikrotik.ideco.ru) **есть несколько особенностей:**

* При подключении нескольких устройств MikroTik к одному Ideco UTM по PSK нужно указывать разные **Идентификаторы ключа (Key id)** для каждого устройства;
* При подключении нескольких устройств MikroTik к одному Ideco UTM по сертификатам нужно указывать разные **Имена сервера** (Common Name) для каждого устройства.

![](/.gitbook/assets/site-to-site-ideco-mikrotik.png)

## Выбор алгоритмов шифрования на удалённых устройствах

При настройке сторонних устройств необходимо явно указать алгоритмы шифрования, используемые для подключения.\
Ideco UTM не поддерживает устаревшие и небезопасные алгоритмы (MD5, SHA1, AES128, DES, 3DES, blowfish и др.).\
При конфигурировании сторонних устройств можно указать несколько поддерживаемых алгоритмов одновременно, так как не все устройства поддерживают современные алгоритмы.

<details>

<summary>Список алгоритмов и пример использования</summary>

* **Phase 1 (IKE):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (hash, целостность):
    * для **AES256-GCM** - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для **AES256**, по приоритету: **SHA512, SHA256**.
  * prf (функция генерации случайных значений):
    * как правило, настраивается автоматически, в зависимости от выбора алгоритмов integrity (поэтому в примере [ниже](connecting-devices.md#primer-nastroiki-podklyucheniya-pfsense-k-ideco-utm-po-ipsec-predstavlen-na-skrinshotakh-nizhe) значение prf: PRF-HMAC-SHA512);
    * для AES-GCM может потребоваться указать явно. В этом случае по приоритету: **AESXCBC, SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman):
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**.
  * Таймауты:
    * **Lifetime**: 14400 сек;
    * **DPD Timeout** (для L2TP/IPsec): 40 сек;
    * **DPD Delay**: 30 сек.
* **Phase 2 (ESP):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (целостность):
    * для **AES256-GCM** - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для **AES-256**, по приоритету: **SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman, PFS). **ВНИМАНИЕ! если не указать, подключаться будет, но не сработает rekey через некоторое время**:
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**.
  * Таймаут:
    * **Lifetime**: 3600 сек.

**Пример:**

* **Phase 1 (IKE)** (нужна одна из строк)**:**
  * AES256-GCM\PRF-HMAC-SHA512\Curve25519;
  * AES256\SHA512\PRF-HMAC-SHA512\ECP384;
  * AES256\SHA256\PRF-HMAC-SHA256\MODP2048.
* **Phase 2 (ESP)** (нужна одна из строк)**:**
  * AES256-GCM\ECP384;
  * AES256\SHA256\MODP2048.

Пример настройки подключения pfSense к Ideco UTM по IPsec:

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik1.png" alt="" data-size="original">

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik2.png" alt="" data-size="original">

</details>

## Исходящее подключение

### Тип аутентификации PSK

<details>

<summary>Настройка Ideco UTM</summary>

1\. Откройте вкладку **Сервисы -> IPsec -> Устройства(исходящие подключения)**, нажмите на **Добавить** ![ok\_with\_icon.png](/.gitbook/assets/ok-with-icon.png) и заполните поля:

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов;
* **Адрес удаленного устройства** - укажите внешний IP-адрес устройства MikroTik;
* **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется для настройки подключения в MikroTik;
* **Идентификатор ключа** - введенный ключ будет использоваться для идентификации исходящего подключения;
* **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут видны противоположной стороне;
* **Удаленные локальные сети** - перечислите все **локальные сети MikroTik**, которые будут видны противоположной стороне.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik3.png" alt="" data-size="original">

2\. После заполнения всех полей нажмите **Добавить подключение**. В списке подключений появится созданное подключение:

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik4.png" alt="" data-size="original">

</details>

<details>

<summary>Настройка Mikrotik</summary>

Настройку устройства MikroTik можно осуществить несколькими способами:

* GUI;
* Консоль устройства;
* Конфигурационными скриптами ([https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru)).

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором, и запустить.

</details>

### Тип аутентификации Сертификат

Подключение по сертификатам является более безопасным по сравнению с PSK.

<details>

<summary>Настройка Ideco UTM</summary>

Сгенерируйте запрос на подпись сертификата:

1\. В Ideco UTM откройте вкладку **Сервисы -> IPsec -> Устройства(исходящие подключения)**, нажмите на **Добавить** ![ok\_with\_icon.png](/.gitbook/assets/ok-with-icon.png) и заполните поля:

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов;
* **Адрес удаленного устройства** - укажите внешний IP-адрес MikroTik;
* **Запрос на подпись сертификата** - будет сгенерирован **запрос, который необходимо выслать для подписи на MikroTik**.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik5.png" alt="" data-size="original">

2\. После подписания запроса необходимо продолжить настройку подключения в Ideco UTM.

**Не закрывайте вкладку с настройками!** При закрытии вкладки с настройками _Запрос на подпись сертификата_ изменит значение и процесс подписания файла UTM.csr потребуется повторить.

</details>

<details>

<summary>Настройка MikroTik</summary>

На данном этапе следует настроить MikroTik, чтобы продолжить настройку UTM.

Файл **UTM.csr**, полученный из Ideco UTM, необходимо загрузить в файловое хранилище MikroTik:

1. Откройте раздел **File**.
2. Нажмите кнопку **Browse**.
3. Выберите файл и загрузите его.

Настройку MikroTik можно осуществить:

* Через GUI;
* Через консоль устройства;
* Через конфигурационные скрипты, сгенерированные по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru).

После генерации скрипта откройте раздел **System -> Scripts**, создайте скрипт и вставьте в него код, сгенерированный конфигуратором, затем запустите.

В файловой системе MikroTik появятся два файла, которые необходимо скачать, чтобы впоследствии загрузить на UTM.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik6.png" alt="" data-size="original">

Файл вида `cert_export_device_<случайный набор символов>.ipsec.crt` - **это подписанный сертификат UTM**.\
Файл вида `cert_export_mk_ca.crt` - **это корневой сертификат MikroTik.**

</details>

<details>

<summary>Завершение настройки Ideco UTM</summary>

Перейдите обратно на Ideco UTM во вкладку с настройками подключения устройства и продолжите заполнять поля:

* **Подписанный сертификат UTM** - загрузите подписанный в MikroTik сертификат UTM;
* **Корневой сертификат удаленного устройства** - загрузите корневой сертификат MikroTik;
* **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут видны противоположной стороне;
* **Удаленные локальные сети** - перечислите все **локальные сети MikroTik**, которые будут видны противоположной стороне.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik7.png" alt="" data-size="original">

Нажмите кнопку **Добавить подключение**.

</details>

## Входящее подключение

### Тип аутентификации PSK

<details>

<summary>Настройка MikroTik</summary>

Настройку устройства MikroTik можно осуществить:

* Через GUI
* Через консоль устройства
* Через конфигурационные скрипты, сгенерированные по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru).

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором и запустить.

</details>

<details>

<summary>Настройка Ideco UTM</summary>

1\. В Ideco UTM откройте вкладку **Сервисы -> IPsec -> Устройства(входящие подключения)**, нажмите на **Добавить** ![ok\_with\_icon.png](/.gitbook/assets/ok-with-icon.png) и заполните поля:

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов;
* **PSK** - вставьте PSK-ключ, полученный от MikroTik;
* **Идентификатор удаленной стороны** - вставьте идентификатор MikroTik (параметр Key ID в `/ip ipsec peers`);
* **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут видны противоположной стороне;
* **Удаленные локальные сети** - перечислите все локальные сети MikroTik, которые будут видны противоположной стороне.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik8.png" alt="" data-size="original">

2\. Нажмите кнопку **Добавить подключение**.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik9.png" alt="" data-size="original">

</details>

### Тип аутентификации Сертификат

Подключение по сертификатам является более безопасным, чем подключение по PSK.

<details>

<summary>Настройка MikroTik</summary>

Настройку MikroTik можно осуществить:

* Через GUI;
* Через консоль устройства
* Через конфигурационные скрипты, сгенерированные по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru) .

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором, и запустить его.

Конфигуратором генерируется два скрипта, потому в MikroTik также нужно создать два скрипта.

Перед настройкой необходимо запустить первый скрипт. В файловом хранилище MikroTik появятся два файла, которые необходимо скачать, они требуются для дальнейшей настройки:

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik10.png" alt="" data-size="original">

* Файл `certificate-request.pem` - **запрос на подпись сертификата**;
* Файл `certificate-request_key.pem` - **приватный ключ**.

Далее переходим к настройке Ideco UTM.

</details>

<details>

<summary>Настройка Ideco UTM</summary>

1\. В Ideco UTM откройте вкладку **Сервисы -> IPsec -> Устройства(входящие подключения)**, нажмите на **Добавить** ![ok\_with\_icon.png](/.gitbook/assets/ok-with-icon.png) и заполните поля:

* **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов;
* **Запрос на подпись сертификата** - загрузите запрос на подпись, **полученный от MikroTik**;
* **Домашние локальные сети** необходимо перечислить все локальные сети UTM, которые будут доступны в IPsec-подключении, т.е. будут видны противоположной стороне.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik11.png" alt="" data-size="original">

2\. Нажмите кнопку **Добавить подключение**. Нажмите на кнопку редактирования соединения, чтобы продолжить настройку.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik12.png" alt="" data-size="original">

3\. Скачайте файлы, которые находятся в полях **Корневой сертификат UTM** и **Подписанный сертификат устройства**, для их последующего использования в MikroTik.

<img src="/.gitbook/assets/site-to-site-ideco-mikrotik13.png" alt="" data-size="original">

</details>

### Проблемы при повторной активации входящего подключения к Ideco UTM

Если подключение было отключено и при попытке включения соединение не установилось, удаленное устройство попало в fail2ban. Для установки соединения сбросьте блокировки по IP на Ideco UTM. О сбросе блокировки читайте в статье [Защита от brute-force атак](/settings/reports/logs.md#защита-от-brute-force-атак).

Fail2ban отслеживает в log-файлах попытки обратиться к сервисам, и если находит повторяющиеся неудачные попытки авторизации с одного и того же IP-адреса или хоста, блокирует IP-адрес.

## Подключение Mikrotik к Ideco UTM по L2TP/IPsec

Настройте подключение, выполнив команды:

1\. Отредактируйте IPsec profile:

```
ip ipsec profile set default hash-algorithm=sha1 enc-algorithm=aes-256 dh-group=modp2048
```

2\. Отредактируйте IPsec proposals:

```
ip ipsec proposal set default auth-algorithms=sha1 enc-algorithms=aes-256-cbc,aes-192-cbc,aes-128-cbc pfs-group=modp2048
```

3\. Создайте подключение к Ideco UTM:

```
interface l2tp-client add connect-to=<server> profile=default disabled=no name=<interface_name> password="<password>" user="<login>" use-ipsec="yes" ipsec-secret="<psk>"
```

4\. Добавьте маршрут до первого адреса VPN-cети UTM (remote VPN subnet):

```
ip route add dst-address=<remote VPN subnet> gateway=l2tp-out1
```

{% hint style="info" %}
Для работы удаленных сетей на UTM и на Mikrotik нужно создавать маршруты на обоих устройствах.
{% endhint %}

{% hint style="info" %}
Если у вас в разделе **Правила трафика -> Файрвол -> SNAT** отключен **Автоматический SNAT локальных сетей**, то может понадобиться прописать маршрут до сети VPN, где шлюзом является UTM.

Пример:

* Aдрес UTM = 169.254.1.5
* Первый адрес VPN = 10.128.0.1

`ip route add dst-address=169.254.1.5 gateway==10.128.0.1`
{% endhint %}

## Подключение Mikrotik к Ideco UTM по IKev2/IPsec

1\. Откройте WinBox.

2\. Перейдите в терминал, нажав `new terminal`:

![](/.gitbook/assets/site-to-site-ideco-mikrotik14.png)

3\. Загрузите сертификат выполнив команды:

```
/tool fetch url="https://letsencrypt.org/certs/letsencryptauthorityx1.pem" dst-path=letsencryptauthorityx1.pem
/tool fetch url="https://letsencrypt.org/certs/lets-encrypt-r3.pem" dst-path=lets-encrypt-r3.pem
```

4\. Импортируйте сертификат выполнив команды:

```
/certificate import file-name=isrgrootx1.pem passphrase="" name=lisrgrootx1.pem
/certificate import file-name=lets-encrypt-r3.pem passphrase="" name=lets-encrypt-r3
```

5\. Настройте алгоритмы шифрования для IPsec step 1 (IKE):

```
/ip ipsec profile add dh-group=modp4096,modp2048,modp1024 dpd-interval=2m dpd-maximum-failures=5 enc-algorithm=aes-256,aes-192,aes-128 hash-algorithm=sha256 lifetime=1d name=IKEv2_TO_UTM nat-traversal=yes proposal-check=obey
```

6\. Настройте алгоритмы шифрования для IPsec step 2 (ESP)

```
/ip ipsec proposal add auth-algorithms=sha512,sha256,sha1 disabled=no enc-algorithms="aes-256-cbc,aes-256-ctr,aes-256-gcm,aes-192-cbc,aes-192-gcm,aes-128-cbc,aes-128-ctr,aes-128-gcm" lifetime=30m name=IKev2_to_UTM pfs-group=modp1024
```

7\. Настройте одноранговый узел. В качестве `address` укажите доменное имя, которое используется для IKev2 подключения:

```
/ip ipsec peer add address={ideco.test.ru} disabled=no exchange-mode=ike2 name=IKEV2_TO_UTM profile=IKEv2_TO_UTM send-initial-contact=yes
```

8\. Создайте группу, которая будет использоваться для автоматического NAT:

```
/ip ipsec policy group add name=IKEv2_TO_UTM
```

9\. Создайте address-list в котором находятся Удаленные сети УТМ. Если за UTM несколько подсетей, то нужно создавать несколько элементов в списке. 

```
/ip firewall address-list add address={1.2.3.0/24} disabled=no list=Behind_UTM_Gateway
```

10\. Создайте новую запись конфигурации режима с ответчиком `= no`, которая будет запрашивать параметры конфигурации с сервера:

```
/ip ipsec mode-config add connection-mark=no-mark name=IKEv2_TO_UTM responder=no src-address-list=Behind_UTM_Gateway use-responder-dns=yes
```

11\. Создайте политику, которая придет с УТМ(в виде шаблона):

```
/ip ipsec policy add disabled=no dst-address=0.0.0.0/0 group=IKEv2_TO_UTM proposal=IKEv2_TO_UTM protocol=all src-address=0.0.0.0/0 template=yes
```

12\. Создайте профиль идентификации пользователя:

```
/ip ipsec identity add auth-method=eap certificate="" disabled=no eap-methods=eap-mschapv2 generate-policy=port-strict mode-config=IKEv2_TO_UTM peer=IKEV2_TO_UTM policy-template-group=IKEv2_TO_UTM username=<'login'> password=<'password'> 
```

13\. Перейдите в веб-интерфейс NGFW в раздел **Пользователи —> VPN подключения** и в строке **Сеть для VPN-подключений** добавьте первый адрес сети VPN:

![](/.gitbook/assets/site-to-site-ideco-mikrotik15.png)

14\. Создайте маршрут до удаленных сетей UTM через интерфейс который смотрит в Интернет.

```
/ip route add disabled=no dst-address={10.128.0.0/16} gateway=ether1 routing-table=main
```
* где в качестве gateway={ether1} интерфейс который выходит в интернет.