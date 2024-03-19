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