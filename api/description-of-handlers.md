# Описание основных хендлеров

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

<details>

<summary>Авторизация</summary>

```
POST /web/auth/login
```

**Json-тело запроса:**

```json5
{
    "login": "string",
    "password": "string",
    "rest_path": "string",
}

```
* `login` - логин, каталог администратора указывается после `@`. Примеры:
    * `admin` - локальный админ, без `@`;
    * `admin@ad_domain.ru` - AD/ALD администратор;
    * `admin@radius` - для RADIUS-администраторов `@radius`.
* `password` - пароль;
* `rest_path` - префикс URL, на который выставлять cookie. Например, `/` или `/rest`.

**Ответ на успешный запрос:** 200 ОК

После успешной авторизации сервер Ideco NGFW передает в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=02428c1c-fcd5-42ef-a533-5353da743806
set-cookie: __Secure-ideco-3ea57fca-65cb-439b-b764-d7337530f102=df164532-b916-4cda-a19b-9422c2897663:1663839003
```

Эти куки нужно передавать при каждом запросе после авторизации в заголовке запроса Cookie.

</details>

<details>

<summary>Разавторизация администратора</summary>

```
DELETE /web/auth/login
```

**Ответ на успешный запрос:** 200 ОК

После успешной разавторизации сервер Ideco NGFW передает в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
set-cookie: __Secure-ideco-b7e3fb6f-7189-4f87-a4aa-1bdc02e18b34=""; HttpOnly; Max-Age=0; Path=/; SameSite=Strict; Secure
```

</details>

<details>
<summary>Добавление правила авторизации</summary>

```
POST /auth/rules
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "ip": "string" | "null",
    "mac": "string" | "null",   
    "user_id":  "integer",
    "always_logged": "boolean",
    "comment": "string"
}
```

* `enabled` - `true` для включения правила, `false` для выключения;
* `ip` - IP-адрес, который нужно авторизовать;
* `mac` - MAC-адрес, который нужно авторизовать;
* `always_logged` - авторизован всегда. Может быть включено только при указанном IP;
* `user_id` - идентификатор пользователя, к которому будет применено правило;
* `comment` - комментарий к правилу, может быть пустым, максимальная длина - 255 символов.

**Ответ на успещный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного правила.

</details>

<details>
<summary>Измененение части правила авторизации</summary>

``` 
PATCH /auth/rules/<id правила>
```

```json5
{
    "enabled": "boolean",
    "ip": "string" | "null",
    "mac": "string" | "null",   
    "user_id":  "integer",
    "always_logged": "boolean",
    "comment": "string"
}
```

* `enabled` - `true` для включения правила, `false` для выключения;
* `ip` - IP-адрес, который нужно авторизовать;
* `mac` - MAC-адрес, который нужно авторизовать;
* `always_logged` - авторизован всегда. Может быть включено только при указанном IP;
* `user_id` - идентификатор пользователя, к которому будет применено правило;
* `comment` - комментарий к правилу, может быть пустым, максимальная длина - 255 символов.

**Ответ на успещный запрос:** 200 ОК

</details>

<details>
<summary>Удаление правила авторизации</summary>

```
DELETE /auth/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Сбор анонимной статистики о работе сервера</summary>

### Получение текущих настроек:

```
GET /gather_stat/settings
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - если `true`, то сбор анонимной статистики о работе сервера включен, `false` - выключен.

### Изменение настроек

```
PUT /gather_stat/settings
```

**Json-тело запроса**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Лицензирование

<details>
<summary>Регистрация сервера</summary>

```
POST /license/register
```

**Json-тело запроса:**

```json5
{
    "token": "string"
}
```

* `token` - получить токен лицензии можно в отделе продаж, он высылается в активационном письме;

**Ответ на успешный запрос:** 200 ОК

Чтобы добавить enterprise-demo лицензию, необходимо сначала получить токен лицензии в личном кабинете. Для этого выполните действия:

1\. Авторизуйтесь в личном кабинете myideco.ru:

```
POST /api/v3/login
```

**Json-тело запроса:**

```json5
{
    "login": "string",
    "password": "string",
    "g_recaptcha_response": "string" | "null"
}
```

2\. Выполните запрос на регистрацию сервера:

```
PUT /api/v3/<company_id>/go_to_product
```

*  `company_id` - идентификатор компании пользователя, его можно получить по запросу `GET /api/v3/companies`.

**Ответ на успешный запрос:**

```json5
{
    "token": "string"
}
```

Используйте полученный токен в теле запроса при регистрации Ideco NGFW.

</details>

<details>
<summary>Получение информации о лицензии</summary>

```
GET /license/info
```

**Пример ответа на успешный запрос:**

```json5
{
    "modules": {
        "active_directory": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "kaspersky_av_for_web": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "kaspersky_av_for_mail": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "application_control": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "suricata": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "advanced_content_filter": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "standard_content_filter": {
            "available": false,
            "expiration_date": 0
        },
        "ips_advanced_rules": {
            "available": true,
            "expiration_date": 1712400382.0
        },
        "icsd": {
            "available": true,
            "max_users_count": 10000
        }
    },
    "general": {
        "available": true,
        "reason": "",
        "not_upgrade_after": 1712400382.0,
        "tech_support_end": 1712400382.0,
        "start_date": 1708944382.2658572,
        "expiration_date": 1712400382.0
    },
    "license_type": "enterprise-demo",
    "license_id": "UTM-3883264353",
    "server_name": "UTM",
    "last_update_time": 1708944385.1747465,
    "company_id": "Ideco",
    "server_id": "OQHsviy10sEOOQXWs-8c7tnwJb4AaOvplT2iJc-im677",
    "registered": true,
    "unreliable": false,
    "has_connection": true,
    "license_server": "https://my.ideco.ru"
}
```

**Если лицензия для данного сервера отсутствует:**

```json5
{
    "registered": false,
    "has_connection": true,
    "license_server": "https://my.ideco.ru"
}
```

</details>

<details>
<summary>Получение информации о механизме обновления лицензии</summary>

```
GET /license/update-type
```

**Ответ на успешный запрос:**

```json5
{
    "update_type": "auto" | "manual"
}
```

* `auto` - при автоматическом получении лицензии;
* `manual` - при ручной загрузке лицензии.

</details>

<details>
<summary>Изменение механизма обновления лицензии</summary>

```
PUT /license/update-type
```

**Json-тело запроса:**

```json5
{
    "update_type": "auto" | "manual"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение ссылки для офлайн-регистрации</summary>

```
GET /license/license-get-offline-registration-url
```

**Ответ на успешный запрос:**

```json5
{
    "registration_url": "https://my.ideco.ru/offline_register?server_name=ZGF0YSB0byBiZSBlbmNvZGVk&hwid=u-CVv6SSNMXI_Mukgnf3SCIxJz9kcl0i50ARFk4FRz1O&version=17.1"
}
```

* `server_name` - имя сервера Ideco NGFW;
* `hwid` - HWID сервера;
* `version` - версия сервера.

Получение ссылки для офлайн-регистрации сервера возможно только при ручном механизме обновления лицензии.

</details>

<details>
<summary>Загрузка файла с лицензией на NGFW</summary>

```
POST /license/license-upload
```

**Тело запроса:** форма загрузки файла, имя поля в форме загрузки файла `license_file`

**Ответ на успешный запрос:** 200 ОК

</details>

## Управление объектами

<details>

<summary>Получение идентификаторов объектов</summary>

```
GET /aliases/<название обьекта> | all
```

**Ответ на успешный запрос:**

```json5
[
    {
        "comment": "string",
        "title": "string",
        "type": "string",
        "values": [
            "string" | "integer",
            "string" | "integer"
        ],
        "id": "type.id.1"
    }, 
{
        "comment": "string",
        "title": "string",
        "type": "string",
        "value": "string" | "integer",
        "id": "type.id.1"
    },
    ...
] 
```

В качестве ответа будет возвращен список всех объектов, существующих в NGFW:

* `protocol.ah` - протокол AH;
* `protocol.esp` - протокол ESP;
* `protocol.gre` - протокол GRE;
* `protocol.icmp` - протокол ICMP;
* `protocol.tcp` - протокол TCP;
* `protocol.udp` - протокол UDP;
* `quota.exceeded`- IP-адреса пользователей, которые превысили квоту;
* `any` - допускается любое значение в этом поле;
* `interface.external_any` - все внешние интерфейсы (равно таблице *Подключение к провайдеру* в веб-интерфейсе и включает в себя подключения к провайдеру по Ethernet/VPN);
* `interface.external_eth` - внешние Ethernet-интерфейсы;
* `interface.external_vpn` - внешние VPN-интерфейсы;
* `interface.ipsec_any` - IPsec-интерфейсы;
* `interface.local_any` - все локальные интерфейсы;
* `interface.tunnel_any` - все туннельные интерфейсы;
* `group.id.` - идентификатор группы пользователей;
* `interface.id.`- идентификатор конкретного интерфейса;
* `interface.utm_outgoing` - исходящий трафик устройства;
* `interface.vpn_traffic` - клиентский VPN-трафик;
* `interface.wccp_gre_any` - все WCCP GRE интерфейсы;
* `hip_profile.id.` - устройства без профиля;
* `security_group.guid.` - идентификатор группы безопасности AD;
* `user.id.` - идентификатор пользователя;
* `domain.id.` - идентификатор домена;
* `ip.id.` - идентификатор IP-адреса;
* `ip_range.id.` - идентификатор объекта *Диапазон адресов*;
* `address_list.id.` - идентификатор объекта *Список IP-объектов*;
* `list_of_iplists.id.` - идентификатор объекта *Список стран*;
* `port_list.id.` - идентификатор объекта *Порты*;
* `time_list.id.` - идентификатор объекта *Расписание*;
* `subnet.id.` - идентификатор объекта *Подсеть*;
* `port_range.id.` - идентификатор объекта *Диапазон портов*;
* `port.id.` - идентификатор объекта *Порт*;
* `time_range.id.` - идентификатор объекта *Время*.

</details>

### Создание обьектов

<details>

<summary>Создание объекта IP-адрес</summary>

```
POST /aliases/ip_addresses
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "string"
}
```

* `title` - название объекта. Максимальная длина - 42 символа;
* `comment` - комментарий к объекту. Может быть пустым, максимальная длина - 255 символов;
* `value` - IP-адрес в формате `192.168.0.0`.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта IP-адрес.

</details>

<details>

<summary>Создание объекта Диапазон IP-адресов</summary>

```
POST /aliases/ip_ranges
```

**Json-тело запроса:**

```json5
{
    "title": "string", 
    "comment": "string", 
    "start": "string", 
    "end": "string"
}
```

* `title` - название объекта. Максимальная длина - 42 символа;
* `comment` - комментарий к объекту. Может быть пустым, максимальная длина - 255 символов;
* `start` - первый IP-адрес в диапазоне, например, `192.168.100.2`;
* `end` - последний IP-адрес в диапазоне, например, `192.168.100.15`.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Диапазон IP-адресов.

</details>

<details>

<summary>Создание объекта Подсеть</summary>

```
POST /aliases/networks
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "string"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - адрес подсети в формате `192.168.0.0/24` либо `192.168.0.0/255.255.255.0`.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Подсеть.

</details>

<details>

<summary>Создание объекта Домен</summary>

```
POST /aliases/domains
```

**Json-тело запроса:**

```json5
{
    "title": "string", 
    "comment": "string",
    "value": "string" 
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - домен в формате mydomain.com.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Домен.

</details>

<details>

<summary>Создание объекта Порт</summary>

```
POST /aliases/ports
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "integer"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - номер порта в формате `8080`.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Порт.

</details>

<details>

<summary>Создание объекта Диапазон портов</summary>

```
POST /aliases/port_ranges
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "start": "integer",
    "end": "integer"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `start` - первый порт в диапазоне, например, 8080;
* `end` - последний порт в диапазоне, например, 8090.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Диапазон портов.

</details>

<details>

<summary>Создание объекта Время</summary>

```
POST /aliases/time_ranges
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "weekdays": [ "integer" ],
    "start": "string",
    "end": "string",
    "period": {
            "first": "integer",
            "last": "integer"
        }
}
```

* `title` - название объекта. Максимальная длина - 42 символа;
* `comment` - комментарий к объекту. Может быть пустым, максимальная длина - 255 символов;
* `weekdays` - список дней недели, где 1-пн, 2-вт ... 7-вс;
* `start` - начало временного отрезка в формате `ЧЧ:ММ`;
* `end` - конец временного отрезка в формате `ЧЧ:ММ`;
* `first` - момент начала срока действия в формате `ГГГГММДДЧЧММСС`, например, `20240215000000`;
* `last` - момент окончания срока действия в формате `ГГГГММДДЧЧММСС`, например, `20240229235959`.

Если для `period` установить значение `null`, у объекта будет включена опция **Бессрочно**.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Время.

</details>

<details>

<summary>Создание объекта Список IP-объектов</summary>

```
POST /aliases/lists/addresses
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string", 
    "values": [ "string" ]
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - идентификаторы IP-объектов, через запятую.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Список IP-объектов.

</details>

<details>

<summary>Создание объекта Список IP-адресов</summary>

```
POST /aliases/ip_address_lists
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ] 
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - список IP-адресов без указания маски, либо с указанием маски подсети в виде десятичного числа 0...32 или четырех десятичных чисел от 0 до 255. Например: `192.168.0.0`, `192.168.0.0/24` или `192.168.0.0/255.255.255.0`.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Список IP-адресов.

</details>

<details>

<summary>Создание объекта Порты</summary>

```
POST /aliases/lists/ports
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ]
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - список портов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Порты.

</details>

<details>

<summary>Создание объекта Расписание</summary>

```
POST /aliases/lists/times
```

**Json-тело запроса:**

```json5
{
    "title": "string", 
    "comment": "string",
    "values": [ "string" ]
}
```

* `title` - название объекта. Максимальная длина - 42 символа;
* `comment` - комментарий к объекту. Может быть пустым, максимальная длина - 255 символов;
* `value` - список идентификаторов объектов Время.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Расписание.

</details>

### Изменение обьектов

<details>

<summary>Изменение объекта IP-адрес</summary>

```
PUT /aliases/ip_addresses/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "string"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - IP-адрес в формате `192.168.0.0`.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Диапазон IP-адресов</summary>

```
PUT /aliases/ip_ranges/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "start": "string",
    "end": "string"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `start` - первый IP-адрес в диапазоне, например, `192.168.100.2`;
* `end` - последний IP-адрес в диапазоне, например, `192.168.100.15`.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Подсеть</summary>

```
PUT /aliases/networks/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string", 
    "comment": "string",
    "value": "string"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - адрес подсети в формате `192.168.0.0/24` либо `192.168.0.0/255.255.255.0`.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Домен</summary>

```
PUT /aliases/domains/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "string"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - домен в формате mydomain.com.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Порт</summary>

```
PUT /aliases/ports/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "value": "integer"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - номер порта в формате `8080`.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Диапазон портов</summary>

```
PUT /aliases/port_ranges/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "start": "integer",
    "end": "integer"
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `start` - первый порт в диапазоне, например, 8080;
* `end` - последний порт в диапазоне, например, 8090.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Время</summary>

```
PUT /aliases/time_ranges/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "weekdays": [ "integer" ],
    "start": "string",
    "end": "string",
    "period": {
            "first": "integer",
            "last": "integer"
        }
}
```

* `title` - название объекта. Максимальная длина - 42 символа;
* `comment` - комментарий к объекту. Может быть пустым, максимальная длина - 255 символов;
* `weekdays` - список дней недели, где 1-пн, 2-вт ... 7-вс;
* `start` - начало временного отрезка в формате `ЧЧ:ММ`;
* `end` - конец временного отрезка в формате `ЧЧ:ММ`;
* `first` - момент начала срока действия в формате `ГГГГММДДЧЧММСС`, например, `20240215000000`;
* `last` - момент окончания срока действия в формате `ГГГГММДДЧЧММСС`, например, `20240229235959`.

Если для `period` установить значение `null`, у объекта будет включена опция **Бессрочно**.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Список IP-объектов</summary>

```
PUT /aliases/lists/addresses/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string", 
    "comment": "string",
    "values": [ "string" ]
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - идентификаторы IP-объектов, через запятую.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Список IP-адресов</summary>

```
PUT /aliases/ip_address_lists/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ]
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - список IP-адресов без указания маски, либо с указанием маски подсети в виде десятичного числа 0...32 или четырех десятичных чисел от 0 до 255. Например: `192.168.0.0`, `192.168.0.0/24` или `192.168.0.0/255.255.255.0`.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Порты</summary>

```
PUT /aliases/lists/ports/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ] 
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - список портов.

**Ответ на успешный запрос**: 200 OK

</details>

<details>

<summary>Изменение объекта Расписание</summary>

```
PUT /aliases/lists/times/<id объекта>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ]
}
```

* `title` - название объекта, максимальная длина - 42 символа;
* `comment` - комментарий к объекту, может быть пустым, максимальная длина - 255 символов;
* `value` - список идентификаторов объектов Время.

**Ответ на успешный запрос**: 200 OK

</details>

### Удаление обьектов

<details>

<summary>Удаление обьектов</summary>

```
DELETE /aliases/<название объекта>/<id объекта>
```

**Ответ на успешный запрос**: 200 OK

**Названия обьектов:**
* `ip_addresses` - IP-адрес;
* `ip_ranges` - Диапазон IP-адресов;
* `networks` - Подсеть;
* `domains` - Домен;
* `ports` - Порт;
* `port_ranges` - Диапазон портов;
* `time_ranges` - Время;
* `ip_address_lists` - Список IP-адресов.

</details>

<details>

<summary>Удаление списка обьектов</summary>

```
DELETE /aliases/lists/<название объекта>/<id объекта>
```

**Ответ на успешный запрос**: 200 OK

**Названия обьектов:**
* `addresses` - Список IP-объектов;
* `ports` - Порты;
* `times` - Расписание.

</details>

## Обнаружение устройств

<details>
<summary>Получение настроек</summary>

```
GET /netscan_backend/settings
```

**Ответ на успешный запрос:**

```json5
{
   "enabled": "boolean",
   "group_id": "integer",
   "networks": [ "string" ]
}
```

* `group_id` - идентификатор группы, в которую будут добавлены обнаруженные устройства;
* `networks` - список локальных сетей, устройства из которых будут автоматически добавлены и авторизованы на Ideco NGFW.


</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /netscan_backend/settings
```

**Json-тело запроса:**

```json5
{
   "enabled": "boolean",
   "group_id": "integer",
   "networks": [ "string" ]
}
```

* `group_id` - идентификатор группы, в которую будут добавлены обнаруженные устройства;
* `networks` - список локальных сетей, устройства из которых будут автоматически добавлены и авторизованы на Ideco NGFW.

**Ответ на успешный запрос:** 200 OK

</details>

## Распространенные статусы

* **200** OK - Операция успешно завершена;
* **302** Found - Запрашиваемая страница была найдена / временно перенесена на другой URL;
* **400** Bad Request - Сервер не смог понять запрос из-за недействительного синтаксиса;
* **401** Unauthorized - Запрещено. Сервер понял запрос, но он не выполняет его из-за ограничений прав доступа к указанному ресурсу;
* **404** Not Found - Запрашиваемая страница не найдена. Сервер понял запрос, но не нашел соответствующего ресурса по указанному URL;
* **405** Method Not Allowed - Метод не поддерживается. Запрос был сделан методом, который не поддерживается данным ресурсом;
* **502** Bad Gateway - Ошибка шлюза. Сервер, выступая в роли шлюза или прокси-сервера, получил недействительное ответное сообщение от вышестоящего сервера;
* **542** - Валидация не пропустила тело запроса.