# Контроль приложений

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
      "insert_after": "boolean"
    }
}
```

* `id` - идентификатор правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false`, то на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /application_control_backend/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>