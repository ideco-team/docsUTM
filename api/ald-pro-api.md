# Управление интеграцией с ALD Pro

## Управление интеграцией с доменами ALD

<details>
<summary>Получение списка присоединенных доменов</summary>

```
GET /ald_backend/domains
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "name": "string",
        "computer_name": "string",
        "dns_ips": ["string"],  
        "status": "string",
        "error": "string",
    }
    ...
]
```

* `id` - идентификатор домена;
* `name` - имя домена, должно быть уникальным;
* `computer_name` - имя компьютера (NGFW) в домене;
* `dns_ips` - список IP-адресов контроллеров домена;
* `status` - статус присоединения. Статус может быть `init`, `error`, `completed`;
* `error` - ошибка, возникшая при присоединении к домену.

</details>

<details>
<summary>Ввод NGFW в домен</summary>

```
POST /ald_backend/domains
```

**JSON-тело запроса:**

```json5
{
    "name": "string",
    "computer_name": "string",
    "dns_ips": ["string"],
    "user": "string",
    "password": "string"
}
```

* `name` - имя домена;
* `computer_name` - имя компьютера (NGFW) в домене;
* `dns_ips` - список IP-адресов контроллеров домена;
* `user` - имя пользователя, имеющего права на ввод компьютера в домен;
* `password` - пароль пользователя.

**Ответ на успешный запрос:** 200 OK


</details>

<details>

<summary>Удалении интеграции с доменом</summary>

```
DELETE /ald_backend/domains/<имя домена>
```

Удалить можно только домены в состоянии error или complete.

**Ответ на успешный запрос:** 200 OK

</details>

## Управление ALD-правилами авторизации

<details>
<summary>Получение списка ALD-правил авторизации</summary>

```
GET /web/admins/ald?format_type=JSON|CSV&columns=["id","enabled",...]
```

**Параметры запроса:**

* `format_type` - поддерживается `CSV` и `JSON`, по умолчанию `JSON`;
* `columns` - список столбцов, которые попадут в `CSV` отчет, по умолчанию пустой список.

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "enabled": "boolean",
        "role": "integer",
        "group_alias": "string",
        "comment": "string"
    },
    ...
]
```

* `id` - идентификатор правила;
* `enabled` - правило включено/выключено (можно/нельзя по нему зайти в систему);
* `role` - идентификатор уровня доступа правила;
* `group_alias` - алиас группы безопасности;
* `comment` - комментарий.

</details>

<details>
<summary>Добавление ALD-правил авторизации</summary>

```
POST /web/admins/ald
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "role": "integer",
    "group_alias": "string",
    "comment": "string"
}
```
* `enabled` - правило включено/выключено (можно/нельзя по нему зайти в систему);
* `role` - идентификатор уровня доступа правила;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
}
```

</details>

<details>
<summary>Изменение ALD-правил авторизации</summary>

```
PATCH /web/admins/ald/<id правила>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "role": "integer",
    "group_alias": "string",
    "comment": "string"
}
```
* `enabled` - правило включено/выключено (можно/нельзя по нему зайти в систему);
* `role` - идентификатор уровня доступа правила;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление ALD-правил авторизации</summary>

```
DELETE /web/admins/ald/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>