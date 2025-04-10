# Управление обратным прокси

<details>
<summary>Получение списка публикаций</summary>

```
GET /reverse_proxy_backend/user_sites
```

**Ответ на успешный запрос:**

```json5
[
    {
    "id": "string",
    "enabled": "boolean",
    "dos_protection_enabled": "boolean",
    "is_internal": "boolean",
    "waf_profile": "string" | "null",
    "redirect_http_to_https": "boolean",
    "bind_remote_addr": "boolean",
    "site_type": "standard" | "owa",
    "domains_and_locations": ["string"],
    "target_schema": "http" | "https",
    "target_servers": ["string"],
    "target_path": "string",
    "comment": "string"
    },
  ...
]
```

* `id` - идентификатор публикации;
* `enabled` - публикация включена/выключена;
* `dos_protection_enabled` - защита от DoS включена/выключена;
* `is_internal` - опция **Внутренний севис Ideco NGFW** включена/выключена;
* `waf_profile` - профиль WAF, может быть `null`. Должен быть `null`, если это внутренний ресурс (почта, ЛК, веб-интерфейс), максимальная длина - 42 символа;
* `redirect_http_to_https` - опция  **Перенаправлять HTTP-запросы на HTTPS** включена/выключена;
* `bind_remote_addr` - опция **Передавать web-серверу реальный IP-адрес клиента** включена/выключена;
* `site_type` - тип публикации: **Стандартный** или **Outlook Web Access**;
* `domains_and_locations` - непустой список доменов или доменов с путями, которые открыты для внешнего доступа. Каждый элемент списка представляет собой строку: `<домен или ip>[/<путь>]`;
* `target_schema` - доступ к публичному локальному веб-серверу осуществляется по протоколу `HTTP` или `HTTPS`;
* `target_servers`- непустой список адресов публикуемого локального веб-сервера, адрес может быть: `<IP-адрес>`, `<IP-адрес:порт>`, `<доменное_имя>`, `<доменное_имя:порт>`. Если `is_internal=false`, то в списке адресов нельзя указывать локальный адрес сервера (`127.0.0.1` или `localhost`);
* `target_path` - путь на публикуемом локальном веб-сервере: либо пустая строка, либо обязан начинаться с символа `/`;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

Если значение `is_internal=true`, то необходимо выбрать один из трех сервисов: личный кабинет пользователя, веб-интерфейс или почта. Для этого укажите фиксированные значения:

* `target_servers`:
  * ЛК - `127.0.0.1:13303`;
  * Веб-интерфейс - `127.0.0.1:8443`;
  * Почта - `127.0.0.1:11071`.
* `target_path`:
  * ЛК - `/`;
  * Веб-интерфейс - `/`;
  * Почта - `/webmail`.
* `target_schema` - `https`;
* `bind_remote_addr` - `false`;
* `site_type` - `standard`.

</details>

<details>
<summary>Создание публикации</summary>

```
POST /reverse_proxy_backend/user_sites
```

**Json-тело запроса:**:

```json5
[
    {
    "id": "string",
    "enabled": "boolean",
    "dos_protection_enabled": "boolean",
    "is_internal": "boolean",
    "waf_profile": "string" | "null",
    "redirect_http_to_https": "boolean",
    "bind_remote_addr": "boolean",
    "site_type": "standard" | "owa",
    "domains_and_locations": ["string"],
    "target_schema": "http" | "https",
    "target_servers": ["string"],
    "target_path": "string",
    "comment": "string"
    },
  ...
]
```

* `enabled` - публикация включена/выключена;
* `dos_protection_enabled` - защита от DoS включена/выключена;
* `is_internal` - опция **Внутренний севис Ideco NGFW** включена/выключена;
* `waf_profile` - профиль WAF, может быть `null`. Должен быть `null`, если это внутренний ресурс (почта, ЛК, веб-интерфейс), максимальная длина - 42 символа;
* `redirect_http_to_https` - опция  **Перенаправлять HTTP-запросы на HTTPS** включена/выключена;
* `bind_remote_addr` - опция **Передавать web-серверу реальный IP-адрес клиента** включена/выключена;
* `site_type` - тип публикации: **Стандартный** или **Outlook Web Access**;
* `domains_and_locations` - непустой список доменов или доменов с путями, которые открыты для внешнего доступа. Каждый элемент списка представляет собой строку: `<домен или ip>[/<путь>]`;
* `target_schema` - доступ к публичному локальному веб-серверу осуществляется по протоколу `HTTP` или `HTTPS`;
* `target_servers`- непустой список адресов публикуемого локального веб-сервера, адрес может быть: `<IP-адрес>`, `<IP-адрес:порт>`, `<доменное_имя>`, `<доменное_имя:порт>`. Если `is_internal=false`, то в списке адресов нельзя указывать локальный адрес сервера (`127.0.0.1` или `localhost`);
* `target_path` - путь на публикуемом локальном веб-сервере: либо пустая строка, либо обязан начинаться с символа `/`;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

Если значение `is_internal=true`, то необходимо выбрать один из трех сервисов: личный кабинет пользователя, веб-интерфейс или почта. Для этого укажите фиксированные значения:

* `target_servers`:
  * ЛК - `127.0.0.1:13303`;
  * Веб-интерфейс - `127.0.0.1:8443`;
  * Почта - `127.0.0.1:11071`.
* `target_path`:
  * ЛК - `/`;
  * Веб-интерфейс - `/`;
  * Почта - `/webmail`.
* `target_schema` - `https`;
* `bind_remote_addr` - `false`;
* `site_type` - `standard`.

**Ответ на успешный запрос:**

```json5
{
  "id": "string"
}
```

* `id` - идентификатор публикации.

</details>

<details>
<summary>Изменение публикации</summary>

```
PATCH /reverse_proxy_backend/user_sites/<id публикации>
```

**Json-тело запроса:**:

```json5
[
    {
    "id": "string",
    "enabled": "boolean",
    "dos_protection_enabled": "boolean",
    "is_internal": "boolean",
    "waf_profile": "string" | "null",
    "redirect_http_to_https": "boolean",
    "bind_remote_addr": "boolean",
    "site_type": "standard" | "owa",
    "domains_and_locations": ["string"],
    "target_schema": "http" | "https",
    "target_servers": ["string"],
    "target_path": "string",
    "comment": "string"
    },
  ...
]
```

* `enabled` - публикация включена/выключена;
* `dos_protection_enabled` - защита от DoS включена/выключена;
* `is_internal` - опция **Внутренний севис Ideco NGFW** включена/выключена;
* `waf_profile` - профиль WAF, может быть `null`. Должен быть `null`, если это внутренний ресурс (почта, ЛК, веб-интерфейс), максимальная длина - 42 символа;
* `redirect_http_to_https` - опция  **Перенаправлять HTTP-запросы на HTTPS** включена/выключена;
* `bind_remote_addr` - опция **Передавать web-серверу реальный IP-адрес клиента** включена/выключена;
* `site_type` - тип публикации: **Стандартный** или **Outlook Web Access**;
* `domains_and_locations` - непустой список доменов или доменов с путями, которые открыты для внешнего доступа. Каждый элемент списка представляет собой строку: `<домен или ip>[/<путь>]`;
* `target_schema` - доступ к публичному локальному веб-серверу осуществляется по протоколу `HTTP` или `HTTPS`;
* `target_servers`- непустой список адресов публикуемого локального веб-сервера, адрес может быть: `<IP-адрес>`, `<IP-адрес:порт>`, `<доменное_имя>`, `<доменное_имя:порт>`. Если `is_internal=false`, то в списке адресов нельзя указывать локальный адрес сервера (`127.0.0.1` или `localhost`);
* `target_path` - путь на публикуемом локальном веб-сервере: либо пустая строка, либо обязан начинаться с символа `/`;
* `comment` - комментарий, максимальная длина - 255 символов, может быть пустым.

Если значение `is_internal=true`, то необходимо выбрать один из трех сервисов: личный кабинет пользователя, веб-интерфейс или почта. Для этого укажите фиксированные значения:

* `target_servers`:
  * ЛК - `127.0.0.1:13303`;
  * Веб-интерфейс - `127.0.0.1:8443`;
  * Почта - `127.0.0.1:11071`.
* `target_path`:
  * ЛК - `/`;
  * Веб-интерфейс - `/`;
  * Почта - `/webmail`.
* `target_schema` - `https`;
* `bind_remote_addr` - `false`;
* `site_type` - `standard`.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление публикации</summary>

```
DELETE /reverse_proxy_backend/user_sites/<id публикации>
```

**Ответ на успешный запрос:** 200 ОК

</details>
