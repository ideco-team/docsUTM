# Управление интеграцией с Active Directory

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

## Управление интеграцией с доменами AD

<details>
<summary>Получение статуса работы службы ad_backend</summary>

```
GET /ad_backend/status
```

**Ответ на успешный запрос:**

```json5
{
    "msg": ["string"] // (список ошибок)
}
```

Возможные ошибки:

* **no_license** - Лицензия отсутствует | License is not available

</details>

<details>
<summary>Ввод NGFW в домен</summary>

```
POST /ad_backend/domains
```

**Json-тело запроса:**

```json5
{
    "name": "string", 
    "computer_name": "string",
    "dns_ips": ["string"],
    "user": "string",
    "password": "string",
    "ldap_paths": ["string"]
}
```

* `name` - имя домена;
* `computer_name` - имя компьютера (NGFW) в домене;
* `dns_ips` - список IP-адресов контроллеров домена;
* `user` - имя пользователя, имеющего права на ввод компьютера в домен;
* `password` - пароль пользователя `user`;
* `ldap_paths` - список LDAP-путей, по которым будет происходит поиск групп безопасности. Максимум 10 путей, максимальная длина строки - 1024 символа. Если при интеграции передать пустой список, то поиск групп безопасности будет производиться по всему лесу доменов. Если указаны конкретные LDAP-пути, импорт прочих пользователей и групп безопасности будет невозможен.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор домена.

</details>

<details>
<summary>Получение списка присоединенных доменов</summary>

```
GET /ad_backend/domains
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "name": "string",  
        "computer_name": "string",
        "dns_ips": ["string"], 
        "user": "string",
        "ldap_paths": ["string"],
    },
    ...
]
```

</details>

<details>
<summary>Выполнение "переинтеграции" с AD</summary>

```
PUT /ad_backend/domains/<id домена>
```

**Json-тело запроса:**

```json5
{
    "computer_name": "string",
    "user": "string",
    "password": "string",
    "ldap_paths": ["string"]
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление интеграции с доменом</summary>

```
DELETE /ad_backend/domains/<id домена>
```

**Ответ на успешный запрос:** 200 OK

При выводе NGFW из домена удаляются все настройки интеграции с контроллером домена, а
также все настройки синхронизируемых групп. При этом сами
группы и пользователи в них становятся локальными.

В AD созданный для NGFW компьютер не удаляется.

</details>

## Управление AD правилами авторизации

<details>
<summary>Получение списка AD правил авторизации</summary>

```
GET /web/admins/ad?format_type=JSON|CSV&columns=["id","enabled",...]
```

**Параметры запроса:**

* `format_type` - поддерживается `CSV` и `JSON`, по умолчанию `JSON`;
* `columns` - список столбцов, которые попадут в `CSV` отчет, по умолчанию пустой список.

Список `columns` состоит из столбцов (значения столбцов описаны ниже):

* `id`;
* `enabled`;
* `role`;
* `group_alias`;
* `comment`.

**Ответ на успешный запрос в формате JSON:**

```json5
[
    {
        "id": "string",
        "enabled": "boolean",
        "role": "integer",
        "group_alias": "string",
        "comment": "string",
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
<summary>Добавление AD правил авторизации</summary>

```
POST /web/admins/ad
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "role": "integer",
    "group_alias": "string",
    "comment": "string",
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
}
```

* `enabled` - правило включено/выключено (можно/нельзя по нему зайти в систему);
* `role` - идентификатор уровня доступа правила;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

</details>

<details>
<summary>Изменение AD правил авторизации</summary>

```
PATCH /web/admins/ad/<id правила>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "role": "integer",
    "group_alias": "string",
    "comment": "string",
}
```
* `enabled` - правило включено/выключено (можно/нельзя по нему зайти в систему);
* `role` - идентификатор уровня доступа правила;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

**Ответ на успешный запрос:** 200 OK

**При успехе веб-сессии удаляются.**

</details>

<details>
<summary>Удаление AD правил авторизации</summary>

```
DELETE /web/admins/ad/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>


## Управление настройками службы

<details>
<summary>Получение настроек авторизации</summary>

```
GET /ad_backend/settings
```

**Ответ на успешный запрос:**

```json5
{
    "authorization_by_logs": "boolean"
}
```

</details>

<details>
<summary>Изменение настроек авторизации</summary>

```
PUT /ad_backend/settings
```

**Json-тело запроса:**

```json5
{
    "authorization_by_logs": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

## Получение информации об объектах контроллера домена

<details>
<summary>Получение списка групп безопасности в заданном домене</summary>

```
GET /ad_backend/domains/<имя домена>/security_groups
```

**Ответ на успешный запрос:**

```json5
[
    {
        "name": "string",
        "guid": "string"
    },
    ...
]
```

* `name` - отображаемое имя группы безопасности;
* `guid` - objectGUID группы безопасности.

</details>

<details>
<summary>Получение дерева OU в заданном домене</summary>

```
GET /ad_backend/domains/<имя домена>/tree
```

**Ответ на успешный запрос:**

```json5
[
    {
        "name": "string",
        "guid": "string",
        "parent_guid": "string" | "null"
    }
    ...
]
```

* `name` - отображаемое имя группы;
* `guid` - objectGUID группы;
* `parent_guid` - objectGUID родительской группы.

Дерево представлено в виде линейного списка со всеми узлами. У каждого узла
есть его `guid` и `parent_guid`.

</details>

<details>
<summary>Получение списка forward-зон контроллера домена</summary>

```
GET /ad_backend/forward_zones
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id":  "string",
        "name": "string",
        "servers": ["string"],
        "enabled": "boolean",
        "comment": "string"
    },
    ...
]
```

* `id` - идентификатор зоны;
* `name` - название зоны;
* `servers` - список IP-адресов DNS-серверов;
* `enabled` - включена/выключена зона;
* `comment` - комментарий, может быть пустым.

</details>

## Управление настройками синхронизации групп

<details>
<summary>Получение настройки синхронизации групп</summary>

```
GET /ad_backend/group_settings
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "integer",
    "group_id": "integer",
    "search_filter": "string",
    "object_guid": "string",
    "domain_name": "string",
    "sync_type": "ldap" | "security"
  },
  ...
]
```

* `id` - идентификатор записи синхронизации;
* `group_id` - идентификатор группы NGFW;
* `search_filter` - фильтр поиска в домене;
* `object_guid` - objectGUID группы из AD, с которой выполняется синхронизация;
* `domain_name` - имя домена, с которым выполняется синхронизация;
* `sync_type` - `security`, если группа синхронизируется с группой безопасности, `ldap` - если группа синхронизируется с OU.

</details>

<details>
<summary>Добавление настроек синхронизации группы с контроллером домена</summary>

Группа безопасности импортируется как плоский список пользователей без
сохранения древовидной структуры AD. Синхронизация с OU сохраняет древовидную структуру пользователей.

Если группа была локальной, а после этого запроса - синхронизируемой, то все ее
текущие потомки считаются импортированными из AD. Если в домене таких
пользователей нет, то они при первой же синхронизации будут перемещены в
корзину.

```
POST /ad_backend/group_settings
```

**Json-тело запроса:**

```json5
{
    "search_filter": "string",
    "object_guid": "string",
    "group_id": "integer",
    "domain_name": "string",
    "sync_type": "ldap" | "security"
  }
```

**Ответ на успешный запрос:**

```json5
{
    "id": "sync_record_id"
}
```

</details>

<details>
<summary>Изменение настроек синхронизации группы с контроллером домена</summary>

Группа безопасности импортируется как плоский список пользователей без
сохранения древовидной структуры AD. Синхронизация с OU сохраняет древовидную структуру пользователей.

```
PUT /ad_backend/group_settings/<id записи синхронизации>
```

**Json-тело запроса:**

```json5
{
    "search_filter": "string",
    "object_guid": "string",
    "domain_name": "string",
    "group_id": "integer",
    "sync_type": "ldap" | "security"
  }
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Отмена синхронизации группы с контроллером домена</summary>

После отмены синхронизации группы с доменом все ее потомки считаются
локальными. Для авторизации таких пользователей нужно либо ставить тип
авторизации "по IP", либо менять всем пароли.

```
DELETE /ad_backend/group_settings/<id группы>
```

**Ответ на успешный запрос:** 200 OK

</details>