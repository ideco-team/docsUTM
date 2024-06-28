# Управление интеграцией с Active Directory

<details>
<summary>Получение статуса работы службы</summary>

```
GET /ad_backend/status
```

**Ответ на успешный запрос:**

```
{
    "msg": ["string"] (Список ошибок)
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

```
{
    "name": "string", 
    "computer_name": "string",
    "dns_ips": ["string"],
    "user": "string",
    "password": "string",
    "ldap_paths": ["string"]
}
```

* `"name"` - имя домена;
* `"computer_name"` -имя компьютера (NGFW) в домене;
* `"dns_ips"` - список IP-адресов контроллеров домена;
* `"user"` - имя пользователя, имеющего права на ввод компьютера в домен;
* `"password"` - пароль пользователя `user`;
* `"ldap_paths"` - список LDAP-путей, по которым будет происходит поиск групп безопасности. Максимум 10 путей, максимальная длина строки - 1024 символа. Если при интеграции передать пустой список, то поиск групп безопасности будет производиться по всему лесу доменов. Если указаны конкретные LDAP-пути, импорт прочих пользователей и групп безопасности будет невозможен.

Ответ: 200 OK

</details>

<details>
<summary>Получение списка присоединенных контроллеров домена</summary>

```
GET /ad_backend/domains
```

**Ответ на успешный запрос:**

```
[
    {
        "name": "string",  
        "computer_name": "string",
        "dns_ips": ["string"], 
        "ldap_paths": ["string"],
    },
    ...
]
```

</details>

<details>
<summary>Выполнение "переинтеграции" с AD</summary>

```
PUT /ad_backend/domains/<domain_name>
```

**Json-тело запроса:**

```
{
    "computer_name": "string",
    "user": "string",
    "password": "string",
    "ldap_paths": ["string"]
}
```

Ответ: 200 OK

</details>

<details>
<summary>Удаление интеграции с доменом</summary>

```
DELETE /ad_backend/domains/<domain_name>
```

Ответ: 200 OK

При выводе NGFW из домена удаляются все настройки интеграции с контроллером доменом, а
так же все настройки синхронизируемых групп. При этом сами
группы и пользователи в них становятся локальными.

Удаление созданного для NGFW компьютера в AD не производится.

</details>

## Управление аккаунтами администраторов

<details>
<summary>Получение списка локальных администраторов</summary>

```
GET /web/admins/local?format_type=JSON|CSV
```

Поддерживается `CSV` и `JSON`, по умолчанию `JSON`

**Ответ на успешный запрос:**

```
[
    {
        "id": "string",
        "enabled": "boolean",
        "name": "string",
        "login": "string",
        "role": "integer",
        "comment": "string",
        "password_timestamp": "integer",
    },
    ...
]
```

* `id` - идентификатор администратора;
* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя администратора;
* `login` - логин администратора;
* `role` - Идентификатор уровня доступа администратора;
* `comment` - момментарий;
* `password_timestamp` - время (таймстамп) последнего успешного изменения пароля.

</details>

<details>
<summary>Добавление локального администратора</summary>

```
POST /web/admins/local
```

**Json-тело запроса:**

```
{
    "enabled": "boolean",
    "name": "string",
    "login": "string",
    "password": "string",
    "role": "integer",
    "comment": "string",
}
```
**Ответ на успешный запрос:**

```
{
    "id": "string",
}
```

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя, ненулевое текстовое поле, длина от 1 до 42 символов;
* `login` - логин не должен содержать `.` (одну точку) или `..` (две точки), а также символов [\\:/~$!\s@]. Длинна поля от 1 до 42 символов включительно;
* `password` - пароль, ненулевое текстовое поле, длина от 10 до 42 символов;
* `role` - идентификатор уровня доступа аккаунта;
* `comment` - комментарий, максимальная длина 256 символов, **может** быть пустым.

</details>

<details>
<summary>Изменение настроек и пароля локального администратора</summary>

```
PATCH /web/admins/local/$ID
```

* `$ID` - Идентификатор администратора.

**Json-тело запроса:**

Все поля необязательные

```
{
    "enabled": "boolean",
    "name": "string",
    "login": "string",
    "password": "string",
    "role": "integer",
    "comment": "string",
}
```

**Ответ на успешный запрос:** 200 ОК

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя;
* `login` - логин;
* `password` - пароль (если `password==null` пароль останется прежним);
* `role` - идентификатор уровня доступа аккаунта;
* `comment` - комментарий, максимальная длина 256 символов, **может** быть пустым.

</details>

<details>
<summary>Удаление локального администратора</summary>

**Последнего локального администратора удалять нельзя!**

```
DELETE /web/admins/local/$ID
```

* `$ID` - Идентификатор администратора.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Добавление AD/ALD администратора</summary>

```
POST /web/admins/external
```

**Json-тело запроса:**

```
{
    "enabled": "boolean",
    "auth_type": "string",
    "domain": "string",
    "group_alias": "string",
    "role": "integer",
    "comment": "string",
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string",
}
```

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `auth_type` - тип домена: "ad", "ald";
* `domain` - имя домена, в который введен NGFW;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `role` - идентификатор уровня доступа аккаунта;
* `comment` - комментарий, максимальная длина 256 символов, **может** быть пустым.

</details>

<details>
<summary>Изменение настроек AD/ALD администратора</summary>

```
PATCH /web/admins/external/$ID
```

* `$ID` - Идентификатор администратора.

**Json-тело запроса:**

```
{
    "enabled": "boolean",
    "auth_type": "string",
    "domain": "string",
    "group_alias": "string",
    "role": "integer",
    "comment": "string",
}
```

**Ответ на успешный запрос:** 200 OK

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `auth_type` - тип домена: "ad", "ald";
* `domain` - имя домена, в который введен NGFW;
* `group_alias` - алиас группы безопасности, тип алиаса должен соответствовать типу домена;
* `role` - идентификатор уровня доступа аккаунта;
* `comment` - комментарий, максимальная длина 256 символов, **может** быть пустым.

</details>

<details>
<summary>Авторизация администратора в Веб-интерфейсе</summary>

```
POST /web/admin/auth/login
```

**Json-тело запроса:**

```
{
    "auth_type": string, 
    "login": "string",
    "password": "string",
    "rest_path": "string",
}
```

**Ответ на успешный запрос:** 200 OK

* `auth_type` - тип авторизации: "local", "ad", "ald";
* `login` - логин, для типа авторизации "ad" и "ald" должен указываться вместе с доменом в формате login@domain;
* `password` - пароль;
* `rest_path` - префикс URL на который выставлять cookie. Например, `/` или `/rest`.

</details>

## Управление настройками службы

<details>
<summary>Получение настроек авторизации</summary>

```
GET /ad_backend/settings
```

**Ответ на успешный запрос:**

```
{
    "authorization_by_logs": boolean (Включена/выключена авторизация по логам AD)
}
```

</details>

<details>
<summary>Изменение настроек авторизации</summary>

```
PUT /ad_backend/settings
```

**Json-тело запроса:**

```
{
    "authorization_by_logs": boolean
}
```

Ответ: 200 OK

</details>

## Получение информации об объектах контроллера домена

<details>
<summary>Получение списка групп безопасности в заданном домене</summary>

```
GET /ad_backend/domains/<domain_name>/security_groups
```

**Ответ на успешный запрос:**

```
[
    {
        "name": "string",
        "guid": "string"
    }
]
```

* `"name"` - отображаемое имя группы безопасности;
* `"guid"` - objectGUID группы безопасности.

</details>

<details>
<summary>Получение дерева OU в заданном домене</summary>

```
GET /ad_backend/domains/<domain_name>/tree
```

**Ответ на успешный запрос:**

```
[
    {
        "name": "string",
        "guid": "string",
        "parent_guid": "string" | null
    }
]
```

* `"name"` - отображаемое имя группы;
* `"guid"` - objectGUID группы;
* `"parent_guid"` - objectGUID родительской группы.

Дерево представлено в виде линейного списка со всеми узлами. У каждого узла
есть его guid и guid родителя.

</details>

<details>
<summary>Получение списка forward-зон контроллера домена</summary>

```
GET /ad_backend/forward_zones
```

**Ответ на успешный запрос:**

```
[
    {
        "id":  "string",
        "name": "string",
        "servers": ["string"],
        "enabled": true,
        "comment": "string"
    },
    ...
]
```

* `"id"` - уникальное название зоны;
* `"name"` - название зоны;
* `"servers"` - список IP-адресов DNS-серверов;
* `"enabled"` - включена/выключена зона;
* `"comment"` - комментарий (может быть пустым).

</details>

## Управление настройками синхронизации групп

<details>
<summary>Получение настройки синхронизации групп</summary> OK

```
GET /ad_backend/group_settings
```

**Ответ на успешный запрос:**

```
[
  {
    "id": "int",
    "group_id": "int",
    "search_filter": "string",
    "object_guid": "string",
    "domain_name": "string",
    "sync_type": "ldap" | "security"
  },
  ...
]
```

* `"id"` - ID записи синхронизации;
* `"group_id"` - id группы NGFW;
* `"search_filter"` - фильтр поиска в домене;
* `"object_guid"` - objectGUID группы из AD, с которой выполняется синхронизация;
* `"domain_name"` - имя домена, с которым выполняется синхронизация;
* `"sync_type"` - `"security"`, если группа синхронизируется с группой безопасности, `"ldap"` - если группа синхронизируется с OU.

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

```
{
    "search_filter": "string",
    "object_guid": "string",
    "group_id": int,
    "domain_name": "string",
    "sync_type": "ldap" | "security"
  }
```

**Ответ на успешный запрос:**

```
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

```
{
    "search_filter": "string",
    "object_guid": "string",
    "domain_name": "string",
    "group_id": int,
    "sync_type": "ldap" | "security"
  }
```

Ответ: 200 ОК

</details>

<details>
<summary>Отмена синхронизации группы с контроллером домена</summary>

После отмены синхронизации группы с доменом все ее потомки считаются
локальными. Для авторизации таких пользователей нужно либо ставить тип
авторизации "по IP", либо менять всем пароли.

```
DELETE /ad_backend/group_settings/<id группы NGFW>
```

Ответ: 200 ОК

</details>