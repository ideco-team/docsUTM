# API: пример использования

## Примеры использования

### Создание списка объектов

1\. Авторизуйте пользователя: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "recaptcha": "", "rest_path": "/"}'
```

Ответ: статус 200

2\. Если требуется, создайте объект: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/aliases/ip_addresses --data '{"comment": "комментарий", "title": "название", "value": "9.9.9.9"}'
```

Ответ: статус 200

Тело ответа:
```
{
    "id": "ip.id.3"
}
```

3\. Создайте список объектов: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/aliases/lists/addresses --data '{"title": "название", "comment": "комментарий", "values": ["ip.id.3", "ip.id.2", "ip.id.1"]}'
```

3.1\. Если для создания списка требуются id объектов, отличных от пункта 2, то получите список всех id. Пример:

```
curl -k -c /tmp/cookie -b /tmp/cookie https://178.154.205.107:8443/aliases/
```

### Добавление URL в пользовательскую категорию контент-фильтра

1\. Авторизуйте пользователя: 

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "recaptcha": "", "rest_path": "/"}'
```

Ответ: статус 200

2\. Добавьте URL в ранее созданную пользовательскую категорию контент-фильтра:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X PUT https://178.154.205.107:8443/content-filter/users_categories/users.id.1 --data '{"name": "название", "description": "комментарий", "urls": ["https://yandex.ru", "https://wrong-url.com"]}'
```

Ответ: статус 200

Тело ответа при добавлении URL в ранее созданную категорию контент-фильтра:

```
{"id": "users.id.3", "name": "test category", "description": "test users category", "urls": ["yandex.ru", "www.standards.ru"]}
```

2.1\. Или создайте новую пользовательскую категорию контент-фильтра:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://178.154.205.107:8443/content-filter/users_categories `{name: "1", description: "1", urls: ["https://wrong-url.com"]}`
```

Тело ответа при создании категории контент-фильтра:

```
{
    "id": "users.id.6"
}
```

## Описание хендлеров

<details>

<summary>Авторизация</summary>

```
POST /web/auth/login
```

**Json тела запроса:**

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

**Json тела запроса:**

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

<summary>Создание объекта "Диапазон IP-адресов"</summary>

```
POST /aliases/ip_ranges
```

**Json тела запроса:**

```
{
    "id": {
        "type": "ip_range",
        "title": "string",
        "comment": "string",
        "start": "string",
        "end": "string",
    },
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

<summary>Создание объекта "Список адресов"</summary>

```
POST /aliases/lists/addresses
```

**Json тела запроса:**

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
        "id": "string",
        "type": "string" (для объектов IP адрес значение = "ip")
        "title": "string"
    }, 
    ...
] 
```

</details>

### Пользовательские категории контент-фильтра

<details>

<summary>Добавление URL</summary>

```
POST /content-filter/users_categories
```

**Json тела запроса:**

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

<summary>Получение ID</summary>

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

**Json тела запроса:**

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