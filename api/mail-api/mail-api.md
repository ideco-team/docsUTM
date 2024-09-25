# Управление Почтовым релеем

<details>
<summary>Получение статуса почтовых служб</summary>

`GET /mail/settings/general/status`

**Ответ на успешный запрос:**

```json5
[
  {
    "name": "string",
    "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
    "msg": [
      "string",
      ...
    ]
  },
  ...
]
```

* `name` - имя демона;
* `status` - одна из строк, означающих состояние демона;
* `msg` - массив строк с сообщениями об ошибках, если ошибки есть.

</details>

## Основные настройки

<details>
<summary>Получение настроек почтового сервера</summary>

`GET /mail/settings/general`

**Ответ на успешный запрос:**

```json5
{
  "mail_domain": "string" | "null",
  "mail_hostname": "string",
  "mail_additional_domains": [
    "string",
    ...
  ],
  "mail_relay_domains": [
    "string",
    ...
  ]
}
```

* `mail_domain` - основной почтовый домен. Если не настроен - `null`;
* `mail_hostname` - имя хоста почтового сервера. Если не настроено - `null`;
* `mail_additional_domains` - массив дополнительных почтовых доменов. Если не настроены - пустой массив;
* `mail_relay_domains` - массив relay-доменов. Если не настроены - пустой массив. Каждый элемент массива имеет вид `from_domain|to_domain`, где:
  * `from_domain` - валидное доменное имя;
  * `to_domain` - валидное доменное имя или IP-адрес.

</details>

<details>
<summary>Сохранение настроек почтового сервера</summary>

`PUT /mail/settings/general`

**Json-тело запроса:**

```json5
{
  "mail_domain": "string",
  "mail_hostname": "string",
  "mail_additional_domains": [
    "string",
    ...
  ],
  "mail_relay_domains": [
    "string",
    ...
  ]
}
```

* `mail_domain` - основной почтовый домен. Если не настроен - `null`. Не может быть пустым;
* `mail_hostname` - имя хоста почтового сервера. Если не настроено - `null`. Не может быть пустым;
* `mail_additional_domains` - массив дополнительных почтовых доменов. Каждый элемент массива должен быть валидным доменным именем и не может быть пустой строкой или `null`. Может быть пустым;
* `mail_relay_domains` - массив relay-доменов. Может быть пустым. Каждый элемент массива должен иметь вид `from_domain|to_domain`, где:
  * `from_domain` - валидное доменное имя, не может быть пустой строкой или `null`;
  * `to_domain` - валидное доменное имя или IP-адрес, не может быть пустой строкой или `null`.

**Ответ на успешный запрос:** 200 ОК

</details>

## Настройки IMAP(S), POP3(S), Web-почты

<details>
<summary>Получение настроек</summary>

`GET /mail/settings/general/server_access`

**Ответ на успешный запрос:**

```json5
{
  "imap_enabled": "boolean",
  "pop3_enabled": "boolean",
  "webmail_enabled": "boolean"
}
```

* `imap_enabled` - `true`, когда IMAP включен, и `false`, когда выключен;
* `pop3_enabled` - `true`, когда POP3 включен, и `false`, когда выключен;
* `webmail_enabled` - `true`, когда интерфейс веб-почты включен, и `false`, когда выключен.

</details>

<details>
<summary>Изменение настроек</summary>

`PATCH /mail/settings/general/server_access`

**Json-тело запроса (все или некоторые поля):**

```json5
{
  "imap_enabled": "boolean",
  "pop3_enabled": "boolean",
  "webmail_enabled": "boolean"
}
```

* `imap_enabled` - `true`, когда IMAP включен, и `false`, когда выключен;
* `pop3_enabled` - `true`, когда POP3 включен, и `false`, когда выключен;
* `webmail_enabled` - `true`, когда интерфейс веб-почты включен, и `false`, когда выключен.

**Ответ на успешный запрос:** 200 ОК

</details>

## Внешний диск для хранения почты

<details>
<summary>Получение списка доступных дисков</summary>

`GET /mail/settings/general/ext_hdd/list`

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string"
  },
  ...
]
```

* `id` - идентификатор диска;
* `title` - название.

</details>

<details>
<summary>Подключение диска</summary>

`POST /mail/settings/general/ext_hdd`

**Json-тело запроса:**

```json5
{
  "id": "string"
}
```

* `id` - идентификатор диска.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение текущего состояния диска для хранения почты</summary>

`GET /mail/settings/general/ext_hdd`

**Ответ на успешный запрос:**

```json5
{
  "disk_id": "string" | "null",
  "title": "string" | "null",
  "status": "connecting" | "connected" | "disconnected" | "error" | "check",
  "fs_uuid": "string" | "null",
  "free_size": "integer" | "null",
  "total_size": "integer" | "null",
  "error": "string" | "null"
}
```

* `disk_id` - идентификатор диска. Может быть `null`, если диск не подключен;
* `title` - название диска. Может быть `null`, если диск не подключен;
* `fs_uuid` - идентификатор файловой системы. Может быть `null`, если диск не подключен;
* `status` - текущее состояние диска:
    * `connecting`- диск в процессе монтирования;
    * `connected`- диск подключен и работает нормально;
    * `disconnected`: диск не подключен;
    * `error`- при подключении диска произошла ошибка;
    * `check`- проверка формата почтовых ящиков.
* `free_size` - количество свободного места, байт. Может быть `null`, если диск не подключен;
* `total_size` - размер диска, байт. Может быть `null`, если диск не подключен;
* `error` - текст ошибки, если текущее состояние диска - `error`, иначе - `null`.

</details>

<details>
<summary>Отключение диска</summary>

`DELETE /mail/settings/general/ext_hdd`

**Ответ на успешный запрос:** 200 ОК

</details>

## Включенность почтового сервера

<details>
<summary>Получение настроек</summary>

`GET /mail/settings/general/state`

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - опция раздела **Основные настройки**: `true` - включена, `false` - выключена.

</details>

<details>
<summary>Включение/отключение почтового сервера</summary>

`PUT /mail/settings/general/state`

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - опция раздела **Основные настройки**: `true` - включена, `false` - выключена.

**Ответ на успешный запрос:** 200 ОК

</details>