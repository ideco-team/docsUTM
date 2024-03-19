# Бекапы

<details>
<summary>Получение настроек бекапов</summary>

```
GET /backup/settings
```

**Ответ на успешный запрос:**

```
{
   "common": {
      "hour": int,
      "rotate": "weekly | monthly"
   },
   "ftp": {
      "enabled": boolean,
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   },
   "cifs": {
      "enabled": boolean,
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   }
}
```

* `common` - общие настройки бекапов;
  * `hour` - час, в который делается автоматический бекап, число от 0 до
    23;
  * `rotate` - удалять бекапы старше недели (`weekly`) или месяца
    (`monthly`);
* `ftp` - настройки выгрузки бекапов на FTP:
  * `enabled` - выгрузка включена/выключена;
  * `server` - адрес сервера, валидный домен или IP-адрес;
  * `login` - логин, не пустая строка;
  * `password` - пароль, не пустая строка, до 42 символов;
  * `remote_dir` - удаленный каталог, не пустая строка;
* `cifs` - настройки выгрузки бекапов в общую папку CIFS:
  * `enabled` - выгрузка включена/выключена;
  * `server` - адрес сервера, валидный домен или IP-адрес;
  * `login` - логин, не пустая строка;
  * `password` - пароль, не пустая строка, до 42 символов;
  * `remote_dir` - удаленный каталог, не пустая строка.

</details>

<details>
<summary>Изменение настроек бекапов и настройка выгрузки на FTP-сервер или в общую папку CIFS</summary>

```
PUT /backup/settings
```

**Json-тело запроса:**

```
{
   "common": {
      "hour": int,
      "rotate": "weekly | monthly"
   },
   "ftp": {
      "enabled": boolean,
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   },
   "cifs": {
      "enabled": boolean,
      "server": "string",
      "login": "string",
      "password": "string",
      "remote_dir": "string"
   }
}
```

Ответ: 200 ОК

</details>

## Управление бекапами

<details>
<summary>Создание бекапа</summary>

```
POST /backup/backups
```

**Json-тело запроса:**

```
{
   "comment": "string" (комментарий, произвольный текст)
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
<summary>Получение списка бекапов</summary>

```
GET /backup/backups
```

**Ответ на успешный запрос:**

```
{
   "id": "string",
   "version": {
      "major": int,
      "minor": int,
      "build": int,
      "timestamp": int,
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

* `id` - идентификатор бекапа;
* `version` - версия системы:
  * `major` -мажорный номер версии;
  * `minor` - минорный номер версии;
  * `build` - номер сборки;
  * `timestamp` - время выхода версии; 
  * `vendor` - вендор ("Ideco");
  * `product` - код продукта;
  * `kind` - вид продукта;
  * `release_type` - тип релиза;
* `timestamp` - дата/время создания бекапа в формате UNIX timestamp;
* `comment` - комментарий, произвольный текст;
* `md5` - контрольная сумма файла бекапа (`data.tar`);
* `size` - размер бекапа, байт;
* `fast_restore_allowed` - можно ли выполнить быстрое восстановление из данного бекапа (версия идентична системной).

</details>

<details>
<summary>Скачивание бекапа</summary>

```
GET /backup/download/<id бекапа>
```

Ответ: тело бекапа.

</details>

<details>
<summary>Загрузка бекапа на Ideco NGFW из файла</summary>

```
POST /backup/upload
```

Используйте стандартный POST-запрос на загрузку файла. Название поля в форме должно
быть `backup_file`.

**Ответ на успешный запрос:**

```
{
   "id": "string"
}
```

</details>

<details>
<summary>Восстановление из бекапа</summary>

```
POST /backup/backups/<id бекапа>/apply
```

Ответ: 200 ОК

</details>

<details>
<summary>Быстрое восстановление из бекапа</summary>

```
POST /backup/backups/<id бекапа>/apply/fast
```

Ответ: 200 ОК

</details>

<details>
<summary>Удаление бекапа</summary>

```
DELETE /backup/backups/<id бекапа>
```

Ответ: 200 ОК

</details>