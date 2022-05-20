# Настройка прозрачной авторизации на Astra linux

{% hint style="warning" %}
Данное решение подходит для браузеров **Chromium** и **Firefox.**
{% endhint %}

1\. Ввести Astra linux в домен.

2\. Зайти под доменной учетной записью на Astra Linux.

3\. В зависимости от выбранного браузера, выполнить действия из подразделов: [**Chromium**](authorization-astra-linux.md#dlya-brauzera-chromium) или [**Firefox**](authorization-astra-linux.md#dlya-brauzera-firefox)

4\. Добавить корневой сертификат Ideco UTM в список доверенных центров сертификации. Для этого сначала [скачайте сертификат с Ideco UTM](../../settings/services/certificates/).

5\. В настройках браузера Firefox в пункте **Защита и приватность** в разделе **Защита** выбрать **Просмотр сертификатов**.

![](../../.gitbook/assets/firefix-sert.png)

6\. Во вкладке **Центры сертификации** нажать **Импортировать** и выбрать скачанный с UTM сертификат.

7\. Отметить пункт **Доверять при идентификации веб-сайтов** и подтвердить.

8\. Открыть браузер, появится окно с авторизацией, после чего произойдет перенаправление на начальную страницу.

## Для браузера **Chromium**

Создать файл **mydomain.json** в директории **/etc/chromium/policies/managed/** и вписать в него строку:

```
{
    "AuthServerWhitelist": "*.имя_домена"
}
```

## Для браузера **Firefox**

* Запустить браузер и в адресной строке ввести **about:config**, чтобы попасть в режим редактирования расширенных настроек.
* Ввести параметр **security.enterprise\_roots.enabled** и нажать по блоку со строчкой два раза левой кнопкой мыши, чтобы значение изменилось на **True.**
* В двух следующих параметрах вписать доменное имя UTM через HTTP и HTTPS через запятую: **network.automatic-ntlm-auth.trusted-uris** и **network.negotiate-auth.trusted-uris** (например, [http://utm.domain.com](http://utm.domain.com), [https://utm.domain.com\\](https://utm.domain.com)).
