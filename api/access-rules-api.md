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

```json5
[
   {
      "name": "rules-in-kernel",
      "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
      "msg": [ "string" ]
  },
  {
        "msg": [ "string" ],
        "status": "active",
        "name": "auto-snat"
    }
]
```

* `msg` - список строк, поясняющих текущее состояние.

</details>

<details>
<summary>Получение настроек Файрвола</summary>

### Включенность пользовательских правил

```
GET /firewall/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
} 
```

* `enabled` - опция раздела **Файрвол**: `true` - включена, `false` - выключена.

### Логирование правил

```
GET /firewall/settings
```

**Ответ на успешный запрос:**

```json5
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": [ "accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log" ]
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT: `true` - включен, `false`- выключен;
* `log_mode` - режим логирования;
* `log_actions` - события, которые будут логироваться.

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /firewall/settings
```

**Json-тело запроса:**

```json5
{
    "automatic_snat_enabled": "boolean",
    "log_mode": "nothing" | "all" | "selected",
    "log_actions": [ "accept" | "drop" | "dnat" | "snat" | "mark_log" | "mark_not_log" ]
} 
```

* `automatic_snat_enabled` - включение автоматического SNAT: `true` - включен, `false`- выключен;
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

**Ответ на успешный запрос:** объекты FilterRuleObject, DnatRuleObject, SnatRuleObject

**Объект FilterRuleObject** (разделы FORWARD и INPUT)

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
    "action": "accept" | "drop"
}
```

* `id` - идентификатор правила.
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `enabled` - если `true`, то правило включено, `false` - выключено;
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
* `dpi_enabled` - если `true`, то обработка с помощью модуля **Контроль приложений** включена, `false` - выключена;
* `ips_profile` - строка в формате UUID, идентификатор профиля IPS. Не может быть пустой строкой, если `ips_enabled` = `true`;
* `ips_enabled` - если `true`, то обработка с помощью модуля **Предотвращение вторжений** включена, `false` - выключена;
* `timetable` - время действия;
* `comment` - комментарий, может быть пустым;
* `action` - действие:
  * `accept` - разрешить;
  * `drop` - запретить.

**Объект DnatRuleObject** (раздел DNAT)

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
    "action": "accept" | "dnat",
    "change_destination_address": "null" | "string",
    "change_destination_port": "null" | "string"
}
```

* `id` - идентификатор правила.
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `enabled` - если `true`, то правило включено, `false` - выключено;
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `source_ports` - порты источников, список идентификаторов алиасов;
* `incoming_interface` - зона источника;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `timetable` - время действия;
* `comment` - комментарий, может быть пустым;
* `action` - действие:
  * `accept` - разрешить;
  * `dnat` - производить DNAT.
* `change_destination_address` - IP-адрес или диапазон IP-адресов для замены назначения, или `null`, если `action` = `accept`;
* `change_destination_port` - порт или диапазон портов для замены значения, или `null`, если `action` = `accept`.

**Объект SnatRuleObject** (раздел SNAT)

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
    "action": "accept" | "snat",
    "change_source_address": "null" | "string"
}
```

* `id` - идентификатор правила.
* `parent_id` - идентификатор группы в Ideco Center, в которую входит сервер, или константа `f3ffde22-a562-4f43-ac04-c40fcec6a88c` (соответствует Корневой группе);
* `enabled` - если `true`, то правило включено, `false` - выключено;
* `protocol` - протокол;
* `source_addresses` - адрес источника;
* `source_addresses_negate` - инвертировать адрес источника;
* `source_ports` - порты источников, список идентификаторов алиасов;
* `destination_addresses` - адрес назначения;
* `destination_addresses_negate` - инвертировать адрес назначения;
* `destination_ports` - порты назначения;
* `outgoing_interface` - зона назначения;
* `timetable` - время действия;
* `action` - действие:
  * `accept` - разрешить;
  * `snat` - производить SNAT.
* `change_destination_address` - IP-адрес для замены источника, или `null`, если `action` = `accept`.

</details>

<details>
<summary>Добавление правила</summary>

* `POST /firewall/rules/forward?anchor_item_id=<id правила>&insert_after={true|false}` - раздел FORWARD;
* `POST /firewall/rules/input?anchor_item_id=<id правила>&insert_after={true|false}` - раздел INPUT;
* `POST /firewall/rules/dnat?anchor_item_id=<id правила>&insert_after={true|false}` - раздел DNAT;
* `POST /firewall/rules/snat?anchor_item_id=<id правила>&insert_after={true|false}` - раздел SNAT;
* `POST /firewall/rules/log?anchor_item_id=<id правила>&insert_after={true|false}` - раздел Логирование.

  * `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое. Если отсутствует, то новое правило будет добавлено в конец таблицы;
  * `insert_after` - вставка до или после. Если значение `true` или отсутствует, то новое правило будет добавлено сразу после указанного в `anchor_item_id`. Если `false` - на месте указанного в `anchor_item_id`.

**Json-тело запроса:** один из объектов FilterRuleObject (разделы FORWARD и INPUT) | DnatRuleObject (раздел DNAT) | SnatRuleObject (раздел SNAT), описанных в раскрывающемся блоке [**Получение списка правил**](access-rules-api.md#poluchenie-spiska-pravil)

* В запросе не должно быть `id`, так как правило еще не создано и не имеет идентификатора.

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

**Json-тело запроса:** один из объектов FilterRuleObject (разделы FORWARD и INPUT) | DnatRuleObject (раздел DNAT) | SnatRuleObject (раздел SNAT), которые описаны в раскрывающемся блоке [**Получение списка правил**](access-rules-api.md#poluchenie-spiska-pravil), без поля `id`

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
   "enabled": "boolean"
}
```

* `enabled` - если `true`, то счетчик включен, `false` - выключен.

</details>

<details>
<summary>Включение/выключение счетчика срабатывания правил</summary>

```
PUT /firewall/watch
```

**Json-тело запроса:**

```json5
{
   "enabled": "boolean"
}
```

* `enabled` - `true` для включения, `false` для выключения.

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
      "packets": "integer"
   },
   ...
]
```

* `id` - идентификатор правила;
* `packets` - сумма сработанных правила.

</details>

### Проверка прохождения трафика

</details>

<details>
<summary>Получение списка проверок</summary>

```
GET /firewall/checks_packets
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string",
    "enabled": "boolean",
    "protocol": "tcp" | "udp",
    "src_ip": "string",
    "src_port": "integer",
    "dst_ip": "string",
    "dst_port": "integer",
    "incoming_interface": "string",
    "expected_result": "drop" | "accept",
    "comment": "string"
}
```

* `id` - идентификатор проверки;
* `enabled` - включена ли данная проверка;
* `protocol` - протокол, используемый в данной проверке. Может быть `tcp` или `udp`;
* `src_ip` - адрес источника тестовых пакетов;
* `src_port` - порт источника тестовых пакетов;
* `dst_ip` - адрес назначения тестовых пакетов;
* `dst_port` - порт назначения тестовых пакетов;
* `incoming_interface` - идентификатор алиаса сетевого интерфейса, на который приходят тестовые пакеты;
* `expected_result` - ожидаемый результат выполнения проверки. Может быть `drop` или `accept`;
* `comment` - комментарий, может быть пустым.

</details>

<details>
<summary>Добавление новых проверок</summary>

```
POST /firewall/checks_packets
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "protocol": "tcp" | "udp",
    "src_ip": "string",
    "src_port": "integer",
    "dst_ip": "string",
    "dst_port": "integer",
    "incoming_interface": "string",
    "expected_result": "drop" | "accept",
    "comment": "string"
}
```

* `enabled` - включена ли данная проверка;
* `protocol` - протокол, используемый в данной проверке. Может быть `tcp` или `udp`;
* `src_ip` - адрес источника тестовых пакетов;
* `src_port` - порт источника тестовых пакетов;
* `dst_ip` - адрес назначения тестовых пакетов;
* `dst_port` - порт назначения тестовых пакетов;
* `incoming_interface` - идентификатор алиаса сетевого интерфейса, на который приходят тестовые пакеты;
* `expected_result` - ожидаемый результат выполнения проверки. Может быть `drop` или `accept`;
* `comment` - комментарий, может быть пустым.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор созданной проверки.

</details>

<details>
<summary>Редактирование проверок</summary>

```
PATCH /firewall/checks_packets/<id проверки>
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "protocol": "tcp" | "udp",
    "src_ip": "string",
    "src_port": "integer",
    "dst_ip": "string",
    "dst_port": "integer",
    "incoming_interface": "string",
    "expected_result": "drop" | "accept",
    "comment": "string",
},
```

* `enabled` - включена ли данная проверка;
* `protocol` - протокол, используемый в данной проверке. Может быть `tcp` или `udp`;
* `src_ip` - адрес источника тестовых пакетов;
* `src_port` - порт источника тестовых пакетов;
* `dst_ip` - адрес назначения тестовых пакетов;
* `dst_port` - порт назначения тестовых пакетов;
* `incoming_interface` - идентификатор алиаса сетевого интерфейса, на который приходят тестовые пакеты;
* `expected_result` - ожидаемый результат выполнения проверки. Может быть `drop` или `accept`;
* `comment` - комментарий, может быть пустым.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление проверок</summary>

```
PATCH /firewall/checks_packets/<id проверки>
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Запуск проверок</summary>

```
POST /firewall/checks_start
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение результатов проверок</summary>

```
GET /firewall/checks_result
```

**Ответ на успешный запрос:**

```json5
{
    "block_status": "boolean",
    "in_progress": "boolean",
    "check_datetime": "integer",
    "data": { 
        "check_id": {
                "result": "drop" | "accept",
                "rule_id": "string",
                "verdict": "boolean"
                }
    }
}
```

* `block_status` - текущий статус блокировки трафика, вызванный провалом проверок;
* `in_progress` - выполняются ли проверки в данный момент;
* `check_datetime` - время выполнения последних проверок в формате `YYYYMMDDHMS`;
* `data` - словарь результатов проверок, ключ - uuid проверки;
* `result` - результат выполнения проверки, может быть `drop` или `accept`;
* `rule_id` - номер отработавшего правила. Например, `fwd.ngfw.2`;
* `verdict` - совпал ли фактический результат с ожидаемым.

</details>

<details>
<summary>Получение настроек блокировки трафика в случае неудачных проверок</summary>

```
GET /firewall/checks_settings
```

**Ответ на успешный запрос:**

```json5
{
    "block_traffic": "boolean"
}
```

* `block_traffic` - настройка блокировки прохождения трафика при провале какой-либо проверки.

</details>

<details>
<summary>Изменение настроек блокировки трафика в случае неудачных проверок</summary>

```
PUT /firewall/checks_settings
```

**Json-тело запроса:**

```json5
{
    "block_traffic": "boolean"
}
```

* `block_traffic` - настройка блокировки прохождения трафика при провале какой-либо проверки.

**Ответ на успешный запрос:** 200 ОК

</details>

## Контроль приложений

<details>
<summary>Получение списка правил</summary>

```
GET /application_control_backend/rules
```

**Ответ на успешный запрос:**

```json5
[ 
    {
        "action": "drop" | "accept",
        "aliases": [ "string" ],
        "comment": "string",
        "enabled": "boolean",
        "name": "string",
        "parent_id": "string",
        "protocols": [ "string" ],
        "id": "integer"
    },
    ...
 ]
```

* `action` - действие, применяемое к правилу;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md));
* `comment` - комментарий правила;
* `enabled` - статус правила: `true` - включено, `false` - выключено;
* `name` - имя правила;
* `parent_id` - идентификатор родительской группы серверов;
* `protocols` - список протоколов;
* `id` - идентификатор правила.

</details>

<details>
<summary>Создание нового правила</summary>

```
POST /application_control_backend/rules
```

**Json-тело запроса:**

```json5
{
    "parent_id": "string",
    "name": "string",
    "action": "drop" | "accept",
    "comment": "string",
    "aliases": [ "string" ],
    "protocols": [ "string" ],
    "enabled": "boolean"
}
```

* `parent_id` - идентификатор родительской группы серверов;
* `name` - имя правила;
* `action` - действие, применяемое к правилу;
* `comment` - комментарий правила;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md#poluchenie-identifikatorov-obektov));
* `protocols` - список протоколов;
* `enabled` - статус правила: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:**

```json5
{
    "id": "integer"
}
```

* `id` - идентификатор созданного правила.

</details>

<details>
<summary>Изменение правила</summary>

```
PUT /application_control_backend/rules/<id правила>
```

**Json-тело запроса:**

```json5
{
    "parent_id": "string",
    "name": "string",
    "comment": "string",
    "aliases": [ "string" ],
    "protocols": [ "string" ],
    "action": "drop" | "accept",
    "enabled": "boolean"
}
```

* `parent_id` - идентификатор родительской группы серверов;
* `name` - имя правила;
* `comment` - комментарий правила;
* `aliases` - объекты, которые используются в правиле (например, any. Список объектов доступен по [ссылке](/api/description-of-handlers.md#poluchenie-identifikatorov-obektov));
* `protocols` - список протоколов;
* `action` - действие, применяемое к правилу;
* `enabled` - статус правила: `true` - включено, `false` - выключено.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Изменение приоритета правила</summary>

```
PATCH /application_control_backend/rules/move
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
* `anchor_item_id` - идентификатор правила, ниже или выше которого нужно создать новое;
* `insert_after` - вставка до или после. Если `true`, то вставить правило сразу после указанного в `anchor_item_id`, если `false`, то на месте указанного в `anchor_item_id`.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление правила</summary>

```
DELETE /application_control_backend/rules/<id правила>
```

**Ответ на успешный запрос:** 200 OK

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

* `enabled` - состояние **Контент-фильтра**: `true` - включен, `false` - выключен.

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

* `enabled` - `true` для включения **Контент-фильтра**, `false` для выключения.

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

### Морфологический анализ

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
        "central_console": "boolean"
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
* `central_console` - `true`, если словарь сформирован в Центральной консоли, только для чтения.

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
        "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
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

* `"column_name":"classtype","operator":"equals","value":[<classtype нужной группы сигнатур (может быть несколько значений через запятую)>]` - фильтр. Отбирает из таблицы групп сигнатур только те группы, у которых значение `classtype` соответствует указанным в `value`.

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
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`);
* `flow` - направление трафика (`to_server`, `from_server`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK;
* `signature_source` - источник сигнатуры;
* `msg` - название сигнатуры;
* `source` - источник подключения;
* `source_ports` - порты источника;
* `destination` - назначение;
* `destination_ports` - порты назначения;
* `updated_at` - дата в формате `YYYY-MM-DD` или строка со значением `-`.

</details>

<details>

<summary>Получение списка сигнатур в определенном профиле</summary>

```
GET /ips/profiles/<id профиля>/signatures
```

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
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`);
* `flow` - направление трафика (`to_server`, `from_server`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK;
* `signature_source` - источник сигнатуры;
* `msg` - название сигнатуры;
* `source` - источник подключения;
* `source_ports` - порты источника;
* `destination` - назначение;
* `destination_ports` - порты назначения;
* `updated_at` - дата в формате `YYYY-MM-DD` или строка со значением `-`.

</details>

<details>

<summary>Получение количества сигнатур профиля для каждого действия</summary>

```
GET /ips/profiles/actions-counts 
```

* Чтобы получить список для конкретного профиля - `/ips/profiles/<id профиля>/actions-counts`.

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

* `profile_id` - идентификатор профиля:
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
 
</details>

<details>
<summary>Получение оригинального содержания сигнатуры</summary>

```
GET /ips/signatures/<sid>
```

* `sid` - идентификатор сигнатуры.
  
**Ответ на успешный запрос:**

```json
{
    "signature": "string"
}
```

* `signature` - содержание сигнатуры.

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
* `rule` - строка с правилом, не более 8196 символов;
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
* `rule` - строка с правилом, не более 8196 символов, переводы строк в ней запрещены.

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
    "status": "up_to_date" | "updating" | "failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float" | "null"
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
    "status": "up_to_date" | "updating" | "failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float" | "null"
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
* `address` - адрес подсети (например, `192.168.0.0/16`).

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

* `address` - адрес подсети (например, `192.168.0.0/16`).

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
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.

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
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.

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
* `enabled` - состояние исключения: `true` - включено, `false` - выключено.

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
<summary>Проверить включенность подсчета квот</summary>

```
GET /quotas/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - если `true`, то подсчет квот включен, `false` - выключен.

</details>

<details>
<summary>Включение/выключение подсчета квот</summary>

```
PUT /quotas/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` для включения, `false` для выключения.

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
* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
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

* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор квоты.

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

* `title` - название квоты, максимальная длина - 42 символа;
* `comment` - комментарий, максимальная длина - 255 символов;
* `quota` - ограничение трафика в байтах;
* `enabled` - применяется ли квота;
* `interval` - период действия квоты (час, день, неделя, месяц, квартал).

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление квоты</summary>

```
DELETE /quotas/quotas/<id квоты>
```

**Ответ на успешный запрос:** 200 ОК

</details>