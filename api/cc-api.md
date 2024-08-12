  # Центральная консоль

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

## Настройки Центральной консоли в Ideco NGFW

<details>
<summary>Получение настроек Ideco Center</summary>

```
GET /central_console/settings
```

**Ответ на успешный запрос:**

```json5
{
    "cc_server": "string" | "null",
    "last_connect": "integer" | "null",
    "last_sync": "integer" | "null",
    "root_ca": "string" | "null"
}
```

* `cc_server` - доменное имя или IP-адрес центральной консоли;
* `last_connect` - timestamp последней успешной синхронизации данных;
* `last_sync` - timestamp;
* `root_ca` - корневой сертификат в формате PEM.

</details>

<details>
<summary>Изменение настроек Ideco Center</summary>

```
PATCH /central_console/settings
```

**Json-тело запроса:**

```json5
{
    "cc_server": "string" | "null"
}
```
</details>

<details>
<summary>Загрузка корневого сертификата Ideco Center на NGFW</summary>

```
POST /central_console/root_ca
```

В тело запроса поместите содержимое корневого сертификата, скачанного в Ideco Center. Для этого откройте сертификат в текстовом редакторе и скопируйте текст.

</details>

<details>
<summary>Удаление корневого сертификата Ideco Center</summary>

```
DELETE /central_console/root_ca
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Отключение NGFW от Ideco Center</summary>

```
DELETE /central_console/settings
```

**Ответ на успешный запрос:** 200 ОК

</details>

## API Ideco Center

<details>
<summary>Получение статуса службы</summary>

```
GET /servers/status
```

**Ответ на успешный запрос:**

```json5
{
    "name": "string",
    "status": "active | activating | deactivating | failed | inactive | reloading",
    "msg": ["string"]
}
```

* `name` - название службы;
* `status` - текущее состояние службы;
* `msg` - список строк, описывающих состояние службы.

</details>

### Общие настройки

<details>
<summary>Получение общих настроек</summary>

```
GET /servers/setting
```

**Ответ на успешный запрос:** 

```json5
{
    "domain": "string" | "null"
}
```

* `domain` - внешний адрес Ideco Center (IP-адрес или доменное имя).

</details>

<details>
<summary>Изменение общих настроек</summary>

```
PUT /servers/setting
```

**Json-тело запроса:**

```json5
{
    "domain": "string" | "null"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение настройки включенности синхронизации правил</summary>

```
GET /servers/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

</details>

<details>
<summary>Включение/выключение синхронизации правил</summary>

```
PUT /servers/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

### Группировка серверов

<details>
<summary>Получение списка групп серверов в Ideco Center</summary>

```
GET /servers/groups
```

**Пример ответа на успешный запрос:**

```json5
[
    {
        "comment": "",
        "name": "Группа 1",
        "parent_id": "f3ffde22-a562-4f43-ac04-c40fcec6a88c",
        "id": "e37ec0bb-fc27-406f-bd24-d0e89200561d"
    },
  ...
    {
        "comment": "",
        "name": "Корневая группа",
        "parent_id": null,
        "id": "f3ffde22-a562-4f43-ac04-c40fcec6a88c"
    }
]
```

* `id` - идентификатор группы;
* `comment` - комментарий, может быть пустым;
* `name` - название группы серверов;
* `parent_id` - идентификатор родительской группы серверов.

</details>

<details>
<summary>Создание группы серверов</summary>

```
POST /servers/groups
```

**Json-тело запроса:**

```json5
{
    "comment": "string",
    "name": "string",
    "parent_id": "string"
}
```

* `name` - название группы;
* `parent_id` - идентификатор родительской группы (если группа входит в Корневую группу, ID Корневой группы);
* `comment` - комментарий, может быть пустым.

**Ответ на успешный запрос:**

```json5
{
    "id": "string" //(идентификатор созданной группы)
}
```

</details>

<details>
<summary>Редактирование группы серверов</summary>

```
PATCH /servers/groups/<id группы серверов>
```

**Json-тело запроса:**

```json5
{
    "comment": "string",
    "name": "string",
    "parent_id": "string"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление группы серверов</summary>

```
DELETE /servers/groups/<id группы серверов>
```

**Ответ на успешный запрос:** 200 OK

</details>

### Управление подключенными серверами

<details>
<summary>Получение списка подключенных серверов</summary>

```
GET /servers/servers
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "parent_id": "string",
        "version": {
          "major": "integer",
          "minor": "integer",
          "build": "integer",
          "timestamp": "integer",
          "vendor": "Ideco",
          "product": "UTM",
          "kind": "FSTEK" | "VPP" | "STANDARD" | "BPF",
          "release_type": "release" | "beta" | "devel"
    },
        "cl_tunnel_addr": "string",
        "title": "string",
        "approved": "bool",
        "last_sync": "int | null",
        "last_connect": "int",
        "utm_login_secret": "string",
        "comment": "string"
    },
    ...
]
```

* `id` - идентификатор сервера;
* `parent_id` - идентификатор группы, в которую входит сервер;
* `version` - версия сервера:
  * `major` -мажорный номер версии;
  * `minor` - минорный номер версии;
  * `build` - номер сборки;
  * `timestamp` - время выхода версии;
  * `vendor` - вендор ("Ideco");
  * `product` - код продукта;
  * `kind` - вид продукта;
  * `release_type` - тип релиза.
* `cl_tunnel_addr` - IPv6-адрес сервера внутри wireguard-туннеля;
* `title` - название сервера;
* `approved` - флаг, означающий, подтверждено ли подключение сервера в Ideco Center;
* `last_sync` - timestamp последней успешной синхронизации данных;
* `last_connect` - timestamp последнего успешного подключения;
* `utm_login_secret` - секретное значение для отправки в URL авторизации Ideco Center в Ideco NGFW;
* `version_diff` - разница мажорных версий Ideco Center и NGFW. Если значение равно нулю - мажор одинаковый, больше нуля - версия Ideco Center выше, меньше нуля - версия NGFW выше;
* `comment` - комментарий, максимум 255 символов, может быть пустым.

</details>

<details>
<summary>Перемещение подключенных серверов между группами/подтверждение подключения сервера к Ideco Center</summary>

```
PATCH /servers/servers/<id сервера>
```

**Json-тело запроса:**

```json5
{
    "parent_id": "string",
    "approved": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

При добавлении нового сервера ему автоматически присваивается parent_id Корневой группы.

После подтверждения подключения сервера (установки approved=true) менять это свойство нельзя (для удаления сервера вызывается метод DELETE)

</details>

<details>
<summary>Удаление сервера из Ideco Center</summary>

```
DELETE /servers/servers/<id сервера>
```

**Ответ на успешный запрос:** 200 OK

</details>

### Управление правилами трафика Ideco Center

#### Контент-фильтр

<details>
<summary>Получение списка категорий (предустановленных и пользовательских)</summary>

```
GET /content-filter/categories
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "type": "string",
        "name": "string",
        "comment": "string"
    },
    ...
]
```

* `id` - номер категории в формате `users.id.1` или `extended.id.1`.
* `type` - тип категории:
  * `users` - пользовательские категории;
  * `extended` - расширенные категории (SkyDNS);
  * `files` - категории для файлов;
  * `special` - специальные предопределенные категории:
    - Прямое обращение по IP;
    - Все категоризированные запросы;
    - Все некатегоризированные запросы;
    - Все запросы (категоризированные и некатегоризированные).
  * `other` - остальные категории.
* `name` - имя категории (для отображения пользователю);
* `comment` - описание категории (для отображения пользователю).

</details>

<details>
<summary>Получение списка пользовательских категорий</summary>

```
GET /content-filter/users_categories
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string", //(номер категории, вида - users.id.1)
        "name": "string", //(название категории, не пустая строка)
        "comment": "string",
        "urls": ["string"]
    },
    ...
]
```

* `"urls"` - список url. Либо полный путь до страницы, либо только доменное имя. В пути может присутствовать любое количество любых символов.

</details>

<details>

<summary>Создание пользовательской категории</summary>

```
POST /content-filter/users_categories
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

</details>

<details>

<summary>Редактирование пользовательских категорий</summary>

```
PUT /content-filter/users_categories/{category_id}
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": ["string"]
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

</details>

<details>
<summary>Получение списка правил</summary>

* `GET /content-filter/rules/before?groups=[UUID1,UUID2]` - начальные правила;
* `GET /content-filter/rules/after?groups=[UUID1,UUID2]` - конечные правила.
  * `UUID1` - идентификатор группы серверов в Центральной консоли (`id`).

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "integer",
        "parent_id": "string",
        "name": "string",
        "comment": "string",
        "aliases": [ "string" ],
        "categories": [ "string" ],
        "http_methods": ["string"],
        "content_types": ["string"],
        "access": "allow" | "deny" | "bump" | "redirect",
        "redirect_url": "string" | "null",
        "enabled": "boolean",
        "timetable": [ "string" ]
    },
    ...
]
```

* `id` - идентификатор правила;
* `parent_id` - идентификатор группы серверов, к которой применяется правило;
* `name` - название правила, не пустая строка;
* `comment` - комментарий (максимальная длина - 255 символов), может быть пустым;
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле, строка, может принимать три значения:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump`- расшифровать запрос;
  * `redirect`: перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled`: правило включено (true) или выключено (false);
* `timetable` - время действия.

</details>

<details>
<summary>Создание правил</summary>

* `POST /content-filter/rules/before?anchor_item_id=123&insert_after={true|false}` - создание начального правила;
* `POST /content-filter/rules/after?anchor_item_id=123&insert_after={true|false}` - создание конечного правила.

**Json-тело запроса:**

```json5
{
    "parent_id": "string", (идентификатор группы серверов, к которой будет применяться правило)
    "name": "string",
    "comment": "string",
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "http_methods": ["string"],
    "content_types": ["string"],
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | "null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `id` - идентификатор правила;
* `parent_id` - идентификатор родительской группы;
* `name` - название правила, не может быть пустым;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`;
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled` - правило включено (true) или выключено (false);
* `timetable` - время действия.


**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор созданного правила.

</details>

<details>
<summary>Редактирование правил</summary>

* `PATCH /content-filter/rules/before/<id правила>` - изменение начального правила;
* `PATCH /content-filter/rules/after/<id правила>` - изменение конечного правила.

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "parent_id": "string",
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "http_methods": ["string"],
    "content_types": ["string"],
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | "null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `id` - идентификатор правила;
* `parent_id` - идентификатор родительской группы;
* `name` - название правила, не может быть пустым;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`;
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled` - правило включено (true) или выключено (false);
* `timetable` - время действия, список идентификаторов алиасов.

**Ответ на успешный запрос:** 200 ОК

**Важно!** Чтобы переместить правило между группами серверов, измените его `parent_id`.

</details>

<details>
<summary>Перемещение правил</summary>

* `PATCH /content-filter/rules/before/move` - перемещение начального правила;
* `PATCH /content-filter/rules/after/move` - перемещение конечного правила.

**Json-тело запроса:**

```json5
{
    "params": {
      "id": "integer",
      "anchor_item_id": "integer",
      "insert_after": "boolean"
  }
}
```

* `id` - идентификатор перемещаемого правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно поместить перемещаемое правило;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление правила</summary>

* `DELETE /content-filter/rules/before/move` - перемещение начального правила;
* `DELETE /content-filter/rules/after/move` - перемещение конечного правила.

**Ответ на успешный запрос:** 200 ОК

</details>

#### Файрвол

<details>
<summary>Получение настроек Файрвола</summary>

```
GET /firewall/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
} 
```

* `enabled` - Опция раздела Файрвол включен (true) или
отключен (false).
</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /firewall/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}  
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение списка правил</summary>

* `GET /firewall/rules/forward/before?groups=[UUID1, UUID2]` - начальные правила раздела FORWARD;
* `GET /firewall/rules/forward/after?groups=[UUID1, UUID2]` - конечные правила раздела FORWARD;
* `GET /firewall/rules/input/before?groups=[UUID1, UUID2]` - начальные правила раздела INPUT;
* `GET /firewall/rules/input/after?groups=[UUID1, UUID2]` - конечные правила раздела INPUT.

**Ответ на успешный запрос:**

```json5
[
   "FilterRuleObject|DnatRuleObject|SnatRuleObject",
]
```

**Обьект FilterRuleObject**

```json5
{
  "id": "integer",
  "parent_id": "string",
  "enabled": "boolean",
  "protocol": "string",
  "source_addresses": [ "string" ],
  "source_addresses_negate": "boolean",
  "source_ports": [ "string" ],
  "incoming_interface": "string",
  "destination_addresses": [ "string" ],
  "destination_addresses_negate": "boolean",
  "destination_ports": [ "string" ],
  "outgoing_interface": "string",
  "hip_profiles": [ "string" ],
  "dpi_profile": "string",
  "dpi_enabled": "boolean",
  "ips_profile": "string",
  "ips_enabled": "boolean",
  "timetable": [ "string" ],
  "comment": "string",
  "action": "accept|drop"
}
```

* `id` - идентификатор правила.
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `enabled` - включено (true) или выключено (false) правило;
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `source_ports` - порты источников, список идентификаторов алиасов;
* `incoming_interface` - зона источника;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `outgoing_interface` - зона назначения;
* `hip_profiles` - HIP-профили;
* `dpi_profile` - строка в формате UUID, идентификатор профиля DPI. Не может быть пустой строкой, если `dpi_enabled` = `true`;
* `dpi_enabled` - включена/выключена обработка с помощью модуля **Контроль приложений**;
* `ips_profile` - строка в формате UUID, идентификатор профиля IPS. Не может быть пустой строкой, если `ips_enabled` = `true`;
* `ips_enabled` - включена/выключена обработка с помощью модуля **Предотвращение вторжений**;
* `timetable` - время действия;
* `comment` - комментарий (может быть пустым);
* `action` - действие:
  * `accept` - разрешить;
  * `drop` - запретить.

**Обьект DnatRuleObject**

```json5
{
   "id": "integer",
   "parent_id": "string",
   "enabled": "boolean",
   "protocol": "string",
   "source_addresses": [ "string" ],
   "source_addresses_negate": "boolean",
   "source_ports": [ "string" ],
   "incoming_interface": "string",
   "destination_addresses": [ "string" ],
   "destination_addresses_negate": "boolean",
   "destination_ports": [ "string" ],
   "timetable": [ "string" ],
   "comment": "string",
   "action": "accept | dnat",
   "change_destination_address": "null | string",
   "change_destination_port": "null | string"
}
```

* `action` - действие:
  * `accept` - разрешить;
  * `dnat` - производить DNAT.
* `change_destination_address` - IP-адрес или диапазон IP-адресов для замены назначения, или `null`, если `action` = `accept`;
* `change_destination_port` - порт или диапазон портов для замены значения, или `null`, если `action` = `accept`.

**Обьект SnatRuleObject**

```json5
{
   "id": "integer",
   "parent_id": "string",
   "enabled": "boolean",
   "protocol": "string",
   "source_addresses": [ "string" ],
   "source_addresses_negate": "boolean",
   "source_ports": [ "string" ],
   "destination_addresses": [ "string" ],
   "destination_addresses_negate": "boolean",
   "destination_ports": [ "string" ],
   "outgoing_interface": "string",
   "timetable": [ "string" ],
   "comment": "string",
   "action": "accept | snat",
   "change_source_address": "null | string"
}
```

* `action` - действие:
  * `accept` - разрешить;
  * `snat` - производить SNAT.
* `change_destination_address` - IP-адрес для замены источника, или `null`, если `action` = `accept`.

</details>

<details>
<summary>Добавление правила</summary>

* `POST /firewall/rules/forward/before?anchor_item_id=123&insert_after={true|false}` - начальное правило в раздел FORWARD;
* `POST /firewall/rules/forward/after?anchor_item_id=123&insert_after={true|false}` - конечное правило в раздел FORWARD;
* `POST /firewall/rules/input/before?anchor_item_id=123&insert_after={true|false}` - начальное правило в раздел INPUT;
* `POST /firewall/rules/input/after?anchor_item_id=123&insert_after={true|false}` - конечное правило в раздел INPUT.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
  * `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
[
   "FilterRuleObject|DnatRuleObject|SnatRuleObject",
]
```

* В запросе не должно быть `id`, так как правило ещё не создано и не имеет идентификатора.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>
<summary>Редактирование правила</summary>

* `PUT /firewall/rules/forward/before/<id правила>` - раздел FORWARD, начальное правило;
* `PUT /firewall/rules/forward/after/<id правила>` - раздел FORWARD, конечное правило;
* `PUT /firewall/rules/input/before/<id правила>` - раздел INPUT, начальное правило;
* `PUT /firewall/rules/input/after/<id правила>` - раздел INPUT, конечное правило.

**Json-тело запроса:**

```json5
[
   "FilterRuleObject|DnatRuleObject|SnatRuleObject",
]
```

**Ответ на успешный запрос:** 200 ОК

**Важно!** Чтобы переместить правило между группами серверов, измените его `parent_id`.

</details>

<details>
<summary>Перемещение правила</summary>

* `PATCH /firewall/rules/forward/before/move` - раздел FORWARD, начальное правило;
* `PATCH /firewall/rules/forward/after/move` - раздел FORWARD, конечное правило;
* `PATCH /firewall/rules/input/before/move` - раздел INPUT, начальное правило;
* `PATCH /firewall/rules/input/after/move` - раздел INPUT, конечное правило.

**Json-тело запроса:**

```json5
{
    "params": {
      "id": "integer",
      "anchor_item_id": "integer",
      "insert_after": "boolean"
  }
}
```

* `id` - идентификатор перемещаемого правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно поместить перемещаемое правило;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос**: 200 ОК

</details>

<details>
<summary>Удаление правила</summary>

* `DELETE /firewall/rules/forward/before/<id правила>` - раздел FORWARD, начальное правило;
* `DELETE /firewall/rules/forward/after/<id правила>` - раздел FORWARD, конечное правило;
* `DELETE /firewall/rules/input/before/<id правила>` - раздел INPUT, начальное правило;
* `DELETE /firewall/rules/input/after/<id правила>` - раздел INPUT, конечное правило.

**Ответ на успешный запрос**: 200 ОК

</details>