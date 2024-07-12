# Настройка прозрачной авторизации на Astra linux

{% hint style="warning" %}
Данное решение подходит для браузеров **Yandex**, **Chromium** и **Firefox.**
{% endhint %}

1\. Введите Astra linux в домен (например, через Active Directory).

2\. Зайдите под доменной учетной записью на Astra Linux. 

3\. В зависимости от выбранного браузера, выполните действия из подразделов [**Yandex**](authorization-astra-linux.md#dlya-brauzera-yandex), [**Chromium**](authorization-astra-linux.md#dlya-brauzera-chromium) или [**Firefox**](authorization-astra-linux.md#dlya-brauzera-firefox).

4\. Добавьте корневой сертификат Ideco NGFW в список доверенных центров сертификации. Для этого сначала [скачайте сертификат с Ideco NGFW](/installation/initial-setup#import-kornevogo-sertifikata-ngfw-v-brauzer/).

5\. В настройках браузера Firefox в пункте **Защита и приватность** в разделе **Защита** выберите **Просмотр сертификатов**.

![](/.gitbook/assets/authorization-astra-linux1.png)

6\. На вкладке **Центры сертификации** нажмите **Импортировать** и выберите скачанный с NGFW сертификат.

7\. Отметьте пункт **Доверять при идентификации веб-сайтов** и подтвердите.

8\. Откройте браузер. Появится окно с авторизацией, после чего произойдет перенаправление на начальную страницу.

## Для браузера **Yandex**

Создайте файл **mydomain.json** в директории **/etc/opt/yandex/browser/policies/managed/** и впишите в него строку:

```
{ 
  "AuthServerAllowlist": "*.имя_домена",
  "AuthNegotiateDelegateAllowlist": "*.имя_домена"
}
```

При возникновении проблем с доверенным сертификатом установите корневой сертификат NGFW через браузер Yandex:

1\. Скачайте корневой сертификат NGFW из раздела **Сервисы -> Сертификаты** по кнопке **Скачать** (![](/.gitbook/assets/icon-download.png)),

2\. В браузере Yandex перейдите во вкладку **Настройки -> Системные -> Управление сертификатами -> Центры сертификации -> Импорт**.

Пример проблемы:

![](/.gitbook/assets/authorization-astra-linux.png)

## Для браузера **Chromium**

Создайте файл **mydomain.json** в директории **/etc/chromium/policies/managed/** и впишите в него строку:

```
{
    "AuthServerWhitelist": "*.имя_домена"
}
```

При возникновении проблем с доверенным сертификатомЫ установите корневой сертификат NGFW через браузер Chromium:

1\. Скачайте корневой сертификат NGFW из раздела **Сервисы -> Сертификаты** по кнопке **Скачать** (![](/.gitbook/assets/icon-download.png)),

2\. В браузере Chromium перейдите во вкладку **Безопасность -> Управление сертификатами -> Центры сертификации -> Импортировать**.

Пример проблемы:

![](/.gitbook/assets/authorization-astra-linux.png)

## Для браузера **Firefox**

1. Запустите браузер и в адресной строке введите **about:config**, чтобы попасть в режим редактирования расширенных настроек;
2. Введите параметр **security.enterprise\_roots.enabled** и нажмите по блоку со строчкой два раза левой кнопкой мыши, чтобы значение изменилось на **True**;
3. В двух следующих параметрах впишите доменное имя NGFW через HTTP и HTTPS через запятую: **network.automatic-ntlm-auth.trusted-uris** и **network.negotiate-auth.trusted-uris** (например, http://utm.domain.com, https://utm.domain.com).
