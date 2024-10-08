# Предотвращение вторжений

Путь в веб-интерфейсе NGFW: **Правила трафика -> Предотвращение вторжений**

<details>
<summary>Получение статуса работы службы</summary>

```
GET /ips/status
```

**Ответ на успешный запрос:** 

```json5
[
    {
        "name": "string",
        "status": "active" | "activating" | "deactivating" | "failed" | "inactive" | "reloading",
        "msg": [ "string" ]
    }
]
```

* `name` - название демона;
* `status` - статус;
* `msg` - список сообщений, объясняющий текущее состояние.

</details>

<details>
<summary>Управление статусом работы службы</summary>

**Получение текущей настройки включенности модуля**

```
GET /ips/state
```

**Ответ на успешный запрос:**

```json5
{
    "enabled": "boolean"
}
```

* `enabled` - `true` если модуль включен, `false` - если выключен.

**Изменение настройки включенности модуля**

```
PUT /ips/state
```

**Json-тело запроса:**

```json5
{
    "enabled": "boolean"
}
```

**Ответ на успешный запрос:** 200 OK

</details>

## Группы сигнатур

<details>
<summary>Получение представления групп сигнатур в табличном виде</summary>

```
GET /ips/signature_groups/table
```

**Ответ на успешный запрос:** 

```json5
{
    "signature_groups": [
        {
            "classtype": "string",
            "classtype_name": "string",  
            "mitre_tactics": [
                {
                    "mitre_tactic_id": "string",
                    "mitre_tactic_name": "string"  
                },
                ...
            ],
            "count": "integer"
        },
        ...
    ]
}
```

* `classtype` - группа сигнатур;
* `classtype_name` - название группы сигнатур (отображается в интерфейсе Ideco NGFW);
* `mitre_tactics` - тактика согласно матрице MITRE ATT&CK, которой соответствует группа сигнатур:
    * `mitre_tactic_id` - идентификатор тактики;
    * `mitre_tactic_name` - название тактики.
* `count` - количество сигнатур в группе.

</details>

<details>
<summary>Получение представления групп сигнатур в матричном виде MITRE ATT&CK</summary>

```
GET /ips/signature_groups/mitre
```

**Ответ на успешный запрос:**

```json5
{
    "signature_groups": [
        {
            "mitre_tactic_id": "string",
            "mitre_tactic_name": "string",  
            "classtypes": [
                {
                    "classtype": "string-admin",
                    "classtype_name": "string",  
                    "count": "integer"
                },
                ...
            ]
        },
        ...
    ]
}
```

* `mitre_tactic_id` - идентификатор тактики согласно матрице MITRE ATT&CK;
* `mitre_tactic_name` - название тактики;
* `classtypes` - группы сигнатур, соответствующие тактике:
    * `classtype` - группа сигнатур;
    * `classtype_name` - название группы сигнатур (отображается в интерфейсе Ideco NGFW);
    * `count` - количество сигнатур в группе.

</details>

<details>
<summary>Получение списка сигнатур определенной группы</summary>

```
GET /ips/signatures?filter=[ { "items": [ {"column_name":"classtype","operator":"equals","value":[<classtype нужной группы сигнатур (может быть несколько значений через запятую)>]} ], "link_operator":"or" } ]
```

* `"column_name":"classtype","operator":"equals","value":[<classtype нужной группы сигнатур (может быть несколько значений через запятую)>]` - фильтр. Отбирает из таблицы групп сигнатур только те группы, у которых значение `classtype` соответствует указанным в `value`.

**Ответ на успешный запрос:**

```json5
{
    "signatures": [
        {
            "action": "string",
            "protocol": "string",
            "flow": "string",
            "classtype": "string-admin",
            "sid": "integer",
            "signature_severity": "string",
            "mitre_tactic_id": "string",
            "signature_source": "string",
            "msg": "string",
            "source": "string",
            "source_ports": "string",
            "destination": "string",
            "destination_ports": "string",
            "updated_at": "string"
        },
        ...
    ]
}
```

* `action` - действие для трафика, соответствующего сигнатуре:
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`). Возможные значения представлены по [ссылке](https://docs.suricata.io/en/latest/rules/intro.html#protocol);
* `flow` - направление трафика (`client2server`, `server2client`, `-`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK;
* `signature_source` - источник сигнатуры: 
    * `standard` - стандартные правила;
    * `advanced` - правила IPS от Лаборатории Касперского;
    * `custom` - пользовательские правила.
* `msg` - название сигнатуры;
* `source` - источник подключения;
* `source_ports` - порты источника;
* `destination` - назначение;
* `destination_ports` - порты назначения;
* `updated_at` - дата в формате `YYYY-MM-DD` или строка со значением `-`.

</details>

<details>
<summary>Получение оригинального содержания сигнатуры</summary>

```
GET /ips/signatures/<sid>
```

* `sid` - идентификатор сигнатуры.
  
**Ответ на успешный запрос:**

```json
{
    "signature": "string"
}
```

* `signature` - содержание сигнатуры.

</details>

## Пользовательские сигнатуры

<details>
<summary>Получение списка пользовательских сигнатур</summary>

```
GET /ips/custom
```

**Ответ на успешный запрос:**

```json5
{
    "signatures": [
        {
            "action": "string",
            "protocol": "string",
            "flow": "string",
            "classtype": "string-admin",
            "sid": "integer",
            "signature_severity": "string",
            "mitre_tactic_id": "string",
            "signature_source": "string",
            "msg": "string",
            "source": "string",
            "source_ports": "string",
            "destination": "string",
            "destination_ports": "string",
            "updated_at": "string"
        },
        ...
    ]
}
```

* `action` - действие для трафика, соответствующего сигнатуре:
  * `pass` - **Пропускать**;
  * `alert` - **Предупреждать**;
  * `drop` - **Блокировать**;
  * `rejectsrc` - **Отправлять RST узлу источника**;
  * `rejectdst` - **Отправлять RST узлу назначения**;
  * `rejectboth` - **Отправлять RST обоим**.
* `protocol` - протокол (`tcp`, `udp`, `icmp`, `ip`). Возможные значения представлены по [ссылке](https://docs.suricata.io/en/latest/rules/intro.html#protocol);
* `flow` - направление трафика (`client2server`, `server2client`, `-`);
* `classtype` - группа, к которой относится сигнатура;
* `sid` - идентификатор сигнатуры;
* `signature_severity` - уровень угрозы;
* `mitre_tactic_id` - тактика согласно матрице MITRE ATT&CK;
* `signature_source` - источник сигнатуры: 
    * `standard` - стандартные правила;
    * `advanced` - правила IPS от Лаборатории Касперского;
    * `custom` - пользовательские правила.
* `msg` - название сигнатуры;
* `source` - источник подключения;
* `source_ports` - порты источника;
* `destination` - назначение;
* `destination_ports` - порты назначения;
* `updated_at` - дата в формате `YYYY-MM-DD` или строка со значением `-`.

</details>

<details>
<summary>Создание пользовательской сигнатуры вручную</summary>

```
POST /ips/custom
```

**Json-тело запроса:**

```json5
{
    "comment": "string",
    "rule": "string"
}
```

* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `rule` - строка с правилом, не более 8196 символов, переводы строк в ней запрещены.

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

* `id` - идентификатор созданной сигнатуры.

</details>

<details>
<summary>Загрузка пользовательских сигнатур из файла</summary>

```
POST /ips/custom_rules_file
```

Файл загружается как тело запроса, он должен иметь текстовый формат text/plain, максимальный размер файла - 32 MB.

**Ответ на успешный запрос:**

```json5
{
    "count": "integer"
}
```

* `count` - количество загруженных правил.

</details>

<details>
<summary>Редактирование пользовательской сигнатуры</summary>

```
PATCH /ips/custom/<sid>
```

* `sid` - идентификатор сигнатуры

**Json-тело запроса (все или некоторые поля):**

```json5
{
    "comment": "string",
    "rule": "string"
}
```

* `comment` - описание, может быть пустым, максимальная длина - 255 символов;
* `rule` - строка с правилом, не более 8196 символов, переводы строк в ней запрещены.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление пользовательской сигнатуры</summary>

```
DELETE /ips/custom/<sid>
```

* `sid` - идентификатор сигнатуры

**Ответ на успешный запрос:** 200 ОК

</details>

## Обновление баз

<details>
<summary>Получение статуса обновления баз правил Suricata и GeoIP</summary>

```
GET /ips/update
```

**Ответ на успешный запрос:**

```json
{
    "status": "up_to_date" | "updating" | "failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float" | "null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваются новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Получение статуса обновления расширенных баз правил Suricata и GeoIP</summary>

```
GET /ips/update_advanced
```

**Ответ на успешный запрос:**

```json
{
    "status": "up_to_date" | "updating" | "failed_to_update|disabled",
    "msg": "i18n_string",
    "last_update": "float" | "null"
}
```

* `status` - текущий статус обновления баз:
  * `up_to_date` - базы успешно обновлены;
  * `updating` - скачиваются новые базы;
  * `failed_to_update` - последняя попытка обновления баз завершилась неудачно;
  * `disabled` - обновление баз выключено.
* `msg` - текстовое описание статуса обновления баз;
* `last_update` - время последнего успешного обновления баз.

</details>

<details>
<summary>Запуск принудительного обновления баз</summary>

```
POST /ips/update
```

**Ответ на успешный запрос:** 200 OK

</details>

## Сети, защищенные от вторжений

<details>
<summary>Получение списка локальных подсетей</summary>

```
GET /ips/nets
```

**Ответ на успешный запрос:**

```json
[
    {
    "id": "string",
    "address": "string"
  },
  ...
]
```

* `id` - идентификатор подсети;
* `address` - адрес подсети (например, `192.168.0.0/16`).

</details>

<details>
<summary>Добавление новой локальной подсети</summary>

```
POST /ips/nets
```

**Json-тело запроса:**

```json
{
    "address": "string"
  }
```

* `address` - адрес подсети (например, `192.168.0.0/16`).

</details>

<details>
<summary>Удаление локальной подсети</summary>

```
DELETE /ips/nets/<id локальной подсети>
```

**Ответ на успешный запрос:** 200 OK

</details>