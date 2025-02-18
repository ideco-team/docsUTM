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
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. Сортировка производится в прямом порядке следования в массиве:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию.
* `search: [{"text": "string", "columns": "string"}]` - объект с параметрами поиска подстроки в данных:
    * `text` - искомая строка;
    * `columns` - непустой набор полей, по которым ведется поиск.
* `last_reboot_only: boolean` - параметр типа `boolean` со значениями: `false` - выводить все записи лога, `true` - только записи после последней загрузки;
* `format_type:` - формат возвращаемых данных:
  * `CSV` - CSV-файл;
  * `JSON` - тип по умолчанию.
* `filter: [{"items": [{"column_name": "string", "operator": "OperatorValue", "value": ["string" | "integer" | "boolean"]}], "link_operator": "and" | "or"}]` - список параметров для фильтрации данных. Фильтры применяются в прямом порядке следования в массиве, с логикой `and` между объектами `Filter`:
    * `items` - массив фильтров FilterItem (`column_name` - поле для фильтрации, `operator` - одно из значений `OperatorValue`, `value` - массив значений фильтра);
    * `link_operator` - логика наложения фильтров `items` (`and` или `or`).

Операторы фильтра `OperatorValue`:
* `contains` - содержит подстроку (без учета регистра);
* `not_contains` - не содержит подстроку (без учета регистра);
* `equals` - равно;
* `not_equals` - не равно;
* `greater` - больше, в `values` передается массив, содержащий только одно значение;
* `greater_equal` - больше или равно, в `values` передается массив, содержащий только одно значение;
* `less_equal` - меньше или равно, в `values` передается массив, содержащий только одно значение;
* `date_range` - диапазон дат, в `values` передается:
    * массив из двух элементов [<левая граница включительно>, <правая граница исключительно>], если нужно отфильтровать по абсолютному диапазону дат;
    * массив из одного элемента ["hour" | "today" | "yesterday" | "cur_week" | "prev_week" | "cur_month" | "prev_month"], если нужно отфильтровать по относительному диапазону дат.

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