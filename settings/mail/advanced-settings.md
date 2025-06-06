
# Расширенные настройки

Раздел **Расширенные настройки** состоит из трех подразделов: **Основное, Безопасность, DKIM-подпись**.

### Основное

* **Внешний SMTP-релей.** Вся исходящая почта будет отправляться на указанный адрес. Используется, например, если почта должна проходить через вышестоящий сервер провайдера перед отправкой в сеть Интернет.
* **Пересылать всю исходящую почту на адрес.** Вся исходящая почта будет дублироваться на указанный почтовый ящик. Рекомендуется включать только при крайней необходимости.
* **Пересылать всю входящую почту на адрес.** Вся входящая почта будет дублироваться на указанный почтовый ящик. Рекомендуется включать только при крайней необходимости.
* **Максимальный размер ящика.** Ограничение на максимальный размер почтового ящика в мегабайтах.
* **Максимальный размер письма.** Ограничение на максимальный размер формируемого сервером письма в мегабайтах.
* **Срок хранения сообщений в корзине.** Количество дней в течении которых почта хранится в корзине перед удалением.

---
### Безопасность

* **Поддержка SASL для аутентификации SMTP-клиентов.** Подключившись к почтовому ящику из интернета и отправить письмо, используя SMTP сервер Ideco, можно будет только пройдя авторизацию по логину и паролю, заданному для этой учетной записи пользователя на сервере. **Не включайте данный параметр, если используете UTM в качестве почтового релея.**
* **Разрешить аутентификацию только через защищенное соединение (TLS).** Запрещает незащищенную передачу учетных данных клиента при аутентификации на SMTP сервере.
* **Фильтрация по серым спискам (greylisting) для входящей почты.** Включает фильтрацию по серым спискам (greylisting) для входящей почты. При этом почта от неизвестных доменов отправителей может приходить с небольшой задержкой.
* **Фильтрация по DNSBL для входящей почты.** Включает фильтрацию по DNSBL для входящей почты.
* **Доверенные сети.** Авторизация на сервере для доступа к почтовому ящику не требуется при попытке доступа из этих сетей. Указываются IP-сети и хосты в нотации CIDR или с префиксом сети, например, `10.0.0.5/255.255.255.255` или `192.168.0.0/16`.

---
### DKIM-подпись

Настраивается в разделе **Почтовый релей -> Расширенные настройки -> DKIM-подпись.** Подписывает исходящую с сервера корреспонденцию уникальной для вашего почтового домена подписью так, что другие почтовые серверы в сети Интернет могут убедиться, что ваша почта легитимна и заслуживает доверия.

Для функционирования технологии вам потребуется создать TXT запись для вашего домена у держателя зоны со значением, которое сформирует для вашего почтового домена наш сервер. TXT записи будут сформированы для основного почтового домена, настроенного на Ideco UTM, и дополнительных почтовых доменов (если указаны). Сервер также проверит, правильно ли была указана запись для вашей зоны, и резолвится ли она в сеть Интернет.

![](/.gitbook/assets/dikm-sign.png)

{% hint style="info" %}
Объем TXT-записи достаточно велик и многие регистраторы/держатели зон испытывают сложности с предоставлением интерфейса клиентам для указания TXT-записей длиннее 256 символов. Зачастую они предоставляют возможность указания TXT-записей длиной до 256 символов, согласно стандарту RFC1035. Но другой стандарт, RFC4408, предполагает объединение строк в случаях, когда нужно использовать длинные TXT-записи при настройке SPF и DKIM. Оперируйте этой информацией в диалоге с держателем вашей доменной зоны. Как правило, держатели зон находят способ создания длинных TXT записей.
{% endhint %}

{% hint style="info" %}
Подпись содержит сочетание кавычек (кавычка-пробел-кавычка: **" "**). \
Если ваш хостинг не воспринимает такой формат записи, то удалите эти символы.
{% endhint %}