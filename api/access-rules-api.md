# Управление правилами трафика

{% hint style="info" %}
API правил трафика Ideco Center описано в статье [Центральная консоль](/api/cc-api.md).
{% endhint %}

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

## Файрвол

<details>
<summary>Получение статуса службы</summary>

```
GET /firewall/status
```

**Ответ на успешный запрос:**

```json
[
  {
      "name": "rules-in-kernel",
      "status": "active|activating|deactivating|failed|inactive|reloading",
      "msg": [ "string" ]  //(Список строк, поясняющих текущее состояние)
  },
  {
        "msg": [ "string" ],
        "status": "active",
        "name": "auto-snat"
    }
]
```

</details>

<details>
<summary>Получение настроек Файрвола</summary>

## Включенность пользовательских правил

```
GET /firewall/state
```

**Ответ на успешный запрос:**

```json
{
    "enabled": "boolean"
} 
```

* `enabled` - Опция раздела Файрвол включен (true) или
отключен (false).

### Логирование правил

```
GET /firewall/settings
```

**Ответ на успешный запрос:**

```json
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": ["accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log"],
} 
```

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /firewall/settings
```

**Json-тело запроса:**

```json
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": ["accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log"],
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT;
* `log_mode` - режим логирования;
* `log_actions` - события, которые будут логироваться. 

**Ответ на успешный запрос**: 200 ОК

</details>

### Управление правилами

<details>
<summary>Получение списка правил</summary>

* `GET /firewall/rules/forward` - раздел FORWARD;
* `GET /firewall/rules/input` - раздел INPUT;
* `GET /firewall/rules/dnat` - раздел DNAT;
* `GET /firewall/rules/snat` - раздел SNAT;
* `GET /firewall/rules/log` - раздел Логирование.

**Ответ на успешный запрос:**

```json5
[
    {
        "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
        "comment": "string",
        "destination_addresses": [ "string" ], 
        "destination_addresses_negate": "boolean",
        "destination_ports": [ "string" ],
        "enabled": "boolean",
        "hip_profiles": [ "string" ],
        "incoming_interface": "string",
        "outgoing_interface": "string",
        "parent_id": "string",
        "protocol": "string",
        "source_addresses": [ "string" ],
        "source_addresses_negate": "boolean",
        "timetable": [ "string" ],
        "id": "integer"
    },
    ...
]
```

* `"action"` - действие:
  * `"accept"` - разрешить; 
  * `"drop"` - запретить;
  * `"dnat"` - производить DNAT;
  * `"snat"` - производить SNAT;
  * `"mark_log"` - логировать; 
  * `"mark_not_log"` - не логировать;
* `"comment"` - комментарий (может быть пустым);
* `"destination_addresses"` - адрес назначения;
* `"destination_addresses_negate"` - инвертировать адрес назначения;
* `"destination_ports"` - порты назначения;
* `"enabled"` - включено (true) или выключено (false) правило;
* `"hip_profiles"` - HIP-профили;
* `"incoming_interface"` - зона источника;
* `"outgoing_interface"` - зона назначения;
* `"parent_id"` - идентификатор группы в Ideco Center, в которую входит сервер, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `"protocol"` - протокол;
* `"source_addresses"` - адрес источника;
* `"source_addresses_negate"` - инвертировать адрес источника;
* `"timetable"` - время действия;
* `"id"` - идентификатор правила.

</details>

<details>
<summary>Добавление правила</summary>

* `POST /firewall/rules/forward?anchor_item_id=123&insert_after={true|false}` - раздел FORWARD;
* `POST /firewall/rules/input?anchor_item_id=123&insert_after={true|false}` - раздел INPUT;
* `POST /firewall/rules/dnat?anchor_item_id=123&insert_after={true|false}` - раздел DNAT;
* `POST /firewall/rules/snat?anchor_item_id=123&insert_after={true|false}` - раздел SNAT;
* `POST /firewall/rules/log?anchor_item_id=123&insert_after={true|false}` - раздел Логирование.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
  * `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
    "comment": "",
    "destination_addresses": [ "string" ],
    "destination_addresses_negate": "boolean",
    "destination_ports": [ "string" ],
    "enabled": "boolean",
    "hip_profiles": [ "string" ],
    "incoming_interface": "string",
    "outgoing_interface": "string",
    "parent_id": "string",
    "protocol": "string",
    "source_addresses": [ "string" ],
    "source_addresses_negate": "boolean",
    "timetable": [ "string" ]
    }
```

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>
<summary>Редактирование правила</summary>

* `PUT /firewall/rules/forward/<id правила>` - раздел FORWARD;
* `PUT /firewall/rules/input/<id правила>` - раздел INPUT;`
* `PUT /firewall/rules/dnat/<id правила>` - раздел DNAT;
* `PUT /firewall/rules/snat/<id правила>` - раздел SNAT;
* `PUT /firewall/rules/log/<id правила>` - раздел Логирование.

**Json-тело запроса:**

```json5
{
    "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
    "comment": "",
    "destination_addresses": [ "string" ],
    "destination_addresses_negate": "boolean",
    "destination_ports": [ "string" ],
    "enabled": "boolean",
    "hip_profiles": [ "string" ],
    "incoming_interface": "string",
    "outgoing_interface": "string",
    "parent_id": "string",
    "protocol": "string",
    "source_addresses": [ "string" ],
    "source_addresses_negate": "boolean",
    "timetable": [ "string" ]
    }
```

**Ответ на успешный запрос**: 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

* `PATCH /firewall/rules/forward/move` - раздел FORWARD;
* `PATCH /firewall/rules/input/move` - раздел INPUT;
* `PATCH /firewall/rules/dnat/move` - раздел DNAT;
* `PATCH /firewall/rules/snat/move` - раздел SNAT;
* `PATCH /firewall/rules/log/move` - раздел Логирование.

**Json-тело запроса:**

```json5
{
  "params": {
    "id": "integer",
    "anchor_item_id": "integer",
    "insert_after": "boolean"
  }
}
```

* `id` - идентификатор перемещаемого правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно поместить перемещаемое правило;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

</details>

<details>
<summary>Удаление правила</summary>

* `DELETE /firewall/rules/forward/<id правила>` - раздел FORWARD;
* `DELETE /firewall/rules/input/<id правила>` - раздел INPUT;
* `DELETE /firewall/rules/dnat/<id правила>` - раздел DNAT;
* `DELETE /firewall/rules/snat/<id правила>` - раздел SNAT;
* `DELETE /firewall/rules/log/<id правила>` - раздел Логирование.

**Ответ на успешный запрос:** 200 ОК

</details>

### Счетчик срабатывания правил

<details>
<summary>Узнать, включен ли счетчик срабатываний правил</summary>

```
GET /firewall/watch
```

**Ответ на успешный запрос:**

```json5
{
   "enabled": "boolean" //(true - если счетчик включен, false - если выключен)
}
```

</details>

<details>
<summary>Включение/выключение счетчика срабатывания правил</summary>

```
PUT /firewall/watch
```

**Json-тело запроса:**

```json5
{
   "enabled": "boolean" //(true - чтобы включить, false - чтобы выключить)
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение счетчиков по правилам</summary>

* `GET /firewall/counters/forward` - раздел FORWARD;
* `GET /firewall/counters/input` - раздел INPUT;
* `GET /firewall/counters/dnat` - раздел DNAT;
* `GET /firewall/counters/snat` - раздел SNAT;
* `GET /firewall/rules/log` - раздел Логирование.

**Ответ на успешный запрос:**

```json5
[
   {
      "id": "integer",
      "packets": "integer" //(количество сработок правила)
   },
   ...
]
```

</details>

## Контроль приложений

<details>
<summary>Получение списка всех правил</summary>

```
GET /application_control_backend/rules
```

**Ответ на успешный запрос:**

```json5
[
{
        "action": "string", // ["drop"|"accept"]
        "aliases": ["string"],
        "comment": "string",
        "enabled": "boolean",
        "name": "string",
        "parent_id": "string",
        "protocols": ["string"],
        "id": "integer"
}
]
```

* `action` - действие, применяемое к правилу;
* `aliases` - алиасы, которые используются в правиле (например, any);
* `comment` - комментарий правила;
* `enabled` - статус правила (true - включено, false - отключено);
* `name` - имя правила;
* `parent_id` - идентификатор родительской группы серверов;
* `protocols` - список протоколов;
* `id` - уникальный номер правила.

</details>

<details>
<summary>Создание нового правила</summary>

```
POST /application_control_backend/rules
```

**Json-тело запроса:**

```json5
{
"parent_id": "string",
"name": "string",
"action": "string", // ["drop"|"accept"],
"comment": "string",
"aliases":["string"],
"protocols":["string"],
"enabled": "boolean"
}
```

* `action` - действие, применяемое к правилу;
* `aliases` - алиасы, которые используются в правиле (например, any);
* `comment` - комментарий правила;
* `enabled` - статус правила (true - включено, false - отключено);
* `name` - имя правила;
* `parent_id` - идентификатор родительской группы серверов;
* `protocols` - список протоколов;

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - уникальный номер созданного правила.

</details>

<details>
<summary>Изменение правила</summary>

```
PUT /application_control_backend/rules/{id}
```

* `id` - уникальный номер правила;

**Json-тело запроса:**

```json5
{
    "parent_id": "str",
    "name": "str",
    "comment": "str",
    "aliases": ["str"],
    "protocols": ["str"],
    "action": "string", // ["drop"|"accept"],
    "enabled": "boolean",
}
```

* `action` - действие, применяемое к правилу;
* `aliases` - алиасы, которые используются в правиле (например, any);
* `comment` - комментарий правила;
* `enabled` - статус правила (true - включено, false - отключено);
* `name` - имя правила;
* `parent_id` - идентификатор родительской группы серверов;
* `protocols` - список протоколов;

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Изменение приоритета правила</summary>

```
PATCH /application_control_backend/rules/move
```

**Json-тело запроса:**

```json5
{
  "params": {
    "id": "integer",
    "anchor_item_id": "integer",
    "insert_after": "boolean",
  },
}
```

* `id` - уникальный идентификатор правила;
* `anchor_item_id` - уникальный идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если True, то вставить правило сразу после указанного в anchor_item_id, если False, то на месте указанного в anchor_item_id.

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /application_control_backend/rules/{id}
```

* `id` - уникальный номер правила, которое нужно удалить.

**Ответ на успешный запрос:** 200 OK

</details>

## Предотвращение вторжений

<details>
<summary>Получение статуса модуля</summary>

```
`GET /ips/status`
```

**Ответ на успешный запрос:**

```json5
[
    {
        "name": "string",
        "status": "string", // ["active"|"activating"|"deactivating"|"failed"|"inactive"|"reloading"],
        "msg": ["str"]
    }
]
```

* `name` - название демона;
* `status` - статус;
* `msg` - cписок сообщений, объясняющий текущее состояние.

</details>

<details>
<summary>Статус обновления баз правил сурикаты и GeoIP</summary>

```
GET /ips/update
```

**Ответ на успешный запрос:**

```json5
{
    "status": "string", // ["up_to_date|updating|failed_to_update|disabled"]
    "msg": "i18n_str",
    "last_update": "float|null"
}
```

* `status` - текущий статус обновления баз:
  - `up_to_date` - базы успешно обновлены;
  - `updating` - скачиваем новые базы;
  - `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  - `disabled` - обновление баз выключено.

* `msg` - текстовое описание статуса обновления баз, переведённое на бэкенде;
* `last_update` - время (таймстамп) последнего успешного обновления баз.

</details>

<details>
<summary>Статус обновления расширенных баз  правил сурикаты и GeoIP</summary>

```
GET /ips/update_advanced
```

**Ответ на успешный запрос:**

```json5
{
    "status": "string", //["up_to_date"|"updating"|"failed_to_update"|"disabled"],
    "msg": "i18n_str",
    "last_update": "float|null"
}
```

* `status` - текущий статус обновления баз:
  - `up_to_date` - базы успешно обновлены;
  - `updating` - скачиваем новые базы;
  - `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  - `disabled` - обновление баз выключено.

* `msg` - текстовое описание статуса обновления баз, переведённое на бэкенде;
* `last_update` - время (таймстамп) последнего успешного обновления баз.

</details>

<details>
<summary>Запуск принудительного обновления баз</summary>

```
POST /ips/update
```

**Тело запроса пустое.**

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение текущей настройки включенности модуля</summary>

```
GET /ips/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` если модуль включен, `false` - если выключен

</details>


<details>
<summary>Изменение настройки включенности модуля</summary>

```
PUT /ips/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` если модуль включен, `false` - если выключен

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка локальных подсетей</summary>

```
GET /ips/nets
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "address": "string"
  }
]
```

* `id` - уникальный идентификатор подсети;
* `address` - подсеть (например "192.168.0.0/16").

</details>

<details>
<summary>Добавление новой локальной подсети</summary>

```
POST /ips/nets
```

**Json-тело запроса:**

```json5
{
    "address": "string"
}
```

* `address` - подсеть (например "192.168.0.0/16").

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "address": "string"
}
```

* `id` - уникальный идентификатор подсети;
* `address` - подсеть (например "192.168.0.0/16").

</details>

<details>
<summary>Удаление локальной подсети</summary>

```
DELETE /ips/nets/{id}
```

`id` - уникальный идентификатор подсети

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка наборов правил</summary>

```
GET /ips/rules
```

```json5
[
  {
    "id": "string",
    "name": "string",
    "enabled": "bool"
  },
  ...
]
```

* `id` - уникальный идентификатор набора правил;
* `name` - название (имя файла) набора правил;
* `enabled` - состояние набора правил: включен/выключен.

</details>

<details>
<summary>Включение/выключение набора правил</summary>

```
PATCH /ips/rules/{id}
```

`id` - уникальный идентификатор набора правил

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>


<details>
<summary>Получение содержимого правила по sid</summary>

```
GET /ips/rules/sid/{id}
```

`id` - sid правила

**Ответ на успешный запрос:**

```json5
{
    "rule": "string"
}
```

* `rule` - текст правила. Если правило не найдено - пустая строка.

</details>

<details>
<summary>Получение списка всех исключений</summary>

```
GET /ips/disabled_rules
```

**Ответ на успешный запрос:**

```json5
[
    {
    "sid": "integer",
    "comment": "string",
    "id": "string"
    }
]
```

* `sid` - уникальный идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина 256;
* `id` - уникальный идентификатор правила на NGFW.

</details>

<details>
<summary>Добавление исключения</summary>

```
POST /ips/disabled_rules
```

**Json-тело запроса:**

```json5
{
    "sid": "int",
    "comment": "string"
}
```

* `sid` - уникальный идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина 256;

**Ответ на успешный запрос:**

```json5
{
  "id": "string" 
}
```

</details>

<details>
<summary>Редактирование описания существующего исключения</summary>

```
PATCH /ips/disabled_rules/{id}
```

* `id` - уникальный идентификатор правила (не sid).

**Json-тело запроса:**

```json5
{
    "sid": "int",
    "comment": "string"
}
```

* `sid` - уникальный идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина 256;

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление существующего исключения</summary>

```
DELETE /ips/disabled_rules/{id}
```

* `id` - уникальный идентификатор правила (не sid).

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка исключений алиасов</summary>

```
GET /ips/bypass
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "aliases": [ "string" ],
        "comment": "string",
        "enabled": "boolean",
    }
]
```

* `id` - id исключения;
* `aliases` - список id алиасов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина 256;
* `enabled` - состояние исключения: включено/выключено.

</details>

<details>
<summary>Добавление исключения алиасов</summary>

```
POST /ips/bypass
```

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "bool",
}
```

* `aliases` - список id алиасов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина 256;
* `enabled` - состояние исключения: включено/выключено.

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

* `id` - уникальный идентификатор созданного исключения.

</details>

<details>

<summary>Изменение исключения алиасов</summary>

```
PATCH /ips/bypass/{id}
```

* `id` - уникальный идентификатор созданного исключения.

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "bool",
}
```

* `aliases` - список id алиасов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина 256;
* `enabled` - состояние исключения: включено/выключено.


**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление существующего исключения алиасов</summary>

```
DELETE /ips/bypass/{id}
```

* `id` - уникальный идентификатор исключения.

**Ответ на успешный запрос:** 200 OK

</details>

## Контент-фильтр

<details>
<summary>Включение/выключение Контент-фильтра</summary>

### Проверить включенность

```
GET /content-filter/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

### Включить/выключить Контент-фильтр

```
PUT /content-filter/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

### Настройки

<details>
<summary>Получение настроек</summary>

```
GET /content-filter/settings
```

**Ответ на успешный запрос:**

```json5
{
    "enabled_extended_categorizer": "boolean",
    "quic_reject_enabled": "boolean"
}
```

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS) включена (true) или выключена (false);
* `quic_reject_enabled` - запрет трафика по протоколу QUIC включен (true) или выключен (false).

</details>

<details>
<summary>Изменение настроек</summary>

```
PATCH /content-filter/settings
```

**Json-тело запроса:**

```json5
{
    "enabled_extended_categorizer": "boolean",
    "quic_reject_enabled": "boolean" //(Любое из полей может отсутствовать)
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение настройки безопасного поиска</summary>

```
GET /proxy_backend/safe_search
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

</details>

<details>
<summary>Изменение настройки безопасного поиска</summary>

```
PUT /proxy_backend/safe_search
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Офлайн-обновление Контент-фильтра</summary>

```
PUT /content-filter/update_archive_upload
```
**Тело запроса:**

Архивный файл с офлайн-обновлением для контент-фильтра, который можно скачать в личном кабинете MY.IDECO. Более подробная информация представлена в [статье](/settings/server-management/server-update.md#bazy-filtracii).

**Ответ на успешный запрос:** 200 ОК и пустое тело

</details>

### Категории Контент-фильтра

<details>
<summary>Получение списка категорий (предустановленных и пользовательских)</summary>

```
GET /content-filter/categories
```

**Json-тело ответа:**

```json5
[
    {
        "id": "string",
        "type": "string",
        "name": "string",
        "comment": "string"
    },
    ...
]
```

* `id` - номер категории в формате `users.id.1` или `extended.id.1`.
* `type` - тип категории:
  * `"users"` - пользовательские категории;
  * `"extended"` - расширенные категории (SkyDNS);
  * `"files"` - категории для файлов;
  * `"special"` - специальные предопределенные категории:
    - Прямое обращение по IP;
    - Все категоризированные запросы;
    - Все некатегоризированные запросы;
    - Все запросы (категоризированные и некатегоризированные).
  * `"other"` - остальные категории.
* `name` - имя категории (для отображения пользователю).
* `comment` - описание категории (для отображения пользователю).

</details>

<details>
<summary>Получение списка пользовательских категорий</summary>

```
GET /content-filter/users_categories
```

**Json-ответ на запрос:**

```json5
[
    {
        "id": "string" (номер категории, вида - users.id.1),
        "name": "string" (название категории, не пустая строка),
        "comment": "string",
        "urls": ["string"]
    },
    ...
]
```

* `"urls"` - список url. Либо полный путь до страницы, либо только доменное имя. В пути может присутствовать любое количество любых символов.

</details>

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

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

</details>

<details>

<summary>Редактирование пользовательских категорий</summary>

```
PUT /content-filter/users_categories/{category_id}
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": ["string"]
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

</details>

### Правила Контент-фильтра

<details>
<summary>Получение списка правил</summary>

```
GET /content-filter/rules
```

**Json-тело ответа:**

```json5
[
    {
        "access": "allow" | "deny" | "bump" | "redirect",
        "aliases": ["string"],
        "categories": ["string"],
        "comment": "string",
        "enabled": "boolean",
        "name": "string",
        "parent_id": "string",
        "redirect_url": "string" | "null",
        "timetable": ["string"],
        "id": "integer"
    },
    ...
]
```

* `id` - идентификатор правила;
* `parent_id` - id группы в Ideco Center, в которую входит Ideco NGFW, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `name` - название правила, не пустая строка;
* `comment` - комментарий (макс. 256 символов), может быть пустым;
* `aliases` - список id алиасов (поле Применяется для);
* `categories` - список id категорий сайтов;
* `access` - действие, которое необходимо выполнить в правиле, строка, может принимать три значения:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump`: расшифровать запрос;
  * `redirect`: перенаправить запрос на `redirect_url`;
* `redirect_url` - URL, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled`: правило включено (true) или выключено (false);
* `timetable` - время действия, список ID алиасов.

</details>

<details>
<summary>Создание правила</summary>

```
POST /content-filter/rules?anchor_item_id=123&insert_after={true|false}
```

* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
* `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "parent_id": "string", 
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow|deny|bump|redirect",
    "redirect_url": "string|null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

</details>

<details>
<summary>Редактирование правила</summary>

```
PUT /content-filter/rules/<id правила>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "parent_id": "string", 
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow|deny|bump|redirect",
    "redirect_url": "string|null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

```
PATCH /content-filter/rules/move
```

**Json-тело запроса:**

```json5
{
  "params": {
    "id": "integer",
    "anchor_item_id": "integer",
    "insert_after": "boolean"
  }
}
```

* `id` - идентификатор правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно вставить правило, которое перемещаем;
* `insert_after` - вставка до или после. Если `true`, то правило будет вставлено сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /content-filter/rules/<id правила>
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Квоты

<details>
<summary>Проверить, включен ли подсчет квот</summary>

```
GET /quotas/state
```

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

</details>

<details>
<summary>Включить/выключить подсчет квот</summary>

```
PUT /quotas/state
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение списка квот</summary>

```
GET /quotas/quotas
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string",
    "comment": "string",
    "quota": "integer",
    "enabled": "bool",
    "interval": "hour" | "day" | "week" | "month" | "quarter"
  },
  ...
]
```

* `id` - идентификатор квоты;
* `title` - название квоты (максимальная длина 42 символа);
* `comment` - комментарий (максимальная длина 256 символов)%
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

</details>

<details>
<summary>Создание квоты</summary>

```
POST /quotas/quotas
```

**Json-тело запроса:**

```json5
{
  "title": "string",
  "comment": "string",
  "quota": "integer",
  "enabled": "boolean",
  "interval": "string"
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

</details>

<details>
<summary>Редактирование квоты</summary>

```
PATCH /quotas/quotas/<id квоты>
```

**Json-тело запроса (все или некоторые поля):**

```json5
{
  "title": "string",
  "comment": "string",
  "quota": "integer",
  "enabled": "boolean",
  "interval": "string"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

**Ответ на успешный запрос:** 200 ОК

</details>