# Настройка удаленной передачи системных логов (Syslog)

<details>
<summary>Получение статуса работы службы</summary>

```
GET /logs_backend/remote_syslog/status
```

**Ответ на успешный запрос:**

```
[
    {
        "name": "string",
        "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading", 
        "msg": [ "string" ]
    },
    ...
]
```

* `name` - название модуля;
* `status` - статус;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

## Общие настройки

<details>
<summary>Включение/выключение службы</summary>

**Проверка состояния:**

```
GET /logs_backend/remote_syslog/state
```

**Ответ на успешный запрос:**

```
{
  "enabled": boolean (true - включен, false - выключен)
}
```

**Включение/выключение**

```
PUT /logs_backend/remote_syslog/state
```

**Json-тело запроса:**

```
{
  "enabled": boolean
}
```

Ответ: 200 ОК

</details>

<details>
<summary>Получение настроек удаленной передачи системных логов</summary>

```
GET /logs_backend/remote_syslog
```

**Ответ на успешный запрос:**

```
{
  "host": "string",
  "port": "int",
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef"
}
```

* `host` - IP-адрес сервера;
* `port` - порт;
* `protocol` - протокол, допустимые значения `tcp` или `udp`;
* `format` - формат, допустимые значения `syslog` или `cef`.

</details>

<details>
<summary>Изменение настроек удаленной передачи системных логов</summary>

```
PATCH /logs_backend/remote_syslog
```

**Json-тело запроса:**

```
{
  "host": "string" | null,
  "port": "int" | null,
  "protocol": "tcp" | "udp",
  "format": "syslog" | "cef",
}
```

Пустые значения "" не допускаются.

Ответ: 200 ОК

</details>