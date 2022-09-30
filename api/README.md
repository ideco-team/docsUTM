# API: пример использования

## Примеры использования

<details>

<summary>Создание объекта типа Список объектов</summary>

**1\.** Авторизуйте администратора: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "recaptcha": "", "rest_path": "/"}'
```

Ответ: статус 200.

**2\.** Получите список идентификаторов объектов типа "Список объектов":

**2.1\.** Если требуется, создайте объект "IP-адрес": 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/aliases/ip_addresses --data '{"comment": "комментарий", "title": "название", "value": "9.9.9.9"}'
```

Ответ: статус 200.

Тело ответа:

```
{
    "id": "ip.id.3"
}
```

**2.2\.** Если нужные объекты уже существуют, то получите список id, выполнив команду:

```
curl -k -c /tmp/cookie -b /tmp/cookie https://178.154.205.107:8443/aliases/
```

В ответе будет список всех объектов системы. Выберите нужные id (вид ip.id.1):

```
[
    {
        comment: "test ip alias",
        title: "test ip alias",
        type: "ip",
        value: "9.9.9.9",
        id: "ip.id.1"
    },
    {
        comment: "test ip alias 2",
        title: "test ip alias 2",
        type: "ip",
        value: "9.9.9.10",
        id: "ip.id.2"
    }
]
```

**3\.** Создайте объект типа Список объектов: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/aliases/lists/addresses --data '{"title": "название", "comment": "комментарий", "values": ["ip.id.3", "ip.id.2", "ip.id.1"]}'
```

</details>

<details>

<summary>Добавление URL в пользовательскую категорию контент-фильтра</summary>

Предполагается, что уже созданы и настроены: пользователи, пользовательская категория контент-фильтра и правило контент-фильтра, в котором используются созданные пользователи и категории. Через API требуется редактировать список URL в конкретной пользовательской категории.

**1\.** Авторизуйте администратора: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "recaptcha": "", "rest_path": "/"}'
```

Ответ: статус 200.

**2\.** Добавьте URL в ранее созданную пользовательскую категорию контент-фильтра:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X PUT https://178.154.205.107:8443/content-filter/users_categories/users.id.1 --data '{"name": "название", "description": "комментарий", "urls": ["https://yandex.ru", "https://wrong-url.com"]}'
```

Ответ: статус 200.

Тело ответа при добавлении URL в ранее созданную категорию контент-фильтра:

```
{"id": "users.id.3", "name": "название", "description": "комментарий", "urls": ["https://yandex.ru", "https://wrong-url.com"]}
```

</details>

## Создание правила Forward

Задача: создать правило Forward с указанием диапазона IP-адресов (192.168.0.1-192.168.0.20) в качестве источника и протоколом TCP. \
Далее в созданное правило внести изменение, указав время действия.

**1\.** Авторизуйте администратора: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "recaptcha": "", "rest_path": "/"}'
```

Ответ: статус 200.

**2\.** Создайте объект Диапазон IP-адресов c 192.168.0.1 по 192.168.0.20:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/aliases/ip_ranges --data '{"title": "test ip range", "comment": "test ip range", "start": "192.168.0.1", "end": "192.168.0.20"}'
```

Ответ: статус 200.

Тело ответа:

```
{
    "id": "ip_range.id.2"
}
```

**3\.** Создайте правило файрвола:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/firewall/rules/forward --data '{"action": "действие: accept - принять пакет; drop - отклонить пакет;", "comment": "комментарий", "destination_addresses": ["адреса назначений, список ID алиасов"], "destination_ports": ["порты назначений, список ID алиасов"], "incoming_interface": "входящий интерфейс, ID алиаса", "outgoing_interface": "исходящий интерфейс, ID алиаса", "protocol": "протокол, ID алиаса", "source_addresses": ["адреса источников"], "timetable": ["время действия"], "enabled": правило включено/выключено}'
```

Ответ: статус 200.

Тело ответа:

```
{"action": "drop", "destination_addresses": ["any"], "destination_ports": ["port.id.1"], "enabled": true, "incoming_interface": "any", "outgoing_interface": "any", "protocol": "protocol.tcp", "source_addresses": ["any"], "timetable": ["any"], "comment": "", "id": 2}
```

**4\.** Отредактируйте созданное правило, указав время действия:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X PUT https://51.250.72.140:8443/firewall/rules/forward/1 --data '{"action": "drop", "comment": "", "destination_addresses": ["any"], "destination_ports": ["port.id.1"], "incoming_interface": "any", "outgoing_interface": "any", "protocol": "protocol.tcp", "source_addresses": ["any"], "timetable": ["time_range.id.1"], "enabled": true, "id": 2}'
```

Ответ: статус 200.

Тело ответа:

```
{"action": "drop", "comment": "", "destination_addresses": ["any"], "destination_ports": ["port.id.1"], "incoming_interface": "any", "outgoing_interface": "any", "protocol": "protocol.tcp", "source_addresses": ["any"], "timetable": ["time_range.id.1"], "enabled": true, "id": 2}
```

## Описание хендлеров

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

### Управление объектами

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
    "end": "string",
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
    "values": ["string"]
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

</details>

### Пользовательские категории контент-фильтра

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
{
    "id": "string", (номер категории, вида - users.id.1)
    "name": "string", (название категории, не пустая строка)
    "description": "string",
    "urls": ["string"] 
}
```

**urls** - список url. Либо полный путь до страницы, либо только доменное имя. В пути могут присутствовать, означающие любое количество любых символов на этом месте

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