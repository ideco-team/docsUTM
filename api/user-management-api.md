# Управление пользователями и группами

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

## Управление пользователями

<details>
<summary>Получение списка пользователей</summary>

```
GET /user_backend/users
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "name": "string",
        "login": "string",
        "parent_id": "string",
        "enabled": "boolean",
        "domain_type": "local" | "ad" | "ald" | "radius" | "device",
        "domain_name": "string",
        "ldap_guid": "string",
        "phone_number": "string",
        "comment": "string"
    },
    ...
]
```

* `id` - идентификатор пользователя;
* `name` - имя пользователя;
* `login` - логин пользователя;
* `parent_id` - идентификатор группы;
* `enabled` - соответствует опции **Запретить доступ**: `true` - включена, `false` - выключена;
* `domain_type` - тип пользователя:
    * `local` - локальный пользователь Ideco NGFW;
    * `ad` - пользователь, импортированный из Active Directory;
    * `ald` - пользователь, импортированный из  ALD Pro;
    * `radius` - пользователь RADIUS-сервера;
    * `device` - клиентское устройство, подключающееся через Ideco Client в режиме Device VPN.
* `domain_name` - имя домена, из которого импортирован пользователь;
* `ldap_guid` - идентификатор объекта AD;
* `phone_number` - номер телефона пользователя;
* `comment` - комментарий.

</details>

<details>
<summary>Создание пользователя</summary>

```
POST /user_backend/users
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "login": "string",
    "psw": "string",
    "parent_id": "string",
    "phone_number": "string" | null,
    "comment": "string"
}
```

* `name` - имя пользователя;
* `login` - логин пользователя;
* `psw` - пароль пользователя;
* `parent_id` - идентификатор группы;
* `phone_number` - номер телефона пользователя, не обязательно;
* `comment` - комментарий, может быть пустым.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор добавленного пользователя.

Если пользователь с указанным логином или именем существует, то исключение с описанием ошибки.

</details>

<details>
<summary>Изменение одного пользователя</summary>

```
PUT /user_backend/users/<id пользователя>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "login": "string",
    "parent_id": "string",
    "enabled": "boolean",
    "domain_type": "string",
    "domain_name": "string",
    "ldap_guid": "string",
    "phone_number": "string" | null,
    "comment": "string"
}
```

* `name` - имя пользователя;
* `login` - логин пользователя;
* `parent_id` - идентификатор группы;
* `enabled` - соответствует опции **Запретить доступ**: `true` - включена, `false` - выключена;
* `domain_type` - тип пользователя:
    * `local` - локальный пользователь Ideco NGFW;
    * `ad` - пользователь, импортированный из Active Directory;
    * `ald` - пользователь, импортированный из  ALD Pro;
    * `radius` - пользователь RADIUS-сервера;
    * `device` - клиентское устройство, подключающееся через Ideco Client в режиме Device VPN.
* `domain_name` - имя домена, из которого импортирован пользователь;
* `ldap_guid` - идентификатор объекта AD;
* `phone_number` - номер телефона пользователя;
* `comment` - комментарий, может быть пустым.

**Важно!** Для пользователя со значением `domain_type`: `radius` можно изменить только значения полей `enabled`, `comment` и `name`. Для пользователя со значением `domain_type`: `device` нельзя изменить никакие значения.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление пользователя</summary>

```
DELETE /user_backend/users/<id пользователя>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Смена пароля пользователя</summary>

```
PUT /user_backend/change_password/<id пользователя>
```

**Json-тело запроса:**

```json5
{
    "password": "string"
}
```

* `password` - новый пароль пользователя, не может быть пустым.

**Ответ на успешный запрос:** 200 ОК

</details>

## Управление группами пользователей

<details>
<summary>Получение групп пользователей</summary>

```
GET /user_backend/groups
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "name": "string",
        "parent_id": "string",
        "domain_type": "string",
        "domain_name": "string",
        "ldap_guid": "string"
    }
]
```

* `id` - идентификатор группы;
* `name` - имя группы;
* `parent_id` - идентификатор родительской группы;
* `domain_type` - тип группы пользователей:
    * `local` - локальная группа Ideco NGFW;
    * `ad` - группа, импортированная из Active Directory;
    * `ald` - группа, импортированная из  ALD Pro;
    * `radius` - группа RADIUS-сервера;
    * `device` - группа Device VPN.
* `domain_name` - имя домена, из которого импортирована группа;
* `ldap_guid` - идентификатор объекта AD.

</details>

<details>
<summary>Создание группы пользователей</summary>

```
POST /user_backend/groups
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "parent_id": "string"
}
```

* `name` - имя группы;
* `parent_id` - идентификатор группы.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор добавленной группы.

Если группа с указанным именем у указанного предка существует, то код ответа 542 c описанием ошибки.

</details>

<details>
<summary>Изменение группы</summary>

```
PUT /user_backend/groups/<id группы>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "parent_id": "string",
    "domain_type": "string",
    "domain_name": "string",
    "ldap_guid": "string"
}
```

* `name` - имя группы;
* `parent_id` - идентификатор родительской группы;
* `domain_type` - тип группы пользователей:
    * `local` - локальная группа Ideco NGFW;
    * `ad` - группа, импортированная из Active Directory;
    * `ald` - группа, импортированная из  ALD Pro;
    * `radius` - группа RADIUS-сервера;
    * `device` - группа Device VPN.
* `domain_name` - имя домена, из которого импортирована группа;
* `ldap_guid` - идентификатор объекта AD.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление группы</summary>

```
DELETE /user_backend/groups/<id группы>
```

**Ответ на успешный запрос:** 200 ОК

</details>