# DHCP-сервер

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

<details>
<summary>Получение статуса службы DHCP-сервера</summary>

```
GET /dhcp_server/status
```

**Ответ на успешный запрос:**

```json5
[
  {
    "name": "string",
    "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
    "msg": ["string"]
  }
]
```

* `name` - название службы;
* `status` - текущее состояние службы;
* `msg` - список строк, подробно описывающих состояние службы;

</details>

## Настройки

<details>
<summary>Получение настроек</summary>

```
GET /dhcp_server/settings
```

**Пример ответа на успешный запрос:**

```json5
[
  {
        "enabled": "boolean",
        "interface": "string",
        "relay": {
            "external_servers": [
                "string"
            ]
        },
        "server": null,
        "id": "string"
    },
  {
        "enabled": "boolean",
        "interface": "string",
        "relay": null,
        "server": {
            "dns": ["string"],
            "domain": "string",
            "gateway": "string",
            "lease_time": "integer",
            "options": [
                {
                    "comment": "string",
                    "enabled": "boolean",
                    "forced": "boolean",
                    "option": "string"
                }
            ],
            "ranges": [ "string" ],
            "routes": [ {
                    "destination": "string",
                    "gateway": "string"
                } ],
            "tftp_filename": "string",
            "tftp_server": "string",
            "wins": [ "string" ],
            "wpad_enabled": "boolean"
        },
        "id": "string"
    },
    ...
]
```

* `id` - идентификатор настройки;
* `enabled` - включена или выключена настройка;
* `interface` - интерфейс Ideco NGFW;
* `relay` - режим работы (если активен `server`, должен быть `null`);
  * `external_servers` - IP-адрес внешнего DHCP-сервера;
* `server` - режим работы (если активен `relay`, должен быть `null`)
  * `dns` - поля DNS-1 и DNS-2 в веб-интерфейсе. Если не задано значение в поле DNS-1 или DNS-2, то DNS-сервером для всех сетевых устройств локальной сети будет являться Ideco NGFW;
  * `domain` - DNS-суффикс;
  * `gateway` - шлюз для направления трафика по умолчанию. Если поле не заполнено, шлюзом будет выступать IP-адрес выбранного интерфейса;
  * `lease_time` - время аренды (в минутах);
  * `options` - опции dnsmasq:
    - `comment` - комментарий (может быть пустым);
    - `enabled` - включена или отключена опция;
    - `forced` - принудительная отправка опции клиенту;
    - `option` - значение опции;
  * `ranges` - диапазон IP-адресов для выдачи;
  * `routes` - статические маршруты:
    - `destination` - хост;
    - `gateway` - шлюз;
  * `tftp_filename` - имя файла для загрузки по TFTP;
  * `tftp_server` - IP-адрес TFTP-сервера для настройки загрузки образа по сети;
  * `wins` - IP-адрес WINS-сервера;
  * `wpad_enabled` - включение протокола автоматической настройки прокси. Для работы WPAD необходимо разрешить прямые подключения к прокси.

</details>

<details>
<summary>Создание настроек</summary>

```
POST /dhcp_server/settings
```

**Json-тело запроса для режима сервера:**

```json5
{
      "enabled": "boolean",
      "interface": "string",
      "relay": null,
      "server": {
          "dns": ["string"],
          "domain": "string",
          "gateway": "string",
          "lease_time": "integer",
          "options": [
              {
                  "comment": "string",
                  "enabled": "boolean",
                  "forced": "boolean",
                  "option": "string"
              }
          ],
          "ranges": [ "string" ],
          "routes": [ {
                  "destination": "string",
                  "gateway": "string"
              } ],
          "tftp_filename": "string",
          "tftp_server": "string",
          "wins": [ "string" ],
          "wpad_enabled": "boolean"
      }
  }
```

**Json-тело запроса для режима релея:**

```json5
{
      "enabled": "boolean",
      "interface": "string",
      "relay": {
          "external_servers": [
              "string"
          ]
      },
      "server": null
  }
```

**Ответ на успешный запрос:**

```json5
{
  "id": "string",
}
```

</details>

<details>
<summary>Изменение настроек</summary>

```
PATCH /dhcp_server/settings/<id настройки>
```

**Json-тело запроса - все или некоторые поля для создания настроек, например:**

```json5
{
      "relay": {
          "external_servers": [
              "string"
          ]
      }
  }
```

**Ответ на успешный запрос:** 200 OK

</details>

<details>
<summary>Удаление настроек</summary>

```
DELETE /dhcp_server/settings/<id настройки>
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Привязка IP к MAC

<details>
<summary>Получение статических привязок</summary>

```
GET /dhcp_server/static_leases
```

**Пример ответа на успешный запрос:**

```json5
[
    {
        "comment": "",
        "enabled": true,
        "ip_address": "192.168.0.40",
        "mac": "50:46:5d:6e:8c:20",
        "id": "3e4827dd-5e0c-4932-98b1-fa2d9826b0ce"
    },
    ...
]
```

</details>

<details>
<summary>Создание статической привязки</summary>

```
POST /dhcp_server/static_leases
```

**Json-тело запроса:**

```json5
{
    "comment": "string",
    "enabled": "boolean",
    "ip_address": "string",
    "mac": "string"
  }
```

Будьте внимательны при согласовании настроек клиентских устройств и DHCP-сервера на Ideco NGFW. Некоторые устройства предоставляют MAC-адрес с разделенными с помощью дефиса октетами (01-02-03-04-05-06). В настройках Ideco NGFW октеты MAC-адреса разделяются только двоеточиями (01:02:03:04:05:06).

**Ответ на успешный запрос:**

```json5
{
  "id": "string"
}
```

</details>

<details>
<summary>Редактирование статической привязки</summary>

```
PATCH /dhcp_server/static_leases/<id статической привязки>
```

**Json-тело запроса (все или некоторые поля):**

```json5
{
    "comment": "string",
    "enabled": "boolean",
    "ip_address": "string",
    "mac": "string"
  }
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление статической привязки</summary>

```
DELETE /dhcp_server/static_leases/<id статической привязки>
```

**Ответ на успешный запрос:** 200 ОК

</details>