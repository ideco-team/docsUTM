# Настройка удаленной передачи системных логов (Syslog)

<details>
<summary>Получение статуса работы службы</summary>

```
GET /logs_backend/remote_syslog/status
```

**Ответ на успешный запрос:**

```json5
[
    {
        "name": "string",
        "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading", 
        "msg": [ "string" ]
    },
    ...
]
```

* `name` - название модуля;
* `status` - статус;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

## Общие настройки

<details>
<summary>Включение/выключение службы</summary>

**Проверка состояния:**

```
GET /logs_backend/remote_syslog/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `msg` - `true` для включения, `false` для выключения.

**Включение/выключение**

```
PUT /logs_backend/remote_syslog/state
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение настроек удаленной передачи системных логов</summary>

```
GET /logs_backend/remote_syslog
```

**Ответ на успешный запрос:**

```json5
{
  "host": "string",
  "port": "integer",
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef"
}
```

* `host` - IP-адрес сервера;
* `port` - порт;
* `protocol` - протокол, допустимые значения: `tcp` или `udp`;
* `format` - формат, допустимые значения: `syslog` или `cef`.

</details>

<details>
<summary>Изменение настроек удаленной передачи системных логов</summary>

```
PATCH /logs_backend/remote_syslog
```

**Json-тело запроса:**

```json5
{
  "host": "string" | "null",
  "port": "integer" | "null",
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef",
}
```

* `host` - IP-адрес сервера;
* `port` - порт;
* `protocol` - протокол, допустимые значения: `tcp` или `udp`;
* `format` - формат, допустимые значения: `syslog` или `cef`.

Пустые значения "" не допускаются.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение данных о логировании для таблицы</summary>

```
GET /logs_backend/logs?<GET-параметры, разделенные знаком &>
```

**Список GET-параметров, которые не являются обязательными:**
* `limit: integer` - ограничение на количество записей, выбираемых из базы данных;
* `offset: integer` - количество строк, которые необходимо пропустить перед выводом записей, указанных в `limit`;
* `sort: [Sort]` - список параметров для сортировки данных. Сортировка производится в прямом порядке следования в массиве;
* `filter: [Filter]` - список параметров для фильтрации данных. Фильтры применяются в прямом порядке следования в массиве, с логикой `and` между объектами `Filter`;
* `search: Search` - объект с параметрами поиска подстроки в данных;
* `last_reboot_only: boolean` - параметр типа `boolean` со значениями: `false` - выводить все записи лога, `true` - только записи после последней загрузки;
* `format_type:` - формат возвращаемых данных:
  * `CSV` - CSV-файл;
  * `JSON` - тип по умолчанию.

**Обьект Sort:**
```json5
{
  "field": "string",
  "direction": "asc | desc"
}
```

* `field` - столбец, по которому производится сортировка;
* `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию.

**Обьект Filter:**
```json5
{
  "items": [    
      {
        "column_name": "string",
        "operator": "contains | not_contains | equals | not_equals | greater | greater_equal | less | less_equal",
        "value": ["string | integer | boolean"]
      },
      ...
    ],
  "link_operator": "and | or"
}
```

* `items` - массив фильтров `FilterItem`:
  * `column_name` - поле для фильтрации;
  * `operator` - одно из значений:
    * `contains` - содержит подстроку (без учета регистра);
    * `not_contains` - не содержит подстроку (без учета регистра);
    * `equals` - равно;
    * `not_equals` - не равно;
    * `greater` - больше, в `values` передается массив, содержащий только одно значение;
    * `greater_equal` - больше или равно, в `values` передается массив, содержащий только одно значение;
    * `less` - меньше, в `values` передается массив, содержащий только одно значение;
    * `less_equal` - меньше или равно, в `values` передается массив, содержащий только одно значение.
  * `value` - массив значений фильтра. Максимальное количество передаваемых в массиве значений - 255. Данные отбираются по логике `or`.
* `link_operator` - логика наложения фильтров `items`.

**Обьект Search:**
```json5
{
  "text": "string",
  "columns": ["string"]
}
```

* `text` - искомая строка;
* `columns` - набор полей, по которым ведется поиск.

**Ответ на успешный запрос:**
```json5
{
  "meta": [
    {
      "name": "string",
      "type": "string"
    },
    ...
  ],
  "data": [
    {
      "id": "string",
      "date_time": "integer",
      "microseconds": "integer",
      "priority": "integer",
      "message": "string",
      "syslog_id": "string",
      "unit": "string"
    },
    ...
  ],
  "rows": "integer",
  "rows_before_limit_at_least": "integer"
}
```

* `meta` - массив метаданных, описывающих поля запроса:
  * `name` - имя поля данных;
  * `type` - тип данных.
* `data` - массив, содержащий `Log` - объект, представляющий собой данные, соответствующие одной строке таблицы:
  * `id` - уникальный идентификатор строки;
  * `date_time` - время возникновения события в формате YYYYMMDDhhmmss;
  * `microseconds` - микросекунды во времени возникновения события (0...999999);
  * `priority` - число от 0 до 7:
    * `0` - LOG_EMERG;
    * `1` - LOG_ALERT;
    * `2` - LOG_CRIT;
    * `3` - LOG_ERR;
    * `4` - LOG_WARNING;
    * `5` - LOG_NOTICE;
    * `6` - LOG_INFO;
    * `7` - LOG_DEBUG.
  * `message` - сообщение логирования;
  * `syslog_id` - название исполняемой программы;
  * `unit` - название сервиса, сообщение которого было сохранено в журнале.
* `rows` - количество строк `Log`;
* `rows_before_limit_at_least` - количество строк `Log`, которое вернет запрос, если использовать ограничение на количество записей из базы данных (GET-параметры `limit` или `offset`).

</details>