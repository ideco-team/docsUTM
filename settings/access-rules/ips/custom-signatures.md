# Пользовательские сигнатуры

На вкладке можно добавить кастомные сигнатуры IPS. Сигнатура -  это шаблон, который позволяет идентифицировать определенные виды вредоносного трафика, аномалий в протоколах или известных атак.

Если добавленные пользователем сигнатуры валидны, они также появятся в таблице [Группы сигнатур](/settings/access-rules/ips/rules.md), их можно будет использовать при создании [профилей **Предотвращения вторжений**](/settings/security-profiles/ips-profiles.md).

Чтобы Ideco NGFW счел сигнатуры валидными, они должны состоять из:

* Действия при совпадении правила;
* Заголовка, определяющего протокол, IP-адреса, порты и направление трафика;
* Опций, определяющих специфику сигнатуры.

**Пример валидной сигнатуры:**

{% code overflow="wrap" %}
```
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"HTTP GET Request Containing Rule in URI"; flow:established,to_server; http.method; content:"GET"; http.uri; content:"rule"; fast_pattern; classtype:bad-unknown; sid:123; rev:1;)
```
{% endcode %}

где:

* `alert` - действие;
* `http $HOME_NET any -> $EXTERNAL_NET any` - заголовок;
* `(msg:"HTTP GET Request Containing Rule in URI"; flow:established,to_server; http.method; content:"GET"; http.uri; content:"rule"; fast_pattern; classtype:bad-unknown; sid:123; rev:1;)` - опции.

{% hint style="warning" %}
Значения SID добавляемых вручную или из файла сигнатур должны быть уникальными и находиться в диапазоне 1-999999.
{% endhint %}

Чтобы добавить сигнатуру, выполните действия:

1\. Нажмите **Добавить** и выберите способ добавления: **Вручную** или **Из файла**.

2\. Если выбран способ **Из файла**, в открывшемся окне выберите необходимый текстовый файл. Если сигнатуры соответствуют требуемой структуре, а значения SID у всех сигнатур в файле уникальны и находятся в нужном диапазоне, то эти сигнатуры появятся в таблице:

![](/.gitbook/assets/ips15.png)

Если структура сигнатур не соответствует нужной, Ideco NGFW выдаст ошибку с указанием номеров строк файла, где найдены ошибки.

3\. Если был выбран способ **Вручную**, в открывшейся форме введите комментарий, сигнатуру и нажмите **Добавить**:

![](/.gitbook/assets/ips14.png)

{% hint style="danger" %}
Проверка валидности сигнатур может занять некоторое время. Если одна из сигнатур не пройдет проверку, появится сообщение об ошибке у названия системы **Предотвращения вторжений**. Подробности можно будет увидеть в логах службы.
{% endhint %}

{% hint style="danger" %}
Сигнатуры, не используемые в профилях **Предотвращения вторжений**, и профили, не используемые в правилах **Файрвола**, не участвуют в обработке трафика!
{% endhint %}