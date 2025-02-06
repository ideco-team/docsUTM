# Управление профилями безопасности

## Предотвращение вторжений

Путь в веб-интерфейсе NGFW: **Профили безопасности -> Предотвращение вторжений**

<details>
<summary>Получение списка профилей</summary>

```
GET /ips/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string"
  },
  ...
]
```
* `id` - идентификатор профиля или фиксированная строка `__DEFAULT_IPS_PROFILE_ID__` (шаблонный профиль);
* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

Шаблонный профиль отображается в режиме **Только для чтения**. Идентификатор шаблонного профиля не может быть использован в запросах на изменение/удаление профиля и на создание/изменение/перемещение/удаление правил профиля.

</details>

<details>
<summary>Создание профиля</summary>

```
POST /ips/profiles
```
**Json-тело запроса:**:

```json5
{
    "name": "string",
    "comment": "string"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:**

```json5
{
  "id": "string"
}
```

* `id` - идентификатор профиля.

</details>

<details>
<summary>Изменение профиля</summary>

```
PATCH /ips/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "comment": "string"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление профиля</summary>

```
DELETE /ips/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение списка правил профиля</summary>

```
GET /ips/profiles/<profile_id>/rules
```

* `profile_id` - идентификатор профиля, список правил которого запрашивается (без скобок и кавычек).

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "integer",
    "filters": [
      {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ],
     },
    ...
    ]
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
  },
  ...
]
```

* `id` - номер правила выбора сигнатур;
* `filters` - список фильтров правила (список не может быть пустым):
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина 255 символов.

</details>

<details>
<summary>Создание правила в профиле</summary>

```
POST /ips/profiles/<profile_id>/rules?anchor_item_id=<integer>&insert_after=<true|false>
```

* `profile_id` - идентификатор профиля, в котором создается правило (без скобок и кавычек);
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "filters": [
       {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ]
      },
      ...
    ],
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
}
```

* `filters` - список фильтров правила (список не может быть пустым):
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 

```json5
{
  "id": "integer"
}
```

* `id` - номер правила выбора сигнатур.

</details>

<details>
<summary>Изменение правила в профиле</summary>

```
PATCH /ips/profiles/<profile_id>/rules/<rule_id>
```

* `profile_id` - идентификатор профиля, в котором изменяется правило;
* `rule_id` - идентификатор правила в профиле.

**Json-тело запроса:** (некоторые или все поля объекта)

```json5
{
    "filters": [
      {
        "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
        "operator": "equals",
        "values": [ "string" | "integer" ]
       },
      ...
    ],
    "action": "default" | "alert" | "drop" | "pass",
    "comment": "string"
}
```

* `filters` - список фильтров правила (список не может быть пустым):
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
* `action` - строка с действием при срабатывании правила;
* `comment` - комментарий, максимальная длина - 255 символов.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Перемещение правила в профиле</summary>

```
PATCH /ips/profiles/rules/move
```

**Json-тело запроса:**:

```json5
{
    "params": {
        "profile_id": "string",
        "rule_id": "integer",
        "anchor_item_id": "integer",
        "insert_after": "boolean"
    }
}
```

* `profile_id` - идентификатор профиля, в котором перемещается правило;
* `rule_id` - идентификатор правила в профиле;
* `anchor_item_id` - идентификатор правила, выше или ниже которого нужно разместить `rule_id`;
* `insert_after` - вставить до (`false`) или после (`true`) правила `anchor_item_id`.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Удаление правила в профиле</summary>

```
DELETE /ips/profiles/<profile_id>/rules/<rule_id>
```

* `profile_id` - идентификатор профиля, в котором удаляется правило;
* `rule_id` - идентификатор правила в профиле.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Создание профиля с правилами</summary>

```
POST /ips/profiles-create-with-rules
```

**Json-тело запроса:**: 

```json5
{
    "name": "string",
    "comment": "string",
    "rules": [
          {
          "filters": [
                {
                "key": "sid" | "mitre_tactic_id" | "protocol" | "signature_severity" | "flow" | "classtype",
                "operator": "equals",
                "values": [ "string" | "integer" ]
                  },
                  ...
                ],
          "action": "default" | "alert" | "drop" | "pass",
          "comment": "string"
          },
          ...
        ]
    }
```

* `name` - название профиля, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `rules` - список правил профиля:
  * `filters` - список фильтров правила (список не может быть пустым):
    * `key` - поле фильтра (`sid` - идентификатор, `mitre_tactic_id` - тактика MITRE, `protocol` - протокол, `signature_severity` - уровень серьезности, `flow` - направление, `classtype` - класс);
    * `operator` - оператор, только `equals`;
    * `values` - список значений, которые должны принимать поля `key` (если `key` - `sid`, то `values` - число).
  * `action` - строка с действием при срабатывании правила;
  * `comment` - комментарий, максимальная длина 255 символов.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного профиля с правилами.

</details>

<details>

<summary>Копирование профиля с правилами</summary>

```
POST /ips/profiles/<id профиля>/copy
```

В качестве `id профиля` может быть указана фиксированная строка `__DEFAULT_IPS_PROFILE_ID__` для создания копии шаблонного профиля. Поле **Комментарий** будет заменено на пустую строку.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданного профиля.

</details>

<details>

<summary>Получение списка сигнатур в определенном профиле</summary>

```
GET /ips/profiles/<id профиля>/signatures
```

В качестве `id профиля` может быть указана фиксированная строка `__DEFAULT_IPS_PROFILE_ID__` для получения списка сигнатур шаблонного профиля.

**Ответ на успешный запрос:**

```json5
{
    "signatures": [
        {
            "action": "string",
            "protocol": "string",
            "flow": "string",
            "classtype": "string-admin",
            "sid": "integer",
            "signature_severity": "string",
            "mitre_tactic_id": "string",
            "signature_source": "string",
            "msg": "string",
            "source": "string",
            "source_ports": "string",
            "destination": "string",
            "destination_ports": "string",
            "updated_at": "string"
        },
        ...
    ]
}
```

* `action` - действие для трафика, соответствующего сигнатуре:
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`). Возможные значения представлены по [ссылке](https://docs.suricata.io/en/latest/rules/intro.html#protocol);
* `flow` - направление трафика (`client2server`, `server2client`, `-`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK;
* `signature_source` - источник сигнатуры: 
    * `standard` - стандартные правила;
    * `advanced` - правила IPS от Лаборатории Касперского;
    * `custom` - пользовательские правила.
* `msg` - название сигнатуры;
* `source` - источник подключения;
* `source_ports` - порты источника;
* `destination` - назначение;
* `destination_ports` - порты назначения;
* `updated_at` - дата в формате `YYYY-MM-DD` или строка со значением `-`.

</details>

<details>

<summary>Получение количества сигнатур профиля по действиям для всех профилей</summary>

```
GET /ips/profiles/actions-counts 
```

**Ответ на успешный запрос:**

```json5
{
    "profile_id": {
      "pass": "integer",
      "alert": "integer",
      "drop": "integer",
      "rejectsrc": "integer",
      "rejectdst": "integer",
      "rejectboth": "integer"
    },
    ...
}
```

* `profile_id` - идентификатор профиля или фиксированная строка `__DEFAULT_IPS_PROFILE_ID__` (шаблонный профиль):
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
 
</details>

<details>

<summary>Получение количества сигнатур профиля по действиям для конкретного профиля</summary>

```
GET /ips/profiles/<id профиля>/actions-counts
```

**Ответ на успешный запрос:**

```json5
{
    "rule_id": {
      "pass": "integer",
      "alert": "integer",
      "drop": "integer",
      "rejectsrc": "integer",
      "rejectdst": "integer",
      "rejectboth": "integer"
    },
    ...
}
```

* `rule_id` - идентификатор правила в профиле:
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
 
</details>

<details>
<summary>Получение профилей Предотвращения вторжений, которые содержат определенную сигнатуру</summary>

```
GET /ips/signatures/<sid>/profiles
```

* `sid` - идентификатор сигнатуры.

**Ответ на успешный запрос:**

```json
{
    "id": "string",
    "name": "string"
}
```

* `id` - идентификатор профиля;
* `name` - название профиля.
  
</details>


## Профили Web Application Control (WAF)

<details>

<summary>Получение списка профилей</summary>

```
GET /reverse_proxy_backend/waf/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "exceptions": [
      {
        "id": "string",
        "rule_id": "integer",
        "comment": "string",
        "enabled": "boolean"
      },
      ...
    ],
    "server_tokens": "boolean",
    "comment": "string",
    "from_central_console": "boolean"
  },
  ...
]
```

* `id` - идентификатор профиля;
* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий для исключения, максимальная длина - 128 символов;
* `exceptions` - исключенные правила:
  * `id` - идентификатор исключенного правила;
  * `rule_id` - идентификатор исключенного правила в профиле;
  * `comment` - комментарий, максимальная длина - 255 символов;
  * `enabled` - статус: `true` - включено, `false` - выключено.
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `from_central_console` - `true`, если профиль создан в Ideco Center, только для чтения.

</details>

<details>

<summary>Создание профиля</summary>

```
POST /reverse_proxy_backend/waf/profiles
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "server_tokens": "boolean",
    "comment": "string",
    "from_central_console": "boolean"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий для исключения, максимальная длина - 128 символов, при создании профиля может быть пустым;
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `from_central_console` - `true`, если профиль создан в Ideco Center, только для чтения.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

</details>

<details>

<summary>Изменение профиля</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
{
    "name": "string",
    "detection_only": "boolean",
    "disabled_categories": ["string"],
    "server_tokens": "boolean",
    "comment": "string",
    "from_central_console": "boolean"
}
```

* `name` - название профиля, максимальная длина - 42 символа;
* `detection_only` - режим работы: `true` - только обнаружение, `false` - обнаружение и блокировка;
* `disabled_categories` - список идентификаторов категорий правил, которые были отключены, максимальная длина - 128 символов;
* `server_tokens` - статус HTTP-заголовка Server: `true` - показывать, `false` - скрывать;
* `comment` - комментарий, может быть пустым, максимальная длина - 255 символов;
* `from_central_console` - `true`, если профиль создан в Ideco Center, только для чтения.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Удаление профиля</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>

<summary>Получение списка категорий правил</summary>

```
GET /reverse_proxy_backend/waf/categories
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string",
    "required": "boolean",
    "description": "string"
  },
  ...
]
```

* `id` - идентификатор категории, максимальная длина - 42 символа;
* `title` - название категории, максимальная длина - 42 символа;
* `required` - является ли категория необходимой, т.е. еe нельзя будет выключать;
* `description` - описание категории, максимальная длина - 255 символов.

</details>

<details>

<summary>Получение списка категорий правил в профиле</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/categories
```

**Ответ на успешный запрос:**

* Список категорий правил, которые включены в профиле.

```json5
[
  {
    "id": "string",
    "title": "string",
    "required": "boolean",
    "description": "string"
  },
  ...
]
```

* `id` - идентификатор категории, максимальная длина - 42 символа;
* `title` - название категории, максимальная длина - 42 символа;
* `required` - является ли категория необходимой, т.е. еe нельзя будет выключать;
* `description` - описание категории, максимальная длина - 255 символов.

</details>

<details>

<summary>Добавление или удаление категории правил в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/categories/<id категории>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:**

* Если профиль или категория не найдены по идентификатору, то код ответа - 542;
* Если enabled - `true`, то категория, идентификатор которой указан в запросе, будет удалена из списка `disabled_categories` профиля. Ответ - 200 ОК;
* Если enabled - `false`, то категория, идентификатор которой указан в запросе, будет добавлена в список `disabled_categories` профиля. Ответ - 200 ОК.

</details>

<details>

<summary>Получение белых и черных списков в профиле</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/rules
```

**Ответ на успешный запрос:**

```json5
[
  {
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean",
    "id": "integer"
  },
  ...
]
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено;
* `id` - номер правила.

</details>

<details>

<summary>Создание белых и черных списков в профиле</summary>

```
POST /reverse_proxy_backend/waf/profiles/<id профиля>/rules?anchor_item_id=<integer>&insert_after=<true|false>
```

* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Json-тело запроса:**

```json5
{
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>

<summary>Изменение белых и черных списков в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/rules/<id правила в профиле>
```

**Json-тело запроса:**

```json5
{
    "aliases": ["string"],
    "aliases_negate": "boolean",
    "action": "block" | "pass",
    "comment": "string",
    "enabled": "boolean"
}
```

* `aliases` - список алиасов IP-адресов, подсетей, стран, списков стран и континентов;
* `aliases_negate` - инверсия правила;
* `action` - действие:
  * `block` - блокировать запросы;
  * `pass` - пропускать запросы.
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Перемещение белых и черных списков в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/rules/move
```

**Json-тело запроса:**

```json5
{
  "params": {
    "profile_id": "string",
    "rule_id": "integer",
    "anchor_item_id": "integer",
    "insert_after": "boolean",
  },
}
```

* `profile_id` - идентификатор профиля, в котором перемещается правило;
* `rule_id` - идентификатор перемещаемого правила;
* `anchor_item_id` - идентификатор правила, относительно которого будет перемещено правило;
* `insert_after` - вставить правило до или после `anchor_item_id`. Если `true` или отсутствует, то вставить правило сразу после указанного в `anchor_item_id`. Если `false`, то на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление белых и черных списков в профиле</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Получение списка исключенных правил профиля</summary>

```
GET /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
  },
  ...
]
```

* `id` - идентификатор исключенного правила;
* `rule_id` - идентификатор правила;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

</details>

<details>

<summary>Создание исключенного правила в профиле</summary>

```
POST /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions
```

**Json-тело запроса:**

```json5
{
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
}
```

* `rule_id` - идентификатор правила. Можно найти в журнале в разделе **Отчеты и журналы -> События безопасности -> [Web Application Firewall](/settings/reports/security-events.md#web-application-firewall)**;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

</details>

<details>

<summary>Изменение исключенного правила в профиле</summary>

```
PATCH /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions/<id исключенного правила>
```

**Json-тело запроса:**

```json5
{
    "rule_id": "integer",
    "comment": "string",
    "enabled": "boolean"
}
```

* `rule_id` - идентификатор правила. Можно найти в журнале в разделе **Отчеты и журналы -> События безопасности -> [Web Application Firewall](/settings/reports/security-events.md#web-application-firewall)**;
* `comment` - комментарий, максимальная длина - 255 символов;
* `enabled` - статус: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление исключенного правила в профиле</summary>

```
DELETE /reverse_proxy_backend/waf/profiles/<id профиля>/exceptions/<id исключенного правила>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Контроль приложений

<details>

<summary>Получение списка профилей</summary>

```
GET /api/application_control/profiles
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
    ],
  }
]
```

* `id` - идентификатор профиля;
* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).      

</details>

<details>

<summary>Создание профиля</summary>

```
POST /api/application_control/profiles
```

**Json-тело запроса:**

```json5

{
  "name": "string",
  "comment": "string",
  "protocols": [
    {
      "id": "string",
      "action": "deny" | "allow"
    },
    ...
    ],
}
```

* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
      ],
  }
]
```

* `id` - идентификатор профиля;
* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

</details>

<details>

<summary>Копирование профиля</summary>

```
POST /api/application_control/profiles/<id профиля>/copy
```

**Ответ на успешный запрос:** 

```json5
{
  "id": "integer"
}
```

* `id` - идентификатор копии профиля.

</details>

<details>

<summary>Редактирование профиля</summary>

```
PATCH /api/application_control/profiles/<id профиля>
```

**Json-тело запроса:**

```json5
[
  {
    "name": "string",
    "comment": "string",
    "protocols": [
      {
        "id": "string",
        "action": "deny" | "allow"
      },
      ...
      ],
  }
]
```

* `name` - название профиля;
* `comment` - комментарий к профилю;
* `protocols` - список протоколов, выбранных для профиля:
    * `id` - строковый идентификатор алиаса протокола с префиксом `id.l7`. Например, `id.l7.ftp_protocol`;
    * `action` - действие, применяемое к протоколу (`deny` - запретить, `allow` - разрешить).

**Ответ на успешный запрос:** 200 OK

</details>

<details>

<summary>Удаление профиля</summary>

```
DELETE /api/application_control/profiles/<id профиля>
```

**Ответ на успешный запрос:** 200 OK

</details>