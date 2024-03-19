# Настройка удаленной передачи системных логов

Настройка отвечает за передачу системных логов в коллекторы логов или в SIEM-системы.

## Общие настройки

<details>
<summary>Включение/выключение модуля</summary>

**Проверка состояния:**

```
GET /logs_backend/remote_syslog/state
```

**Ответ на успешный запрос:**

```
{
  "enabled": boolean (true - включен, false - выключен)
}
```

**Включение/выключение**

```
PUT /logs_backend/remote_syslog/state
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
<summary>Получение состояния работы модуля</summary>

```
GET /logs_backend/remote_syslog/status
```

**Ответ на успешный запрос:**

```
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

<details>
<summary>Получение настроек удаленной передачи системных логов</summary>

```
GET /logs_backend/remote_syslog
```

**Ответ на успешный запрос:**

```
{
  "host": "string",
  "port": "int",
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef"
}
```

* `host` - IP-адрес сервера;
* `port` - порт;
* `protocol` - протокол, допустимые значения `tcp` или `udp`;
* `format` - формат, допустимые значения `syslog` или `cef`.

</details>

<details>
<summary>Изменение настроек удаленной передачи системных логов</summary>

```
PATCH /logs_backend/remote_syslog
```

**Json-тело запроса:**

```
{
  "host": "string" | null,
  "port": "int" | null,
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef",
}
```

Пустые значения "" не допускаются.

Ответ: 200 ОК

</details>

<details>
<summary>Получение данных о логировании для таблицы</summary>

```
GET /logs_backend/logs?<GET-параметры, разделенные знаком &>`
```

Перечень GET-параметров:
* `limit: integer` - ограничение на количество записей, выбираемых из базы данных;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи, указанные в `limit`;
* `sort: [Sort]` - непустой список параметров сортировки Sort. Сортировка производится в прямом порядке следования в массиве;
* `filter: [Filter]` - непустой массив наборов фильтров Filter с параметрами фильтрации данных. Фильтры применяются в прямом порядке следования в массиве, с логикой И между объектами Filter;
* `search: Search` - объект Search с параметрами поиска подстроки в данных;
* `last_reboot_only` - параметр типа 'boolean' со значениями: false - выводить все записи лога, true - только записи после последней загрузки;
* `format_type` - формат возвращаемых данных:
  * `CSV` - CSV-файл;
  * `JSON` - тип по умолчанию.

Все параметры - необязательны.

**Ответ на успешный запрос:**

```
{
  "meta": [
    {
      "name": "string",
      "type": "string",
    },
  ],
  "data": [ "Log", ],
  "rows": int,
  "rows_before_limit_at_least": int
}
```

* `meta` - массив метаданных, описывающих поля запроса:
  * `name` - имя поля данных;
  * `type` - тип данных;
* `data` - массив из `Log` для отображения в таблице; 
* `Log` - объект с данными, соответствующими одной строке таблицы;
* `rows` - количество `Log`;
* `rows_before_limit_at_least` - количество строк, которое вернет запрос без ограничения на количество записей, выбираемых из базы данных (GET-параметр `limit`), и количество строк, которые необходимо пропустить, прежде чем начать выводить записи (GET-параметр `offset`). Если в параметрах запроса отсутствуют `limit` и `offset`, поле `rows_before_limit_at_least` в ответе на запрос будет отсутствовать.

</details>

## Объекты 

<details>
<summary>Объект Log</summary>

```
  {
    "id": "string",
    "date_time": int,
    "microseconds": int,
    "priority": int,
    "message": "string",
    "syslog_id": "string",
    "unit": "string"
}
```

* `id` - идентификатор строки;
* `date_time` - время возникновения события в формате YYYYMMDDhhmmss;
* `microseconds` - микросекунды во времени возникновения события (0...999999);
* `priority` - число 0...7:
    * 0 - LOG_EMERG - system is unusable;
    * 1 - LOG_ALERT - action must be taken immediately;
    * 2 - LOG_CRIT - critical conditions;
    * 3 - LOG_ERR - error conditions;
    * 4 - LOG_WARNING - warning conditions;
    * 5 - LOG_NOTICE - normal but significant condition;
    * 6 - LOG_INFO - informational;
    * 7 - LOG_DEBUG - debug-level messages;
* `message` - сообщение логирования;
* `syslog_id` - имя исполняемой программы (короткое);
* `unit` - имя сервиса, чьё сообщение сохранено в журнале.

</details>

<details>
<summary>Параметр сортировки Sort</summary>

```
  {
    "field": "string",
    "direction": "asc" | "desc"
  }
```

* `field` - столбец (поле), по которому производится сортировка;
* `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию.

</details>

<details>
<summary>Поиск вхождения строки - объект Search</summary>

```
    {
      "text": "string",
      "columns": ["string"],
    }
```

* `text` - искомая строка;
* `columns` - непустой набор полей, по которым ведется поиск.

Поиск строки - регистронезависимый.

</details>

## Фильтрация

<details>
<summary>Набор фильтров Filter</summary>

```
{
  "items": [ FilterItem ],
  "link_operator": "and" | "or"
}
```

* `items` - массив фильтров FilterItem;
* `link_operator` - логика наложения фильтров `items`, "И" | "ИЛИ".

</details>

<details>
<summary>Фильтр FilterItem</summary>

```
    {
      "column_name": "string",
      "operator": "OperatorValue",
      "value": ["string" | int | boolean],
    }
```

* `column_name` - поле для фильтрации
* `operator` - одно из значений [OperatorValue](#operatorValue)
* `value` - массив значений фильтра. Максимальное количество передаваемых в массиве значений - 255. Данные отбираются по логике ИЛИ. 
 
Например:
  
```
    {
      "column_name": "priority",
      "operator": "equals",
      "value": [4, 6],
    }
```

означает, что нужно отобрать данные, в которых поле `priority` равно "LOG_WARNING" ИЛИ "LOG_INFO"

</details>

<details>
<summary>Оператор фильтра OperatorValue</summary>

Операторы:

  * `contains` - содержит подстроку (без учета регистра);
  * `not_contains` - не содержит подстроку (без учета регистра);
  * `equals` - равно;
  * `not_equals` - не равно;
  * `greater` - больше, в `values` передаётся массив, содержащий только одно значение;
  * `greater_equal` - больше или равно, в `values` передается массив, содержащий только одно значение;
  * `less` - меньше, в `values` передаётся массив, содержащий только одно значение;
  * `less_equal` - меньше или равно, в `values` передается массив, содержащий только одно значение;
  * `date_range` - диапазон дат, в `values` передается:
    * массив из двух элементов `[<левая граница включительно>, <правая граница исключительно>]`, если нужно отфильтровать по абсолютному диапазону дат;
    * массив из одного элемента `["today | yesterday | cur_week | prev_week | cur_month | prev_month"]`, если нужно отфильтровать по относительному диапазону дат.

Применимость фильтров к полям:

* `date_time` - `greater_equal`, `less_equal`, `date_range`;
* `microseconds` - `greater_equal`, `less_equal`, `equals`, `not_equals`; 
* `priority` - `greater_equal`, `less_equal`, `equals`;
* `message` - `contains`, `not_contains`;
* `syslog_id` - `equals`, `not_equals`;
* `unit` - `equals`, `not_equals`.

</details>

## Получение списка имен исполняемых программ (`syslog_id`)

```
GET /logs_backend/syslog_ids
```

**Ответ на успешный запрос:**

```
[ "string" ]
```

## Получение списка имен сервисов (`unit`)

```
GET /logs_backend/units
```

**Ответ на успешный запрос:**

```
[ "string" ]
```