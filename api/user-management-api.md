# Управление пользователями и группами

<details>
<summary>Получение списка пользователей</summary>

```
GET /user_backend/users
```

**Ответ на успешный запрос:**

```
[
    {
        "id": int,
        "name": str,
        "login": str,
        "parent_id": int,
        "enabled": bool,
        "domain_type": str,  # domain_type ['local'|'ad'|'ald'|'radius']
        "domain_name": str,
        "ldap_guid": str,
        "phone_number": str,
        "comment": str
    }
]
```

* `id` - уникальный идентификатор пользователя;
* `name` - имя пользователя;
* `login` - логин пользователя;
* `parent_id` - id-группы;
* `enabled` - соответствует опции **Запретить доступ** (false -  опция **Запретить доступ** не включена, true - включена);
* `domain_type` - тип домена;
* `domain_name` - имя домена, из которого импортирован пользователь;
* `ldap_guid` - уникальный идентификатор объекта AD;
* `phone_number` - номер телефона пользователя;
* `comment` - комментарий.

</details>

<details>
<summary>Изменение одного пользователя</summary>

```
PUT /user_backend/users/<id>
```

**Json-тело запроса:**

```
{
    "name": str,
    "login": str,
    "parent_id": int,
    "enabled": bool,
    "domain_type": str,
    "domain_name": str,
    "ldap_guid": str,
    "phone_number": str,
    "comment": str
}
```

* `name` - имя пользователя;
* `login` - логин пользователя;
* `parent_id` - id-группы;
* `enabled` - оответствует опции **Запретить доступ** (false -  опция **Запретить доступ** не включена, true - включена);
* `domain_type` - тип домена;
* `domain_name` - имя домена, из которого импортирован пользователь;
* `ldap_guid` - уникальный идентификатор объекта AD;
* `phone_number` - номер телефона пользователя;
* `comment` - комментарий.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление пользователя</summary>

```
DELETE /user_backend/users/<id>
```

* `id` - уникальный идентификатор пользователя.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Запрет удаленного подключения для пользователя</summary>

```
PATCH /user_backend/users/<id>/disable-vpn
```

* `id` - уникальный идентификатор пользователя.

**Тело запроса пустое**

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Создание пользователя</summary>

```
POST /user_backend/users
```

**Json-тело запроса:**
```
{
    "name": str,
    "login": str,
    "psw": str,
    "parent_id": int,
    "phone_number": Optional[str],
    "comment": str
}
```

* `name` - имя пользователя;
* `login` - логин пользователя;
* `psw` - пароль пользователя;
* `parent_id` - id-группы;
* `phone_number` - номер телефона пользователя;
* `comment` - комментарий.

**Ответ на успешный запрос:**

```
{
    'id': int
}
```

* `id` - идентификатор добавленного пользователя.

**Если пользователь с указанным логином или именем существует, то исключение с описанием ошибки**
</details>

<details>
<summary>Создание группы</summary>

```
POST /user_backend/groups
```

**Json-тело запроса:**
```
{
    "name": str,
    "parent_id": int
}
```

* `name` - имя группы;
* `parent_id` - id-группы;


**Ответ на успешный запрос:**

```
{
    'id': int
}
```

* `id` - идентификатор добавленной группы.


Если группа с указанным именем у указанного предка существует, то код ответа 542 c описанием ошибки

</details>


<details>
<summary>Получение групп</summary>

```
GET /user_backend/groups
```

**Ответ на успешный запрос:**

```
[
    {
        "id": int,
        "name": str,
        "parent_id": int,
        "domain_type": str,
        "domain_name": str,
        "ldap_guid": str
    }
]
```

* `id` - id группы;
* `name` - имя группы;
* `parent_id` - id родительской группы;
* `domain_type` - тип домена;
* `domain_name` - имя домена, из которого импортирована группа;
* `ldap_guid` - уникальный идентификатор объекта AD.

</details>

<details>
<summary>Изменение группы</summary>

```
PUT /user_backend/groups/<id>
```

**Json-тело запроса:**
```
{
    "name": str,
    "parent_id": int,
    "domain_type": str,
    "domain_name": str,
    "ldap_guid": str
}
```

* `name` - имя группы;
* `parent_id` - id родительской группы;
* `domain_type` - тип домена;
* `domain_name` - имя домена, из которого импортирована группа;
* `ldap_guid` - уникальный идентификатор объекта AD.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление группы</summary>

```
DELETE /user_backend/groups/<id>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Смена пароля пользователя</summary>

```
PUT /user_backend/change_password/<id>
```


**Json-тело запроса:**

```
{
    "password": str
}
```

* `id` - идентификатор пользователя.
* `password` - новый пароль пользователя, не может быть пустым.

**Ответ на успешный запрос:** 200 ОК

</details>



