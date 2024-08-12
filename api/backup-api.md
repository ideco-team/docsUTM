# Бэкапы

{% hint style="info" %}
Длина комментариев (`comment`) при API-запросах ограничена 255 символами.
{% endhint %}

<details>
<summary>Получение настроек бэкапов</summary>

```
GET /backup/settings
```

**Ответ на успешный запрос:**

```json5
{
   "common": {
      "hour": "integer",
      "rotate": "weekly | monthly"
   },
   "ftp": {
      "enabled": "boolean",
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   },
   "cifs": {
      "enabled": "boolean",
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   }
}
```

* `common` - общие настройки бэкапов;
  * `hour` - час, в который делается автоматический бэкап, число от 0 до
    23;
  * `rotate` - удалять бэкапы старше недели (`weekly`) или месяца
    (`monthly`);
* `ftp` - настройки выгрузки бэкапов на FTP:
  * `enabled` - выгрузка включена/выключена;
  * `server` - адрес сервера, валидный домен или IP-адрес;
  * `login` - логин, не пустая строка;
  * `password` - пароль, не пустая строка, до 42 символов;
  * `remote_dir` - удаленный каталог, не пустая строка;
* `cifs` - настройки выгрузки бэкапов в общую папку CIFS:
  * `enabled` - выгрузка включена/выключена;
  * `server` - адрес сервера, валидный домен или IP-адрес;
  * `login` - логин, не пустая строка;
  * `password` - пароль, не пустая строка, до 42 символов;
  * `remote_dir` - удаленный каталог, не пустая строка.

</details>

<details>
<summary>Изменение настроек бэкапов и настройка выгрузки на FTP-сервер или в общую папку CIFS</summary>

```
PUT /backup/settings
```

**Json-тело запроса:**

```json5
{
   "common": {
      "hour": "integer",
      "rotate": "weekly | monthly"
   },
   "ftp": {
      "enabled": "boolean",
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   },
   "cifs": {
      "enabled": "boolean",
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   }
}
```

**Ответ на успешный запрос:** 200 ОК

</details>

## Управление бэкапами

<details>
<summary>Создание бэкапа</summary>

```
POST /backup/backups
```

**Json-тело запроса:**

```json5
{
   "comment": "string" //(комментарий, произвольный текст)
}
```

**Ответ на успешный запрос:**

```json5
{
    "id": "string"
}
```

</details>

<details>
<summary>Получение списка бэкапов</summary>

```
GET /backup/backups
```

**Ответ на успешный запрос:**

```json5
{
   "id": "string",
   "version": {
      "major": "integer",
      "minor": "integer",
      "build": "integer",
      "timestamp": "integer",
      "vendor": "Ideco",
      "product": "UTM" | "CC",
      "kind": "FSTEK" | "VPP" | "STANDARD" | "BPF",
      "release_type": "release" | "beta" | "devel"
   },
   "timestamp": "float",
   "comment": "string",
   "md5": "string",
   "size": "integer",
   "fast_restore_allowed": "boolean"
}
```

* `id` - идентификатор бэкапа;
* `version` - версия системы:
  * `major` -мажорный номер версии;
  * `minor` - минорный номер версии;
  * `build` - номер сборки;
  * `timestamp` - время выхода версии; 
  * `vendor` - вендор ("Ideco");
  * `product` - код продукта;
  * `kind` - вид продукта;
  * `release_type` - тип релиза;
* `timestamp` - дата/время создания бэкапа в формате UNIX timestamp;
* `comment` - комментарий, произвольный текст;
* `md5` - контрольная сумма файла бэкапа (`data.tar`);
* `size` - размер бэкапа, байт;
* `fast_restore_allowed` - можно ли выполнить быстрое восстановление из данного бэкапа (версия идентична системной).

</details>

<details>
<summary>Скачивание бэкапа</summary>

```
GET /backup/download/<id бэкапа>
```

**Ответ на успешный запрос:** тело бэкапа.

</details>

<details>
<summary>Загрузка бэкапа на Ideco NGFW из файла</summary>

```
POST /backup/upload
```

Используйте стандартный POST-запрос на загрузку файла. Название поля в форме должно
быть `backup_file`.

**Ответ на успешный запрос:**

```json5
{
   "id": "string"
}
```

</details>

<details>
<summary>Восстановление из бэкапа</summary>

```
POST /backup/backups/<id бэкапа>/apply
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Быстрое восстановление из бэкапа</summary>

```
POST /backup/backups/<id бэкапа>/apply/fast
```

**Ответ на успешный запрос:** 200 ОК

</details>

<details>
<summary>Удаление бэкапа</summary>

```
DELETE /backup/backups/<id бэкапа>
```

**Ответ на успешный запрос:** 200 ОК

</details>