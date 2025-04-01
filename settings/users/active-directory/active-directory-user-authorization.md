---
description: >-
  В статье описано как настроить аутентификацию пользователей AD/Samba DC в Ideco NGFW.
---

# Аутентификация пользователей AD/Samba DC

{% hint style="success" %}
Видеоинструкцию смотрите по ссылкам:
* [Rutube](https://rutube.ru/video/590d482c7e412deb0dcfbe945e1448e4/?r=wd);
* [Youtube](https://youtu.be/RgzyOM7opUY?si=7M2U2OvM04Ab_znL).
{% endhint %}

Перейдите на вкладку **Пользователи -> Авторизация -> Основное** и заполните поля: 

![](/.gitbook/assets/authorization9.png)

* **Доменное имя Ideco NGFW** - используйте доменное имя Ideco NGFW длиной не более 15 символов;
* **Веб-аутентификация** - включите настройку и выберите **SSO-аутентификация через Active Directory и ALD Pro**;
* **Авторизации через журнал безопасности Active Directory** - включите настройку, если необходимо записывать события, связанные с проверкой прав доступа пользователей к ресурсам сети. Рекомендуем использовать совместно с SSO-аутентефикацией;
* **Разавторизация пользователей** - установите тайм-аут [разавторизации пользователей](settings\users\active-directory\auto-de-authorization-script.md). Значение по умолчанию - 15 минут. Диапазон доступных значений - от 10 минут до 1 дня.

После сохранения настроек будет выдан Let’s Encrypt сертификат, пользователь будет перенаправляться на окно авторизации, минуя страницу исключения безопасности:

![](/.gitbook/assets/web-autorization2.png)

Если сертификат для такого домена уже загружен в разделе [Сертификаты](/settings/services/certificates/), то будет использоваться загруженный сертификат. Новый сертификат выдаваться не будет.

{% content-ref url="active-ditrctory-server-configuring.md" %}
[active-ditrctory-server-configuring.md](active-ditrctory-server-configuring.md)
{% endcontent-ref %}

{% content-ref url="active-directory-web-authentication.md" %}
[active-directory-web-authentication.md](active-directory-web-authentication.md)
{% endcontent-ref %}

{% content-ref url="ad-autorization.md" %}
[ad-autorization.md](ad-autorization.md)
{% endcontent-ref %}

{% content-ref url="auto-de-authorization-script.md" %}
[auto-de-authorization-script.md](auto-de-authorization-script.md)
{% endcontent-ref %}
