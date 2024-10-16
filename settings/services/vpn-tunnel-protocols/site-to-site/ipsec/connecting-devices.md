---
title: Подключение устройств
published: true
date: '2021-06-02T06:21:52.323Z'
tags: ipsec
editor: markdown
dateCreated: '2021-04-02T07:28:30.490Z'
description: >-
  Описание вариантов подключения различных роутеров (Mikrotik, Zyxel Keenetic и
  др.) к Ideco UTM для организации site-to-site VPN с использованием протокола
  IPsec IKEv2.
---

# Подключение устройств

Устройства, которые не описаны в данной инструкции, как правило, можно подключить с использованием аналогичных настроек.

{% hint style="info" %}
При объединении сетей с помощью VPN, локальные сети в разных офисах не должны пересекаться.
{% endhint %}

**При использовании нашего конфигуратора скриптов настроек MikroTik (**[https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru)**) есть несколько особенностей:**

* При подключении нескольких устройств MikroTik к одному Ideco UTM по PSK, нужно указывать разные **Идентификаторы ключа (Key id)** для каждого устройства.
* При подключении нескольких устройств MikroTik к одному Ideco UTM по сертификатам, нужно указывать разные **Имена сервера** (Common Name) для каждого устройства.

![](../../../../../.gitbook/assets/screenshot\_9.png)

### Выбор крипто-алгоритмов на удалённых устройствах.

При настройке сторонних устройств необходимо явно указать криптоалгоритмы, используемые для подключения. Ideco UTM поддерживает самые современные и одновременно достаточно безопасные алгоритмы, не нагружающие сервер и устройства. При этом, не поддерживаются устаревшие и считающиеся небезопасными алгоритмы (MD5, SHA1, AES128, DES, 3DES, blowfish и др.). При конфигурировании сторонних устройств, как правило, можно указать несколько поддерживаемых алгоритмов одновременно. По факту, нужен один алгоритм каждого вида. К сожалению, не все устройства поддерживают самые лучшие алгоритмы, поэтому Ideco UTM поддерживает сразу несколько. Список алгоритмов каждого вида указан ниже в порядке убывания приоритета для выбора.

* **Phase 1 (IKE):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (hash, целостность):
    * для AES256-GCM - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для AES256, по приоритету: **SHA512, SHA256**.
  * prf (функция генерации случайных значений):
    * как правило, настраивается автоматически, в зависимости от выбора алгоритмов integrity (поэтому в примере [ниже](connecting-devices.md#primer-nastroiki-podklyucheniya-pfsense-k-ideco-utm-po-ipsec-predstavlen-na-skrinshotakh-nizhe) значение prf: PRF-HMAC-SHA512).
    * для AES-GCM может потребоваться указать явно. В этом случае по приоритету: **AESXCBC, SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman):
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**.
* **Phase 2 (ESP):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (целостность):
    * для AES256-GCM - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для AES-256, по приоритету: **SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman, PFS). **ВНИМАНИЕ! если не указать, подключаться будет, но не сработает rekey через некоторое время**:
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**.

#### **Пример:**

* **Phase 1 (IKE)** (нужна одна из строк)**:**
  * AES256-GCM\PRF-HMAC-SHA512\Curve25519
  * AES256\SHA512\PRF-HMAC-SHA512\ECP384
  * AES256\SHA256\PRF-HMAC-SHA256\MODP2048
* **Phase 2 (ESP)** (нужна одна из строк)**:**
  * AES256-GCM\ECP384
  * AES256\SHA256\MODP2048

#### Пример настройки подключения pfSense к Ideco UTM по IPsec представлен на скриншотах ниже:

![](../../../../../.gitbook/assets/phase1.png)

![](../../../../../.gitbook/assets/phase2.png)

## Подключение Ideco UTM к MikroTik с использованием PSK

При наличии на устройстве MikroTik «белого» IP-адреса, выполните действия ниже, чтобы настроить подключение Ideco UTM к MikroTik.

### Шаг 1. Настройка Ideco UTM

1\. В Ideco UTM откройте вкладку **Сервисы -> IPSec -> Устройства**, нажмите на значок ![](<../../../../../.gitbook/assets/ok-with-icon (3).png>) и заполните следующие поля:

2\. **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.

3\. **Тип соединения** - выберите **Исходящее**, поскольку осуществляется подключение от UTM.

4\. **Адрес удаленного устройства** - укажите внешний IP-адрес устройства MikroTik.

5\. **Тип аутентификации** - выберите тип **PSK**.

6\. **PSK** - будет сгенерирован случайный PSK-ключ. Он потребуется, чтобы настроить подключение в MikroTik.

7\. **Идентификатор ключа** - введенный вами ключ будет использоваться для идентификации исходящего подключения.

8\. **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

9\. **Удаленные локальные сети** - перечислите все **локальные сети MikroTik**, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

![](../../../../../.gitbook/assets/connetc\_device.png)

10\. После заполнения всех полей нажмите кнопку **Добавить подключение**. В списке подключений появится ваше подключение.

![](../../../../../.gitbook/assets/out-connection.png)

### Шаг 2. Настройка Mikrotik

Настройку устройства MikroTik можно осуществить несколькими способами - через GUI, через консоль устройства или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru).

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором и запустить.

После того как скрипт закончит свою работу, никаких дополнительных действий по настройке не требуется.

## Подключение MikroTik к Ideco UTM с использованием PSK

При наличии на Ideco UTM «белого» IP-адреса, выполните действия ниже, чтобы настроить подключение устройства MikroTik к Ideco UTM.

### Шаг 1. Настройка MikroTik

Настройку устройства MikroTik можно осуществить несколькими способами - через GUI, через консоль устройства или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru).

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором и запустить.

После того как скрипт закончит свою работу, никаких дополнительных действий по настройке не требуется.

### Шаг 2. Настройка Ideco UTM

1\. В Ideco UTM откройте вкладку **Сервисы -> IPSec -> Устройства**, нажмите на значок ![](<../../../../../.gitbook/assets/ok-with-icon (3).png>) и заполните следующие поля:

2\. **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.

3\. **Тип соединения** - выберите **Входящее**, поскольку осуществляется подключение к UTM.

4\. **Тип аутентификации** - укажите тип **PSK**.

5\. **PSK** - вставьте PSK-ключ, полученный от MikroTik.

6\. **Идентификатор удаленной стороны** - вставьте идентификатор MikroTik (параметр Key ID в `/ip ipsec peers`).

7\. **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

8\. **Удаленные локальные сети** - перечислите все локальные сети MikroTik, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

![](../../../../../.gitbook/assets/in-device.png)

9\. После заполнения всех полей нажмите кнопку **Добавить подключение**. В списке подключений появится ваше подключение.

![](../../../../../.gitbook/assets/in-connection.png)

## Подключение Ideco UTM к MikroTik с использованием сертификатов

Подключение по сертификатам используется, так как является более безопасным, чем подключение по PSK, либо в случаях, когда устройство не поддерживает PSK.

{% hint style="info" %}
Для корректной работы подключений по сертификатам необходимо, чтобы на MikroTIk время было синхронизировано по NTP. Для этого достаточно, чтобы на устройстве присутствовал доступ в сеть Интернет.
{% endhint %}

### Шаг 1. Настройка Ideco UTM

1\. В Ideco UTM откройте вкладку **Сервисы -> IPSec -> Устройства**, нажмите на значок ![](<../../../../../.gitbook/assets/ok-with-icon (3).png>) и заполните следующие поля:

2\. **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.

3\. **Тип подключения** - выберите **Исходящее**, поскольку осуществляется подключение от UTM.

4\. **Тип аутентификации** - укажите тип **Сертификат**.

5\. **Адрес удаленного устройства** - укажите внешний IP-адрес MikroTik.

6\. **Запрос на подпись сертификата** - будет сгенерирован **запрос, который необходимо выслать для подписи на MikroTik**.

![](../../../../../.gitbook/assets/sign\_sert.png)

7\. После того как запрос будет подписан, необходимо будет продолжить настройку подключения в Ideco UTM.

{% hint style="warning" %}
**Не закрывайте вкладку с настройками!**
{% endhint %}

### Шаг 2. Настройка MikroTik

На данном этапе следует настроить MikroTik, чтобы продолжить настройку UTM.

Файл **UTM.csr**, полученный из Ideco UTM, необходимо загрузить в файловое хранилище MikroTik. Для этого необходимо открыть раздел **File**, нажать кнопку **Browse**, выбрать файл и загрузить его.

Настройку MikroTik можно осуществить несколькими способами - через GUI, через консоль устройства или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru).

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором и запустить.

После того как скрипт закончит свою работу, в файловой системе MikroTik появятся два файла, которые необходимо скачать, чтобы впоследствии загрузить на UTM.

![](<../../../../../.gitbook/assets/6587096 (1) (1) (2).png>)

Файл вида `cert_export_device_<случайный набор символов>.ipsec.crt` - **это подписанный сертификат UTM**. Файл вида `cert_export_mk_ca.crt` - **это корневой сертификат MikroTik.**

На этом настройку MikroTik можно считать завершенной.

### Шаг 3. Завершение настройки Ideco UTM

Перейдите обратно на Ideco UTM во вкладку с настройками подключения устройства и продолжите заполнять следующие поля:

* **Подписанный сертификат UTM** - загрузите подписанный в MikroTik сертификат UTM.
* **Корневой сертификат удаленного устройства** - загрузите корневой сертификат MikroTik.
* **Домашние локальные сети** - перечислите все **локальные сети UTM**, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.
* **Удаленные локальные сети** - перечислите все **локальные сети MikroTik**, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

![](../../../../../.gitbook/assets/ipsec-cert.png)

После заполнения полей нажмите кнопку **Добавить подключение**. В списке подключений появится ваше подключение.

## Подключение MikroTik к Ideco UTM по сертификатам

Подключение по сертификатам используется, так как является более безопасным, чем подключение по PSK, либо в случаях, когда устройство не поддерживает PSK.

{% hint style="info" %}
Для корректной работы подключений по сертификатам необходимо, чтобы на MikroTIk время было синхронизировано по NTP. Для этого достаточно, чтобы на устройстве присутствовал доступ в сеть Интернет.
{% endhint %}

### Шаг 1. Настройка MikroTik

Настройку MikroTik можно осуществить несколькими способами - через GUI, через консоль устройства или, воспользовавшись нашими конфигурационными скриптами, сгенерированными по адресу [https://mikrotik.ideco.ru/](https://mikrotik.ideco.ru) .

После генерации скрипта необходимо открыть раздел **System -> Scripts**, создать скрипт, вставить в него код, сгенерированный конфигуратором и запустить его.

Поскольку скриптов конфигуратором генерируется два, то и в MikroTik также нужно создать два скрипта.

Перед настройкой необходимо запустить первый скрипт. После того как он завершит работу, в файловом хранилище MikroTik появятся два файла, которые необходимо скачать, поскольку они требуются для дальнейшей настройки.:

![](<../../../../../.gitbook/assets/6587097 (1).png>)

* Файл `certificate-request.pem` - **запрос на подпись сертификата**.
* Файл `certificate-request_key.pem` - **приватный ключ**.

Далее потребуется заполнить поле **Запрос на подпись сертификата** в Ideco UTM, поэтому перейдем к его настройке.

### Шаг 2. Настройка Ideco UTM

1\. В Ideco UTM откройте вкладку **Сервисы -> IPSec -> Устройства**, нажмите на значок ![](<../../../../../.gitbook/assets/ok-with-icon (3).png>) и заполните следующие поля:

2\. **Название подключения** - укажите произвольное имя для подключения. Значение не должно быть длиннее 42 символов.

3\. **Тип подключения** - выберите **Входящее**, поскольку осуществляется подключение к UTM.

4\. **Тип аутентификации** - укажите тип **Сертификат**.

5\. **Запрос на подпись сертификата** - загрузите запрос на подпись, **полученный от MikroTik**.

6\. **Домашние локальные сети** необходимо перечислить все локальные сети UTM, которые будут доступны в IPSec-подключении, т.е. будут видны противоположной стороне.

![](../../../../../.gitbook/assets/ipsec-query.png)

7\. После настроек нажмите кнопку **Добавить подключение**. В списке подключений появится ваше подключение. Нажмите на кнопку редактирования соединения, чтобы продолжить настройку.

![](../../../../../.gitbook/assets/edit-connection.png)

8\. Появится область редактирования настроек подключения. Необходимо скачать файлы, которые находятся в полях **Корневой сертификат UTM** и **Подписанный сертификат устройства**, для их последующего использования в MikroTik.

![](../../../../../.gitbook/assets/edit-cert.png)

### Проблемы при повторной активации входящего подключения к Ideco UTM

Если, после использования данного подключения, вы его отключили, например, за ненадобностью, и, при попытке повторного включения, соединение не установилось, то скорее всего удаленное устройство попало в fail2ban (инструмент, который отслеживает в log-файлах попытки обратиться к сервисам, и если находит повторяющиеся неудачные попытки авторизации с одного и того же IP-адреса или хоста, блокирует дальнейшие попытки).\
Для того чтобы соединение установилось, необходимо сбросить блокировки по IP на Ideco UTM. О том как это сделать, читайте в статье [Защита от bruteforce атак](../../../../access-rules/fail2ban.md).

## Подключение Mikrotik к Ideco UTM по L2TP/IPsec

Настройте подключение, выполнив следующие команды:

1\. Отредактируйте IPSec profile:

```
ip ipsec profile set default hash-algorithm=sha1 enc-algorithm=aes-256 dh-group=modp2048
```

2\. Отредактируйте IPSec proposals:

```
ip ipsec proposal set default auth-algorithms=sha1 enc-algorithms=aes-256-cbc,aes-192-cbc,aes-128-cbc pfs-group=modp2048
```

3\. Создайте подключение к Ideco UTM:

```
interface l2tp-client add connect-to={server} profile=default disabled=no name={interface_name} password="{password}" user="{login}" use-ipsec="yes" ipsec-secret="{psk}"
```