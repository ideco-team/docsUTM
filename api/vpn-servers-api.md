# Управление VPN

<details>
<summary>Статус VPN-сервера</summary>

```
GET /vpn_servers/status
```

**Ответ на успешный запрос:**

```json5
{
    "name": "string",
    "status": "string",
    "msg": ["string"]
}
```

* `name` - доменное имя;
* `status` - статус домена;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

## Настрока VPN-подключения по PPTP, SSTP

<details>
<summary>Получение настроек</summary>

```
GET /vpn_servers/settings
```

**Ответ на успешный запрос:**

```json5
{
  "pptp_enabled": "boolean",
  "sstp": {
      "enabled": "boolean",
      "domain": "string",
      "port": "integer"
  },
  "network": "string",
  "zone": "string|null",
  "dns_suffix": "string"
}
```

* `pptp_enabled` - включен/выключен сервер PPTP;
* `sstp` - настройки сервера SSTP:
  * `enabled` - включен/выключен сервер SSTP;
  * `domain` - доменное имя, присвоенное внешнему интерфейсу. Если домен еще не задан, то `null`;
  * `port` - порт для подключения, одно из предустановленных значений:
    * 1443;
    * 2443;
    * 3443;
    * 4443.
* `network` - сеть, из которой VPN-серверы раздают адреса. Первый адрес в этой сети - всегда адрес самого сервера;
* `zone` - зона для Lvpn0-интерфейса. Если зона не назначена, то `null`;
* `dns_suffix` - DNS-суффикс, передаваемый в Ideco Client. Если не назначен, то может быть пустой строкой.

</details>


<details>
<summary>Изменение настроек</summary>

```
PUT /vpn_servers/settings
```

**Json-тело запроса:**

```json5
{
  "pptp_enabled": "boolean",
  "sstp": {
      "enabled": "boolean",
      "domain": "string",
      "port": "integer"
  },
  "network": "string",
  "zone": "string|null",
  "dns_suffix": "string"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

## Скрипт для подключения пользователей по SSTP

<details>
<summary>Проверка возможности сгенерировать скрипт</summary>

```
GET /vpn_servers/powershell/status
```

**Ответ на успешный запрос:**

```json5
{
  "sstp_available": "bool",
}
```

</details>

<details>
<summary>Создание скрипта</summary>

```
GET /vpn_servers/powershell/sstp
```

**Ответ на успешный запрос:** создается cкрипт для подключения пользователей по SSTP. В ответе отображается заголовок `Content-Disposition: attachment; filename=\"Ideco_NGFW_VPN_SSTP.ps1`

</details>

## Управление правилами доступа к VPN

<details>
<summary>Получение списка правил</summary>

```
GET /vpn_servers/access_rules
```

**Ответ на успешный запрос:**

```json5
{
  "id": "integer",
  "enabled": "boolean",
  "title": "string",
  "sources": [ "string" ],
  "objects": [ "string" ],
  "vpns": [ "string" ],
  "action": "allow|deny",
  "two_factor": "smsaero|totp|multifactor|not_required",
  "comment": "string"
}
```

* `id` - уникальный идентификатор правила;
* `enabled` - статус правила: включено/выключено;
* `title` - название правила, может быть пустым, но не должно превышать 42 символов;
* `sources` - список источников подключения (не может быть пустым), допустимые типы:
  * `any` - любой источник подключения (если указан алиас `any`, то других алиасов в списке быть не должно);
  * `ip.id` - IP-адрес;
  * `ip_range.id` - диапазон IP-адресов;
  * `subnet.id` - подсеть;
  * `ip_address_list.id` - список IP-адресов;
  * `list_of_iplists.id` - cписок стран;
  * `domain.id` - домен.
* `objects` - список объектов, для которых будут назначены адреса (не может быть пустым). Объекты могут быть следующими:
  * `any` - для любых объектов (если указан обьект `any`, то других объектов в списке быть не должно);
  * `user.id` - для пользователей;
  * `group.id` - для групп;
  * `security_group.guid` - для групп безопасности AD.
* `vpns` - список типов VPN (протоколов подключения), не может быть пустым. Допустимые варианты:
  * `any` - любой тип подключения (если указан `any`, то других типов VPN в списке быть не должно);
  * `pptp` - подключение по PPTP;
  * `l2tp` - подключение по L2TP;
  * `sstp` - подключение по SSTP;
  * `ikev2`- подключение по IKEv2;
  * `agent-vpn-ng` - подключение по Wireguard (Ideco Client).
* `action` - действие при совпадении источника, объекта и типа VPN, не может быть пустым, допустимые варианты:
  * `allow` - разрешить;
  * `deny` - запретить.
* `two_factor` - тип требуемой двухфакторной авторизации, не может быть пустым. Должен быть `not_required`, если в поле `action` выбран `deny`. Допустимые варианты:
  * `smsaero` - аутентификация при помощи вода кода из СМС;
  * `totp` - аутентификация сканированием QR-кода или использованием токена;
  * `multifactor` - аутентификация подтверждением личности в стороннем приложении;
  * `not_required` - означает, что двухфакторная авторизация не требуется.
* `comment` - комментарий, может быть пустым, но не должен превышать 256 символов.

</details>

<details>
<summary>Добавление правил</summary>

```
POST /vpn_servers/access_rules?anchor_item_id={int}&insert_after={true|false}
```

Параметры запроса:
* `anchor_item_id` - уникальный идентификатор правила, ниже или выше которого необходимо создать новое правило. Если параметр не указан, то правило будет создано в конце списка;
* `insert_after` - указывает, куда необходимо вставить новое правило. Если параметр не указан или равен `true`, то новое правило будет добавлено сразу после правила с указанным идентификатором. Если параметр равен `false`, то новое правило заменит правило с указанным идентификатором.

**Json-тело запроса:**

```json5
{
  "enabled": "boolean",
  "title": "string",
  "sources": [ "string" ],
  "objects": [ "string" ],
  "vpns": [ "string" ],
  "action": "allow|deny",
  "two_factor": "smsaero|totp|multifactor|not_required",
  "comment": "string"
}
```

**Ответ на успешный запрос:**

```json5
{
   "id": "integer",
}
```

* `id` - уникальный идентификатор добавленного правила.

</details>

<details>
<summary>Редактирование правил</summary>

```
PATCH /vpn_servers/access_rules/{id}
```

* `id` - уникальный идентификатор изменяемого правила.

**Json-тело запроса:**

```json5
{
  "enabled": "boolean",
  "title": "string",
  "sources": [ "string" ],
  "objects": [ "string" ],
  "vpns": [ "string" ],
  "action": "allow|deny",
  "two_factor": "smsaero|totp|multifactor|not_required",
  "comment": "string"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правил</summary>

```
DELETE /vpn_servers/access_rules/{id}
```

* `id` - уникальный идентификатор удаляемого правила.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Изменение порядка правил</summary>

```
PATCH /vpn_servers/access_rules/{id}/position
```

* `id` - уникальный идентификатор перемещаемого правила.

**Json-тело запроса:**

```json5
{
   "direction": "up|down",
}
```

* `direction` - направление сдвига строки с правилом в таблице:
  * `up` - правило поднимается на одну позицию вверх;
  * `down` - правило опускается на одну позицию вниз.

**Ответ на успешный запрос:** 200 OK

</details>

## Управление правилами выдачи IP-адресов

<details>
<summary>Получение списка правил</summary>

```
GET /vpn_servers/lease_rules
```

**Ответ на успешный запрос:**

```json5
{
  "id": "integer",
  "title": "string",
  "objects": ["string"],
  "address": "string",
  "comment": "string",
  "enabled": "boolean"
}
```

* `id` - идентификатор правила получения адресов;
* `title` - название правила, может быть пустым, но не должно превышать 42 символов;
* `objects` - список объектов, для которых будут назначены адреса (не может быть пустым). Объекты могут быть следующими:
  * `any` - для любых объектов (если указан обьект `any`, то других объектов в списке быть не должно);
  * `user.id` - для пользователей;
  * `group.id` - для групп;
  * `security_group.guid` - для групп безопасности AD.
* `address` - IP-адрес, который будет назначен пользователю, или адрес сети, в которой ему будет выделен IP-адрес, если пользователь соответствует списку объектов. В строке может быть указан IP-адрес без маски или подсеть (значение не может быть пустым и не должно повторяться);
* `comment` - комментарий, может быть пустым, но не должен превышать 256 символов;
* `enabled` - статус правила: включено/выключено.

</details>

<details>
<summary>Добавление правил</summary>

```
POST /vpn_servers/lease_rules?anchor_item_id={int}&insert_after={true|false}
```

Параметры запроса:
* `anchor_item_id` - уникальный идентификатор правила, ниже или выше которого необходимо создать новое правило. Если параметр не указан, то правило будет создано в конце списка;
* `insert_after` - указывает, куда необходимо вставить новое правило. Если параметр не указан или равен `true`, то новое правило будет добавлено сразу после правила с указанным идентификатором. Если параметр равен `false`, то новое правило заменит правило с указанным идентификатором.

**Json-тело запроса:**

```json5
{
  "title": "string",
  "objects": ["string"],
  "address": "string",
  "comment": "string",
  "enabled": "boolean"
}
```

**Ответ на успешный запрос:**

```json5
{
   "id": "integer",
}
```

* `id` - уникальный идентификатор добавленного правила.

</details>

<details>
<summary>Редактирование правил</summary>

```
PATCH /vpn_servers/lease_rules/{id}
```

* `id` - уникальный идентификатор изменяемого правила.

**Json-тело запроса:**

```json5
{
  "title": "string",
  "objects": ["string"],
  "address": "string",
  "comment": "string",
  "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правил</summary>

```
DELETE /vpn_servers/lease_rules/{id}
```

* `id` - уникальный идентификатор удаляемого правила.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Изменение порядка правил</summary>

```
PATCH /vpn_servers/lease_rules/{id}/position
```

* `id` - уникальный идентификатор перемещаемого правила.

**Json-тело запроса:**

```json5
{
   "direction": "up|down",
}
```

* `direction` - направление сдвига строки с правилом в таблице:
  * `up` - правило поднимается на одну позицию вверх;
  * `down` - правило опускается на одну позицию вниз.

**Ответ на успешный запрос:** 200 OK

</details>

## Работа с таблицей VPN

<details>
<summary>Получение типов VPN, используемых в таблице Доступ по VPN</summary>

```
GET /vpn_servers/vpns_in_access_rules
```

**Ответ на успешный запрос:**

```json5
{
   "pptp": "boolean",
   "l2tp": "boolean",
   "sstp": "boolean",
   "ikev2": "boolean",
   "agent-vpn-ng": "boolean",
}
```

Значение по ключу `boolean` указывает, используется ли этот тип в таблице VPN.

</details>

<details>
<summary>Получение типов двуфакторной авторизации, используемых в таблице Доступ по VPN</summary>

```
GET /vpn_servers/two_factor_in_access_rules
```

**Ответ на успешный запрос:**

```json5
{
   "smsaero": "boolean",
   "totp": "boolean",
   "multifactor": "boolean"
}
```

Значение по ключу `boolean` указывает, используется ли этот тип в таблице VPN.

</details>

<details>
<summary>Получение списка правил доступа к VPN для конкретного пользователя</summary>

```
GET /vpn_servers/user_access_rules/{id}
```

* `id` - уникальный идентификатор пользователя.

**Ответ на успешный запрос:**

```json5
{
  "id": "integer",
  "enabled": "boolean",
  "title": "string",
  "sources": [ "string" ],
  "objects": [ "string" ],
  "vpns": [ "string" ],
  "action": "allow|deny",
  "two_factor": "smsaero|totp|multifactor|not_required",
  "comment": "string"
}
```

 Для несуществующего пользователя или пользователя, для которого нельзя получить полный список групп, возвращается пустой список правил.

</details>

## DHCP-сервер

<details>
<summary>Получение настроек</summary>

```
GET /vpn_servers/dhcp
```

**Ответ на успешный запрос:**

```json5
{
  "mode": "all|utm|local|none|custom",
  "networks": ["string"],
  "excluded_networks": ["string"]
}
```

* `mode` - режим раздачи маршрутов:
  * `all` - направляем весь трафик на NGFW (маршрут 0.0.0.0/0);
  * `utm` - раздаем маршруты до локальных и внутренних сетей NGFW;
  * `local` - раздаем маршруты только до локальных сетей NGFW;
  * `none` - не раздаем маршруты;
  * `custom` - раздаем только маршруты до указанных подсетей.
* `networks` - список подсетей, маршруты до которых передаются в режиме custom. Допустимы алиасы подсетей, IP-адресов, доменов;
* `excluded_networks` - список подсетей, маршруты до которых исключаются в любом режиме. Допустимы алиасы подсетей, IP-адресов, доменов.

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /vpn_servers/dhcp
```

**Json-тело запроса:**

```json5
{
  "mode": "all|utm|local|none|custom",
  "networks": ["string"],
  "excluded_networks": ["string"]
}
```

**Ответ на успешный запрос:** 200 OK

</details>