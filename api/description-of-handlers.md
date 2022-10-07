# Описание хендлеров

<details>

<summary>Авторизация</summary>

```
POST /web/auth/login
```

**Json тело запроса:**

```
{
    "login": "string",    
    "password": "string",    
    "recaptcha": "string" (по умолчанию пустая строка - ""),
    "rest_path": "string" (по умолчанию строка со слэшем "/")
}

```
После успешной авторизации, сервер Ideco UTM передаёт в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=02428c1c-fcd5-42ef-a533-5353da743806
set-cookie: __Secure-ideco-3ea57fca-65cb-439b-b764-d7337530f102=df164532-b916-4cda-a19b-9422c2897663:1663839003
```

Эти куки нужно передавать при каждом запросе после авторизации в заголовке запроса Cookie.

</details>

<details>

<summary>Разавторизация</summary>

```
DELETE /web/auth/login
```
После успешной разавторизации, сервер Ideco UTM передаёт в заголовках куки. Пример значений:

```
set-cookie: insecure-ideco-session=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
set-cookie: __Secure-ideco-b7e3fb6f-7189-4f87-a4aa-1bdc02e18b34=""; HttpOnly; Max-Age=0; Path=/; SameSite=Strict; Secure
```

</details>

## Управление объектами

<details>

<summary>Создание объекта IP-адрес</summary>

```
POST /aliases/ip_addresses
```

**Json тело запроса:**

```
{
    "comment": "string",    
    "title": "string",    
    "value": "string"
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

<summary>Создание объекта Диапазон IP-адресов</summary>

```
POST /aliases/ip_ranges
```

**Json тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "start": "string",
    "end": "string"
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

<summary>Создание объекта Список адресов</summary>

```
POST /aliases/lists/addresses
```

**Json тело запроса:**

```
{
    "title": "string",
    "comment": "string",
    "values": ["string"] (идентификаторы объектов IP-адреса, через запятую)
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

<summary>Создание объекта Время</summary>

```
POST /aliases/time_ranges
```

**Json тело запроса:**

```
{
    "title":"string",
    "comment":"string",
    "weekdays":[int], (список дней недели, где 1-пн, 2-вт ... 7-вс)
    "start":"string", (начало временного отрезка в формате ЧЧ:ММ)
    "end":"string"(конец временного отрезка в формате ЧЧ:ММ)
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

<summary>Получение ID объектов</summary>

```
GET /aliases
```

**Ответ на успешный запрос:**

```
[
    {
        comment: "string",
        title: "string",
        type: "string",
        values: [
            "ip.id.1",
            "ip.id.2"
        ],
        id: "type.id.1"
    }, 
    ...
] 
```

В качестве ответа будет возвращен список всех объектов, существующих в UTM:
* "protocol.ah" - протокол AH,
* "protocol.esp" - протокол ESP,
* "protocol.gre" - протокол GRE,
* "protocol.icmp" - протокол ICMP,
* "protocol.tcp" - протокол TCP,
* "protocol.udp" - протокол UDP,
* "quota.exceeded"- IP-адреса пользователей, которые превысили квоту,
* "any" - допускается любое значение в этом поле,
* "interface.external_any" - все внешние интерфейсы (равно таблице *Подключение к провайдеру* в веб-интерфейсе и включает в себя подключения к провайдеру по Ethernet/VPN),
* "interface.external_eth" - внешние Ethernet-интерфейсы,
* "interface.external_vpn" - внешние VPN-интерфейсы,
* "interface.local_any" - все локальные интерфейсы,
* "group.id." - идентификатор группы пользователей,
* "interface.id." - идентификатор конкретного интерфейса,
* "security_group.guid." - идентификатор группы безопасности AD,
* "user.id." - идентификатор пользователя,
* "domain.id." - идентификатор домена,
* "ip.id." - идентификатор IP-адреса,
* "ip_range.id." - идентификатор объекта *Диапазон адресов*,
* "address_list.id." - идентификатор объекта *Список адресов*,
* "port_list.id." - идентификатор объекта *Список портов*,
* "time_list.id." - идентификатор объекта *Расписание*,
* "subnet.id." - идентификатор объекта *Подсеть*,
* "port_range.id." - идентификатор объекта *Диапазон портов*,
* "port.id." - идентификатор объекта *Порт*,
* "time_range.id." - идентификатор объекта *Время*.

</details>

## Пользовательские категории контент-фильтра

<details>

<summary>Создание пользовательской категории</summary>

```
POST /content-filter/users_categories
```

**Json тело запроса:**

```
{
    "name": "string",
    "description": "string",
    "urls": [ "string" ]
}
```

**urls** - список url. Либо полный путь до страницы, либо только доменное имя. В пути могут присутствовать, означающие любое количество любых символов на этом месте.

**Ответ на успешный запрос:** 

```
{
    "id": "string"
}
```

</details>

<details>

<summary>Получение пользовательских категорий</summary>

```
GET /content-filter/users_categories
```

**Json ответ на запрос:**

```
[
    {
        "id": "string", (номер категории, вида - users.id.1)
        "name": "string", (название категории, не пустая строка)
        "description": "string",
        "urls": ["string"] 
    },
    ...
]
```

**urls** - список url. Либо полный путь до страницы, либо только доменное имя. В пути могут присутствовать, означающие любое количество любых символов на этом месте.

</details>

<details>

<summary>Редактирование</summary>

```
PUT /content-filter/users_categories/{category_id}
```

**Json тело запроса:**

```
{
    "name": "string",
    "description": "string",
    "urls": ["string"]
}
```

**Ответ на успешный запрос:**

```
{
    "id": "string",
    "name": "string",
    "description": "string",
    "urls": [ "string" ]
}
```

</details>

## Распространенные статусы

* **200** OK – Операция успешно завершена.
* **302** Found – Запрашиваемая страница была найдена / временно перенесена на другой URL.
* **400** Bad Request – Сервер не смог понять запрос из-за недействительного синтаксиса.
* **401** Unauthorized – Запрещено. Сервер понял запрос, но он не выполняет его из-за ограничений прав доступа к указанному ресурсу.
* **404** Not Found – Запрашиваемая страница не найдена. Сервер понял запрос, но не нашёл соответствующего ресурса по указанному URL.
* **405** Method Not Allowed – Mетод не поддерживается. Запрос был сделан методом, который не поддерживается данным ресурсом.
* **502** Bad Gateway – Ошибка шлюза. Сервер, выступая в роли шлюза или прокси-сервера, получил недействительное ответное сообщение от вышестоящего сервера.
* **542** – Валидация не пропустила тело запроса.