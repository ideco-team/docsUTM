---
description: В статье описаны шаги для изменения страницы блокировки Контент-фильтра.
---

# Изменение страницы блокировки Контент-фильтра

Страница блокировки Контент-фильтра по умолчанию содержит уведомление о блокировке доступа к ресурсу администратором сети и категоризацию ресурса. Если требуется изменить страницу блокировки, выполните действия ниже.

Перед изменением страницы блокировки подготовьте:

* Логотип в формате svg c прозрачным фоном;
* Фавикон в формате png;
* Hex-коды фирменных цветов.
 
Для создания персонализированного шаблона страницы выполните действия:

1\. Удалите директорию со старыми файлами страниц ошибок Squid:

```
rm -R /var/cache/ideco/proxy-backend/error_pages
```

2\. Загрузите фавикон клиента через инженерную панель.

3\. Скопируйте фавикон в директорию **/usr/share/ideco/vendor/**. Имя файла должно быть обязательно **favicon.png**:

```
cp /var/cache/ideco/engineering-panel-backend/favicon.png /usr/share/ideco/vendor/favicon.png
```

4\. Замените все изображения в директории 
**/usr/share/ideco/proxy-backend/error_page_templates/images/** на пользовательский логотип. Названия файлов должны остаться такими же.

{% hint style="info" %}
Для удобства можно сохранить у себя локально один и тот же файл с разными названиями, затем загрузить их через инженерную панель и скопировать в нужную директорию.
{% endhint %}

5\. Замените содержание файла стилей страниц ошибок style.css на новое. Файл находится в директории
**/usr/share/ideco/proxy-backend/error_page_templates/**. Для открытия файла воспользуйтесь текстовым редактором vi или nano:

```
vi /usr/share/ideco/proxy-backend/error_page_templates/style.css
```

```
nano /usr/share/ideco/proxy-backend/error_page_templates/style.css
```

<details>
<summary>Пример изменения файла style.css</summary>

Возьмите в качестве цвета фона #d9d9d9. Измените в файле style.css  строки в секции color, подставив свой цвет:

```
.error {
  background-color: #d9d9d9;
  color: #d9d9d9;
}

.warning {
  background-color: #d9d9d9;
  color: #d9d9d9;
}

.info {
  background-color: #d9d9d9;
  color: #d9d9d9;
}

.success {
  background-color: #d9d9d9;
  color: #d9d9d9;
}
```

Для изменения размера и других параметров шрифта измените секцию body:

```
body {
  padding: 5% 12px;
  box-sizing: border-box;
  overflow: auto;
  background-color: #d9d9d9;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 18px;
}
```

Для изменения размера логотипа на нужный измените секцию .icon:

```
.icon {
  width: 300px;
  min-width: 100px;
  height: 80px;
  min-height: 30px;
  margin-right: 50px;
  background-position: center;
  background-size: cover;
}
```

Удалите строки:

```
border-radius: 4px;
  / material ui elevation 3 */
  box-shadow: 0px 3px 3px -2px rgb(0 0 0 / 20%), 0px 3px 4px 0px rgb(0 0 0 / 14%), 0px 1px 8px 0px rgb(0 0 0 / 12%);
```

Пример страницы:

![](/.gitbook/assets/block-page1.png)

</details>

{% hint style="info" %}
Если какая-то информация должна отображаться во всех шаблонах, то добавьте ее в общий шаблон ERR_TEMPLATE.html. Например, можно добавить адрес для связи с администратором и скрипт, который будет отображать дату.
{% endhint %}


6\. Перезапустите сервис ideco-proxy-backend:

```
systemctl restart ideco-proxy-backend.service
```

7\. Проверьте корректность работы страниц, перейдя по запрещенным ссылкам.