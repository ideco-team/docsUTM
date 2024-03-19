# Управление правилами трафика

{% hint style="info" %}
API правил трафика Ideco Center описано в статье [Центральная консоль](/api/cc-api.md).
{% endhint %}

## Файрвол

<details>
<summary>Получение статуса службы</summary>

```
GET /firewall/status
```

**Ответ на успешный запрос:**

```
[
  {
      "name": "rules-in-kernel",
      "status": "active|activating|deactivating|failed|inactive|reloading",
      "msg": [ "string" ]  (Список строк, поясняющих текущее состояние)
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

## Включенность пользовательских правил

```
GET /firewall/state
```

**Ответ на успешный запрос:**

```
{
    "enabled": "boolean"
} 
```

* `enabled` - Переключатель раздела Файрвол включен (true) или
отключен (false).

### Логирование правил

```
GET /firewall/settings
```

**Ответ на успешный запрос:**

```
{
    "automatic_snat_enabled": boolean,
    "log_actions": ["accept" | "drop" | "dnat" | "snat"],
    "log_mode": "string"
} 
```

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /firewall/settings
```

**Json-тело запроса:**

```
{
    "automatic_snat_enabled": boolean,
    "log_actions": ["accept" | "drop" | "dnat" | "snat"],
    "log_mode": "string"
} 
```

Ответ: 200 ОК

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

```
[
    {
        "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
        "comment": "string",
        "destination_addresses": [ "string" ], 
        "destination_addresses_negate": boolean,
        "destination_ports": [ "string" ],
        "enabled": boolean,
        "hip_profiles": [ "string" ],
        "incoming_interface": "string",
        "outgoing_interface": "string",
        "parent_id": "string",
        "protocol": "string",
        "source_addresses": [ "string" ],
        "source_addresses_negate": boolean,
        "timetable": [ "string" ],
        "id": int
    },
    ...
]
```

* `"action"` - действие:
  * `"accept"` - разрешить; 
  * `"drop"` - запретить;
  * `"dnat"` - производить DNAT;
  * `"snat"` - производить SNAT;
  * `"mark_log"` - логировать; 
  * `"mark_not_log"` - не логировать;
* `"comment"` - комментарий (может быть пустым);
* `"destination_addresses"` - адрес назначения;
* `"destination_addresses_negate"` - инвертировать адрес назначения;
* `"destination_ports"` - порты назначения;
* `"enabled"` - включено (true) или выключено (false) правило;
* `"hip_profiles"` - HIP-профили;
* `"incoming_interface"` - зона источника;
* `"outgoing_interface"` - зона назначения;
* `"parent_id"` - идентификатор группы в ЦК, в которую входит сервер, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `"protocol"` - протокол;
* `"source_addresses"` - адрес источника;
* `"source_addresses_negate"` - инвертировать адрес источника;
* `"timetable"` - время действия;
* `"id"` - идентификатор правила.

</details>

<details>
<summary>Добавление правила</summary>

* `POST /firewall/rules/forward?anchor_item_id=123&insert_after={true|false}` - раздел FORWARD;
* `POST /firewall/rules/input?anchor_item_id=123&insert_after={true|false}` - раздел INPUT;
* `POST /firewall/rules/dnat?anchor_item_id=123&insert_after={true|false}` - раздел DNAT;
* `POST /firewall/rules/snat?anchor_item_id=123&insert_after={true|false}` - раздел SNAT;
* `POST /firewall/rules/log?anchor_item_id=123&insert_after={true|false}` - раздел Логирование.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
  * `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```
{
    "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
    "comment": "",
    "destination_addresses": [ "string" ],
    "destination_addresses_negate": boolean,
    "destination_ports": [ "string" ],
    "enabled": boolean,
    "hip_profiles": [ "string" ],
    "incoming_interface": "string",
    "outgoing_interface": "string",
    "parent_id": "string",
    "protocol": "string",
    "source_addresses": [ "string" ],
    "source_addresses_negate": boolean,
    "timetable": [ "string" ]
    }
```

**Ответ на успешный запрос:**

```
{
    "id": int
}
```

</details>

<details>
<summary>Редактирование правила</summary>

* `PUT /firewall/rules/forward/<id правила>` - раздел FORWARD;
* `PUT /firewall/rules/input/<id правила>` - раздел INPUT;`
* `PUT /firewall/rules/dnat/<id правила>` - раздел DNAT;
* `PUT /firewall/rules/snat/<id правила>` - раздел SNAT;
* `PUT /firewall/rules/log/<id правила>` - раздел Логирование.

**Json-тело запроса:**

```
{
    "action": "accept" | "drop" | "dnat" | "snat" ("mark_log" | "mark_not_log" для раздела Логирование),
    "comment": "",
    "destination_addresses": [ "string" ],
    "destination_addresses_negate": boolean,
    "destination_ports": [ "string" ],
    "enabled": boolean,
    "hip_profiles": [ "string" ],
    "incoming_interface": "string",
    "outgoing_interface": "string",
    "parent_id": "string",
    "protocol": "string",
    "source_addresses": [ "string" ],
    "source_addresses_negate": boolean,
    "timetable": [ "string" ]
    }
```

Ответ: 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

* `PATCH /firewall/rules/forward/move` - раздел FORWARD;
* `PATCH /firewall/rules/input/move` - раздел INPUT;
* `PATCH /firewall/rules/dnat/move` - раздел DNAT;
* `PATCH /firewall/rules/snat/move` - раздел SNAT;
* `PATCH /firewall/rules/log/move` - раздел Логирование.

**Json-тело запроса:**

```
{
  "params": {
    "id": int,
    "anchor_item_id": int,
    "insert_after": boolean
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

Ответ: 200 ОК

</details>

### Счетчик срабатывания правил

<details>
<summary>Узнать, включен ли счетчик срабатываний правил</summary>

```
GET /firewall/watch
```

**Ответ на успешный запрос:**

```
{
   "enabled": boolean (true - если счетчик включен, false - если выключен)
}
```

</details>

<details>
<summary>Включение/выключение счетчика срабатывания правил</summary>

```
PUT /firewall/watch
```

**Json-тело запроса:**

```
{
   "enabled": boolean (true - чтобы включить, false - чтобы выключить)
}
```

Ответ: Статус 200 ОК

</details>

<details>
<summary>Получение счетчиков по правилам</summary>

* `GET /firewall/counters/forward` - раздел FORWARD;
* `GET /firewall/counters/input` - раздел INPUT;
* `GET /firewall/counters/dnat` - раздел DNAT;
* `GET /firewall/counters/snat` - раздел SNAT;
* `GET /firewall/rules/log` - раздел Логирование.

**Ответ на успешный запрос:**

```
[
   {
      "id": int,
      "packets": int (количество сработок правила)
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

```
{
    "enabled": boolean
}
```

### Включить/выключить Контент-фильтр

```
PUT /content-filter/state
```

**Json-тело запроса:**

```
{
    "enabled": boolean
}
```

Ответ: 200 ОК

</details>

### Настройки

<details>
<summary>Получение настроек</summary>

```
GET /content-filter/settings
```

**Ответ на успешный запрос:**

```
{
    "enabled_extended_categorizer": boolean,
    "quic_reject_enabled": boolean
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

```
{
    "enabled_extended_categorizer": boolean,
    "quic_reject_enabled": boolean (Любое из полей может отсутствовать)
}
```

Ответ на запрос: 200 OK.

</details>

<details>
<summary>Получение настройки безопасного поиска</summary>

```
GET /proxy_backend/safe_search
```

**Ответ на успешный запрос:**

```
{
    "enabled": boolean
}
```

</details>

<details>
<summary>Изменение настройки безопасного поиска</summary>

```
PUT /proxy_backend/safe_search
```

**Json-тело запроса:**

```
{
    "enabled": boolean
}
```

Ответ: 200 OK

</details>

### Категории Контент-фильтра

<details>
<summary>Получение списка категорий (предустановленных и пользовательских)</summary>

```
GET /content-filter/categories
```

**Json-тело ответа:**

```
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
  * `"users"` - пользовательские категории;
  * `"extended"` - расширенные категории (SkyDNS);
  * `"files"` - категории для файлов;
  * `"special"` - специальные предопределенные категории:
    - Прямое обращение по IP;
    - Все категоризированные запросы;
    - Все некатегоризированные запросы;
    - Все запросы (категоризированные и некатегоризированные).
  * `"other"` - остальные категории.
* `name` - имя категории (для отображения пользователю).
* `comment` - описание категории (для отображения пользователю).

</details>

<details>
<summary>Получение списка пользовательских категорий</summary>

```
GET /content-filter/users_categories
```

**Json-ответ на запрос:**

```
[
    {
        "id": "string" (номер категории, вида - users.id.1),
        "name": "string" (название категории, не пустая строка),
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

```
{
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

**Ответ на успешный запрос:** 

```
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

```
{
    "name": "string",
    "comment": "string",
    "urls": ["string"]
}
```

**Ответ на успешный запрос:**

```
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

**Json-тело ответа:**

```
[
    {
        "access": "allow" | "deny" | "bump" | "redirect",
        "aliases": ["string"],
        "categories": ["string"],
        "comment": "string",
        "enabled": boolean,
        "name": "string",
        "parent_id": "string",
        "redirect_url": "string" | null,
        "timetable": ["string"],
        "id": int
    },
    ...
]
```

* `id` - идентификатор правила;
* `parent_id` - id группы в ЦК, в которую входит Ideco NGFW, или константа "f3ffde22-a562-4f43-ac04-c40fcec6a88c" (соответствует Корневой группе);
* `name` - название правила, не пустая строка;
* `comment` - комментарий (макс. 256 символов), может быть пустым;
* `aliases` - список id алиасов (поле Применяется для);
* `categories` - список id категорий сайтов;
* `access` - действие, которое необходимо выполнить в правиле, строка, может принимать три значения:
  * `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump`: расшифровать запрос;
  * `redirect`: перенаправить запрос на `redirect_url`;
* `redirect_url` - URL, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled`: правило включено (true) или выключено (false);
* `timetable` - время действия, список ID алиасов.

</details>

<details>
<summary>Создание правила</summary>

```
POST /content-filter/rules?anchor_item_id=123&insert_after={true|false}
```

* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
* `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```
{
    "name": "string",
    "comment": "string",
    "parent_id": "string", 
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow|deny|bump|redirect",
    "redirect_url": "string|null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

</details>

<details>
<summary>Редактирование правила</summary>

```
PUT /content-filter/rules/<id правила>
```

**Json-тело запроса:**

```
{
    "name": "string",
    "comment": "string",
    "parent_id": "string", 
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow|deny|bump|redirect",
    "redirect_url": "string|null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Перемещение правила</summary>

```
PATCH /content-filter/rules/move
```

**Json-тело запроса:**

```
{
  "params": {
    "id": int,
    "anchor_item_id": int,
    "insert_after": boolean
  }
}
```

* `id` - идентификатор правила;
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно вставить правило, которое перемещаем;
* `insert_after` - вставка до или после. Если `true`, то правило будет вставлено сразу после указанного в `anchor_item_id`, если `false` - на месте указанного в `anchor_item_id`.

Ответ: 200 OK.

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /content-filter/rules/<id правила>
```

Ответ: 200 ОК

</details>

## Квоты

<details>
<summary>Проверить, включен ли подсчет квот</summary>

```
GET /quotas/state
```

**Ответ на успешный запрос:**

```
{
  "enabled": boolean
}
```

</details>

<details>
<summary>Включить/выключить подсчет квот</summary>

```
PUT /quotas/state
```

**Json-тело запроса:**

```
{
  "enabled": boolean
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Получение списка квот</summary>

```
GET /quotas/quotas
```

**Ответ на успешный запрос:**

```
[
  {
    "id": "string",
    "title": "string",
    "comment": "string",
    "quota": "integer",
    "enabled": "bool",
    "interval": "hour" | "day" | "week" | "month" | "quarter"
  },
  ...
]
```

* `id` - идентификатор квоты;
* `title` - название квоты (максимальная длина 42 символа);
* `comment` - комментарий (максимальная длина 256 символов)%
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

```
{
  "title": "string",
  "comment": "string",
  "quota": int,
  "enabled": boolean,
  "interval": "string"
}
```

**Ответ на успешный запрос:**

```
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

**Json-тело запроса (все или некоторые поля):**

```
{
  "title": "string",
  "comment": "string",
  "quota": "integer",
  "enabled": boolean,
  "interval": "string"
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

Ответ: 200 ОК

</details>