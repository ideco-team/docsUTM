# Управление VPN

## DHCP-сервер

<details>
<summary>Получение настроек</summary>

```
GET /vpn_servers/dhcp
```

**Ответ на успешный запрос:**

```json5
  {
    "mode": "all|utm|local|none|custom",
    "networks": ["string"],
    "excluded_networks": ["string"]
  }
```

* `mode` - режим раздачи маршрутов:
  * `all` - направляем весь трафик на NGFW (маршрут 0.0.0.0/0);
  * `utm` - раздаем маршруты до локальных и внутренних сетей NGFW;
  * `local` - раздаем маршруты только до локальных сетей NGFW;
  * `none` - не раздаем маршруты;
  * `custom` - раздаем только маршруты до указанных подсетей;
* `networks` - список подсетей, маршруты до которых передаются в режиме custom. Допустимы алиасы подсетей, IP-адресов, доменов;
* `excluded_networks` - список подсетей, маршруты до которых исключаются в любом режиме. Допустимы алиасы подсетей, IP-адресов, доменов.

</details>

<details>
<summary>Изменение настроек</summary>

```
PUT /vpn_servers/dhcp
```

**Json-тело запроса:**

```json5
  {
    "mode": "all|utm|local|none|custom",
    "networks": ["string"],
    "excluded_networks": ["string"]
  }
```

**Ответ на успешный запрос:** 200 OK
</details>