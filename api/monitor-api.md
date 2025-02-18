# Мониторинг и журналы

## Монитор трафика

<details>
<summary>Получение списка сессий</summary>

```
GET /reports/traffic/sessions?<GET-параметры, разделенные знаком &>
```

Перечень необязательных GET-параметров:
* `limit: integer` - ограничение на количество срабатываний (строк). Минимальное значение `1`;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `duration`.

**Ответ на успешный запрос:**

```json5
[
    {
        "id": "string",
        "source_ip": "string",
        "src_aliases": ["string"],
        "destination_ip": "string",
        "dst_aliases": ["string"],
        "source_proto": "string",
        "destination_proto": "string",
        "application": "string",
        "duration": "integer",
        "bps_in": "integer",
        "bps_out": "integer",
        "pps_in": "integer",
        "pps_out": "integer",
        "in_iface_alias": "string",
        "out_iface_alias": "string"
    },
    ...
]
```

* `id` - идентификатор сессии, в формате ULID;
* `source_ip` - IP-адрес источника;
* `src_aliases` - список всех id алиасов, связанных с IP-адресом источника;
* `destination_ip` - IP-адрес назначения;
* `dst_aliases` - список всех id алиасов, связанных с IP-адресом назначения;
* `source_proto` - протокол источника (если TCP или UDP, также указывается порт);
* `destination_proto` - протокол назначения (если TCP или UDP, также указывается порт);
* `application` - приложение;
* `duration` -  продолжительность сессии в секундах;
* `bps_in` - входящая скорость трафика (байты в секунду);
* `bps_out` - исходящая скорость трафика (байты в секунду);
* `pps_in` - скорость обработки входящих пакетов (пакеты в секунду);
* `pps_out` - скорость обработки исходящих пакетов (пакеты в секунду);
* `in_iface_alias` - алиас сетевого интерфейса (входящий);
* `out_iface_alias` - алиас сетевого интерфейса (исходящий).

</details>

<details>
<summary>Получение списка сессий, сгруппированных по узлам локальной сети</summary>

```
GET /reports/traffic/top/sources?<GET-параметры, разделенные знаком &>
```

Перечень необязательных GET-параметров:
* `limit: integer` - ограничение на количество срабатываний (строк). Минимальное значение `1`;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `sessions`.

**Ответ на успешный запрос:**

```json5
[
    {
        "source_ip": "string",
        "src_aliases": ["string"],
        "bps_in": "integer",
        "bps_out": "integer",
        "pps_in": "integer",
        "pps_out": "integer",
        "sessions": "integer"
    },
    ...
]
```

* `source_ip` - IP-адрес источника подключения;
* `src_aliases` - список всех идентификаторов алиасов, связанных с IP-адресом источника;
* `bps_in` - входящая скорость трафика (байты в секунду);
* `bps_out` - исходящая скорость трафика (байты в секунду);
* `pps_in` - скорость обработки входящих пакетов (пакеты в секунду);
* `pps_out` - скорость обработки исходящих пакетов (пакеты в секунду);
* `sessions` - количество сессий.

</details>

<details>
<summary>Получение списка сессий, сгруппированных по приложению</summary>

```
GET /reports/traffic/top/applications?<GET-параметры, разделенные знаком &>
```

Перечень необязательных GET-параметров:
* `limit: integer` - ограничение на количество срабатываний (строк). Минимальное значение `1`;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `sessions`.

**Ответ на успешный запрос:**

```json5
[
    {
        "application": "string",
        "bps_in": "integer",
        "bps_out": "integer",
        "pps_in": "integer",
        "pps_out": "integer",
        "sessions": "integer"
    },
    ...
]
```

* `application` - приложение;
* `bps_in` - входящая скорость трафика (байты в секунду);
* `bps_out` - исходящая скорость трафика (байты в секунду);
* `pps_in` - скорость обработки входящих пакетов (пакеты в секунду);
* `pps_out` - скорость обработки исходящих пакетов (пакеты в секунду);
* `sessions` - количество сессий.

</details>

## Netflow

<details>
<summary>Получение состояния экспорта Netflow</summary>

```
GET /api/netflow-export/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true`, если экспорт через Netflow включен; `false` - если выключен.

</details>

<details>
<summary>Изменение состояния экспорта Netflow</summary>

```
PATCH /api/netflow-export/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true`, чтобы включить экспорт через Netflow; `false` - чтобы выключить.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Получение настроек экспорта NetFlow</summary>

```
GET /api/netflow-export/settings
```

**Ответ на успешный запрос:**

```json5
{
    "version": "integer",
    "exported_interfaces": ["string"],
    "destination_ip": "string",
    "destination_port": "integer",
    "active_flow_interval": "integer",
    "template_tx_counter": "integer" | "null",
    "template_tx_interval": "integer" | "null"
}
```

* `version` - версия протокола NetFlow: 
    * `5` - для NetFlow 5;
    * `9` - для NetFlow 9;
    * `10` - для NetFlow 10 (IPFIX).
* `exported_interfaces` - алиасы интерфейсов учета трафика в NetFlow. Допустимы алиасы  Ethernet-интерфейсов, Ethernet + PPTP/L2TP/PPPoE, GRE, локального VPN-трафика, IPsec, GRE over IPsec;
* `destination_ip` - IP-адрес коллектора NetFlow. Не может иметь значение `0.0.0.0`. Если пустая строка, статистика не будет экспортироваться;
* `destination_port` - UDP-порт коллектора NetFlow. Целое число от `1` до `65535`;
* `active_flow_interval` - интервал отправки статистики NetFlow для активного потока (от `60` до `3600` секунд), через который NGFW будет отправлять на коллектор отчеты (информация о завершенных потоках отправляется по завершении);
* `template_tx_counter` - количество пакетов, через которое на коллектор будет послан шаблон. Минимум `10`, максимум `6000`. Должно быть `null` при значении `5` в поле `version`;
* `template_tx_interval` - количество секунд, через которое на коллектор будет послан шаблон. Минимум `60`, максимум `86400`. Должно быть `null` при значении `5` в поле `version`.

</details>

<details>
<summary>Изменение настроек экспорта NetFlow</summary>

```
PATCH /api/netflow-export/settings
```

**Json-тело запроса:** 

```json5
{
    "version": "integer",
    "exported_interfaces": ["string"],
    "destination_ip": "string",
    "destination_port": "integer",
    "active_flow_interval": "integer",
    "template_tx_counter": "integer" | "null",
    "template_tx_interval": "integer" | "null"
}
```

* `version` - версия протокола NetFlow: 
    * `5` - для NetFlow 5;
    * `9` - для NetFlow 9;
    * `10` - для NetFlow 10 (IPFIX).
* `exported_interfaces` - алиасы интерфейсов учета трафика в NetFlow. Допустимы алиасы  Ethernet-интерфейсов, Ethernet + PPTP/L2TP/PPPoE, GRE, локального VPN-трафика, IPsec, GRE over IPsec;
* `destination_ip` - IP-адрес коллектора NetFlow. Не может иметь значение `0.0.0.0`. Если пустая строка, статистика не будет экспортироваться;
* `destination_port` - UDP-порт коллектора NetFlow. Целое число от `1` до `65535`;
* `active_flow_interval` - интервал отправки статистики NetFlow для активного потока (от `60` до `3600` секунд), через который NGFW будет отправлять на коллектор отчеты (информация о завершенных потоках отправляется по завершении);
* `template_tx_counter` - количество пакетов, через которое на коллектор будет послан шаблон. Минимум `10`, максимум `6000`. Должно быть `null` при значении `5` в поле `version`;
* `template_tx_interval` - количество секунд, через которое на коллектор будет послан шаблон. Минимум `60`, максимум `86400`. Должно быть `null` при значении `5` в поле `version`.

**Ответ на успешный запрос:** 200 ОК

</details>

## SNMP

<details>
<summary>Получение настройки включенности модуля</summary>

```
GET /monitor_backend/snmp/state
```

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - если `true`, то модуль включен, `false` - выключен.

</details>

<details>
<summary>Включение/выключение модуля</summary>

```
PATCH /monitor_backend/snmp/state
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - включить (`true`) или выключить (`false`) модуль.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Получение состояния работы модуля</summary>

```
GET /monitor_backend/snmp/status
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

* `name` - название модуля;
* `status` - статус модуля;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

<details>
<summary>Получение настроек SNMP</summary>

```
GET /monitor_backend/snmp/settings
```

**Ответ на успешный запрос:**

```json5
{
    "community": "string",
    "allow_external": "boolean",
    "version": "2 | 3",
    "user": "string",
    "password": "string",
    "private_key": "string",
    "hosts": [
        "string",
        ...
    ],
    "location": "string",
    "contact": "string",
    "name": "string"
}
```

* `community` - назначение поля, может быть пустой строкой;
* `allow_external` - разрешить запросы к серверу SNMP;
* `version` - версия протокола, может принимать только значение 2 или 3;
* `user` - логин, может быть пустой строкой;
* `password` - пароль, может быть пустой строкой;
* `private_key` - приватный ключ, может быть пустой строкой;
* `hosts` - список доверенных адресов и сетей, может быть пустой строкой;
* `location` - расположение, может быть пустой строкой;
* `contact` - контактная информация, может быть пустой строкой;
* `name` - имя узла, может быть пустой строкой.

</details>

<details>
<summary>Изменение настроек SNMP</summary>

```
PATCH /monitor_backend/snmp/settings
```

**Json-тело запроса:**

```json5
{
    "community": "string",
    "allow_external": "boolean",
    "version": "2 | 3",
    "user": "string",
    "password": "string",
    "private_key": "string",
    "hosts": [
        "string",
        ...
    ],
    "location": "string",
    "contact": "string",
    "name": "string"
}
```

* `community` - назначение поля, может быть пустой строкой;
* `allow_external` - разрешить запросы к серверу SNMP;
* `version` - версия протокола, может принимать только значение 2 или 3;
* `user` - логин, может быть пустой строкой;
* `password` - пароль, может быть пустой строкой;
* `private_key` - приватный ключ, может быть пустой строкой;
* `hosts` - список доверенных адресов и сетей, может быть пустой строкой;
* `location` - расположение, может быть пустой строкой;
* `contact` - контактная информация, может быть пустой строкой;
* `name` - имя узла, может быть пустой строкой.

**Ответ на успешный запрос:** 200 OK

</details>

## Zabbix-агент

<details>
<summary>Получение статуса Zabbix-агента</summary>

```
GET /monitor_backend/zabbix_agent/status
```

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - если `true`, то Zabbix-агент включен, `false` - выключен.

</details>

<details>
<summary>Получение настроек Zabbix-агента</summary>

```
GET /monitor_backend/zabbix_agent
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean",
    "active_mode_enabled": "boolean",
    "passive_mode_enabled": "boolean",
    "active_mode_servers": [ "string" ],
    "passive_mode_servers": [ "string" ],
    "hostname": "string",
    "listen_port": "integer"
}
```

* `enabled` - если `true`, то Zabbix-агент включен, `false` - выключен;
* `active_mode_enabled` - если `true`, то активный режим включен, `false` - выключен;
* `passive_mode_enabled` - если `true`, то пассивный режим включен, `false` - выключен;
* `active_mode_servers` - список адресов Zabbix-серверов для активного режима. Допустимые форматы: IP-адрес, имя домена, IP-адрес:порт, домен:порт (можно указать интернационализированные доменные имена). Пустой список допустим, если активный режим выключен;
* `passive_mode_servers` - список адресов Zabbix-серверов для пассивного режима. Допустимые форматы: IP-адрес, имя домена, IP-адрес:порт, домен:порт (можно указать интернационализированные доменные имена). Пустой список допустим, если пассивный режим выключен;
* `hostname` - имя сервера Ideco NGFW, допустимые значения: английские буквы, цифры, символы `.`, `_`, `-` и `'` (пробелы в начале и конце запрещены). Максимальная длина - 64 символа, может быть пустой строкой, если активный режим выключен.
* `listen_port` - порт для подключения в пассивном режиме, разрешены только порты `10050` и `10051`.

</details>

<details>
<summary>Изменение настроек Zabbix-агента</summary>

```
PATCH /monitor_backend/zabbix_agent
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean",
    "active_mode_enabled": "boolean",
    "passive_mode_enabled": "boolean",
    "active_mode_servers": [ "string" ],
    "passive_mode_servers": [ "string" ],
    "hostname": "string",
    "listen_port": "integer"
}
```

* `enabled` - если `true`, то Zabbix-агент включен, `false` - выключен;
* `active_mode_enabled` - если `true`, то активный режим включен, `false` - выключен;
* `passive_mode_enabled` - если `true`, то пассивный режим включен, `false` - выключен;
* `active_mode_servers` - список адресов Zabbix-серверов для активного режима. Допустимые форматы: IP-адрес, имя домена, IP-адрес:порт, домен:порт (можно указать интернационализированные доменные имена). Пустой список допустим, если активный режим выключен;
* `passive_mode_servers` - список адресов Zabbix-серверов для пассивного режима. Допустимые форматы: IP-адрес, имя домена, IP-адрес:порт, домен:порт (можно указать интернационализированные доменные имена). Пустой список допустим, если пассивный режим выключен;
* `hostname` - имя сервера Ideco NGFW, допустимые значения: английские буквы, цифры, символы `.`, `_`, `-` и `'` (пробелы в начале и конце запрещены). Максимальная длина - 64 символа, может быть пустой строкой, если активный режим выключен.
* `listen_port` - порт для подключения в пассивном режиме, разрешены только порты `10050` и `10051`.

**Ответ на успешный запрос:** 200 OK

</details>


## Журнал трафика

<details>
<summary>Получение таблицы Журнал трафика</summary>

```
GET /reports/report/firewall/journal?<GET-параметры, разделенные знаком &>
```

Перечень необязательных GET-параметров:
* `limit: integer` - ограничение на количество срабатываний (строк). Минимальное значение `1`;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи. Минимальное значение `0`;
* `format_type` - формат данных, поддерживает `CSV` и `JSON`, по умолчанию `JSON`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `duration`.

**Ответ на успешный запрос:**

```json5
{
    "data": [
        {
            "date_time": "integer",
            "result": "string",
            "rule_id": "integer",
            "table": "string",
            "action": "string",
            "protocol": "string",
            "ips_profile": "string",
            "ips_action": "string",
            "ips_signature_id": "integer",
            "dpi_profile": "string",
            "dpi_action": "string",
            "dpi_app": "string",
            "dpi_protocol": "string",
            "src_ip": "string",
            "src_port": "integer",
            "src_zone": "string",
            "src_user_login": "string",
            "src_user_name": "string",
            "src_group": "string",
            "src_location_name": "string",
            "src_location_code": "string",
            "dst_ip": "string",
            "dst_port": "integer",
            "dst_zone": "string",
            "dst_user_login": "string",
            "dst_user_name": "string",
            "dst_group": "string",
            "dst_location_name": "string",
            "dst_location_code": "string",
            "dnat_rule_id": "integer",
            "dnat_ip": "string",
            "dnat_port": "integer",
            "snat_rule_id": "integer",
            "snat_ip": "string",
            "cluster_id": "string",
            "cluster_name": "string",
            "vce_id": "string",
            "vce_name": "string",
            "flow_id": "string"
        }
    ],
    "rows": "integer",
    "rows_before_limit_at_least": "integer"
}
```

* `date_time` - дата и время срабатывания правила в формате `YYYYMMDDHHMMSS`;
* `result` - общий результат проверки трафика тремя модулями фильтрации: **Файрвол**, **Предотвращение вторжений**, **Контроль приложений**:
  * `absent` - значение отсутствует;
  * `accept` - разрешить;
  * `drop` - запретить.
* `rule_id` - идентификатор правила **Файрвола**. `0` указывает на отсутствие значения;
* `table` - таблица **Файрвола**, правило котрой сработало:
  * `absent` - значение отсутствует;
  * `fwd` - таблица FORWARD **Файрвола** Ideco NGFW;
  * `fwd_a` - постправило FORWARD Ideco Center;
  * `fwd_b` - предправило FORWARD Ideco Center;
  * `fwd_s` - системное правило FORWARD;
  * `inp` - таблица INPUT **Файрвола** Ideco NGFW;
  * `inp_a` - постправило INPUT Ideco Center;
  * `inp_b` - предправило INPUT Ideco Center;
  * `inp_s` - системное правило INPUT.
* `action` - действие, определенное для трафика, подпадающего под сработавшее правило:
  * `absent` - значение отсутствует;
  * `accept` - разрешить;
  * `drop` - запретить;
  * `l7_inspection` - перенаправить в профиль.
* `protocol` - протокол соединения;
* `ips_profile` - название профиля **Предотвращения вторжений**, использованного в правиле **Файрвола**;
* `ips_action` - действие для трафика, определенное профилем:
  * `absent` - значение отсутствует;
  * `accept` - разрешить;
  * `drop` - запретить.
* `ips_signature_id` - идентификатор сигнатуры, сработавшей в профиле;
* `dpi_profile` - название профиля **Контроля приложений**, использованного в правиле **Файрвола**;
* `dpi_action` - действие для трафика, определенное профилем:
  * `absent` - значение отсутствует;
  * `accept` - разрешить;
  * `drop` - запретить.
* `dpi_app` - приложение, действие для которого определено профилем;
* `dpi_protocol` - протокол, к которому применяется действие, определенное профилем;
* `src_ip` - IP-адрес источника трафика;
* `src_port` - порт источника трафика. `0` указывает на отсутствие значения;
* `src_zone` - интерфейс или группа интерфейсов, из которых пришел трафик;
* `src_user_login` - логин пользователя источника;
* `src_user_name` - имя пользователя источника;
* `src_group` - группа, в которую входит пользователь;
* `src_location_name` - страна источника трафика (GeoIP);
* `src_location_code` - код страны источника трафика (GeoIP);
* `dst_ip` - IP-адрес назначения трафика;
* `dst_port` - порт назначения трафика. `0` указывает на отсутствие значения;
* `dst_zone` - интерфейс или группа интерфейсов, в которые вошел трафик;
* `dst_user_login` - логин пользователя назначения;
* `dst_user_name` - имя пользователя назначения;
* `dst_group` - группа, в которую входит пользователь;
* `dst_location_name` - страна назначения трафика (GeoIP);
* `dst_location_code` - код страны назначения трафика (GeoIP);
* `dnat_rule_id` - идентификатор сработавшего **DNAT** правила. `0` указывает на отсутствие значения;
* `dnat_ip` - IP-адрес, на который **Файрвол** поменял `dst_ip`;
* `dnat_port` - порт, на который **Файрвол** поменял `dst_port`;
* `snat_rule_id` - идентификатор сработавшего **SNAT** правила. `0` указывает на отсутствие значения;
* `snat_ip` - IP-адрес, на который **Файрвол** поменял `src_ip`;
* `cluster_id` - идентификатор кластера (если он настроен на NGFW);
* `cluster_name` - название кластера (если он настроен на NGFW);
* `vce_id` - идентификатор **VCE**;
* `vce_name` - название **VCE**;
* `flow_id` - идентификатор соединения. Уникален для каждой записи.

* `rows` - количество записей в `data`;
* `rows_before_limit_at_least` - абсолютное количество записей в таблице.

</details>

## Журнал аутентификации ЛК

<details>
<summary>Получение авторизованных пользователей</summary>

```
GET /user_cabinet_reports/auth_journal?<GET-параметры, разделенные знаком &>
```

Перечень GET-параметров:
* `limit: integer` - ограничение на количество записей, выбираемых из базы данных;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи, указанные в `limit`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. Сортировка производится в прямом порядке следования в массиве:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию.
* `search: [{"text": "string", "columns": "string"}]` - объект Search с параметрами поиска подстроки в данных:
    * `text` - искомая строка;
    * `columns` - непустой набор полей, по которым ведется поиск.
* `format_type` - формат данных, поддерживает `CSV` и `JSON`, по умолчанию `JSON`;
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
    * массив из одного элемента ["today" | "yesterday" | "cur_week" | "prev_week" | "cur_month" | "prev_month"], если нужно отфильтровать по относительному диапазону дат.
* `range` - диапазон числовых значений;
* `contains_any` - один из элементов массива содержит подстроку (без учета регистра);
* `not_contains_any` - ни один из элементов массива не содержит подстроку (без учета регистра).

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
            "user_id": "number",
            "login": "string",
            "name": "string",
            "group_name": "string",
            "domain_type": "local" | "ad" | "ald" | "radius" | "device",
            "ip": "string",
            "country_name": "string",
            "country_code": "string",
            "end": "number",
            "time_online": "number"
        },
        ...
    ],
    "rows": "integer",
    "rows_before_limit_at_least": "integer"
}
```

* `meta` - массив метаданных, описывающих поля запроса:
* `name` - имя поля данных;
* `type` - тип данных;
* `data` - массив из `AuthUser` для отображения в таблице. `AuthUser` - объект с данными, соответствующими одной строке таблицы:
    * `id` - уникальный идентификатор сессии;
    * `date_time` - время создания сессии, целое положительное число в формате `YYYYmmddHHMMSS`;
    * `user_id` - идентификатор пользователя;
    * `login` - логин пользователя;
    * `name` - имя пользователя;
    * `group_name` - название родительской группы пользователя, может быть пустой строкой для записей, созданных в UTM до 17 версии;
    * `domain_type` - тип пользователя;
    * `ip` - IP-адрес, с которого подключался пользователь;
    * `country_name` - страна IP-адреса;
    * `country_code` - код страны IP-адреса;
    * `end` - время удаления сессии, целое положительное число в формате `YYYYmmddHHMMSS`;
    * `time_online` - время в сети, в секундах (может быть отрицательным числом, если после старта сессии изменили время).
* `rows` - количество `AuthUser`;
* `rows_before_limit_at_least` - общее количество строк (без учета `limit` и `offset`). Если в параметрах запроса отсутствуют `limit` и `offset`, поле `rows_before_limit_at_least` в ответе на запрос будет отсутствовать.

</details>

<details>
<summary>Выгрузка данных в CSV за определенный период</summary>

```
GET /user_cabinet_reports/auth_journal?format_type=CSV&<GET-параметры, разделенные знаком &>
```

Перечень GET-параметров:
* `limit: integer` - ограничение на количество записей, выбираемых из базы данных;
* `offset: integer` - количество строк, которые необходимо пропустить, прежде чем начать выводить записи, указанные в `limit`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. Сортировка производится в прямом порядке следования в массиве:
    * `field` - столбец, по которому производится сортировка;
    * `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию.
* `search: [{"text": "string", "columns": "string"}]` - объект Search с параметрами поиска подстроки в данных:
    * `text` - искомая строка;
    * `columns` - непустой набор полей, по которым ведется поиск.
* `format_type` - формат данных, поддерживает `CSV` и `JSON`, по умолчанию `JSON`;
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
    * массив из одного элемента ["today" | "yesterday" | "cur_week" | "prev_week" | "cur_month" | "prev_month"], если нужно отфильтровать по относительному диапазону дат.
* `range` - диапазон числовых значений;
* `contains_any` - один из элементов массива содержит подстроку (без учета регистра);
* `not_contains_any` - ни один из элементов массива не содержит подстроку (без учета регистра).


**Ответ на успешный запрос:** CSV-файл

</details>

</details>

<details>
<summary>Получение уникальных значений полей</summary>

```
GET /user_cabinet_reports/auth_journal/unique_values/<column_name>
```

* `column_name` - значение для получения:
    * `ip` - списка IP-адресов;
    * `country_name` - списка стран.

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
        {"column_name": "string"},
    ],
    "rows": "integer",
    "rows_before_limit_at_least": "integer"
}
```

* `meta` - массив метаданных, описывающих поля запроса:
* `name` - имя поля данных;
* `type` - тип данных;
* `rows` - количество объектов `data`;
* `rows_before_limit_at_least` - общее количество строк (без учета `limit` и `offset`). Если в параметрах запроса отсутствуют `limit` и `offset`, поле `rows_before_limit_at_least` в ответе на запрос будет отсутствовать.

</details>