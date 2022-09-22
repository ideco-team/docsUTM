# API Ideco UTM

## Авторизация

```
POST /web/auth/login
```

Json тела запроса:

```
{
    "login": string,    
    "password": string,    
    "recaptcha": string (по умолчанию пустая строка - ""),
    "rest_path": string (по умолчанию строка со слешем "/")
}

```
После успешной авторизации, сервер Ideco UTM передаёт в заголовках куки. Пример значений ниже:

```
set-cookie: insecure-ideco-session=02428c1c-fcd5-42ef-a533-5353da743806
set-cookie: __Secure-ideco-3ea57fca-65cb-439b-b764-d7337530f102=df164532-b916-4cda-a19b-9422c2897663:1663839003
```

Эти куки нужно передавать при каждом запросе после авторизации в качестве заголовка запроса Cookie.

**Пример запроса:**

```
curl -k -b /tmp/cookie -c /tmp/cookie -X POST https://51.250.13.222:8443/web/auth/login --data '{"login": "administrator", "password": "test", "recaptcha": "", "rest_path": "/"}'
```

## Создание объекта IP-адрес

```
POST /aliases/ip_addresses
```

Json тела запроса:

```
{
    "comment": "string",    
    "title": "string",    
    "value": "string"
}
```

Ответ на запрос: *{"id": "string"}*.

**Пример запроса:**

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://51.250.13.222:8443/aliases/ip_addresses --data '{"title": "qwe", "comment": "from rest", "value": "9.9.9.9"}'
```

## Получение ID объектов

```
GET /aliases/
```

Json ответ на запрос:

```
[
    {
        "comment": "string",
        "id": "string",
        "title": "string",
        "type": "string" (для объектов IP адрес значение = "ip")
        "value": "string"
    }
] 
```

## Создание объекта Список адресов

```
POST /aliases/lists/addresses
```

Json тела запроса:

```
{
    "comment": "string",
    "title": "string",
    "values": ["string"]
}
```

Ответ на запрос: *{"id": "string"}*.


## Получение ID пользовательской категории контент-фильтра

```
GET /content-filter/users_categories
```

Json ответ на запрос:

```
{
    "description": string,
    "id": string,
    "name": string,
    "urls": [string]
}
```



## Добавление URL  в пользовательскую категорию контент-фильтра
```
PUT /content-filter/users_categories/{category_id}
```

Json тела запроса:

```
{
    "description": string,
    "name": string,
    "urls": [string]
}
```

Json ответ на запрос:

```
{
    "description": string,
    "id": string,
    "name": string,
    "urls": [string]
}
```