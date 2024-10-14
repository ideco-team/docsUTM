# Управление администраторами

## Управление локальными администраторами

<details>
<summary>Получение списка локальных администраторов</summary>

```
GET /web/admins/local?format_type=JSON|CSV&columns=["id","name", ...]
```

* `format_type` - поддерживается `CSV` и `JSON`, по умолчанию `JSON`;
* `columns` - список столбцов, которые попадут в `CSV` отчет, по умолчанию пустой список.

Список `columns` состоит из столбцов (значения столбцов описаны ниже):

* `id`
* `name`
* `enabled`
* `login`
* `role`
* `comment`
* `password_timestamp`

**Ответ на успешный запрос в формате JSON:**

```json5
[
    {
        "id": "string",
        "enabled": "boolean",
        "name": "string",
        "login": "string",
        "role": "string",
        "comment": "string",
        "password_timestamp": "integer"
    },
    ...
]
```

**Ответ на успешный запрос в формате CSV:**

```
id,name,enabled,login,role,comment,password_timestamp
8aa49b1f-5711-4e5e-ab66-4828c6785b84,Administrator,True,administrator,predefined_admin_write,Создано через cloud-init.,1724047828
8aa49b1f-5711-4e5e-ab66-4828c6785b92,Admin,True,administrator,predefined_admin_write,Главный администратор,1724047850
```

* `id` - идентификатор администратора;
* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя администратора;
* `login` - логин администратора;
* `role` - идентификатор уровня доступа администратора;
* `comment` - комментарий;
* `password_timestamp` - время последнего успешного изменения пароля.

</details>

<details>
<summary>Добавление локального администратора</summary>

```
POST /web/admins/local
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "name": "string",
    "login": "string",
    "password": "string",
    "role": "string",
    "comment": "string"
}
```

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя, ненулевое текстовое поле, длина от 1 до 42 символов;
* `login` - логин не должен содержать `.` (одну точку) или `..` (две точки), а также символов [\\:/~$!\s@]. Длина поля от 1 до 42 символов включительно;
* `password` - пароль, ненулевое текстовое поле, длина от 10 до 42 символов;
* `role` - идентификатор уровня доступа аккаунта:
    * `predefined_admin_write` - администратор (полный доступ к настройке);
    * `predefined_admin_readonly` - только просмотр;
    * `predefined_reports_view` - просмотр отчетов;
    * `predefined_reports_change` - создание отчетов (доступно создание шаблонов, расписание отправки и просмотр отчетов);
    * `predefined_security_admin` - администратор информационной безопасности (работа с событиями безопасности);
    * `predefined_firewall_admin` - администратор файрвола (создание учетный записей, работа с правилами фильтрации, управление режимами работы файрвола);
    * `predefined_access_settings_admin` - администратор настройки доступов (настройки сетевого взаимодействии пользователей файрвола, субъектов доступа, информационных систем).
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор администратора.

</details>

<details>
<summary>Изменение настроек и пароля локального администратора</summary>

```
PATCH /web/admins/local/<id администратора>
```

**Json-тело запроса:**

Все поля необязательные

```json5
{
    "enabled": "boolean",
    "name": "string",
    "login": "string",
    "password": "string",
    "role": "string",
    "comment": "string"
}
```

**Ответ на успешный запрос:** 200 ОК

* `enabled` - аккаунт включен/выключен (можно/нельзя под ним зайти в систему);
* `name` - имя администратора;
* `login` - логин администратора;
* `password` - пароль (если значение `null`, пароль останется прежним);
* `role` - идентификатор уровня доступа аккаунта;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

**При смене пароля или отключении аккаунта веб-сессии удаляются.**

</details>

<details>
<summary>Удаление локального администратора</summary>

**Последнего локального администратора удалять нельзя!**

```
DELETE /web/admins/local/<id администратора>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Управление сессиями

<details>
<summary>Получение списка сессий</summary>

```
GET /monitor_backend/admin_sessions
```

**Ответ на успешный запрос:**

```json5
[
   {
    "id": "string",
    "login": "string",
    "name": "string",
    "competence": [ "string" ],
    "role_id": "string",
    "role_name": "string",
    "domain_name": "string",
    "ip": "string",
    "auth_type": "string",
    "auth_rule_id": "string",
    "admin_id": "string",
    "login_timestamp": "integer",
    "country_code": "string"
    }
]
```

* `id` - идентификатор сессии администратора;
* `login` - логин администратора;
* `name` - имя администратора;
* `competence` - список доступных администратору компетенций (`admin_write` - редактирование, `admin_read` - чтение, `allow_terminal` - доступ к терминалу, `reports_view` - просмотр отчетов, `reports_change` - изменение отчетов);
* `role_id` - идентификатор уровня доступа аккаунта;
* `role_name` - название уровня доступа аккаунта;
* `domain_name` - домен, в котором находится авторизованный администратор (пустое значение, если `auth_type` не равен `ad` или `ald`);
* `ip` - IP-адрес, с которого авторизовался администратор;
* `auth_type` - тип авторизации администратора (`ad`, `ald`, `local`, `radius`);
* `auth_rule_id` - идентификатор правила, по которому авторизовался администратор;
* `admin_id` - идентификатор администратора;
* `login_timestamp` - время момента успешной авторизации администратора (число в формате `YYYYMMDDhhmmss`).
* `country_code` - код страны источника подключения. Пустая строка, если страну не удалось определить.

</details>

<details>
<summary>Удаление сессии</summary>

```
DELETE /monitor_backend/admin_sessions/<id сессии авторизации администратора>
```

**Ответ на успешный запрос:** 200 ОК

</details>