# Управление профилями безопасности

## Профили Предотвращения вторжений

<details>
<summary>Получение списка профилей</summary>

```
GET /ips/profiles
```

**Ответ на успешный запрос:** список объектов `IPSProfile`

```json5
{
    "id": "string",
    "name": "string",
    "comment": "string",
}
```
* `id` - уникальный идентификатор профиля;
* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 256 символов.

</details>

<details>
<summary>Создание профиля</summary>

```
POST /ips/profiles
```
**Тело запроса**: объект `IPSProfile` без поля `id`

```json5
{
    "name": "string",
    "comment": "string",
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 256 символов.

**Ответ на успешный запрос:**

```json5
{
  "id": "string",
}
```

* `id` - уникальный идентификатор профиля.

</details>

<details>
<summary>Изменение профиля</summary>

```
PATCH /ips/profiles/{id}
```

* `id` - уникальный идентификатор профиля.

**Тело запроса:** некоторые или все поля объекта `IPSProfile` без поля `id`

```json5
{
    "name": "string",
    "comment": "string",
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 256 символов.

**Ответ на успешный запрос:** 200 ОК

</details>

</details>

<details>
<summary>Удаление профиля</summary>

```
DELETE /ips/profiles/{id}
```

* `id` - уникальный идентификатор профиля.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение списка правил профиля</summary>

```
GET /ips/profile_rules?profile_id={string}
```

* `profile_id` - идентификатор профиля, список правил которого запрашивается.

**Ответ на успешный запрос:** список объектов `IPSProfileRule`

```json5
{
    "id": "integer",
    "filter": {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": ["string" | "integer"],
    },
    "action": "default" | "alert" | "drop" | "skip",
    "comment": "string",
}
```

* `id` - номер правила выбора сигнатур;
* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, который используется для всех типов `key`, кроме `sid`(число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, макимальная длина 256 символов.

</details>

<details>
<summary>Создание правила в профиле</summary>

```
POST /ips/profile_rules?profile_id={string}&anchor_item_id={int}&insert_after={true|false}
```

* `profile_id` - идентификатор профиля, в котором создается правило;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Тело запроса:** список объектов `IPSProfileRule` без поля `id`

```json5
{
    "filters": [
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": ["string" | "integer"],
    ],
    "action": "default" | "alert" | "drop" | "skip",
    "comment": "string",
}
```

* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, который используется для всех типов `key`, кроме `sid`(число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 256 символов.

**Ответ на успешный запрос:** 

```json5
{
  "id": "integer",
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

**Тело запроса:** некоторые или все поля объекта `IPSProfileRule` без поля `id`

```json5
{
    "filters": [
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": ["string" | "integer"],
    ],
    "action": "default" | "alert" | "drop" | "skip",
    "comment": "string",
}
```

* `filters` - список фильтров правила:
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, который используется для всех типов `key`, кроме `sid`(число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 256 символов.

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