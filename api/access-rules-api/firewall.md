# Файрвол

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

## Включенность пользовательских правил

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

## Логирование правил

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

## Управление правилами

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

**Json-тело запроса:** один из объектов FilterRuleObject (разделы FORWARD и INPUT) | DnatRuleObject (раздел DNAT) | SnatRuleObject (раздел SNAT), описанных в раскрывающемся блоке [**Получение списка правил**](access-rules-api/firewall.md#poluchenie-spiska-pravil)

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

**Json-тело запроса:** один из объектов FilterRuleObject (разделы FORWARD и INPUT) | DnatRuleObject (раздел DNAT) | SnatRuleObject (раздел SNAT), которые описаны в раскрывающемся блоке [**Получение списка правил**](access-rules-api/firewall.md#poluchenie-spiska-pravil), без поля `id`

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

## Счетчик срабатывания правил

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
* `packets` - сумма сработанных правил.

</details>

## Проверка прохождения трафика

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

**Номер правила в поле `rule_id` будет отсутствовать, если пакет был заблокирован пользовательским правилом INPUT. В этом случае поле `rule_id` будет иметь вид `inp.ngfw`**.

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