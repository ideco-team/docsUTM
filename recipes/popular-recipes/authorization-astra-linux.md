---
description: >-
  Как настроить прозрачную авторизацию на Astra Linux через Ideco NGFW с использованием SSO-аутентификации.
---

# Настройка прозрачной авторизации на Astra Linux

{% hint style="warning" %}
Решение подходит для браузеров **Yandex**, **Chromium** и **Firefox.**
{% endhint %}

1\. Установите и настройте NGFW на устройстве администратора, получите лицензию.

2\. Введите Astra Linux в домен (например, через Active Directory).

3\. Введите NGFW в тот же домен и импортируйте пользователей (в том числе Astra Linux) в группу.

4\. Включите в NGFW **SSO-аутентификацию через Active Directory и ALD Pro** в разделе **Пользователи -> Авторизация -> Веб-аутентификация**:

![](/.gitbook/assets/authorization10.png)

5\. Зайдите под доменной учетной записью на Astra Linux.

6\. В зависимости от выбранного браузера, выполните действия:

<details>

<summary>Для браузера Yandex</summary>

1\. Создайте файл **mydomain.json** в директории `/etc/opt/yandex/browser/policies/managed/` и впишите в него строку:

```
{ 
  "AuthServerAllowlist": "имя_NGFW.имя_домена",
  "AuthNegotiateDelegateAllowlist": "имя_NGFW.имя_домена"
}
```

2\. Откройте страницу любого сайта в браузере. Появится окно с авторизацией, после чего произойдет перенаправление на начальную страницу.

</details>

<details>

<summary>Для браузера Chromium</summary>

1\. Создайте файл **mydomain.json** в директории `/etc/chromium/policies/managed/` и впишите в него строку:

```
{ 
    "AuthServerAllowlist": "имя_NGFW.имя_домена" ,
    "AuthNegotiateDelegateAllowlist": "имя_NGFW.имя_домена"
}
```

2\. Откройте страницу любого сайта в браузере. Появится окно с авторизацией, после чего произойдет перенаправление на начальную страницу.
</details>

<details>

<summary>Для браузера Firefox </summary>

1\. Запустите браузер и в адресной строке введите `about:config`, чтобы попасть в режим редактирования расширенных настроек.

2\. Введите параметр `security.enterprise_roots.enabled` и дважды кликните по блоку, чтобы значение изменилось на **True**, что позволит Firefox доверять системным сертификатам и авторизовывать пользователей при переходе на HTTPS-сайты.

3\. В параметрах `network.automatic-ntlm-auth.trusted-uris` и `network.negotiate-auth.trusted-uris` укажите `имя_NGFW.имя_домена`.

4\. Откройте страницу любого сайта в браузере. Появится окно с авторизацией, после чего произойдет перенаправление на начальную страницу.

</details>

7\. При возникновении проблемы с доверенным сертификатом установите корневой сертификат NGFW. Пример проблемы:

![](/.gitbook/assets/authorization-astra-linux2.png)

<details>

<summary>Для браузера Yandex</summary>

1\. Скачайте корневой [сертификат](/installation/initial-setup.md#import-kornevogo-sertifikata-ngfw-v-brauzer/) NGFW из раздела **Сервисы -> Сертификаты** по кнопке **Скачать** ![](/.gitbook/assets/icon-download.png).

2\. В браузере Yandex перейдите на вкладку **Настройки -> Системные -> Управление сертификатами -> Центры сертификации -> Импорт** и добавьте сертификат в список доверенных.

3\. Включите опции доверия для сертификата:

![](/.gitbook/assets/ald-pro2.png)

</details>

<details>

<summary>Для браузера Chromium</summary>

1\. Скачайте корневой [сертификат](/installation/initial-setup.md#import-kornevogo-sertifikata-ngfw-v-brauzer/) NGFW из раздела **Сервисы -> Сертификаты** по кнопке **Скачать** ![](/.gitbook/assets/icon-download.png).

2\. В браузере Chromium перейдите на вкладку **Настройки -> Конфиденциальность и безопасность -> Безопасность -> Настроить сертификаты -> Центры сертификации -> Импортировать** и добавьте сертификат в список доверенных.

3\. Включите опции доверия для сертификата:

![](/.gitbook/assets/ald-pro3.png)

</details>

<details>

<summary>Для браузера Firefox</summary>

1\. Скачайте корневой [сертификат](/installation/initial-setup.md#import-kornevogo-sertifikata-ngfw-v-brauzer/) NGFW из раздела **Сервисы -> Сертификаты** по кнопке **Скачать** ![](/.gitbook/assets/icon-download.png).

2\. В настройках браузера Mozilla Firefox в пункте **Приватность и Защита** в разделе **Защита** выберите **Просмотр сертификатов**:

![](/.gitbook/assets/authorization-astra-linux1.png)

3\. На вкладке **Центры сертификации** нажмите **Импортировать** и выберите скачанный с NGFW сертификат.

4\. Отметьте пункт **Доверять при идентификации веб-сайтов** и подтвердите.

</details>