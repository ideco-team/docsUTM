# Сетевые интерфейсы

## Внешние и локальные интерфейсы

<details>
<summary>Получение списка всех внешних и локальных интерфейсов</summary>

```
GET /network/connections
```

**Ответ на успешный запрос:**

Список объектов: LAN, WAN, PPTP, L2TP или PPPoE:

```json5
[
  "LAN" | "WAN" | "PPTP" | "L2TP" | "PPPoE"
]
```

**Объект LAN (Локальный Ethernet-интерфейс):**

```json5
{
    "id": "integer",
    "type": "lan",
    "title": "string",
    "enabled": "boolean",
    "mac": "string",
    "enable_dhcp": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `enabled` - включен или выключен интерфейс;
* `mac` - MAC-адрес сетевой карты или идентификатор агрегированного интерфейса. MAC-адрес в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `addresses` - список адресов в формате "IP/prefix". Может быть пустым, если включено получение
  адресов по DHCP;
* `gateway` - IP-адрес шлюза. Может быть равен `null`, если включено получение адресов по DHCP;
* `dns` - список IP-адресов DNS, может быть пустым независимо от флага включения DHCP;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно). Может быть равен `null`, если не назначен;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен;
* `is_vce_vlan` - `true`, если подключение создано на основе проброшенного в VCE VLAN-а.

**Объект WAN (Подключение к провайдеру по Ethernet):**

```json5
{
    "id": "integer",
    "type": "wan",
    "title": "string",
    "enabled": "boolean",
    "mac": "string",
    "enable_dhcp": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `enabled` - включен или выключен данный интерфейс;
* `mac` - MAC-адрес сетевой карты или идентификатор агрегированного интерфейса. MAC-адрес в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `enable_dhcp` - получать ли адрес интерфейса и адрес шлюза от провайдера по DHCP;
* `addresses` - список адресов. Адреса в формате "IP/prefix". Может быть пустым, если включено получение
  адресов по DHCP;
* `gateway` - IP-адрес шлюза. Может быть равен `null`, если включено получение адресов по DHCP;
* `dns` - список IP-адресов DNS, может быть пустым независимо от флага включения DHCP;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно), `null`, если не назначен;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен;
* `is_vce_vlan` - `true`, если подключение создано на основе проброшенного в VCE VLAN-а.

**Объект PPTP (Подключение к провайдеру по PPTP):**

```json5
{
    "id": "integer",
    "type": "pptp",
    "title": "string",
    "enabled": "boolean",
    "server": "string",
    "login": "string",
    "password": "string",
    "mac": "string",
    "enable_dhcp": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `enabled` - включен или выключен интерфейс;
* `server` - IP-адрес или доменное имя PPTP-сервера, к которому осуществляется подключение;
* `login` - логин на сервере PPTP, не может быть пустым;
* `password` - пароль на сервере PPTP, не может быть пустым;
* `mac` - MAC-адрес сетевой карты или идентификатор агрегированного интерфейса. MAC-адрес в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `enable_dhcp` - получать ли адрес интерфейса и адрес шлюза от провайдера по DHCP;
* `addresses` - список адресов в формате "IP/prefix". Может быть пустым, если включено получение
  адресов по DHCP;
* `gateway` - IP-адрес шлюза. Может быть равен `null`, если включено получение адресов по DHCP или PPTP-сервер находится в той же подсети, что назначена на интерфейс;
* `dns` - список IP-адресов DNS, может быть пустым независимо от флага включения DHCP;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно). Может быть равен `null` если не назначен;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен;
* `is_vce_vlan` - `true`, если подключение создано на основе проброшенного в VCE VLAN-а.

**Объект L2TP (Подключение к провайдеру по L2TP):**

```json5
{
    "id": "integer",
    "type": "l2tp",
    "title": "string",
    "enabled": "boolean",
    "server": "string",
    "login": "string",
    "password": "string",
    "mac": "string",
    "enable_dhcp": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `enabled` - включен или выключен данный интерфейс;
* `server` - IP-адрес или доменное имя L2TP-сервера, к которому осуществляется подключение;
* `login` - логин на сервере L2TP, не может быть пустым;
* `password` - пароль на сервере L2TP, не может быть пустым;
* `mac` - MAC-адрес сетевой карты или идентификатор агрегированного интерфейса. MAC-адрес в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `enable_dhcp` - получать ли адрес интерфейса и адрес шлюза от провайдера по DHCP;
* `addresses` - список адресов в формате "IP/prefix". Может быть пустым, если включено получение
  адресов по DHCP;
* `gateway` - IP-адрес шлюза. Может быть равен `null`, если включено получение адресов по DHCP или L2TP-сервер находится в той же подсети, что назначена на интерфейс;
* `dns` - список IP-адресов DNS, может быть пустым независимо от флага включения DHCP;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно), `null`, если не назначен;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен;
* `is_vce_vlan` - `true`, если подключение создано на основе проброшенного в VCE VLAN-а.

**Объект PPPoE (Подключение к провайдеру по PPPoE):**

```json5
{
    "id": "integer",
    "type": "pppoe",
    "title": "string",
    "enabled": "boolean",
    "login": "string",
    "password": "string",
    "service": "string",
    "concentrator": "string",
    "mac": "string",
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `enabled` - включен или выключен данный интерфейс;
* `login` - логин на сервере PPPoE, не может быть пустым;
* `password` - пароль на сервере PPPoE, не может быть пустым;
* `service` - название сервиса, может быть пустым;
* `concentrator` - название концентратора, может быть пустым;
* `mac` - MAC-адрес сетевой карты или id агрегированного интерфейса. MAC-адрес в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно), `null`, если не назначен;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен;
* `is_vce_vlan` - `true`, если подключение создано на основе проброшенного в VCE VLAN-а.

</details>

<details>
<summary>Получение состояния локальных интерфейсов и подключений</summary>

```
GET /network/states
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "integer",
    "type": "lan" | "wan" | "pptp" | "l2tp" | "pppoe",
    "ether": {
        "device": "null" | "string",
        "vlan_tag": "null" | "integer",
        "addresses": ["string"],
        "gateway": "null" | "string",
        "dns": ["string"],
        "status": "down" | "going-up" | "up",
        "errors": ["string"]
    },
    "ppp": {
        "device": "null" | "string",
        "remote_address": "null" | "string",
        "local_address": "null" | "string",
        "dns": ["string"],
        "status": "down" | "going-up" | "up",
        "errors": ["string"]
    },
    "summary": {
        "device": "null" | "string",
        "addresses": ["string"],
        "dns": ["string"],
        "gateway": "null" | "string",
        "zone": "null" | "string",
        "ifindex": "null" | "integer",
        "scope": "kernel" | "vpp"
    }
  },
...
]
```

* `id` - идентификатор интерфейса;
* `type` - тип подключения;
* `ether` - состояние Ethernet или VLAN:
    * `device` - название устройства в системе, например, `Leth1`;
    * `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно) или `null`, если не назначен;
    * `addresses` - список адресов, может быть пустым. Адреса в формате "IP/prefix";
    * `gateway` - IP-адрес шлюза, может быть равен `null`, если шлюза нет;
    * `dns` - адреса DNS, выданные по DHCP или назначенные пользователем;
    * `status` - текущее состояние интерфейса;
    * `errors` - список ошибок;
* `ppp` - состояние РРР-подключения. Поле определено только для интерфейсов с полем
  `type` равным `pptp | l2tp | pppoe`, для всех остальных типов `lan | wan` равно `null`:
    * `device` - название устройства в системе, например `Eppp4`;
    * `remote_address` - туннельный IP-адрес сервера;
    * `local_address` - туннельный IP-адрес клиента (IP-адрес NGFW);
    * `dns` - адреса DNS, выданные из PPP;
    * `status` - текущее состояние интерфейса;
    * `errors` - список ошибок;
* `summary` - общее состояние подключение: 
    * `device` - итоговое активное устройство, например, `Eppp4` или `Eeth3`;
    * `addresses` - список адресов интерфейса или подключения к провайдеру;
    * `dns` - адреса DNS, пригодные к использованию для сервера DNS и других целей;
    * `gateway` - IP-адрес шлюза, может быть равен `null`, если шлюза нет;
    * `zone` - алиас зоны. Может быть равен `null`, если не назначен;
    * `ifindex` - числовой индентификатор интерфейса;
    * `scope` - принадлежность интерфейса сетевому стеку: kernel - ядро.

</details>

<details>
<summary>Создание внешнего или локального интерфейса</summary>

```
POST /network/connections
```

**Json-тело запроса:** 

Объект LAN | WAN | PPTP | L2TP | PPPoE без поля id, например:

```json5
{
    "type": "wan",
    "title": "string",
    "enabled": "boolean",
    "mac": "string",
    "enable_dhcp": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "number"  // идентификатор созданного интерфейса LAN
}
```

</details>

<details>
<summary>Редактирование внешнего или локального интерфейса</summary>

```
PATCH /network/connections/<id интерфейса>
```

**Json-тело запроса:**

Поля из объекта LAN | WAN | PPTP | L2TP | PPPoE, например:

```json5
{
    "enabled": "boolean",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "dns": ["string"],
    "vlan_tag": "null" | "integer",
    "zone": "null" | "string",
    "is_vce_vlan": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление внешнего или локального интерфейса</summary>

```
DELETE /network/connections/<id интерфейса>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Агрегированные интерфейсы

<details>
<summary>Получение списка агрегированных интерфейсов</summary>

```
GET /network/aggregated
```

**Ответ на успешный запрос:**

```json5
[  
  {
  "id": "string",
  "enabled": "boolean",
  "title": "string",
  "comment": "string",
  "nics": ["string"]
  },
...
]
```

* `id` - идентификатор агрегированного интерфейса;
* `enabled` - включен или выключен интерфейс;
* `title` - название, не может быть пустым;
* `comment` - комментарий, может быть пустым;
* `nics` - список MAC-адресов в формате "11:22:33:44:55:66", все буквы в нижнем регистре, может быть пустым. 

</details>

<details>
<summary>Получение состояния агрегированных интерфейсов</summary>

```
GET /network/aggregated_states
```

**Ответ на успешный запрос:**

```json5
[
  {
  "id": "string",
  "link": "up" | "down"
  },
...
]
```

* `id` - идентификатор агрегированного интерфейса;
* `link` - состояние соединения на агрегированном интерфейсе.

</details>

<details>
<summary>Создание нового агрегированного интерфейса</summary>

```
POST /network/aggregated
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean",
  "title": "string",
  "comment": "string",
  "nics": ["string"]
  }
```

**Ответ на успешный запрос:**

```json5
{
  "id": "string"  // идентификатор созданного агрегированного интерфейса
}
```

</details>

<details>
<summary>Редактирование агрегированного интерфейса</summary>

```
PUT /network/aggregated/<id агрегированного интерфейса>
```

**Json-тело запроса:**

```json5
{
  "enabled": "boolean",
  "title": "string",
  "comment": "string",
  "nics": ["string"]
  }
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление агрегированного интерфейса</summary>

```
DELETE /network/aggregated/<id агрегированного интерфейса>
```

**Ответ на успешный запрос:** 200 OK

</details>

## Туннельные интерфейсы

<details>
<summary>Получение списка всех туннельных интерфейсов</summary>

```
GET /network/tunnels
```

**Ответ на успешный запрос:**

```json5
[  
  {
    "id": "string",
    "title": "string",
    "enabled": "boolean",
    "comment": "string",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "parent_interface": "string",
    "osdevname": "string",
    "server": "string",
    "zone": "null" | "string"
  },
...
]
```

* `id` - идентификатор интерфейса (строка в формате UUID);
* `title` - название интерфейса, не может быть пустым, максимальная длина - 42 символа;
* `enabled` - включен или выключен интерфейс;
* `comment` - комментарий, может быть пустым;
* `addresses` - список адресов в формате "IP/prefix";
* `gateway` - IP-адрес шлюза, может быть равен `null`;
* `parent_interface` - алиас родительского интерфейса, его IP-адрес будет источником туннеля;
* `osdevname` - название существующего или планируемого сетевого интерфейса в ядре (например, `Gre00000001`). Значение создается автоматически, является уникальным и **доступно только для чтения**;
* `server` - IP-адрес или доменное имя устройства, к которому осуществляется подключение;
* `zone` - алиас зоны. Может быть равен `null`, если не назначен.

**Важно:** Для каждого родительского интерфейса все настроенные туннели должны иметь уникальные значения в поле `server`.
Не допускается создание туннельных интерфейсов с повторяющимися значениями в полях `parent_interface` и `server`!

</details>

<details>
<summary>Получение состояния туннельных интерфейсов</summary>

```
GET /network/tunnel_states
```

**Ответ на успешный запрос:**

```json5
{
  "id": "string",
  "link": "up" | "down" | "inactive",
  "local_ip": "string"
}
```

* `id` - идентификатор интерфейса;
* `link` - состояние туннельного интерфейса, `inactive` при недоступности родительского интерфейса;
* `local_ip` - IP-адрес родительского интерфейса запущенного туннеля.

</details>

<details>
<summary>Создание нового туннельного интерфейса</summary>

```
POST /network/tunnels
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "enabled": "boolean",
    "comment": "string",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "parent_interface": "string",
    "osdevname": "string",
    "server": "string",
    "zone": "null" | "string"
}
```

**Ответ на успешный запрос:**

```json5
{
  "id": "string"  // идентификатор созданного туннельного интерфейса
}
```

</details>

<details>
<summary>Редактирование туннельного интерфейса</summary>

```
PUT /network/tunnels/<id туннельного интерфейса>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "enabled": "boolean",
    "comment": "string",
    "addresses": ["string"],
    "gateway": "null" | "string",
    "parent_interface": "string",
    "osdevname": "string",
    "server": "string",
    "zone": "null" | "string"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление туннельного интерфейса</summary>

```
DELETE /network/tunnels/<id туннельного интерфейса>
```

**Ответ на успешный запрос:** 200 OK

</details>

## VCE-интерфейсы

<details>
<summary>Получение списка всех сетевых интерфейсов, пробрасываемых в VCE</summary>

```
GET /network/vce_conns
```

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "title": "string",
    "vce_id": "string",
    "mac": "string",
    "vlan_tag": "null" | "integer",
    "comment": "string"
  },
  ...
]
```

* `id` - идентификатор интерфейса;
* `title` - название интерфейса, не может быть пустым;
* `vce_id` - идентификатор VCE, для которого создан интерфейс;
* `mac` - MAC-адрес сетевой карты в формате "11:22:33:44:55:66", все буквы в нижнем регистре;
* `vlan_tag` - тэг VLAN, число от 1 до 4095 (включительно). Может быть `null`, если пробрасывается сетевой интерфейс целиком;
* `comment` - комментарий, может быть пустым.

**Важно:** Изменяемыми являются только поля `title` и `comment`.

</details>

<details>
<summary>Создание пробрасываемого в VCE интерфейса</summary>

```
POST /network/vce_conns
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "vce_id": "string",
    "mac": "string",
    "vlan_tag": "null" | "integer",
    "comment": "string"
}
```

**Ответ на успешный запрос:**

```json5
{
  "id": "string"  // идентификатор созданного интерфейса
}
```

</details>

<details>
<summary>Редактирование пробрасываемого в VCE интерфейса</summary>

```
PATCH /network/vce_conns/<id пробрасываемого интерфейса>
```

**Json-тело запроса:**

```json5
{
    "title": "string",
    "comment": "string"
}
```

Поля опциональны, можно передавать любое из них отдельно или оба сразу.

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление пробрасываемого в VCE интерфейса</summary>

```
DELETE /network/vce_conns/<id пробрасываемого интерфейса>
```

**Ответ на успешный запрос:** 200 OK

</details>