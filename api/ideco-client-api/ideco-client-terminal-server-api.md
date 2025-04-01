# Терминальные сервера Ideco Client

## Управление терминальными серверами Ideco Client

<details>
<summary>Получение списка терминальных серверов</summary>

```
GET /agent_backend/agent-server/terminal-servers
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string",
    "device": "string",
    "network": "string",
    "comment": "string",
    "enabled": "boolean"
  },
  ...
]
```

* `id` - уникальный идентификатор сервера;
* `title` - название сервера, максимальная длина - 42 символа;
* `device` - индентификатор пользователя с типом `device` (подключенного по Device VPN), например, `user.id.33`;
* `network` - подсеть терминального сервера, минимум - `/30`. Значение должно быть уникальным для сервера;
* `comment` - комментарий, максимальная длина 256 символов;
* `enabled` - состояние сервера:
  * `true` - включен;
  * `false` - выключен.

</details>

<details>
<summary>Добавление терминального сервера</summary>

```
POST /agent_backend/agent-server/terminal-servers
```

**Json-тело запроса:**

```json5
{
  "title": "string",
  "device": "string",
  "network": "string",
  "comment": "string",
  "enabled": "boolean",
}
```

* `title` - название сервера, максимальная длина - 42 символа;
* `device` - индентификатор пользователя с типом `device` (подключенного по Device VPN), например, `user.id.33`;
* `network` - подсеть терминального сервера, минимум - `/30`. Значение должно быть уникальным для сервера;
* `comment` - комментарий, максимальная длина 256 символов;
* `enabled` - состояние сервера:
  * `true` - включен;
  * `false` - выключен.

**Ответ на успешный запрос:**

```json5
{
    "id" : "string"
}
```

* `id` - уникальный идентификатор созданного сервера.

</details>

<details>
<summary>Обновление терминального сервера</summary>

```
PATCH /agent_backend/agent-server/terminal-servers/<id терминального осервера>
```

**Ответ на успешный запрос:**
Введите только те поля, которые необходимо отредактировать:

```json5
[
  {
    "title": "string",
    "device": "string",
    "network": "string",
    "comment": "string",
    "enabled": "boolean",
  },
  ...
]
```

* `title` - название сервера, максимальная длина - 42 символа;
* `device` - индентификатор пользователя с типом `device` (подключенного по Device VPN), например, `user.id.33`;
* `network` - подсеть терминального сервера, минимум - `/30`. Значение должно быть уникальным для сервера;
* `comment` - комментарий, максимальная длина 256 символов;
* `enabled` - состояние сервера:
  * `true` - включен;
  * `false` - выключен.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление терминального сервера</summary>

```
DELETE /agent_backend/agent-server/terminal-servers/<id терминального осервера>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Протокол подключения и авторизации терминального сервера

Процесс подключения и авторизации должен проходить в несколько этапов обмена сообщениями:

<details>
<summary>1. Подключение и запрос соответствия версии Ideco Client</summary>

Аналогичен процессу подключения и запроса соответсвия версии [Ideco Client](ideco-client-api.md).

</details>

<details>
<summary>2. Авторизация терминального сервера (Windows)</summary>

**Json-тело запроса:**

```json5
{
  "type": "authorize_win_terminal_server"
}
```

* `type` - тип команды: `authorize_win_terminal_server` - запрос на авторизацию терминального сервера.

**Ответ на успешный запрос:**

```json5
{
  "type": "auth_state",
  "authorized": "boolean",
  "connection_type": "string",
  "timeout": "integer",
  "message": "string",
  "welcome_url": "string"
}
```

* `type` - тип ответа: `auth_state` - состояние авторизации сервера;
* `authorized` - состояние авторизации:
  * `true` - авторизован;
  * `false` - не авторизован.
* `connection_type` - тип подключения. Для терминального агента возможно только значение `agent_udp`.
* `timeout` - время до повторной попытки авторизации (в секундах), если возникли ошибки в процессе авторизации. Если повторная попытка авторизации не требуется, то значение - `0`;
* `message` - сообщение о состоянии авторизации;
* `welcome_url` - URL, который должен быть открыт в браузере на пользовательском устройстве, если пользователь авторизован и сессия авторизации была заблокирована в ожидании прохождения 2FA (Мультифактор). В противном случае - пустая строка.
  
</details>

<details>
<summary>3. Настройка туннеля</summary>

**Json-тело запроса:**

```json5
{
  "type": "tunnel_wg",
  "public_key": "string"
}
```

* `type` - тип команды: `tunnel_wg` - запрос установки туннеля;
* `public_key` - публичный ключ сервера.

**Ответ на успешный запрос:**

```json5
{
  "type": "tunnel_wg",
  "server_port": "integer",
  "public_key": "string",
  "client_tunnel_ipv4": "string",
  "user_tunnel_ipv4_network": "string",
  "dns_ipv4": "string",
  "forward_nets": [ "string" ],
  "dns_suffix": "string"
}
```

* `type` - тип ответа: `tunnel_wg` - настройки туннеля;
* `server_port` - порт сервера, через который устанавливается туннель;
* `public_key` - публичный ключ клиента;
* `client_tunnel_ipv4` - IPv4-адрес и маска туннеля на стороне терминального сервера;
* `user_tunnel_ipv4_network` - подсеть для виртуализации пользователей;
* `dns_ipv4` - IPv4-адрес DNS-сервера, используемого в туннеле;
* `forward_nets` - массив подсетей, трафик к которым пересылается через туннель;
* `dns_suffix` - доменный суффикс.
  
</details>

<details>
<summary>4. Авторизация пользователей терминального сервера (Windows)</summary>

**Json-тело запроса:**

```json5
{
  "type": "authorize_win_terminal_user",
  "term_server_id": "string",
  "user_name": "string",
  "user_domain": "string",
  "user_uuid": "string"
}
```

* `type` - тип команды: `authorize_win_terminal_user` - запрос на авторизацию пользователя терминального сервера;
* `term_server_id` - идентификатор терминального сервера;
* `user_name` - логин пользователя;
* `user_domain` - домен пользователя;
* `user_uuid` - идентификатор пользователя.

**Ответ на успешный запрос:**

```json5
{
  "type": "term_user_auth_state",
  "authorized": "boolean",
  "user_name": "string",
  "user_domain": "string",
  "user_uuid": "string",
  "term_user_tunnel_ipv4": "string"
}
```

* `type` - тип ответа: `term_user_auth_state` - состояние авторизации пользователя терминального сервера;
* `authorized` - состояние авторизации:
  * `true` - авторизован;
  * `false` - не авторизован.
  * `user_name` - логин пользователя;
* `user_domain` - домен пользователя;
* `user_uuid` - идентификатор пользователя;
* `term_user_tunnel_ipv4` - IP-адрес пользователя.
  
</details>

## Разавторизация пользователей и терминального сервера

<details>
<summary>Разавторизация пользователей терминального сервера (Windows)</summary>

**Json-тело запроса:**

```json5
{
  "type": "unauthorize_win_terminal_user",
  "term_server_id": "string",
  "user_name": "string",
  "user_domain": "string",
  "user_uuid": "string"
}
```

* `type` - тип команды: `unauthorize_win_terminal_user` - запрос на разавторизацию пользователя терминального сервера;
* `term_server_id` - идентификатор терминального сервера;
* `user_name` - логин пользователя;
* `user_domain` - домен пользователя;
* `user_uuid` - идентификатор пользователя.

**Ответ на успешный запрос:**

```json5
{
  "type": "term_user_auth_state",
  "authorized": "boolean",
  "user_name": "string",
  "user_domain": "string",
  "user_uuid": "string"
}
```

* `type` - тип ответа: `term_user_auth_state` - состояние авторизации пользователя терминального сервера;  
* `authorized` - состояние авторизации:
  * `true` - авторизован;
  * `false` - не авторизован.
* `user_name` - логин пользователя;
* `user_domain` - домен пользователя;
* `user_uuid` - идентификатор пользователя.

</details>

<details>
<summary>Разавторизация терминального сервера</summary>

**Json-тело запроса:**

```json5
{
  "type": "unauthorize"
}
```

* `type` - тип команды: `unauthorize` - запрос на разавторизацию терминального сервера.

**Ответ на успешный запрос:**

```json5
{
  "type": "auth_state",
  "authorized": "boolean",
  "need_tunnel": "boolean",
  "timeout": "integer",
  "message": "string",
  "welcome_url": "string"
}
```

* `type` - тип ответа: `auth_state` - состояние авторизации терминального сервера;
* `authorized` - состояние авторизации:
  * `true` - авторизован;
  * `false` - не авторизован.
* `need_tunnel` - требуется ли установить туннель:
  * `true` - требуется;
  * `false` - не требуется.
* `timeout` - время до повторной попытки авторизации (в секундах), если возникли ошибки в процессе авторизации. Если повторная попытка авторизации не требуется, то значение - `0`;
* `message` - сообщение о состоянии авторизации;
* `welcome_url` - URL, который должен быть открыт в браузере на пользовательском устройстве, если пользователь авторизован и сессия авторизации была заблокирована в ожидании прохождения 2FA (Мультифактор). В противном случае - пустая строка.

</details>