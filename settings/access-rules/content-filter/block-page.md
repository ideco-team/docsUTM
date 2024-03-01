---
description: В статье описаны шаги для изменения страницы блокировки Контент-фильтра.
---

# Изменение страницы блокировки Контент-фильтра

Страница блокировки Контент-фильтра по умолчанию содержит уведомление о блокировке доступа к ресурсу администратором сети и категоризацию ресурса. Если на страницу блокировки требуется добавить корпоративную информацию, то выполните действия: 

1\. Внесите изменения в файл с именем `ERR_CF_BLOCK_PAGE` (путь до файла `/usr/share/ideco/proxy-backend/error_page_templates/langs/ru_RU/error_content/ERR_CF_BLOCK_PAGE`). Пример изменения страницы ниже.

2\. Удалите кэш, выполнив команду `rm -r /var/cache/ideco/proxy-backend/error_pages`.

3\. Перезагрузите службу, выполнив команду `systemctl restart ideco-proxy-backend.service`.

**Содержимое файла `ERR_CF_BLOCK_PAGE` по умолчанию:**

```
<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width" />
  <link rel="icon" type="image/x-icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALE>
  <link rel="apple-touch-icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYA>
  <title>Доступ к ресурсу заблокирован</title>
  <style type="text/css">%l</style>
</head>

<body>

<div class="widget info viewport_big">
  <span class="icon"></span>
  <div class="widget_content">
    <h1>Доступ к ресурсу заблокирован</h1>
    <p>Данный сайт предоставляет контент, заблокированный администратором вашей сети как некорректный.</p>
    <p>Ресурс категоризирован как:</p>
    %O
  </div>
</div>
<div class="blocked_content">
  <h1>Контент заблокирован</h1>
</div>
</body>
</html>
```

**Как выглядит блокировка страницы по умолчанию:**

![](/.gitbook/assets/kf-r5.png)

**Пример изменения:**

Задача: Добавить на страницу блокировки ссылку на внутренний регламент, изменить заголовок на странице блокировки, добавить контакты для связи с системным администратором.

1\. Меняем заголовок на странице блокировки на **Доступ заблокирован** и добавляем ссылку на внутренний регламент:

{% code overflow="wrap" %}
```
<h1>Доступ заблокирован</h1>
<p>Данный сайт предоставляет контент, заблокированный администратором вашей сети как некорректный. Причины блокировки описаны во <a href="https://test.ru">внутреннем регламенте</a>.</p>
```
{% endcode %}

2\. Добавляем информацию о способах связи с системным администратором:

{% code overflow="wrap" %}
```
<p>Для предоставления доступа к ресурсу обратитесь к системному администратору одним из способов:</p>
<p>Тел.: +7(000)000-00-00</p>
<p>administrator@mail.ru</p>
<p><a href="https://telegram.im/@admin">Отправить заявку в Telegram</a></p>
```
{% endcode %}

3\. Вносим изменения в тело запроса:

{% code overflow="wrap" %}
```
<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width" />
  <link rel="icon" type="image/x-icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALE>
  <link rel="apple-touch-icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYA>
  <title>Доступ к ресурсу заблокирован</title>
  <style type="text/css">%l</style>
</head>

<body>

<div class="widget info viewport_big">
  <span class="icon"></span>
  <div class="widget_content">
    <h1>Доступ заблокирован</h1>
    <p>Данный сайт предоставляет контент, заблокированный администратором вашей сети как некорректный. Причины блокировки описаны во <a href="https://test.ru">внутреннем регламенте</a>.</p>
    <p>Ресурс категоризирован как:</p>
    %O
    <p>Для предоставления доступа к ресурсу обратитесь к системному администратору одним из способов:</p>
    <p>Тел.: +7(000)000-00-00</p>
    <p>administrator@mail.ru</p>
    <p><a href="https://telegram.im/@admin">Отправить заявку в Telegram</a></p>
  </div>
</div>
<div class="blocked_content">
  <h1>Контент заблокирован</h1>
</div>
</body>
</html>
```
{% endcode %}

![](/.gitbook/assets/kf-r4.png)