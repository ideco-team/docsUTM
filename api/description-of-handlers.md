# Описание хендлеров

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
    "rest_path": "string"
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
<summary>Получение информации о лицензии</summary>

```
GET /license
```

**Пример ответа на успешный запрос:**

```json5
{
    "modules": {
        "active_directory": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "kaspersky_av_for_web": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "kaspersky_av_for_mail": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "application_control": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "suricata": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "advanced_content_filter": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "standard_content_filter": {
            "available": false,
            "expiration_date": 0
        },
        "ips_advanced_rules": {
            "available": true,
            "expiration_date": 1713084779.0
        },
        "icsd": {
            "available": true,
            "max_users_count": 10000
        }
    },
    "general": {
        "available": true,
        "reason": "",
        "not_upgrade_after": 1713084779.0,
        "tech_support_end": 1713084779.0,
        "start_date": 1709628779.7338443,
        "expiration_date": 1713084779.0
    },
    "license_type": "enterprise-demo",
    "license_id": "UTM-1098592203",
    "server_name": "UTM",
    "last_update_time": 1709628781.5150864,
    "company_id": "Ideco",
    "server_id": "CI-GYYWDwzjGBZ8by3drEAwdYMLIVWTa9RD-AsMGk63h",
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
<summary>Сбор анонимной статистики о работе сервера</summary>

### Получение текущих настроек:

```
GET /gather_stat
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
PUT /gather_stat
```

**Json-тело запроса**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Управление объектами

<details>

<summary>Создание объекта IP-адрес</summary>

```
POST /aliases/ip_addresses
```

**Json-тело запроса:**

```json5
{
    "comment": "string",    
    "title": "string",
    "value": "string"
}
```

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - IP-адрес.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта IP-адрес.

</details>

<details>

<summary>Создание объекта Cписок IP-адресов</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список IP-адресов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Список IP-адресов.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `start` - первый IP-адрес диапазона;
* `end` - последний IP-адрес диапазона.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Диапазон IP-адресов.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - идентификаторы IP-объектов через запятую.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Список IP-объектов.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - домен.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - номер порта.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `start` - первый порт диапазона;
* `end` - последний порт диапазона.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Диапазон портов.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список портов.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Порты.

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
    "end": "string"
}
```

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `weekdays` - список дней недели, где 1-пн, 2-вт, ... 7-вс;
* `start` - начало временного отрезка в формате `ЧЧ:ММ`;
* `end` - конец временного отрезка в формате `ЧЧ:ММ`.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Время.

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список идентификаторов объектов Время.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор объекта Расписание.

</details>

<details>

<summary>Получение идентификаторов объектов</summary>

```
GET /aliases
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
            "string" | "integer",
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
* `interface.ipsec_any` - все IPsec-интерфейсы;
* `interface.local_any` - все локальные интерфейсы;
* `interface.utm_outgoing` - исходящий трафик устройства;
* `interface.vpn_traffic` - клиентский VPN трафик;
* `group.id.` - идентификатор группы пользователей;
* `interface.id.` - идентификатор конкретного интерфейса;
* `security_group.guid.` - идентификатор группы безопасности AD;
* `user.id.` - идентификатор пользователя;
* `domain.id.` - идентификатор домена;
* `ip.id.` - идентификатор IP-адреса;
* `iplist.` - идентификатор объекта *GeoIP (Страна)*;
* `list_of_iplists.id.` - идентификатор объекта *Список стран*;
* `ip_range.id.` - идентификатор объекта *Диапазон IP-адресов*;
* `ip_address_list.id.` - идентификатор объекта *Список IP-адресов*;
* `address_list.id.` - идентификатор объекта *Список IP-объектов*;
* `port_list.id.` - идентификатор объекта *Список портов*;
* `time_list.id.` - идентификатор объекта *Расписание*;
* `subnet.id.` - идентификатор объекта *Подсеть*;
* `port_range.id.` - идентификатор объекта *Диапазон портов*;
* `port.id.` - идентификатор объекта *Порт*;
* `time_range.id.` - идентификатор объекта *Время*;
* `zero_subnet` - сеть `0.0.0.0/0`.

</details>

<details>

<summary>Редактирование объекта IP-адрес</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - IP-адрес.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Список IP-адресов</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список IP-адресов.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Диапазон IP-адресов</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `start` - первый IP-адрес диапазона;
* `end` - последний IP-адрес диапазона.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Список IP-объектов</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - идентификаторы IP-объектов через запятую.

**Ответ на успешный запрос:** 200 ОК

</details>


<details>

<summary>Редактирование объекта Подсеть</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - адрес подсети в формате `192.168.0.0/24` либо `192.168.0.0/255.255.255.0`.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Домен</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - домен.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Порт</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `value` - номер порта.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Диапазон портов</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `start` - первый порт диапазона;
* `end` - последний порт диапазона.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Порты</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список портов.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Время</summary>

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
    "period": { "first": "integer", "last": "integer" } | "null"
}
```

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `weekdays` - список дней недели, где 1-пн, 2-вт, ... 7-вс;
* `start` - начало временного отрезка в формате `ЧЧ:ММ`;
* `end` - конец временного отрезка в формате `ЧЧ:ММ`;
* `period` - срок действия. Может быть `null`, если бессрочно.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Редактирование объекта Расписание</summary>

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

* `title` - заголовок, максимальная длина - 42 символа;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `values` - список идентификаторов объектов Время.

**Ответ на успешный запрос:** 200 ОК

</details>

## Пользовательские категории Контент-фильтра

<details>

<summary>Создание пользовательской категории</summary>

```
POST /content-filter/users_categories
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

* `name` - название пользовательской категории;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор пользовательской категории.

</details>

<details>

<summary>Получение пользовательских категорий</summary>

```
GET /content-filter/users_categories
```

**Json-ответ на запрос:**

```json5
[
    {
        "id": "string",
        "name": "string",
        "comment": "string",
        "urls": [ "string" ] 
    },
    ...
]
```

* `id` - номер категории в формате `users.id.1`;
* `name` - название категории, не пустая строка;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

</details>

<details>

<summary>Редактирование пользовательских категорий</summary>

```
PUT /content-filter/users_categories/<id категории>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

* `name` - название категории, не пустая строка;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "name": "string",
    "description": "string",
    "urls": [ "string" ]
}
```

* `id` - идентификатор пользовательской категории;
* `description` - описание пользовательской категории.

</details>

## Обнаружение устройств

<details>
<summary>Получение настроек</summary>

```
GET /netscan_backend
```

**Ответ на успешный запрос:**

```json5
{
   "enabled": "boolean",
   "group_id": "integer",
   "networks": [ "string" ]
}
```

* `enabled` - статус: `true` - включен, `false` - выключен;
* `group_id` - идентификатор группы, в которую будут добавлены обнаруженные устройства;
* `networks` - список локальных сетей, устройства из которых будут автоматически добавлены и авторизованы на Ideco NGFW.

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /netscan_backend
```

**Json-тело запроса:**

```json5
{
   "enabled": "boolean",
   "group_id": "integer",
   "networks": [ "string" ]
}
```

* `enabled` - статус: `true` - включен, `false` - выключен;
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