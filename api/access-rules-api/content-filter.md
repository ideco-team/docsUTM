# Контент-фильтр

<details>

<summary>Включение/выключение Контент-фильтра</summary>

## Проверить включенность

```
GET /content-filter/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - состояние **Контент-фильтра**: `true` - включен, `false` - выключен.

## Включить/выключить Контент-фильтр

```
PUT /content-filter/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` для включения **Контент-фильтра**, `false` для выключения.

**Ответ на успешный запрос:** 200 ОК

</details>

## Настройки

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

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS): `true` - включена, `false` - выключена;
* `quic_reject_enabled` - запрет трафика по протоколу QUIC: `true` - включен, `false` - выключен.

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
    "quic_reject_enabled": "boolean"
}
```

* `enabled_extended_categorizer` - расширенная категоризация (SkyDNS): `true` - включена, `false` - выключена;
* `quic_reject_enabled` - запрет трафика по протоколу QUIC: `true` - включен, `false` - выключен.

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

* `enabled` - состояние безопасного поиска: `true` - включен, `false` - выключен.

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

* `enabled` - `true` для включения, `false` для выключения.

**Ответ на успешный запрос:** 200 OK

</details>

## Категории Контент-фильтра

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
  * `users` - пользовательские категории;
  * `extended` - расширенные категории (SkyDNS);
  * `files` - категории для файлов;
  * `special` - специальные предопределенные категории (Прямое обращение по IP, Все категоризированные запросы, Все некатегоризированные запросы, Все запросы);
  * `other` - остальные категории.
* `name` - имя категории;
* `comment` - описание категории.

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
        "id": "string",
        "name": "string",
        "comment": "string",
        "urls": [ "string" ]
    },
    ...
]
```

* `id` - идентификатор категории в формате `users.id.1`;
* `name` - название категории, не пустая строка;
* `comment` - комментарий;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

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

* `name` - название категории, не пустая строка;
* `comment` - комментарий;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

**Ответ на успешный запрос:** 

```json5
{
    "id": "string"
}
```

* `id` - идентификатор пользовательской категории.

</details>

<details>

<summary>Редактирование пользовательских категорий</summary>

```
PUT /content-filter/users_categories/<id категории>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

* `name` - название категории, не пустая строка;
* `comment` - комментарий;
* `urls` - список адресов. Полный путь до страницы или только доменное имя, любое количество любых символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "name": "string",
    "comment": "string",
    "urls": [ "string" ]
}
```

* `id` - идентификатор пользовательской категории.

</details>

## Правила Контент-фильтра

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
        "http_methods": [ "string" ],
        "content_types": [ "string" ],
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
POST /content-filter/rules?anchor_item_id=<id правила>&insert_after={true|false}
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
    "http_methods": [ "string" ],
    "content_types": [ "string" ],
    "access": "allow" | "deny" | "bump" | "redirect",
    "redirect_url": "string" | "null",
    "enabled": "boolean",
    "timetable": [ "string" ]
}
```

* `name` - название правила, не пустая строка;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `parent_id` - идентификатор группы в Ideco Center, в которую входит Ideco NGFW, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
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
    "http_methods": [ "string" ],
    "content_types": [ "string" ],
    "access": "allow | deny | bump | redirect",
    "redirect_url": "string" | "null",
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

## Морфологический анализ

<details>
<summary>Получение текущего состояние модуля морфологического анализа</summary>

```
GET /content-filter/morph_analysis/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - состояние: `true` - включен, `false` - выключен.

</details>

<details>
<summary>Изменение состояния модуля морфологического анализа</summary>

```
PUT /content-filter/morph_analysis/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - состояние: `true` - включен, `false` - выключен.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение списка словарей</summary>

```
GET /content-filter/morph_analysis_dicts
```

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "title": "string",
        "comment": "string",
        "enabled": "boolean",
        "read_only": "boolean",
        "threshold": "integer",
        "words": [
            {
            "value":  "string",
            "weight": "integer"
            },
            ...
        ],
        "from_central_console": "boolean"
    },
    ...
]
```

* `id` - идентификатор словаря, формируется автоматически при добавлении правила;
* `title` - название словаря, максимальная длина - 42 символа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включен, `false` - выключен. Предустановленные словари по умолчанию выключены, дополнительные - включены;
* `read_only` - тип словаря: `true` - предустановленный, `false` - дополнительный;
* `threshold` - пороговый вес словаря, целое неотрицательное число. Может быть равен нулю, но не должен быть пустым. Если пороговый вес равен нулю, страница блокируется при наличии любого слова из словаря весом больше нуля;
* `words` - массив словарей:
    * `value` - слово/словосочетание. Длина - не больше 50 символов. Количество слов в словаре - не больше 1000;
    * `weight` - вес в словаре, целое неотрицательное число, может быть равен нулю.
* `from_central_console` - `true`, если словарь сформирован в Ideco Center, только для чтения.

</details>

<details>
<summary>Создание дополнительного словаря</summary>

```
POST /content-filter/morph_analysis_dicts
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string",
    "enabled": "boolean",
    "read_only": "boolean",
    "threshold": "integer",
    "words": [
        {
          "value":  "string",
          "weight": "integer", 
        },
        ...
    ]
}
```

* `title` - название словаря, максимальная длина - 42 символа;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включен, `false` - выключен;
* `read_only` - тип словаря: `true` - предустановленный, `false` - дополнительный;
* `threshold` - пороговый вес словаря, целое неотрицательное число. Может быть равен нулю, но не должен быть пустым. Если пороговый вес равен нулю, страница блокируется при наличии любого слова из словаря весом больше нуля;
* `words` - массив словарей:
    * `value` - слово/словосочетание. Длина - не больше 50 символов. Количество слов в словаре - не больше 1000;
    * `weight` - вес в словаре, целое неотрицательное число, может быть равен нулю.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного словаря.

</details>

<details>
<summary>Редактирование дополнительного словаря</summary>

```
PATCH /content-filter/morph_analysis_dicts/<id словаря>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "enabled": "boolean", 
    "comment": "string",
    "threshold": "integer",
    "words": [
        {
          "value":  "string",
          "weight": "integer", 
        },
        ...
    ]
}
```

* `title` - название словаря, максимальная длина - 42 символа;
* `enabled` - статус: `true` - включен, `false` - выключен;
* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `threshold` - пороговый вес словаря, целое неотрицательное число. Может быть равен нулю, но не должен быть пустым. Если пороговый вес равен нулю, страница блокируется при наличии любого слова из словаря весом больше нуля;
* `words` - массив словарей:
    * `value` - слово/словосочетание. Длина - не больше 50 символов. Количество слов в словаре - не больше 1000;
    * `weight` - вес в словаре, целое неотрицательное число, может быть равен нулю.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление дополнительного словаря</summary>

```
DELETE /content-filter/morph_analysis_dicts/<id словаря>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Скачивание словаря</summary>

```
GET /content-filter/morph_analysis_dicts/download/<id словаря>
```

**Ответ на успешный запрос:** файл в формате CSV. В первой строке записан пороговый вес словаря;название словаря;комментарий. В последующих строках представлены слова и их вес. Пример:

```
100;Словарь;Комментарий
слово;20
словосочетание;20
```

</details>