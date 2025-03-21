---
title: Авторизация пользователей Active Directory
published: true
date: '2021-04-16T09:46:39.579Z'
tags: user_authorization, ad_authorization, ad
editor: markdown
dateCreated: '2021-04-02T07:26:40.810Z'
---

# Авторизация пользователей Active Directory

{% hint style="success" %}
Импортируйте учетные записи из Active Directory, подробнее в статье [Импорт пользователей](user-import.md).
{% endhint %}

## Настройка авторизации пользователей

Для пользователей, импортированных из Active Directory, доступны все типы авторизации пользователей. Наиболее часто используемые варианты авторизации пользователей - Single Sign-On аутентификация через Active Directory с использованием Kerberos/NTLM для авторизации через веб-браузер и авторизация через журнал безопасности Active Directory (рекомендуется одновременное использование обоих типов авторизации).

## Настройка Ideco UTM

Для включения **Single Sign-On аутентификации** и **Авторизация через журнал безопасности Active Directory** перейдите на вкладку **Пользователи -> Авторизация -> Основное** и включите эти типы авторизации. Далее нажмите кнопку **Сохранить**.

![](/.gitbook/assets/adauth.png)

## Настройка компьютеров пользователей и политик домена

### Авторизация через журнал безопасности Active Directory

{% hint style="info" %}
Поддерживается начиная с версии контроллера домена 2008 standard edition.
{% endhint %}

Для работы авторизации через журнал безопасности необходимо выполнить настройку на основном контроллере домена:

*   В настройках брандмауэра Windows на всех контроллерах домена (или доменов) разрешить удаленный доступ к логам безопасности.

    > В англоязычной версии, правило именуется: **Remote Event Log Management (RPC)**

![](/.gitbook/assets/firewallrule.png)

* Добавить Ideco UTM в группу безопасности **Читатели журнала событий (Event Log Readers)**.

![](/.gitbook/assets/read-event.png)

* После настройки доступа к журналу, необходим перезапуск службы **Авторизация через журнал безопасности Active Directory** на Ideco UTM, для этого отключите эту настройку и заново включите.
*   Если вы изменяли политики безопасности контроллеров домена по сравнению со стандартными, то нужно включить логирование в политиках безопасности, активировав следующий параметр: **Default Domain Controllers Policy -> Computer Configuration->Policies->Windows Settings->Security Settings-> Advanced Audit Policy Configuration -> Audit Policies -> Logon/Logoff -> Audit Logon -> Success**.

    Путь для русскоязычной версии: **Политика Default Domain Controllers Policy -> Конфигурация Windows -> Параметры безопасности -> Конфигурация расширенной политики аудита -> Политики аудита -> Вход/выход -> Аудит входа в систему -> Успех**.
*   Также необходимо включить следующие параметры: **Default Domain Controllers Policy -> Computer Configuration->Policies->Windows Settings->Security Settings-> Advanced Audit Policy Configuration -> Audit Policies -> Account logon -> "Audit Kerberos Authentication Service" и "Audit Kerberos Service Ticket Operations" -> Success**.

    Путь для русскоязычной версии: **Политика Default Domain Controllers Policy -> Конфигурация Windows -> Параметры безопасности -> Конфигурация расширенной политики аудита -> Политики аудита -> Вход учетной записи -> "Аудит службы проверки подлинности Kerberos" и "Аудит операций билета службы керберос" -> Успех**.
* Для обновления политик контроллеров доменов выполните команду `gpupdate /force`.
* Если авторизация пользователей при логине не происходит, нужно проверить в журнале безопасности наличие событий 4768, 4769, 4624.

### Веб-аутентификация (SSO или NTLM)

Для работы аутентификации через веб-браузер (с использованием Kerberos либо NTLM) необходима настройка Internet Explorer (остальные браузеры подхватывают его настройки). В системе Windows 10 параметры прокси нужно настроить без Internet Explorer, в разделе **Параметры -> Сеть и интернет -> Прокси-сервер**. \
Обязательно используйте эти настройки, даже если обычно пользователи авторизуются через журнал безопасности, в некоторых случаях будет необходима их аутентификация через браузер.

Для того чтобы настроить аутентификацию через веб-браузер, необходимо выполнить следующие действия:

1. Зайдите в свойствах браузера на вкладку **Безопасность**.
2. Выберите **Местная интрасеть -> Сайты -> Дополнительно**.
3. Добавьте в открывшемся окне ссылку на Ideco UTM под тем именем, под которым вы ввели его в домен. Нужно указывать два URL: c `http://` и с `https://`.

На скриншоте ниже Ideco UTM введен в домен `example.ru` под именем `idecoics`.

![](/.gitbook/assets/active-directory.jpg)

Также данную настройку можно сделать с помощью групповых политик Active Directory сразу для всех пользователей. Для этого необходимо выполнить следующие действия:

1.  В групповых политиках для пользователей перейдите по пути: **Default Policy Group > Computer Configuration > Policies > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Security Page > Site to Zone Assignment List**

    Путь для русскоязычной версии: **Конфигурация компьютера -> Политики -> Административные шаблоны -> Компоненты Windows -> Internet Explorer -> Панель управления браузером -> Вкладка безопасность -> Список назначений зоны для веб-сайтов**.
2. Введите назначение зоны для DNS-имени Ideco UTM (в примере idecoics.example.ru) со значением равным 1 (интрасеть). Необходимо указать два назначения, для схем работы по http и https.

![](/.gitbook/assets/active-directory.png)

{% hint style="info" %}
При входе на HTTPS-сайт, для аутентификации необходимо разрешить браузеру доверять сертификату Ideco UTM (чтобы не делать это каждый раз, можно добавить корневой сертификат Ideco UTM в доверенные корневые сертификаты устройства. Например, с помощью политик домена). Можно также использовать [скрипты для автоматической авторизации](auto-authorization-and-de-authorization-script.md) пользователей при логине.
{% endhint %}

На странице настроек браузера **Mozilla Firefox** (about:config в адресной строке) настройте следующие параметры:

* **network.automatic-ntlm-auth.trusted-uris** и **network.negotiate-auth.trusted-uris** добавьте адрес локального интерфейса Ideco UTM (например `idecoUTM.example.ru`).
* **security.enterprise\_roots.enabled** в значении true позволит Firefox доверять системным сертификатом и авторизовать пользователей при переходе на HTTPS-сайты.

Также для пользователей, импортированных через AD, возможны следующие способы авторизации:

* **Через Ideco Agent** - подходит для аутентификации пользователей терминальных серверов (с использованием Remote Desktop IP Virtualization на терминальном сервере).
* **Авторизация по IP-адресу** - подходит в случае, если пользователи всегда работают с фиксированных IP-адресов. IP-адреса на UTM необходимо прописывать вручную каждому пользователю.
* **Авторизация по PPTP** - если в сети предъявляются повышенные требования к конфиденциальности информации, передаваемой между шлюзом и устройствами пользователей, или используется слабо защищенный от перехвата трафика Wi-Fi.

## Настройка авторизации пользователей при прямых подключениях к прокси-серверу

Настройка прозрачной аутентификации пользователей при прямых подключениях к прокси-серверу аналогична настройке прозрачной **Single Sign-On** аутентификации, описанной выше в инструкции. Единственная особенность - указание в качестве адреса прокси-сервера **не IP-адреса Ideco UTM, а его DNS-имени**.

![](/.gitbook/assets/active-directory1.png)

### Настройка браузера Mozilla Firefox для аутентификации по NTLM при прямом подключении к прокси-северу

Для компьютеров, которые **не находятся в домене Active Directory**, в случае необходимости их аутентификации под доменным пользовательским аккаунтом, на странице настроек браузера **Mozilla Firefox** (about:config в адресной строке) настройте следующие параметры:

* **network.automatic-ntlm-auth.allow-proxies** = false;
* **network.negotiate-auth.allow-proxies** = false.

{% hint style="info" %}
Не отключайте данные опции для компьютеров, входящих в домен Active Directory, т.к. в таком случае будет использоваться устаревший метод аутентификации по NTLM.
{% endhint %}

## Возможные причины ошибок при аутентификации

* Если в Internet Explorer появляется окно с текстом **Для получения доступа требуется аутентификация**, и авторизация происходит только при ручном переходе по ссылке на аутентификацию, то по каким-то причинам не происходит редирект в браузере на страницу авторизации (он может быть ограничен настройками безопасности браузера). В таком случае, установите параметр **Активные сценарии** в Internet Explorer в значение **Включить**.

![](/.gitbook/assets/active-directory2.jpg)

* Доменному пользователю должно быть разрешено аутентифицироваться на Ideco UTM. На контроллере домена зайдите в свойства выбранных пользователей во вкладку **Учетная запись** -> **Вход на...**, выберите пункт **только на указанные компьютеры** и пропишите имя рабочей станции для входа в систему.

Пример данной настройки представлен на скриншоте ниже:

![](/.gitbook/assets/active-directory2.png)

* При аутентификации через журнал безопасности контроллера домена Active Directory пользователи будут аутентифицированы при попытке выхода в Интернет (любым трафиком). Автоматической аутентификации без прохождения трафика через UTM не происходит, т.к. используется конкурентная политика авторизации.
