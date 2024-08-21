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

**Json-тело запроса:** (некоторые или все поля)

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
        "values": ["string" | "integer"],
     },
    ...
    ]
    "action": "default" | "alert" | "drop" | "skip",
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
POST /ips/profile_rules?profile_id={string}&anchor_item_id={int}&insert_after={true|false}
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
        "values": ["string" | "integer"]
      },
      ...
    ],
    "action": "default" | "alert" | "drop" | "skip",
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
PATCH /ips/profile_rules?profile_id={string}&rule_id={int}
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
        "values": ["string" | "integer"]
       },
      ...
    ],
    "action": "default" | "alert" | "drop" | "skip",
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
DELETE /ips/profile_rules?profile_id={string}&rule_id={int}
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
                      "values": ["string" | "integer"]
                        },
                        ...
                      ],
              "action": "default" | "alert" | "drop" | "skip",
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
      "action": "deny | allow"
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
      "action": "deny | allow"
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
      "action": "deny | allow"
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
      "action": "deny | allow"
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