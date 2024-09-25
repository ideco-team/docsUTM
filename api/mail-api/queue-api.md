## Почтовая очередь

<details>
<summary>Получение очереди</summary>

`GET /mail/mail_queue`

**Ответ на успешный запрос:**

```json5
[
  {
    "id": "string",
    "arrival_time": "integer",
    "sender": "string",
    "recipient": "string",
    "delay_reason": "string"
  },
  ...
]
```

* `id` - идентификатор письма;
* `arrival_time` - время отправки;
* `sender` - отправитель;
* `recipient` - получатель;
* `delay_reason` - причина задержки. Может быть пустой строкой.

</details>

<details>
<summary>Повторная отправка</summary>

`POST /mail/mail_queue_retry`

**Json-тело запроса:**

```json5

{
  "ids": ["string", "string", ...]
}

```

- `ids` - список идентификаторов писем.

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление писем из очереди</summary>

`DELETE /mail/mail_queue/ID1,ID2,...`

* `ID1,ID2,...` - список идентификаторов писем.

**Ответ на успешный запрос:** 200 ОК

</details>