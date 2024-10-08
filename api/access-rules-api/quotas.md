# Квоты

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

* `enabled` - если `true`, то подсчет квот включен, `false` - выключен.

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

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

**Ответ на успешный запрос:** 200 ОК

</details>