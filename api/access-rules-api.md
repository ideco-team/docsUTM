# Управление правилами трафика

{% hint style="info" %}
API правил трафика Ideco Center описано в статье [Центральная консоль](/api/cc-api.md).
{% endhint %}

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

## Файрвол

<details>
<summary>Получение статуса службы</summary>

```
GET /firewall/status
```

**Ответ на успешный запрос:**

```json
[
   {
      "name": "rules-in-kernel",
      "status": "active | activating | deactivating | failed | inactive | reloading",
      "msg": [ "string" ]  //(Список строк, поясняющих текущее состояние)
    },
   {
      "msg": [ "string" ],
      "status": "active",
      "name": "auto-snat"
    }
]
```

</details>

<details>
<summary>Получение настроек Файрвола</summary>

### Включенность пользовательских правил

```
GET /firewall/state
```

**Ответ на успешный запрос:**

```json
{
    "enabled": "boolean"
} 
```

* `enabled` - Опция раздела Файрвол включен (true) или
отключен (false).

### Логирование правил

```
GET /firewall/settings
```

**Ответ на успешный запрос:**

```json
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": ["accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log"]
} 
```

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /firewall/settings
```

**Json-тело запроса:**

```json
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": ["accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log"]
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT;
* `log_mode` - режим логирования;
* `log_actions` - события, которые будут логироваться. 

**Ответ на успешный запрос**: 200 ОК

</details>

### Управление правилами

<details>
<summary>Получение списка правил</summary>

* `GET /firewall/rules/forward` - раздел FORWARD;
* `GET /firewall/rules/input` - раздел INPUT;
* `GET /firewall/rules/dnat` - раздел DNAT;
* `GET /firewall/rules/snat` - раздел SNAT;
* `GET /firewall/rules/log` - раздел Логирование.

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
    "action": "accept | drop"
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

* `POST /firewall/rules/forward?anchor_item_id=123&insert_after={true|false}` - раздел FORWARD;
* `POST /firewall/rules/input?anchor_item_id=123&insert_after={true|false}` - раздел INPUT;
* `POST /firewall/rules/dnat?anchor_item_id=123&insert_after={true|false}` - раздел DNAT;
* `POST /firewall/rules/snat?anchor_item_id=123&insert_after={true|false}` - раздел SNAT;
* `POST /firewall/rules/log?anchor_item_id=123&insert_after={true|false}` - раздел Логирование.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы;
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

* `id` - идентификатор созданного правила.

</details>

<details>
<summary>Редактирование правила</summary>

* `PUT /firewall/rules/forward/<id правила>` - раздел FORWARD;
* `PUT /firewall/rules/input/<id правила>` - раздел INPUT;
* `PUT /firewall/rules/dnat/<id правила>` - раздел DNAT;
* `PUT /firewall/rules/snat/<id правила>` - раздел SNAT;
* `PUT /firewall/rules/log/<id правила>` - раздел Логирование.

**Json-тело запроса:**

```json5
[
   "FilterRuleObject|DnatRuleObject|SnatRuleObject",
]
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

* `PATCH /firewall/rules/forward/move` - раздел FORWARD;
* `PATCH /firewall/rules/input/move` - раздел INPUT;
* `PATCH /firewall/rules/dnat/move` - раздел DNAT;
* `PATCH /firewall/rules/snat/move` - раздел SNAT;
* `PATCH /firewall/rules/log/move` - раздел Логирование.

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

</details>

<details>
<summary>Удаление правила</summary>

* `DELETE /firewall/rules/forward/<id правила>` - раздел FORWARD;
* `DELETE /firewall/rules/input/<id правила>` - раздел INPUT;
* `DELETE /firewall/rules/dnat/<id правила>` - раздел DNAT;
* `DELETE /firewall/rules/snat/<id правила>` - раздел SNAT;
* `DELETE /firewall/rules/log/<id правила>` - раздел Логирование.

**Ответ на успешный запрос:** 200 ОК

</details>

### Счетчик срабатывания правил

<details>
<summary>Проверка включенности счетчика срабатываний правил</summary>

```
GET /firewall/watch
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean" //(true - если счетчик включен, false - если выключен)
}
```

</details>

<details>
<summary>Включение/выключение счетчика срабатывания правил</summary>

```
PUT /firewall/watch
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean" //(true - чтобы включить, false - чтобы выключить)
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение счетчиков по правилам</summary>

* `GET /firewall/counters/forward` - раздел FORWARD;
* `GET /firewall/counters/input` - раздел INPUT;
* `GET /firewall/counters/dnat` - раздел DNAT;
* `GET /firewall/counters/snat` - раздел SNAT;
* `GET /firewall/rules/log` - раздел Логирование.

**Ответ на успешный запрос:**

```json5
[
   {
      "id": "integer",
      "packets": "integer" //(количество сработок правила)
   },
   ...
]
```

</details>

## Контент-фильтр

<details>

<summary>Включение/выключение Контент-фильтра</summary>

### Проверить включенность

```
GET /content-filter/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

### Включить/выключить Контент-фильтр

```
PUT /content-filter/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

### Настройки

<details>
<summary>Получение настроек</summary>

```
GET /content-filter/settings
```

**Ответ на успешный запрос:**

```json5
{
    "enabled_extended_categorizer": "boolean",
    "quic_reject_enabled": "boolean"
}
```

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS) включена (true) или выключена (false);
* `quic_reject_enabled` - запрет трафика по протоколу QUIC включен (true) или выключен (false).

</details>

<details>
<summary>Изменение настроек</summary>

```
PATCH /content-filter/settings
```

**Json-тело запроса:**

```json5
{
    "enabled_extended_categorizer": "boolean",
    "quic_reject_enabled": "boolean" //(Любое из полей может отсутствовать)
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение настройки безопасного поиска</summary>

```
GET /proxy_backend/safe_search
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

</details>

<details>
<summary>Изменение настройки безопасного поиска</summary>

```
PUT /proxy_backend/safe_search
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

### Категории Контент-фильтра

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

* `id` - номер категории в формате `users.id.1` или `extended.id.1`;
* `type` - тип категории:
  * `"users"` - пользовательские категории;
  * `"extended"` - расширенные категории (SkyDNS);
  * `"files"` - категории для файлов;
  * `"special"` - специальные предопределенные категории (Прямое обращение по IP, Все категоризированные запросы, Все некатегоризированные запросы, Все запросы);
  * `"other"` - остальные категории.
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
        "id": "string" (идентификатор категории, вида - users.id.1),
        "name": "string" (название категории, не пустая строка),
        "comment": "string",
        "urls": ["string"]
    },
    ...
]
```

* `urls` - список url. Либо полный путь до страницы, либо только доменное имя. В пути может присутствовать любое количество любых символов.

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

### Правила Контент-фильтра

<details>
<summary>Получение списка правил</summary>

```
GET /content-filter/rules
```

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
        "redirect_url": "string | null",
        "enabled": "boolean",
        "timetable": [ "string" ]
    },
    ...
]
```

* `id` - идентификатор правила;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled` - правило включено (true) или выключено (false);
* `timetable` - время действия, список идентификаторов алиасов.

</details>

<details>
<summary>Создание правила</summary>

```
POST /content-filter/rules?anchor_item_id=123&insert_after={true|false}
```

* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы;
* `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

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
    "redirect_url": "string|null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled` - правило включено (true) или выключено (false);
* `timetable` - время действия.

</details>

<details>
<summary>Редактирование правила</summary>

```
PUT /content-filter/rules/<id правила>
```

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
    "access": "allow | deny | bump | redirect",
    "redirect_url": "string | null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```
* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым (максимальная длина - 255 символов);
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `aliases` - список идентификаторов алиасов (поле Применяется для);
* `categories` - список идентификаторов категорий сайтов;
* `http_methods` - список методов HTTP. Доступен выбор из списка: GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, TRACE, CONNECT;
* `content_types` -  список mime types;
* `access` - действие, которое необходимо выполнить в правиле:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump` - расшифровать запрос;
  * `redirect` - перенаправить запрос на `redirect_url`.
* `redirect_url` - адрес, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled` - правило включено (true) или выключено (false);
* `timetable` - время действия.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

```
PATCH /content-filter/rules/move
```

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

* `id` - идентификатор правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно вставить правило, которое перемещаем;
* `insert_after` - вставка до или после. Если `true`, то правило будет вставлено сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /content-filter/rules/<id правила>
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Предотвращение вторжений

<details>
<summary>Получение статуса работы службы</summary>

```
GET /ips/status
```

**Ответ на успешный запрос:** 

```json5
[
    {
        "name": "string",
        "status": "active|activating|deactivating|failed|inactive|reloading",
        "msg": [ "string" ]
    }
]
```

* `name` - название демона;
* `status` - статус;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

<details>
<summary>Управление статусом работы службы</summary>

**Получение текущей настройки включенности модуля**

```
GET /ips/state
```

**Ответ на успешный запрос:** 

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` если модуль включен, `false` - если выключен.

**Изменение настройки включенности модуля**

```
PUT /ips/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

### Группы сигнатур

<details>
<summary>Получение представления групп сигнатур в табличном виде</summary>

```
GET /ips/signature_groups/table
```

**Ответ на успешный запрос:** 

```json5
{
    "signature_groups": [
        {
            "classtype": "string",
            "classtype_name": "string",  
            "mitre_tactics": [
                {
                    "mitre_tactic_id": "string",
                    "mitre_tactic_name": "string"  
                },
                ...
            ],
            "count": "integer"
        },
        ...
    ]
}
```

* `classtype` - группа сигнатур;
* `classtype_name` - название группы сигнатур (отображается в интерфейсе Ideco NGFW);
* `mitre_tactics` - тактика согласно матрице MITRE ATT&CK, которой соответствует группа сигнатур:
    * `mitre_tactic_id` - идентификатор тактики;
    * `mitre_tactic_name` - название тактики.
* `count` - количество сигнатур в группе.

</details>

<details>
<summary>Получение представления групп сигнатур в матричном виде MITRE ATT&CK</summary>

```
GET /ips/signature_groups/mitre
```

**Ответ на успешный запрос:** 

```json5
{
    "signature_groups": [
        {
            "mitre_tactic_id": "string",
            "mitre_tactic_name": "string",  
            "classtypes": [
                {
                    "classtype": "string-admin",
                    "classtype_name": "string",  
                    "count": "integer"
                },
                ...
            ]
        },
        ...
    ]
}
```

* `mitre_tactic_id` - идентификатор тактики согласно матрице MITRE ATT&CK;
* `mitre_tactic_name` - название тактики;
* `classtypes` - группы сигнатур, соответствующие тактике:
    * `classtype` - группа сигнатур;
    * `classtype_name` - название группы сигнатур (отображается в интерфейсе Ideco NGFW);
    * `count` - количество сигнатур в группе.

</details>

<details>
<summary>Получение списка сигнатур определенной группы</summary>

```
GET /ips/signatures?filter=[ { "items": [ {"column_name":"classtype","operator":"equals","value":[<classtype нужной группы сигнатур (может быть несколько значений через запятую)>]} ], "link_operator":"or" } ]
```

* `"column_name":"classtype","operator":"equals","value":[<classtype нужной группы сигнатур (может быть несколько значений через запятую)>]` - фильтр: отбирает из таблицы групп сигнатур только те группы, у которых значение `classtype` соответствует указанным в `value`.

**Ответ на успешный запрос:**

```json5
{
    "signatures": [
            {
                "action": "drop",
                "protocol": "tcp",
                "flow": "to_server",
                "classtype": "attempted-admin",
                "sid": 2050604,
                "signature_severity": "Major",
                "mitre_tactic_id": "TA0001",
            },
            ...
        ]
}
```

* `action` - действие для трафика, соответствующего сигнатуре;
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`);
* `flow` - направление трафика (`to_server`, `from_server`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK.

</details>

<details>
<summary>Получение оригинального содержания сигнатуры</summary>

```
GET /ips/signatures/<sid>
```

**Ответ на успешный запрос:**

```json
{
    "signature": "string"
}
```

</details>

### Пользовательские сигнатуры

<details>
<summary>Получение списка пользовательских сигнатур</summary>

```
GET /ips/custom
```

**Ответ на успешный запрос:**

```json5
[
    {
    "id": "string",
    "comment": "string",
    "rule": "string",
    "sid": "integer",
    "classtype": "string"
  },
  ...
]
```

* `id` - идентификатор правила;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `rule` - cтрока с правилом, не более 8196 символов;
* `sid` - идентификатор сигнатуры. Указывается в строке с правилом, извлекается из нее;
* `classtype` - тип правила (может быть пустой строкой).

</details>

<details>
<summary>Создание пользовательской сигнатуры вручную</summary>

```
POST /ips/custom
```

**Json-тело запроса:**

```json5
{
    "comment": "string",
    "rule": "string"
}
```

* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `rule` - строка с правилом, не более 8196 символов, переводы строк в ней запрещены.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданной сигнатуры.

</details>

<details>
<summary>Загрузка пользовательских сигнатур из файла</summary>

```
POST /ips/custom_rules_file
```

Файл загружается как тело запроса, он должен иметь текстовый формат text/plain, максимальный размер файла - 32 MB.

**Ответ на успешный запрос:**

```json5
{
    "count": "integer"
}
```

* `count` - количество загруженных правил.

</details>

<details>
<summary>Редактирование пользовательской сигнатуры</summary>

```
PATCH /ips/custom/<id сигнатуры>
```

**Json-тело запроса (все или некоторые поля):**

```json5
{
    "comment": "string",
    "rule": "string"
}
```

* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `rule` - cтрока с правилом, не более 8196 символов, переводы строк в ней запрещены.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление пользовательской сигнатуры</summary>

```
DELETE /ips/custom/<id сигнатуры>
```

**Ответ на успешный запрос:** 200 ОК

</details>

### Обновление баз

<details>
<summary>Получение статуса обновления баз правил Suricata и GeoIP</summary>

```
GET /ips/update
```

**Ответ на успешный запрос:**

```json
{
    "status": "up_to_date|updating|failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float|null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваются новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Получение статуса обновления расширенных баз правил Suricata и GeoIP</summary>

```
GET /ips/update_advanced
```

**Ответ на успешный запрос:**

```json
{
    "status": "up_to_date|updating|failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float|null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваются новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Запуск принудительного обновления баз</summary>

```
POST /ips/update
```

**Ответ на успешный запрос:** 200 OK

</details>

### Сети, защищенные от вторжений

<details>
<summary>Получение списка локальных подсетей</summary>

```
GET /ips/nets
```

**Ответ на успешный запрос:**

```json
[
    {
    "id": "string",
    "address": "string"
  },
  ...
]
```

* `id` - идентификатор подсети;
* `address` - адрес подсети (например: `192.168.0.0/16`).

</details>

<details>
<summary>Добавление новой локальной подсети</summary>

```
POST /ips/nets
```

**Json-тело запроса:**

```json
{
    "address": "string"
  }
```

* `address` - адрес подсети (например: `192.168.0.0/16`).

</details>

<details>
<summary>Удаление локальной подсети</summary>

```
DELETE /ips/nets/<id локальной подсети>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Исключения

<details>
<summary>Получение списка исключений объектов</summary>

```
GET /ips/bypass
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "aliases": [ "string" ],
        "comment": "string",
        "enabled": "boolean"
    },
    ...
]
```

* `id` - идентификатор исключения;
* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: включено/выключено.

</details>

<details>
<summary>Добавление исключения объектов</summary>

```
POST /ips/bypass
```

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: включено/выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного исключения.

</details>

<details>

<summary>Изменение исключения объектов</summary>

```
PATCH /ips/bypass/<id исключения>
```

**Json-тело запроса:**

```json5
{
    "aliases": [ "string" ],
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список идентификаторов объектов. Допустимые типы: IP-адрес, Диапазон IP-адресов, Список IP-объектов, Список IP-адресов, Подсеть, Домен, Пользователь, Группа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - состояние исключения: включено/выключено.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление существующего исключения объектов</summary>

```
DELETE /ips/bypass/<id исключения>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Квоты

<details>
<summary>Проверить, включен ли подсчет квот</summary>

```
GET /quotas/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

</details>

<details>
<summary>Включить/выключить подсчет квот</summary>

```
PUT /quotas/state
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
<summary>Получение списка квот</summary>

```
GET /quotas/quotas
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "title": "string",
        "comment": "string",
        "quota": "integer",
        "enabled": "boolean",
        "interval": "hour" | "day" | "week" | "month" | "quarter"
    },
    ...
]
```

* `id` - идентификатор квоты;
* `title` - название квоты (максимальная длина - 42 символа);
* `comment` - комментарий (максимальная длина - 255 символов);
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

</details>

<details>
<summary>Создание квоты</summary>

```
POST /quotas/quotas
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "quota": "integer",
    "enabled": "boolean",
    "interval": "string"
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
<summary>Редактирование квоты</summary>

```
PATCH /quotas/quotas/<id квоты>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "quota": "integer",
    "enabled": "boolean",
    "interval": "string"
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

**Ответ на успешный запрос:** 200 ОК

</details>