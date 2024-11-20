---
description: В статье описаны шаги для изменения страницы блокировки Контент-фильтра.
---

# Изменение страницы блокировки Контент-фильтра

Страница блокировки Контент-фильтра по умолчанию содержит уведомление о блокировке доступа к ресурсу и категоризацию:

![](/.gitbook/assets/kf-r5.png)

{% hint style="danger" %}
В процессе обновления Ideco NGFW все ранее настроенные параметры шаблона блокировки будут сброшены.
{% endhint %}

Для создания персонализированного шаблона страницы выполните действия:

1\. Удалите директорию, в которой хранятся файлы кеша страниц ошибок:

```
rm -R /var/cache/ideco/proxy-backend/error_pages
```

2\. Чтобы изменить фавикон, загрузите новый файл в директорию **/usr/share/ideco/vendor/**. Для этого перейдите в раздел **Управление сервером -> Администраторы** и убедитесь, что доступ по SSH разрешен. Затем откройте терминал на компьютере и введите следующую команду:

```
scp C:\Users\Admin\Downloads\favicon.png admin@192.168.0.23:/usr/share/ideco/vendor
```

* `C:\Users\Admin\Downloads\favicon.png` - путь к файлу на вашем компьютере;
* `admin@192.168.0.23` - логин администратора и IP-адрес или домен NGFW;
* Файл обязательно должен иметь имя **favicon.png**.

3\. Чтобы изменить иконки предупреждения, загрузите новые файлы в директорию **/usr/share/ideco/proxy-backend/error_page_templates/images**. Для этого откройте терминал на компьютере и введите следующую команду:

```
scp C:\Users\Admin\Downloads\IDECO_ICON_INFO.svg admin@192.168.0.23:/usr/share/ideco/proxy-backend/error_page_templates/images
```

* `C:\Users\Admin\Downloads\favicon.png` - путь к файлу на вашем компьютере;
* `admin@192.168.0.23` - логин администратора и IP-адрес или домен NGFW;
* Файлы обязательно должны иметь имя **IDECO_ICON_ERROR.svg, IDECO_ICON_INFO.svg, IDECO_ICON_SUCCESS.svg, IDECO_ICON_WARNING.svg**.

4\. Чтобы изменить CSS-файл стилей для страниц ошибок, перейдите в директорию **/usr/share/ideco/proxy-backend/error_page_templates/** и откройте файл **style.css** в текстовом редакторе:

```
nano /usr/share/ideco/proxy-backend/error_page_templates/style.css
```

<details>
<summary>Пример изменения файла style.css</summary>

Чтобы изменить цвет текста и фона, отредактируйте блоки `error`, `warning`, `info`, `success`:

```
.error {
  background-color: #E6E2DD;
  color: #373A36;
}

.warning {
  background-color: #E6E2DD;
  color: #373A36;
}

.info {
  background-color: #E6E2DD;
  color: #373A36;
}

.success {
  background-color: #E6E2DD;
  color: #373A36;
}
```

Чтобы изменить цвет страницы, размер и отступы текста, отредактируйте блок `body`:

```
body {
  padding: 5% 12px;
  box-sizing: border-box;
  overflow: auto;
  background-color: #E6E2DD;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10px;
  line-height: 14px;
}
```

Чтобы изменить размер шрифта, отредактируйте блоки `h1` и `p`:

```
h1 {
  margin: 0;
  padding-bottom: 8px;
  font-weight: 500;
  font-size: 24px;
  line-height: 25px;
}

p {
  margin: 0;
  padding: 8px 0;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 16px;
}
```

Чтобы изменить цвет гиперссылок, отредактируйте блок `a`:

```
a {
  color: #D48166;
  text-decoration: none;
}
```

Чтобы изменить размер логотипа, отредактируйте блок `.icon`:

```
.icon {
  width: 150px;
  min-width: 150px;
  height: 150px;
  min-height: 150px;
  margin-right: 100px;
  background-position: center;
  background-size: cover;
}
```

Пример страницы:

![](/.gitbook/assets/block-page1.png)

</details>

5\. Чтобы изменить общий шаблон для страниц ошибок, отредактируйте HTML-файл. Перейдите в директорию **/usr/share/ideco/proxy-backend/error_page_templates/langs/ru_RU** и откройте файл **ERR_TEMPLATE.html** в текстовом редакторе:

```
nano /usr/share/ideco/proxy-backend/error_page_templates/langs/ru_RU/ERR_TEMPLATE.html
```
<details>
<summary>Пример изменения файла ERR_TEMPLATE.html</summary>

```
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width" />
  <link rel="icon" type="image/x-icon" href="IDECO_ICON_FAVICON">
  <link rel="apple-touch-icon" href="IDECO_ICON_FAVICON">
  <title>Доступ заблокирован</title>
  <style type="text/css">%l</style>
</head>

<body>
  <div class="widget info viewport_big">
    <span class="icon"></span>
    <div class="widget_content">
      <h1>Доступ заблокирован</h1>
      <p>Данный сайт предоставляет контент, заблокированный администратором. Причины блокировки описаны во <a href="https://test.ru">внутреннем регламенте</a>.</p>
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
```

Пример страницы:

![](/.gitbook/assets/block-page2.png)

</details>

6\. Перезапустите сервис ideco-proxy-backend:

```
systemctl restart ideco-proxy-backend.service
```

7\. Проверьте, корректно ли работают страницы ошибок, перейдя по запрещенным ссылкам.