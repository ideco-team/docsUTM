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
      "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
      "msg": [ "string" ]
  },
  {
        "msg": [ "string" ],
        "status": "active",
        "name": "auto-snat"
    }
]
```

* `msg` - список строк, поясняющих текущее состояние.

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

* `enabled` - опция раздела **Файрвол**: `true` - включена, `false` - выключена.

### Логирование правил

```
GET /firewall/settings
```

**Ответ на успешный запрос:**

```json
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": [ "accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log" ]
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT: `true` - включен, `false`- выключен;
* `log_mode` - режим логирования;
* `log_actions` - события, которые будут логироваться.

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
    "log_actions": [ "accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log" ]
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT: `true` - включен, `false`- выключен;
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

* `action` - действие:
  * `accept` - разрешить; 
  * `drop` - запретить;
  * `dnat` - производить DNAT;
  * `snat` - производить SNAT;
  * `mark_log` - логировать; 
  * `mark_not_log` - не логировать;
* `comment` - комментарий, может быть пустым;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `enabled` - статус правила: `true` - включено, `false` - выключено;
* `hip_profiles` - HIP-профили;
* `incoming_interface` - зона источника;
* `outgoing_interface` - зона назначения;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `timetable` - время действия;
* `id` - идентификатор правила.

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
    "timetable": [ "string" ]
}
```

* `action` - действие:
  * `accept` - разрешить; 
  * `drop` - запретить;
  * `dnat` - производить DNAT;
  * `snat` - производить SNAT;
  * `mark_log` - логировать; 
  * `mark_not_log` - не логировать;
* `comment` - комментарий, может быть пустым;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `enabled` - статус правила: `true` - включено, `false` - выключено;
* `hip_profiles` - HIP-профили;
* `incoming_interface` - зона источника;
* `outgoing_interface` - зона назначения;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `timetable` - время действия.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор правила.

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
    "timetable": [ "string" ]
}
```

* `action` - действие:
  * `accept` - разрешить; 
  * `drop` - запретить;
  * `dnat` - производить DNAT;
  * `snat` - производить SNAT;
  * `mark_log` - логировать; 
  * `mark_not_log` - не логировать;
* `comment` - комментарий, может быть пустым;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `enabled` - статус правила: `true` - включено, `false` - выключено;
* `hip_profiles` - HIP-профили;
* `incoming_interface` - зона источника;
* `outgoing_interface` - зона назначения;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `timetable` - время действия.

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
<summary>Проверка включенности счетчика срабатываний правил</summary>

```
GET /firewall/watch
```

**Ответ на успешный запрос:**

```json5
{
   "enabled": "boolean"
}
```

* `enabled` - если `true`, то счетчик включен, если `false` - выключен.

</details>

<details>
<summary>Включение/выключение счетчика срабатывания правил</summary>

```
PUT /firewall/watch
```

**Json-тело запроса:**

```json5
{
   "enabled": "boolean"
}
```

* `enabled` - `true` для включения, `false` для выключения.

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
      "packets": "integer"
   },
   ...
]
```

* `id` - идентификатор правила;
* `packets` - количество сработок правила.

</details>

## Контроль приложений

<details>
<summary>Получение списка правил</summary>

```
GET /application_control_backend/rules
```

**Ответ на успешный запрос:**

```json5
[ 
    {
        "action": "drop" | "accept",
        "aliases": [ "string" ],
        "comment": "string",
        "enabled": "boolean",
        "name": "string",
        "parent_id": "string",
        "protocols": [ "string" ],
        "id": "integer"
    },
    ...
 ]
```

* `action` - действие, применяемое к правилу;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md#poluchenie-identifikatorov-obektov));
* `comment` - комментарий правила;
* `enabled` - статус правила: `true` - включено, `false` - выключено;
* `name` - имя правила;
* `parent_id` - идентификатор родительской группы серверов;
* `protocols` - список протоколов;
* `id` - идентификатор правила.

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
    "action": "drop" | "accept",
    "comment": "string",
    "aliases": [ "string" ],
    "protocols": [ "string" ],
    "enabled": "boolean"
}
```

* `parent_id` - идентификатор родительской группы серверов;
* `name` - имя правила;
* `action` - действие, применяемое к правилу;
* `comment` - комментарий правила;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md#poluchenie-identifikatorov-obektov));
* `protocols` - список протоколов;
* `enabled` - статус правила: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор созданного правила.

</details>

<details>
<summary>Изменение правила</summary>

```
PUT /application_control_backend/rules/<id правила>
```

**Json-тело запроса:**

```json5
{
    "parent_id": "string",
    "name": "string",
    "comment": "string",
    "aliases": [ "string" ],
    "protocols": [ "string" ],
    "action": "drop" | "accept",
    "enabled": "boolean"
}
```

* `parent_id` - идентификатор родительской группы серверов;
* `name` - имя правила;
* `comment` - комментарий правила;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md#poluchenie-identifikatorov-obektov));
* `protocols` - список протоколов;
* `action` - действие, применяемое к правилу;
* `enabled` - статус правила: `true` - включено, `false` - выключено.

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

* `id` - идентификатор правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false`, то на месте указанного в `anchor_item_id`.

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /application_control_backend/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Предотвращение вторжений

<details>
<summary>Получение статуса модуля</summary>

```
GET /ips/status
```

**Ответ на успешный запрос:**

```json5
[
    {
        "name": "string",
        "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
        "msg": [ "string" ]
    },
  ...
]
```

* `name` - название домена;
* `status` - статус;
* `msg` - cписок сообщений, объясняющий текущее состояние.

</details>

<details>
<summary>Статус обновления баз правил Suricata и GeoIP</summary>

```
GET /ips/update
```

**Ответ на успешный запрос:**

```json5
{
    "status": "up_to_date" | "updating" | "failed_to_update" | "disabled"],
    "msg": "i18n_str",
    "last_update": "float" | "null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваем новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Получение статуса обновления расширенных баз правил Suricata и GeoIP</summary>

```
GET /ips/update_advanced
```

**Ответ на успешный запрос:**

```json5
{
    "status": "up_to_date" | "updating" | "failed_to_update" | "disabled",
    "msg": "i18n_str",
    "last_update": "float" | "null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваем новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Запуск принудительного обновления баз</summary>

```
POST /ips/update
```

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

* `enabled` - `true`, если модуль включен, `false` - выключен.

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

* `enabled` - `true` если модуль включен, `false` - выключен.

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
  },
  ...
]
```

* `id` - идентификатор подсети;
* `address` - адрес подсети (например, `192.168.0.0`).

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

* `address` - адрес подсети (например,`192.168.0.0`).

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор подсети.

</details>

<details>
<summary>Удаление локальной подсети</summary>

```
DELETE /ips/nets/<id подсети>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка наборов правил</summary>

```
GET /ips/rules
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "enabled": "boolean"
  },
  ...
]
```

* `id` - идентификатор набора правил;
* `name` - название набора правил;
* `enabled` - состояние набора правил: `true` - включен, `false` - выключен.

</details>

<details>
<summary>Включение/выключение набора правил</summary>

```
PATCH /ips/rules/<id набора правил>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` для включения набора правил, `false` для выключения.

**Ответ на успешный запрос:** 200 OK

</details>


<details>
<summary>Получение содержимого правила по sid</summary>

```
GET /ips/rules/sid/<sid правила>
```

**Ответ на успешный запрос:**

```json5
{
    "rule": "string"
}
```

* `rule` - текст правила. Если правило не найдено, то пустая строка.

</details>

<details>
<summary>Получение списка исключений</summary>

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
  },
  ...
]
```

* `sid` - идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `id` - идентификатор правила.

</details>

<details>
<summary>Добавление исключения</summary>

```
POST /ips/disabled_rules
```

**Json-тело запроса:**

```json5
{
    "sid": "integer",
    "comment": "string"
}
```

* `sid` - идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string" 
}
```

* `id` - идентификатор исключения.

</details>

<details>
<summary>Редактирование описания существующего исключения</summary>

```
PATCH /ips/disabled_rules/<id правила (не sid)>
```

**Json-тело запроса:**

```json5
{
    "sid": "integer",
    "comment": "string"
}
```

* `sid` - идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление существующего исключения</summary>

```
DELETE /ips/disabled_rules/<id исключения>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка исключений объектов</summary>

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
    },
    ...
]
```

* `id` - идентификатор исключения;
* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.

</details>

<details>
<summary>Добавление исключения объектов</summary>

```
POST /ips/bypass
```

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного исключения.

</details>

<details>

<summary>Изменение исключения объектов</summary>

```
PATCH /ips/bypass/<id исключения>
```

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.


**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление существующего исключения объектов</summary>

```
DELETE /ips/bypass/<id исключения>
```

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

* `enabled` - состояние **Контент-фильтра**: `true` - включен, `false` - выключен.

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

* `enabled` - `true` для включения **Контент-фильтра**, `false` для выключения.

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

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS): `true` - включена, `false` - выключена;
* `quic_reject_enabled` - запрет трафика по протоколу QUIC: `true` - включен, `false` - выключен.

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
    "quic_reject_enabled": "boolean"
}
```

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS): `true` - включена, `false` - выключена;
* `quic_reject_enabled` - запрет трафика по протоколу QUIC: `true` - включен, `false` - выключен.

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

* `enabled` - состояние безопасного поиска: `true` - включен, `false` - выключен.

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

* `enabled` - `true` для включения, `false` для выключения.

**Ответ на успешный запрос:** 200 OK

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

* `id` - номер категории в формате `users.id.1` или `extended.id.1`;
* `type` - тип категории:
  * `users` - пользовательские категории;
  * `extended` - расширенные категории (SkyDNS);
  * `files` - категории для файлов;
  * `special` - специальные предопределенные категории (Прямое обращение по IP, Все категоризированные запросы, Все некатегоризированные запросы, Все запросы);
  * `other` - остальные категории.
* `name` - имя категории;
* `comment` - описание категории.

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
        "id": "string",
        "name": "string",
        "comment": "string",
        "urls": [ "string" ]
    },
    ...
]
```

* `id` - идентификатор категории в формате `users.id.1`;
* `name` - название категории, не пустая строка;
* `comment` - комментарий;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

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

* `name` - название категории, не пустая строка;
* `comment` - комментарий;
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
* `comment` - комментарий;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

* `id` - идентификатор пользовательской категории.

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
        "aliases": [ "string" ],
        "categories": [ "string" ],
        "comment": "string",
        "enabled": "boolean",
        "name": "string",
        "parent_id": "string",
        "redirect_url": "string" | "null",
        "timetable": [ "string" ],
        "id": "integer"
    },
    ...
]
```

* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `enabled` - статус правила: `true` - включено, `false` выключено;
* `name` - название правила, не пустая строка;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `redirect_url` - адрес, на который перенаправляются запросы: `string` при `access` = `redirect`, `null` при остальных вариантах `access`;
* `timetable` - время действия, список идентификаторов алиасов;
* `id` - идентификатор правила.

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
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | "null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы: `string` при `access` = `redirect`, `null` при остальных вариантах `access`;
* `enabled` - `true` для включения, `false` для выключения;
* `timetable` - время действия, список идентификаторов алиасов.

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
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | "null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы: `string` при `access` = `redirect`, `null` при остальных вариантах `access`;
* `enabled` - `true` для включения, `false` для выключения;
* `timetable` - время действия, список идентификаторов алиасов.

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
<summary>Проверить включенность подсчета квот</summary>

```
GET /quotas/state
```

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - если `true`, то подсчет квот включен, если `false` - выключен.

</details>

<details>
<summary>Включение/выключение подсчета квот</summary>

```
PUT /quotas/state
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - `true` для включения, `false` для выключения.

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
    "enabled": "boolean",
    "interval": "hour" | "day" | "week" | "month" | "quarter"
  },
  ...
]
```

* `id` - идентификатор квоты;
* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
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

* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор квоты.

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

* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

**Ответ на успешный запрос:** 200 ОК

</details>