# Антиспам и антивирус Касперского

<details>
<summary>Получение настроек Антиспама и антивируса</summary>

`GET /mail/klms/state`

**Ответ на успешный запрос:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - `true`, когда KLMS включен, и `false`, когда выключен.

</details>

<details>
<summary>Изменение настроек Антиспама и антивируса</summary>

`PUT /mail/klms/state`

**Json-тело запроса:**

```json5
{
  "enabled": "boolean"
}
```

* `enabled` - `true`, когда KLMS требуется включить, и `false`, когда выключить.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Загрузка ключа лицензии</summary>

**ВАЖНО!** Загрузить ключ лицензии можно только в том случае, когда KLMS включен. Если KLMS выключен, то загрузка ключа недоступна.

`POST /mail/klms/license`

**Тело запроса:** двоичные данные файла лицензии.

</details>

<details>
<summary>Получение даты/времени обновления баз</summary>

`GET /mail/klms/last_update`

**Ответ на успешный запрос:**

```json5
{
  "last_update": "null" | "float"
}
```

* `last_update` - дата/время последнего обновления баз в формате UNIX timestamp; `null`, если невозможно определить статус; 0, если базы не установлены.

</details>

<details>
<summary>Получение даты/времени окончания ключа лицензии</summary>

`GET /mail/klms/license`

**Ответ на успешный запрос:**

```json5
{
  "is_active": "null" | "boolean",
  "expiration_date": "null" | "float"
}
```

* `is_active` - `true`, когда ключ лицензии активирован, и `false`, когда не активирован; `null`, если невозможно определить статус активированности.
* `expiration_date` - дата/время окончания действия ключа лицензии в формате UNIX timestamp; `null`, когда ключ отсутствует или невозможно определить статус.

</details>

