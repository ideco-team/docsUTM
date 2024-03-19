# Центральная консоль

## Подключение Ideco NGFW к Ideco Center

<details>
<summary>Получение настроек ЦК</summary>

```
GET /central_console/settings
```

**Ответ на успешный запрос:**

```
{
    cc_server: "string" | null,
    last_connect: int | null,
    last_sync: int | null,
    root_ca: "string" | null
}
```

* `cc_server` - доменное имя или IP-адрес центральной консоли;
* `last_connect` - timestamp последней успешной синхронизации данных;
* `last_sync` - timestamp;
* `root_ca` - корневой сертификат в формате PEM.

</details>

<details>
<summary>Изменение настроек ЦК</summary>

```
PATCH /central_console/settings
```

**Json-тело запроса:**

```
{
  cc_server: "string" | null
}
```

Для удаления настроек ЦК выполните запрос:

```
DELETE /central_console/settings
```

</details>

<details>
<summary>Загрузка корневого сертификата ЦК на NGFW</summary>

```
POST /central_console/root_ca
```

В тело запроса поместите содержимое корневого сертификата, скачанного в Ideco Center. Для этого откройте сертификат в текстовом редакторе и скопируйте текст.

</details>

<details>
<summary>Удаление корневого сертификата ЦК</summary>

```
DELETE /central_console/root_ca
```

Ответ: 200 ОК

</details>

## Управление правилами трафика в Ideco Center

<details>
<summary>Получение списка групп серверов в ЦК</summary>

```
GET /servers/groups
```

**Пример ответа на успешный запрос:**

```
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

* `"id"` - идентификатор группы;
* `"comment"` - комментарий, может быть пустым;
* `"name"` - название группы серверов;
* `"parent_id"` - идентификатор родительской группы серверов.

</details>

### Контент-фильтр

<details>
<summary>Получение списка правил</summary>

* `GET /content-filter/rules/before?groups=[UUID1,UUID2]` - начальные правила;
* `GET /content-filter/rules/after?groups=[UUID1,UUID2]` - конечные правила.

  * `UUID1` - идентификатор группы серверов в Центральной консоли (`id`). 

```
[
    {
        "id": int,
        "parent_id": "string",
        "name": "string",
        "comment": "string",
        "aliases": [ "string" ],
        "categories": [ "string" ],
        "access": "allow" | "deny" | "bump" | "redirect",
        "redirect_url": "string" | null,
        "enabled": boolean,
        "timetable": [ "string" ]
    },
    ...
]
```

* `id` - идентификатор правила;
* `parent_id` - id группы серверов, к которой применяется правило;
* `name` - название правила, не пустая строка;
* `comment` - комментарий (макс. 256 символов), может быть пустым;
* `aliases` - список id алиасов (поле Применяется для);
* `categories` - список id категорий сайтов;
* `access` - действие, которое необходимо выполнить в правиле, строка, может принимать три значения:
  *  `allow` - разрешить данный запрос;
  * `deny` - запретить запрос и показать страницу блокировки;
  * `bump`: расшифровать запрос;
  * `redirect`: перенаправить запрос на `redirect_url`;
* `redirect_url` - URL, на который перенаправляются запросы. `String` при `access` = `redirect` и `null` при остальных вариантах `access`;
* `enabled`: правило включено (true) или выключено (false);
* `timetable` - время действия, список ID алиасов.

</details>

<details>
<summary>Создание правил</summary>

* `POST /content-filter/rules/before?anchor_item_id=123&insert_after={true|false}` - создание начального правила;
* `POST /content-filter/rules/after?anchor_item_id=123&insert_after={true|false}` - создание конечного правила.

**Json-тело запроса:**

```
{
    "parent_id": "string", (id группы серверов, к которой будет применяться правило)
    "name": "string",
    "comment": "string",
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | null,
    "enabled": boolean,
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
<summary>Редактирование правил</summary>

* `PUT /content-filter/rules/before/<id правила>` - изменение начального правила;
* `PUT /content-filter/rules/after/<id правила>` - изменение конечного правила.

**Json-тело запроса:**

```
{
    "name": "string",
    "comment": "string",
    "parent_id": "string",
    "aliases": [ "string" ],
    "categories": [ "string" ],
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | null,
    "enabled": boolean,
    "timetable": [ "string" ]
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Перемещение правил</summary>

* `PATCH /content-filter/rules/before/move` - перемещение начального правила;
* `PATCH /content-filter/rules/after/move` - перемещение конечного правила.

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

Ответ: 200 ОК

</details>

### Файрвол

<details>
<summary>Получение списка правил</summary>

* `GET /firewall/rules/forward/before?groups=[UUID1, UUID2]` - начальные правила раздела FORWARD;
* `GET /firewall/rules/forward/after?groups=[UUID1, UUID2]` - конечные правила раздела FORWARD;
* `GET /firewall/rules/input/before?groups=[UUID1, UUID2]` - начальные правила раздела INPUT;
* `GET /firewall/rules/input/after?groups=[UUID1, UUID2]` - конечные правила раздела INPUT.

**Json-тело ответа:**

```
[
   {
      "action": "accept" | "drop",
      "comment": "",
      "destination_addresses": [ "string" ],
      "destination_addresses_negate": boolean,
      "destination_ports": [ "string" ],
      "enabled": boolean,
      "hip_profiles": ["string"],
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
* `"comment"` - комментарий (может быть пустым);
* `"destination_addresses"` - адрес назначения;
* `"destination_addresses_negate"` - инвертировать адрес назначения;
* `"destination_ports"` - порты назначения;
* `"enabled"` - включено (true) или выключено (false) правило;
* `"hip_profiles"` - HIP-профили;
* `"incoming_interface"` - входящий интерфейс;
* `"outgoing_interface"` - исходящий интерфейс;
* `"parent_id"` - идентификатор группы, к которой применяется правило;
* `"protocol"` - протокол;
* `"source_addresses"` - адрес источника;
* `"source_addresses_negate"` - инвертировать адрес источника;
* `"timetable"` - время действия;
* `"id"` - идентификатор правила.

Правила возвращаются в порядке их применения. 

</details>

<details>
<summary>Создание правила</summary>

* `POST /firewall/rules/forward/before?anchor_item_id=123&insert_after={true|false}` - начальное правило в раздел FORWARD;
* `POST /firewall/rules/forward/after?anchor_item_id=123&insert_after={true|false}` - конечное правило в раздел FORWARD;
* `POST /firewall/rules/input/before?anchor_item_id=123&insert_after={true|false}` - начальное правило в раздел INPUT;
* `POST /firewall/rules/input/after?anchor_item_id=123&insert_after={true|false}` - конечное правило в раздел INPUT.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы.
  * `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```
{
  "action": "accept" | "drop",
  "comment": "",
  "destination_addresses": [ "string" ],
  "destination_addresses_negate": boolean,
  "destination_ports": [ "string" ],
  "enabled": boolean,
  "hip_profiles": ["string"],
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

* `PUT /firewall/rules/forward/before/<id правила>` - раздел FORWARD, начальное правило;
* `PUT /firewall/rules/forward/after/<id правила>` - раздел FORWARD, конечное правило;
* `PUT /firewall/rules/input/before/<id правила>` - раздел INPUT, начальное правило;
* `PUT /firewall/rules/input/after/<id правила>` - раздел INPUT, конечное правило.

**Json-тело запроса:**

```
{
  "action": "accept" | "drop",
  "comment": "",
  "destination_addresses": [ "string" ],
  "destination_addresses_negate": boolean,
  "destination_ports": [ "string" ],
  "enabled": boolean,
  "hip_profiles": ["string"],
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

* `PATCH /firewall/rules/forward/before/move` - раздел FORWARD, начальное правило;
* `PATCH /firewall/rules/forward/after/move` - раздел FORWARD, конечное правило;
* `PATCH /firewall/rules/input/before/move` - раздел INPUT, начальное правило;
* `PATCH /firewall/rules/input/after/move` - раздел INPUT, конечное правило.

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

Ответ: 200 ОК

</details>

<details>
<summary>Удаление правила</summary>

* `DELETE /firewall/rules/forward/before/<id правила>` - раздел FORWARD, начальное правило;
* `DELETE /firewall/rules/forward/after/<id правила>` - раздел FORWARD, конечное правило;
* `DELETE /firewall/rules/input/before/<id правила>` - раздел INPUT, начальное правило;
* `DELETE /firewall/rules/input/after/<id правила>` - раздел INPUT, конечное правило.

Ответ: 200 ОК

</details>