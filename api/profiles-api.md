# Управление профилями безопасности

## Предотвращение вторжений

<details>
<summary>Получение списка профилей</summary>

```
GET /ips/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string"
  },
  ...
]
```
* `id` - идентификатор профиля;
* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

</details>

<details>
<summary>Создание профиля</summary>

```
POST /ips/profiles
```
**Json-тело запроса:**:

```json5
{
    "name": "string",
    "comment": "string"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:**

```json5
{
  "id": "string"
}
```

* `id` - идентификатор профиля.

</details>

<details>
<summary>Изменение профиля</summary>

```
PATCH /ips/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 200 ОК

</details>

</details>

<details>
<summary>Удаление профиля</summary>

```
DELETE /ips/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение списка правил профиля</summary>

```
GET /ips/profile_rules?profile_id=<string>
```

* `profile_id` - идентификатор профиля, список правил которого запрашивается (без скобок и кавывчек).

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "integer",
    "filters": [
      {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ],
     },
    ...
    ]
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
  },
  ...
]
```

* `id` - номер правила выбора сигнатур;
* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, макимальная длина 255 символов.

</details>

<details>
<summary>Создание правила в профиле</summary>

```
POST /ips/profile_rules?profile_id=<string>&anchor_item_id=<integer>&insert_after=<true|false>
```

* `profile_id` - идентификатор профиля, в котором создается правило (без скобок и кавывчек);
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "filters": [
       {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ]
      },
      ...
    ],
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
}
```

* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 

```json5
{
  "id": "integer"
}
```

* `id` - номер правила выбора сигнатур.

</details>

<details>
<summary>Изменение правила в профиле</summary>

```
PATCH /ips/profile_rules?profile_id=<string>&rule_id=<integer>
```

* `profile_id` - идентификатор профиля, в котором изменяется правило;
* `rule_id` - идентификатор правила в профиле.

**Json-тело запроса:** (некоторые или все поля объекта)

```json5
{
    "filters": [
      {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ]
       },
      ...
    ],
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
}
```

* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Удаление правила в профиле</summary>

```
DELETE /ips/profile_rules?profile_id=<string>&rule_id=<integer>
```

* `profile_id` - идентификатор профиля, в котором удаляется правило;
* `rule_id` - идентификатор правила в профиле.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Создание профиля с правилами</summary>

```
POST /ips/profiles-create-with-rules
```

**Json-тело запроса:**: 

```json5
{
    "name": "string",
    "comment": "string",
    "rules": [
          {
          "filters": [
                {
                "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
                "operator": "equals",
                "values": [ "string" | "integer" ]
                  },
                  ...
                ],
          "action": "default" | "alert" | "drop" | "pass",
          "comment": "string"
          },
          ...
        ]
    }
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `rules` - список правил профиля:
  * `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
  * `action` - строка с действием при срабатывании правила;
  * `comment` - комментарий, макимальная длина 255 символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного профиля с правилами.

</details>

<details>

<summary>Копирование профиля с правилами</summary>

```
POST /ips/profiles/<id профиля>/copy
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного профиля.

</details>

## Профили Web Application Control (WAF)

<details>

<summary>Получение списка профилей</summary>

```
GET /reverse_proxy_backend/waf/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "exceptions": [
      {
        "id": "string",
        "rule_id": "integer",
        "comment": "string",
        "enabled": "boolean"
      },
      ...
    ],
    "server_tokens": "boolean",
    "comment": "string",
    "central_console": "boolean"
  },
  ...
]
```

* `id` - идентификатор профиля;
* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий для исключения, максимальная длина - 128 символов;
* `exceptions` - исключенные правила:
  * `id` - идентификатор исключенного правила;
  * `rule_id` - идентификатор исключенного правила в профиле;
  * `comment` - комментарий, максимальная длина - 255 символов;
  * `enabled` - статус: `true` - включено, `false` - выключено.
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `central_console` - `true`, если профиль создан в Центральной консоли, только для чтения.

</details>

<details>

<summary>Создание профиля</summary>

```
POST /reverse_proxy_backend/waf/profiles
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "server_tokens": "boolean",
    "comment": "string",
    "central_console": "boolean"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий для исключения, максимальная длина - 128 символов, при создании профиля может быть пустым;
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `central_console` - `true`, если профиль создан в Центральной консоли, только для чтения.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

</details>

<details>

<summary>Изменение профиля</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "server_tokens": "boolean",
    "comment": "string",
    "central_console": "boolean"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий правил, которые были отключены, максимальная длина - 128 символов;
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `central_console` - `true`, если профиль создан в Центральной консоли, только для чтения.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Удаление профиля</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Получение списка категорий правил</summary>

```
GET /reverse_proxy_backend/waf/categories
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string",
    "description": "string"
  },
  ...
]
```

* `id` - идентификатор категории, максимальная длина - 42 символа;
* `title` - название категории, максимальная длина - 42 символа;
* `description` - описание категории, максимальная длина - 255 символов.

</details>

<details>

<summary>Получение списка категорий правил в профиле</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/categories
```

**Ответ на успешный запрос:**

* Список категорий правил, которые включены в профиле.

```json5
[
  {
    "id": "string",
    "title": "string",
    "description": "string"
  },
  ...
]
```

* `id` - идентификатор категории, максимальная длина - 42 символа;
* `title` - название категории, максимальная длина - 42 символа;
* `description` - описание категории, максимальная длина - 255 символов.

</details>

<details>

<summary>Добавление или удаление категории правил в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/categories/<id категории>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:**

* Если профиль или категория не найдены по идентификатору, то код ответа - 542;
* Если enabled - `true`, то категория, идентификатор которой указан в запросе, будет удалена из списка `disabled_categories` профиля. Ответ - 200 ОК;
* Если enabled - `false`, то категория, идентификатор которой указан в запросе, будет добавлена в список `disabled_categories` профиля. Ответ - 200 ОК.

</details>

<details>

<summary>Получение белых и черных списков в профиле</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/rules
```

**Ответ на успешный запрос:**

```json5
[
  {
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean",
    "id": "integer"
  },
  ...
]
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено;
* `id` - номер правила.

</details>

<details>

<summary>Создание белых и черных списков в профиле</summary>

```
POST /reverse_proxy_backend/waf/profiles/<id профиля>/rules?anchor_item_id=<integer>&insert_after=<true|false>
```

* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>

<summary>Изменение белых и черных списков в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/rules/<id правила в профиле>
```

**Json-тело запроса:**

```json5
{
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Перемещение белых и черных списков в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/rules/move
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

* `id` - идентификатор перемещаемого правила;
* `anchor_item_id` - идентификатор правила, относительно которого будет перемещено правило;
* `insert_after` - вставить правило до или после `anchor_item_id`. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление белых и черных списков в профиле</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Получение списка исключенных правил профиля</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
  },
  ...
]
```

* `id` - идентификатор исключенного правила;
* `rule_id` - идентификатор правила;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

</details>

<details>

<summary>Создание исключенного правила в профиле</summary>

```
POST /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions
```

**Json-тело запроса:**

```json5
{
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
}
```

* `rule_id` - идентификатор правила. Можно найти в журнале в разделе **Отчеты и журналы -> События безопасности -> [Web Application Firewall](/settings/reports/security-events.md#web-application-firewall)**;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>

<summary>Изменение исключенного правила в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions/<id исключенного правила>
```

**Json-тело запроса:**

```json5
{
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
}
```

* `rule_id` - идентификатор правила. Можно найти в журнале в разделе **Отчеты и журналы -> События безопасности -> [Web Application Firewall](/settings/reports/security-events.md#web-application-firewall)**;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление исключенного правила в профиле</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions/<id исключенного правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Контроль приложений

<details>

<summary>Получение списка профилей</summary>

```
GET /api/application_control/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
    ],
  }
]
```

* `id` - идентификатор профиля;
* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).      

</details>

<details>

<summary>Создание профиля</summary>

```
POST /api/application_control/profiles
```

**Json-тело запроса:**

```json5

{
  "name": "string",
  "comment": "string",
  "protocols": [
    {
      "id": "string",
      "action": "deny" | "allow"
    },
    ...
    ],
}
```

* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
      ],
  }
]
```

* `id` - идентификатор профиля;
* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

</details>

<details>

<summary>Копирование профиля</summary>

```
POST /api/application_control/profiles/<id профиля>/copy
```

**Ответ на успешный запрос:** 

```json5
{
  "id": "integer"
}
```

* `id` - идентификатор копии профиля.

</details>

<details>

<summary>Редактирование профиля</summary>

```
PATCH /api/application_control/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
[
  {
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
      ],
  }
]
```

* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление профиля</summary>

```
DELETE /api/application_control/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 OK

</details>