# DNS-сервер

<details>
<summary>Получение состояния службы DNS</summary>

```
GET /dns/status
```

**Ответ на успешный запрос:**

```
[
  {
    "name": "string",
    "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
    "msg": ["string"]
  },
  ...
]
```

* `name` - название службы;
* `status` - состояние службы;
* `msg` - список ошибок. Может быть пустым.

</details>

## Настройки

<details>
<summary>Получение настроек DNS-сервера</summary>

```
GET /dns/settings
```

**Ответ на успешный запрос:**

```
{
	"intercept_enabled": boolean (перехватывать DNS запросы на серверы в интернет)
}
```

</details>

<details>
<summary>Включение/выключение DNS-сервера</summary>

```
PUT /dns/settings
```

**Json-тело запроса:**

```
{
    "intercept_enabled": boolean
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Включение/выключение переадресации DNS для безопасного поиска</summary>

### Получение настроек:

```
GET /dns/safesearch
```

Ответ на успешный запрос:

```
{
	"enabled": boolean (переадресовывать DNS-запросы на безопасные домены поиска Google, Yandex, YouTube, Bing, DuckDuckGo, Qwant и Pixabay)
}
```

### Изменение настроек:

```
PUT /dns/safesearch
```

**Json-тело запроса:**

```
{
    "enabled": boolean
}
```

Ответ: 200 ОК

</details>

## Управление корневыми DNS-серверами

<details>
<summary>Получение списка</summary>

```
GET /dns/zones/root
```

**Ответ на успешный запрос:**

```
[
    {
    "id": "string",
    "enabled": boolean,
    "type": "ip" | "interface",
    "object": "string",
    "comment": "string"
},
...
]
```

* `id` - идентификатор объекта;
* `enabled` - элемент включен/выключен;
* `type` - принимает два значения:
  * `"ip"` - IP-адрес DNS-сервера, заданного вручную;
  * `"interface"` - ID алиаса подключения к провайдеру (DNS-серверы, выданные подключению). Тип алиаса - `isp`;
* `object` - сам объект - IP адрес, если тип `"ip"`, или ID алиаса подключения к провайдеру, если тип `"interface"`;
* `comment` - комментарий, может быть пустым, максимум 256 символов.

</details>

<details>
<summary>Добавление корневого DNS-сервера</summary>

```
POST /dns/zones/root
```

**Json-тело запроса:** 

```
{
    "enabled": boolean,
    "type": "ip" | "interface",
    "object": "string",
    "comment": "string"
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>
<summary>Редактирование корневого DNS-сервера</summary>

```
PATCH /dns/zones/root/<id записи>
```

**Json-тело запроса (все или некоторые поля):** 

```
{
    "enabled": boolean,
    "type": "ip" | "interface",
    "object": "string",
    "comment": "string"
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Удаление корневого DNS-сервера</summary>

```
DELETE /dns/zones/root/<id записи>
```

Ответ: 200 ОК

</details>

## Управление forward-зонами

<details>
<summary>Получение списка</summary>

```
GET /dns/zones/forward
```

**Ответ на успешный запрос:**

```
[
    {
    "id": "string",
    "name": "string",
    "enabled": boolean,
    "servers": ["string"],
    "comment": "string",
},
    ...
]
```

* `id` - идентификатор объекта;
* `name` - название зоны;
* `enabled` - зона включена/выключена;
* `servers` - список IP-адресов DNS-серверов, заданных вручную;
* `comment` - комментарий, может быть пустым, максимум 256 символов.

</details>

<details>
<summary>Добавление forward-зоны</summary>

```
POST /dns/zones/forward
```

**Json-тело запроса:**

```
{
    "name": "string",
    "enabled": boolean,
    "servers": ["string"],
    "comment": "string"
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>
<summary>Редактирование forward-зоны</summary>

```
PATCH /dns/zones/forward/<id forward-зоны>
```

**Json-тело запроса (все или некоторые поля):** 

```
{
    "name": "string",
    "enabled": boolean,
    "servers": ["string"],
    "comment": "string"
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Удаление forward-зоны</summary>

```
DELETE /dns/zones/forward/<id forward-зоны>
```

Ответ: 200 ОК

</details>

## Управление master-зонами

<details>
<summary>Получение списка</summary>

```
GET /dns/zones/master
```

**Ответ на успешный запрос:**

```
[
    {
    "id": "string",
    "name": "string",
    "enabled": boolean,
    "config": "string",
    "comment": "string",
},
    ...
]
```

* `id` - идентификатор объекта;
* `name` - уникальное название зоны, имеет вид домена example.com;
* `enabled` - зона включена/выключена;
* `config` - текст с параметрами зоны, не может быть пустым. Максимум 10000 символов;
* `comment` - комментарий, может быть пустым, максимум 256 символов.

Подробнее о формате записей для настройки master-зоны - в статье [Master-зоны](/settings/services/dns/master-zon.md).

</details>

<details>
<summary>Добавление master-зоны</summary>

```
POST /dns/zones/master
```

**Json-тело запроса:** 

```
{
    "name": "string",
    "enabled": boolean,
    "config": "string",
    "comment": "string",
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string"
}
```

</details>

<details>
<summary>Редактирование master-зоны</summary>

```
PATCH /dns/zones/master/<id master-зоны>
```

**Json-тело запроса (все или некоторые поля):** 

```
{
    "name": "string",
    "enabled": boolean,
    "config": "string",
    "comment": "string",
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Удаление master-зоны</summary>

```
DELETE /dns/zones/master/<id master-зоны>
```

Ответ: 200 ОК

</details>