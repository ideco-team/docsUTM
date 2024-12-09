# Управление экспортом через Netflow

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