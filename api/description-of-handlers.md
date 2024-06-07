# Описание основных хендлеров

<details>

<summary>Авторизация</summary>

```
POST /web/auth/login
```

**Json-тело запроса:**

```
{
    "login": "string",    
    "password": "string",    
    "rest_path": "string" (по умолчанию строка со слэшем "/")
}

```

После успешной авторизации, сервер Ideco NGFW передает в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=02428c1c-fcd5-42ef-a533-5353da743806
set-cookie: __Secure-ideco-3ea57fca-65cb-439b-b764-d7337530f102=df164532-b916-4cda-a19b-9422c2897663:1663839003
```

Эти куки нужно передавать при каждом запросе после авторизации в заголовке запроса Cookie.

</details>

<details>

<summary>Разавторизация</summary>

```
DELETE /web/auth/login
```
После успешной разавторизации сервер Ideco NGFW передает в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
set-cookie: __Secure-ideco-b7e3fb6f-7189-4f87-a4aa-1bdc02e18b34=""; HttpOnly; Max-Age=0; Path=/; SameSite=Strict; Secure
```

</details>

<details>
<summary>Сбор анонимной статистики о работе сервера</summary>

### Получение текущих настроек:

```
GET /gather_stat/settings
```

**Ответ на успешный запрос:**

```
{
      "enabled": boolean
   }
```

Значение `"enabled"` равно `true`, если сбор анонимной статистики о работе сервера включен, и `false`, если выключен.

### Изменение настроек

```
PUT /gather_stat/settings
```

**Json-тело запроса**

```
{
      "enabled": boolean
   }
```

Ответ на такой запрос будет пустым.

</details>

## Лицензирование

<details>
<summary>Регистрация сервера</summary>

```
POST /license/register
```

**Json-тело запроса:**

```
{
    "token": "str" (Получить токен лицензии можно в отделе продаж. Он высылается в активационном письме)
}
```

Ответ: 200 ОК

Чтобы добавить enterprise-demo лицензию, необходимо сначала получить токен лицензии в личном кабинете. Для этого выполните действия:

1\. Авторизуйтесь в личном кабинете myideco.ru:

```
POST /api/v3/login
```

**Json-тело запроса:**

```
{
    "login": "string",
    "password": "string",
    "g_recaptcha_response": "string" | null
}
```

2\. Выполните запрос на регистрацию сервера:

```
PUT /api/v3/{company_id}/go_to_product
```

*  `company_id` - id компании пользователя. Его можно получить по запросу `GET /api/v3/companies`.

**Тело ответа на успешный запрос:**

```
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

```
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

```
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

```
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

```
{
  "update_type": "auto" | "manual"
}
```

**Ответ на успешный запрос**: 200 ОК

</details>

<details>
<summary>Получение ссылки для оффлайн-регистрации</summary>

```
GET /license/license-get-offline-registration-url
```

**Ответ на успешный запрос**

```
{
    "registration_url": "https://my.ideco.ru/offline_register?server_name=ZGF0YSB0byBiZSBlbmNvZGVk&hwid=u-CVv6SSNMXI_Mukgnf3SCIxJz9kcl0i50ARFk4FRz1O&version=17.1"
}
```

* `server_name` - имя сервера Ideco NGFW;
* `hwid` - HWID сервера;
* `version` - версия сервера.

Получение ссылки для оффлайн-регистрации сервера возможно только при ручном механизме обновления лицензии.

</details>

<details>
<summary>Загрузка файла с лицензией на NGFW</summary>

```
POST /license/license-upload
```

Тело запроса: форма загрузки файла. Имя поля в форме загрузки файла - `license_file`

**Ответ на успешный запрос**: 200 ОК

</details>

## Управление объектами

<details>

<summary>Создание объекта IP-адрес</summary>

```
POST /aliases/ip_addresses
```

**Json-тело запроса:**

```
{
    "comment": "string",    
    "title": "string",    
    "value": "string"
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Диапазон IP-адресов</summary>

```
POST /aliases/ip_ranges
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "start": "string",
    "end": "string"
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Подсеть</summary>

```
POST /aliases/networks
```

**Json-тело запроса:**

```
{
    "title": "string" (максимальная длина 42 символа),
    "comment": "string" (может быть пустым, максимальная длина 256 символов),
    "value": "string" (адрес подсети в формате `192.168.0.0/24` либо `192.168.0.0/255.255.255.0`)
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Домен</summary>

```
POST /aliases/domains
```

**Json-тело запроса:**

```
{
    "title": "string" (максимальная длина 42 символа),
    "comment": "string" (может быть пустым, максимальная длина 256 символов),
    "value": "string" (домен)
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Порт</summary>

```
POST /aliases/ports
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "value": integer (номер порта)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Диапазон портов</summary>

```
POST /aliases/port_ranges
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "start": integer (первый порт диапазона),
    "end": integer (последний порт диапазона)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Время</summary>

```
POST /aliases/time_ranges
```

**Json-тело запроса:**

```
{
    "title":"string",
    "comment":"string",
    "weekdays":[integer] (список дней недели, где 1-пн, 2-вт ... 7-вс),
    "start":"string" (начало временного отрезка в формате: ЧЧ:ММ),
    "end":"string"(конец временного отрезка в формате: ЧЧ:ММ),
    "period": {
            "first": integer (момент начала срока действия в формате ГГГГММДДЧЧММСС, например, 20240215000000),
            "last": integer (момент окончания срока действия в формате ГГГГММДДЧЧММСС, например, 20240229235959)
        }
}
```

Если для `"period"` установить значение `null`, у объекта будет включена опция **Бессрочно**.

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Список IP-объектов</summary>

```
POST /aliases/lists/addresses
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "values": ["string"] (идентификаторы IP-объектов, через запятую)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Список IP-адресов</summary>

```
POST /aliases/ip_address_lists
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ] (Список IP-адресов без указания маски, либо с указанием маски подсети в виде десятичного числа 0...32 или четырех десятичных чисел от 0 до 255. Например: `192.168.0.0/24` или `192.168.0.1`)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Порты</summary>

```
POST /aliases/lists/ports
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ] (список портов)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Создание объекта Расписание</summary>

```
POST /aliases/lists/times
```

**Json-тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "values": [ "string" ] (список id объектов Время)
}
```

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Получение ID объектов</summary>

```
GET /aliases/all
```

**Ответ на успешный запрос:**

```
[
    {
        comment: "string",
        title: "string",
        type: "string",
        values: [
            "string" | integer,
            "string" | integer
        ],
        id: "type.id.1"
    }, 
{
        comment: "string",
        title: "string",
        type: "string",
        value: "string" | integer,
        id: "type.id.1"
    },
    ...
] 
```

В качестве ответа будет возвращен список всех объектов, существующих в NGFW:

* "protocol.ah" - протокол AH;
* "protocol.esp" - протокол ESP;
* "protocol.gre" - протокол GRE;
* "protocol.icmp" - протокол ICMP;
* "protocol.tcp" - протокол TCP;
* "protocol.udp" - протокол UDP;
* "quota.exceeded"- IP-адреса пользователей, которые превысили квоту;
* "any" - допускается любое значение в этом поле;
* "interface.external_any" - все внешние интерфейсы (равно таблице *Подключение к провайдеру* в веб-интерфейсе и включает в себя подключения к провайдеру по Ethernet/VPN);
* "interface.external_eth" - внешние Ethernet-интерфейсы;
* "interface.external_vpn" - внешние VPN-интерфейсы;
* "interface.ipsec_any" - IPsec-интерфейсы;
* "interface.local_any" - все локальные интерфейсы;
* "interface.tunnel_any" - все туннельные интерфейсы;
* "group.id." - идентификатор группы пользователей;
* "interface.id." - идентификатор конкретного интерфейса;
* "interface.utm_outgoing" - исходящий трафик устройства;
* "interface.vpn_traffic" - клиентский VPN-трафик;
* "interface.wccp_gre_any" - все WCCP GRE интерфейсы;
* "hip_profile.id." - устройства без профиля;
* "security_group.guid." - идентификатор группы безопасности AD;
* "user.id." - идентификатор пользователя;
* "domain.id." - идентификатор домена;
* "ip.id." - идентификатор IP-адреса;
* "ip_range.id." - идентификатор объекта *Диапазон адресов*;
* "address_list.id." - идентификатор объекта *Список IP-объектов*;
* "list_of_iplists.id." - идентификатор объекта *Список стран*;
* "port_list.id." - идентификатор объекта *Порты*;
* "time_list.id." - идентификатор объекта *Расписание*;
* "subnet.id." - идентификатор объекта *Подсеть*;
* "port_range.id." - идентификатор объекта *Диапазон портов*;
* "port.id." - идентификатор объекта *Порт*;
* "time_range.id." - идентификатор объекта *Время*.

</details>

## Обнаружение устройств

<details>
<summary>Получение настроек</summary>

```
GET /netscan_backend/settings
```

**Ответ на успешный запрос:**

```
{
   "enabled": boolean,
   "group_id": integer (идентификатор группы, в которую будут добавлены обнаруженные устройства),
   "networks": ["string"] (список локальных сетей, устройства из которых будут автоматически добавлены и авторизованы на Ideco NGFW)
}
```

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /netscan_backend/settings
```

**Json-тело запроса:**

```
{
   "enabled": boolean,
   "group_id": integer,
   "networks": ["string"]
}
```

**Ответ на успешный запрос**: 200 OK.

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