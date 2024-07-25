---
description: Создание WAF-профилей для защиты опубликованных веб-ресурсов от атак.
---

# Web Application Firewall

Использование WAF-профилей позволит настроить параметры защиты для опубликованного веб-ресурса. Создается профиль в разделе **Профили безопасности -> Web Application Firewall** и используется в [**Обратном прокси**](settings/services/reverse-proxy.md) при создании правила. 

## Создание профиля WAF

Для создания профиля WAF выполните действия:

1\. Нажмите **Добавить** и заполните поля:

![](/.gitbook/assets/waf-profiles2.png)

* **Hазвание** - введите название профиля;
* **Комментарий** - введите пояснение для профиля;
* **Режим работы**:
    * **Обнаружение и блокировка** - подозрительные запросы будут блокироваться и логироваться WAF;
    * **Только обнаружение** - подозрительные запросы будут логироваться WAF, но не будут блокироваться;
* **Дополнительные настройки**:
    * **Скрывать HTTP-заголовок Server** - позволяет скрыть данные идентифицирующие сервер.

2\. Для включения и просмотра правил перейдите во вкладку **Категории**:

![](/.gitbook/assets/waf-profiles3.png)

3\. Для добавления определенного правила в исключения перейдите во вкладку **Исключения**:

![](/.gitbook/assets/waf-profiles4.png)

4\. Настройте белый и черный список подсетей профиля во вкладке **Белый и черный списки**:

* Для добавления IP-адреса/подсети в белый список нажмите **Добавить** и выберите действие **Не проверять**:

![](/.gitbook/assets/waf-profiles5.png)

* Для добавления IP-адреса/подсети в черный список нажмите **Добавить** и выберите действие **Блокировать**:

![](/.gitbook/assets/waf-profiles6.png)

5\. После конфигурации профиля нажмите **Добавить профиль WAF**.