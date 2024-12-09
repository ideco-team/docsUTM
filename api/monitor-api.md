# Мониторинг

## Монитор трафика

<details>
<summary>Получение списка сессий</summary>

```
GET /reports/traffic/sessions?<GET-параметры, разделенные знаком &>
```

Перечень необязательных GET-параметров:
* `limit: integer` - ограничение на количество срабатываний (строк). Минимальное значение `1`;
* `offset: integer` - количество строк, которые необходимо пропустить прежде, чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. `field` - столбец, по которому производится сортировка, `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `duration`.

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
* `offset: integer` - количество строк, которые необходимо пропустить прежде, чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. `field` - столбец, по которому производится сортировка, `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `sessions`.

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
* `offset: integer` - количество строк, которые необходимо пропустить прежде, чем начать выводить записи. Минимальное значение `0`;
* `sort: [{"field": "string", "direction": "asc | desc"}]` - список параметров сортировки. `field` - столбец, по которому производится сортировка, `direction` - направление сортировки: `asc` - по возрастанию, `desc` - по убыванию. Сортировка производится в прямом порядке следования в массиве. По умолчанию сортируется по убыванию столбец `sessions`.

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
PUT /api/netflow-export/state
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