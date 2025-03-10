---
description: >- 
  Описывается процесс объединения локальной сети Ideco UTM и удаленного устройства.
---

# Устройства

Подключение устройств по IPsec позволит обеспечить безопасность сетевых соединений и защитить данные, передаваемые между устройствами. 

Воспользуйтесь конфигураторами подключений для [MikroTik](https://mikrotik.ideco.ru/) или [Cisco](https://cisco.ideco.ru/). Они позволяют сгенерировать конфиг, запуск которого на удаленном устройстве установит заранее подготовленные настройки IPsec.

## Исходящие подключения

Настройте исходящее подключение, если Ideco UTM инициатор подключения, а удаленное устройство принимающая сторона.

Для настройки исходящего подключения, в зависимости от типа аутентификации, подготовьте:

**Сертификат**
* Подписанный удаленным устройством **Запрос на подпись сертификата**. Файл запроса скачивается из веб-интерфейса UTM при создании подключения (![](/.gitbook/assets/icon-down.png)), отправляется удаленному устройству и подписанный возвращается для настройки UTM;
* Корневой сертификат удаленного устройства;
* Список домашних локальных сетей UTM, которые будут видны противоположной стороне;
* Список всех локальных сетей удаленного устройства, которые будут видны противоположной стороне.

**PSK**
* PSK-ключ. Генерируется на UTM при создании подключения;
* Идентификатор ключа, который потребуется удаленному устройству для идентификации подключения;
* Список локальных сетей UTM, которые будут видны противоположной стороне;
* Список локальных сетей удаленного устройства, которые будут видны противоположной стороне.

## Входящие подключения

Настройте входящее подключение, если удаленное устройство инициатор подключения, а Ideco UTM принимающая сторона.

Для настройки входящего подключения, в зависимости от типа аутентификации, подготовьте:

**Сертификат**
* Запрос на подпись сертификата (`.csr`), полученный от удаленного устройства;
* Список домашних локальных сетей UTM, которые будут видны противоположной стороне;
* Список всех локальных сетей удаленного устройства, которые будут видны противоположной стороне.

**PSK**
* PSK-ключ, сгенерированный на удаленном устройстве;
* Идентификатор удаленной стороны для идентификации входящего подключения;
* Список локальных сетей UTM, которые будут видны противоположной стороне;
* Список локальных сетей удаленного устройства, которые будут видны противоположной стороне.

{% hint style="info" %}
Примеры подключения устройств описаны в статьях [Подключение офисов (site-to-site)](../ipsec/connect-offices/README.md).
{% endhint %}
