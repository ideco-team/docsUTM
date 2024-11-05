---
description: >-
  Включение этого модуля дает возможность передавать все системные сообщения
  (syslog) Ideco NGFW в сторонние коллекторы (Syslog Collector) или в
  SIEM-системы.
---

# Syslog

{% hint style="success" %}
Название службы раздела **Syslog**: `ideco-monitor-backend`. \
Список служб для других разделов доступен по [ссылке](/settings/server-management/terminal/README.md).
{% endhint %}

## Пересылка системных сообщений

Чтобы настроить пересылку системных сообщений, перейдите в раздел **Отчеты и журналы -> Syslog** и выполните действия:

1\. Укажите IP-адрес сервера-коллектора (любой локальный "серый" или публичный "белый" IP-адрес);

2\. В поле **Порт** укажите любой порт из диапазона от 1 до 65535;

3\. Выберите формат передаваемых системных сообщений (Syslog или CEF);

4\. Выберите протокол передачи системных логов - TCP или UDP;

5\. Нажмите **Сохранить** и включите опцию Syslog:

![](/.gitbook/assets/remote-syslog.png)

{% hint style="info" %}
Рекомендуется передавать логи по протоколу TCP, так как он гарантирует доставку и соблюдает последовательность сообщений.
{% endhint %}

## Расшифровка передаваемых логов

### Формат CEF

Логи в CEF-формате начинаются со строки вида:

{% code overflow="wrap" %}
``` 
192.168.1.100 Nov 05 14:57:10 daemon warning 2024-11-05T14:44:20+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|
```
{% endcode %}
где:

* `192.168.1.100` - IP-адрес NGFW отправителя;
* `Nov 05 14:57:10` - время получения события по Syslog;
* `warning` - приоритет сообщения в логах. Другие значения: `info` (информационное сообщение), `notice` (уведомление);
* `2024-11-05T14:44:20+05:00` - время события в Ideco NGFW;
* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `CEF:0` - версия формата CEF;
* `Ideco` - вендор;
* `NGFW` - название продукта;
* `17.0` - версия продукта;
* `0|syslog|0` - идентификатор лога, постоянный для NGFW. Состоит из трех полей: идентификатор типа события, описание события, важность события.

<details>

<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 14:57:10 daemon warning 2024-11-05T14:44:20+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730799860 Severity=Warning DeviceProcessName=web-proxy DeviceCustomString1=1218332722865011 DeviceInboundInterface=seq:Leth1{3 DeviceProcessName=suricata_debug DeviceCustomString5=alert SourceAddress=192.168.101.25 DeviceCustomString1=local DeviceCustomString1Label=Src IP Type SourcePort=38003 SourceCountry= DeviceCustomString2= DeviceCustomString2Label=Src Country Code DeviceCustomString3=6103759e-5ad6-48b1-81b5-d15894b005ef DeviceCustomString3Label=Src session UUID SourceUserID=2 SourceUserName=user DestinationAddress=192.168.101.10 DeviceCustomString4=local DeviceCustomString4Label=Dst IP Type DestinationPort=53 DestinationCountry= DeviceCustomString5= DeviceCustomString5Label=Dst Country Code DeviceCustomString6= DeviceCustomString6Label=Dst session UUID DestinationUserID=-1 DestinationUserName= TransportProtocol=UDP DeviceEventClassID=1900005 Message=Mining pool DeviceEventCategory=Пулы криптомайнеров Severity=2 DeviceCustomString8=1 DeviceCustomString8Label=Alert GID DeviceCustomString9=blocked DeviceCustomString9Label=Alert action DestinationHostName= RequestUrl= RequestClientApplication= FlexNumber1=1 FlexNumber1Label=Flow packets to server FlexNumber2=0 FlexNumber2Label=Flow packets to client BytesIn=81 BytesOut=0 StartTime=2024-11-05 09:44:20.021521 EndTime=2024-11-05 09:44:20.021846 FlexNumber3=0 FlexNumber3Label=flow DeviceCustomString11= DeviceCustomString11Label=flow.state DeviceCustomString12= DeviceCustomString12Label=flow.reason FlexNumber4=0 FlexNumber4Label=flow.alerted DeviceCustomString14= DeviceCustomString14Label=tcp.tcp_flags DeviceCustomString15= DeviceCustomString15Label=tcp.tcp_flags_ts DeviceCustomString16= DeviceCustomString16Label=tcp.tcp_flags_tc FlexNumber5=0 FlexNumber5Label=tcp.cwr FlexNumber6=0 FlexNumber6Label=tcp.ecn FlexNumber7=0 FlexNumber7Label=tcp.urg FlexNumber8=0 FlexNumber8Label=tcp.ack FlexNumber9=0 FlexNumber9Label=tcp.psh FlexNumber10=0 FlexNumber10Label=tcp.rst FlexNumber11=0 FlexNumber11Label=tcp.syn FlexNumber12=0 FlexNumber12Label=tcp.fin DeviceCustomString17= DeviceCustomString17Label=tcp.state
```
{% endcode %}
где:

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `DeviceCustomString1=1218332722865011` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `DeviceInboundInterface=seq:Leth1{3` - содержит идентификатор входящего интерфейса;
* `DeviceProcessName=suricata_debug` - имя экземпляра системы предотвращения вторжений;
* `DeviceCustomString5=alert` - тип события;
* `SourceAddress=192.168.101.25` - IP-адрес источника;
* `DeviceCustomString1=local DeviceCustomString1Label=Src IP Type` - тип IP-адреса источника (`local` - локальный, `external` - внешний);
* `SourcePort=38003` - порт источника;
* `SourceCountry` - название местоположения источника;
* `DeviceCustomString2= DeviceCustomString2Label=Src Country Code` - ISO-код страны источника;
* `DeviceCustomString3=6103759e-5ad6-48b1-81b5-d15894b005ef DeviceCustomString3Label=Src session UUID` - внутренний идентификатор сессии Ideco NGFW источника; 
* `SourceUserID=2` - идентификатор пользователя источника;
* `SourceUserName=user` - имя пользователя источника;
* `DestinationAddress=192.168.101.10` - IP-адрес назначения;
* `DeviceCustomString4=local DeviceCustomString4Label=Dst IP Type` - тип IP-адреса назначения (`local` - локальный, `external` - внешний);
* `DestinationPort=53` - порт назначения;
* `DestinationCountry` - название местоположения назначения;
* `DeviceCustomString5= DeviceCustomString5Label=Dst Country Code` - ISO-код страны назначения;
* `DeviceCustomString6= DeviceCustomString6Label=Dst session UUID` - внутренний идентификатор сессии Ideco NGFW назначения;
* `DestinationUserID=-1` - идентификатор пользователя назначения;
* `DestinationUserName` - имя пользователя назначения;
* `TransportProtocol=UDP` - протокол;
* `DeviceEventClassID=1900005` - ID правила системы предотвращения вторжений;
* `Message=Mining pool` - сообщение из сработавшего правила;
* `DeviceEventCategory=Пулы криптомайнеров` - описание колонки в веб-интерфейсе События безопасности. Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf);
* `Severity=2` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы;
* `DeviceCustomString8=1 DeviceCustomString8Label=Alert GID` - GID угрозы;
* `DeviceCustomString9=blocked DeviceCustomString9Label=Alert action` - действие по отношению к угрозе (блокировать).

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:

* `DestinationHostName` - идентификатор хоста;
* `RequestUrl` - URL, на который велось обращение;
* `RequestClientApplication` - информация, идентифицирующая HTTP-клиента.

Служебные поля flow (сессии):

* `FlexNumber1=1 FlexNumber1Label=Flow packets to server` - количество пакетов, переданное от клиента к серверу;
* `FlexNumber2=0 FlexNumber2Label=Flow packets to client` - количество пакетов, переданное от сервера к клиенту;
* `BytesIn=81` - количество байт, переданное от клиента к серверу;
* `BytesOut=0` - количество байт, переданное от сервера к клиенту;
* `StartTime=2024-11-05 09:44:20.021521` - начало;
* `EndTime=2024-11-05 09:44:20.021846` - окончание;
* `FlexNumber3=0 FlexNumber3Label=flow` - возраст;
* `DeviceCustomString11= DeviceCustomString11Label=flow.state` - текущее состояние;
* `DeviceCustomString12= DeviceCustomString12Label=flow.reason` - запущен ли IPsec в режиме отладки;
* `FlexNumber4=0 FlexNumber4Label=flow.alerted` - сгенерировался ли поток alert.

Состояние флага [TCP flow (сессии)](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_(%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D0%B1%D0%B8%D1%82%D1%8B)):

* `DeviceCustomString14= DeviceCustomString14Label=tcp.tcp_flags` - значение поля flags в заголовке TCP;
* `DeviceCustomString15= DeviceCustomString15Label=tcp.tcp_flags_ts` -  [timestamp флаги](https://www.atraining.ru/windows-network-tuning/#:~:text=TCP%20Timestamps%20–%20базовая%20низкоуровневая,не%20может%20высчитать%20данные%20значения);
* `DeviceCustomString16= DeviceCustomString16Label=tcp.tcp_flags_tc` - [флаг Truncated response](https://www.rfc-editor.org/rfc/rfc5966);
* `FlexNumber5=0 FlexNumber5Label=tcp.cwr` - флаг TCP-пакета, информирующий отправителя, что получен пакет с установленным флагом ECE (Подробнее в [RFC-3186](https://datatracker.ietf.org/doc/html/rfc3168));
* `FlexNumber6=0 FlexNumber6Label=tcp.ecn` - флаг TCP-пакета, информирующий получателя, что узел способен на явное уведомление о перегрузке сети;
* `FlexNumber7=0 FlexNumber7Label=tcp.urg` - флаг TCP-пакета, указывающий важность пакета;
* `FlexNumber8=0 FlexNumber8Label=tcp.ack` - флаг TCP-пакета, указывающий, что пакет получен;
* `FlexNumber9=0 FlexNumber9Label=tcp.psh` - флаг TCP-пакета, информирующий получателя, что все данные переданы и можно передать их приложению;
* `FlexNumber10=0 FlexNumber10Label=tcp.rst` - флаг TCP-пакета, указывающий, что соединение завершено в аварийном режиме;
* `FlexNumber11=0 FlexNumber11Label=tcp.syn` - флаг TCP-пакета, отвечающий за установку соединения;
* `FlexNumber12=0 FlexNumber12Label=tcp.fin` - флаг TCP-пакета, указывающий на завершение соединения в штатном порядке;
* `DeviceCustomString17= DeviceCustomString17Label=tcp.state` - [состояния сеанса TCP](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#Состояния_сеанса_TCP).

</details>

<details>

<summary>Файрвол</summary>

Логирование включается в разделе **Правила трафика -> Файрвол -> Логирование**.

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 16:49:00 daemon notice 2024-11-05T16:48:49+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730807329 Severity=Warning DeviceProcessName=ideco-nflog msg=TCP src 192.168.101.25 sport 52416 dst 161.148.164.31 dport 443 table FWD rule 1 action drop
```
{% endcode %}
где:

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `TCP` - протокол. Это поле принимает значения: UDP, TCP, ICMP, GRE, ESP и AH;
* `src` - IP-адрес источника;
* `sport` - порт источника для UDP и TCP;
* `dst` - IP-адрес назначения;
* `dport` - порт назначения для UDP и TCP;
* `table` - таблица правил, в которой произошло логирование;
* `rule` - ID правила из таблицы;
* `action` - действие, которое произошло.

</details>

<details>

<summary>Контроль приложений</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 16:07:01 daemon info 2024-11-05T16:06:52+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730804812 Severity=Notice DeviceProcessName=ideco-app-control msg=(flow_info_rules_was_checked) 192.168.101.25:37936 -> 192.168.101.10:53 [Nintendo] \= 'DROP'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `flow_info_rules_was_checked` - идентификатор процесса;
* `192.168.101.25:37936` - IP-адрес источника;
* `192.168.101.10:53 [Nintendo] \= 'DROP'` - результат анализа трафика, где  `[Nintendo]` - название приложения, к которому был применен результат. [Список всех приложений](https://static.ideco.ru/static/app_control.pdf).

</details>

<details>

<summary>Контент-фильтр</summary>

Логирование включается в разделе **Сервисы -> Прокси -> Основное**. Просмотр логов доступен в веб-интерфейсе в разделе **Отчеты и журналы -> Журнал веб-доступа**. Название служб для фильтрации: `ideco-content-filter-backend` и `squid`.

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 16:39:20 daemon info 2024-11-06T18:39:18+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730900358 Severity=Notice DeviceProcessName=squid msg=192.168.101.25 - - [06/Nov/2024:18:39:18 +0500] "GET https://www.last.fm/ HTTP/1.1" 403 7479 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0" TCP_DENIED:HIER_NONE "Custom deny 2 Запрещенные сайты users.id.2 group.id.1 " "av_name": "-", "av_object_infected": "-", "av_object_size": "-", "av_virus_name": "-"
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.101.25` - IP-адрес пользователя;
* `[06/Nov/2024:18:39:18 +0500] "GET https://www.last.fm/ HTTP/1.1"`:
  * `[06/Nov/2024:18:39:18 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `https://www.last.fm/` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7479` - передано байт (в ответ, включая HTTP-заголовок);
* `Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0` - цифровой отпечаток браузера; 
* `TCP_DENIED:HIER_NONE` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `Custom deny 2 Запрещенные сайты users.id.2 group.id.1`:
  * `2 Запрещенные сайты` - название и номер правила блокировки;
  * `users.id.2` - категория сайта;
  * `group.id.1` - значение поля **Применяется для** в сработавшем правиле.

</details>

<details>

<summary>SSO-аутентификация</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:11:40+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721304700 Severity=Notice DeviceProcessName=ideco-web-authd msg=Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'web'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'web'` - тип авторизации веб.

</details>

<details>
<summary>Авторизация через журнал безопасности AD</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:20:22+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721305222 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'log'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'log'` - тип авторизации через журнал безопасности AD.

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 18:18:58 daemon info 2024-11-05T18:18:51+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730812731 Severity=Notice DeviceProcessName=ideco-web-authd msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'web'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'web'` - тип авторизации (веб).

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:17:32 daemon info 2024-11-05T19:17:23+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730816243 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'ip'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'ip'` - тип авторизации (IP).

</details>

<details>
<summary>Авторизация по MAC</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:23:03 daemon info 2024-11-05T19:22:55+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730816575 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'mac'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'mac'` - тип авторизации (MAC).

</details>

<details>
<summary>Авторизация по подсети</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:27:05 daemon info 2024-11-05T19:26:58+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730816818 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.0/24 is authorized as user 'user'. Connection made from None, type 'net'
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `192.168.101.0/24` - подсеть, по которой происходит авторизация;
* `user` - логин пользователя;
* `type 'net'` - тип авторизации (подсеть).

</details>

<details>

<summary>Подключение по VPN</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 12:15:46 daemon info 2024-11-06T14:15:35+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730884535 Severity=Notice DeviceProcessName=ideco-vpn-authd msg=Subnet 10.128.0.3/32 is authorized as user 'user'. Connection made from '192.168.1.25', type 'pptp'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `10.128.0.3/32` - сеть для VPN-подключений;
* `user` - логин пользователя;
* `192.168.1.25` - IP-адрес, откуда установлено подключение;
* `pptp` - протокол.

</details>

<details>

<summary>Служба fail2ban</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 15:02:25 daemon info 2024-11-06T17:02:17+05:00 ngfw-17 CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1730894537 Severity=Notice DeviceProcessName=fail2ban msg=INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-06 17:02:16
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `INFO` или `NOTICE` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-06 17:02:16` - факт обнаружения правил безопасности с указанием группы правил ([utm-vpn-authd]), IP-адреса и даты/времени. Список групп правил: 
  * `utm-dovecot` - авторизация на почтовом сервере через почтовые клиенты;
  * `utm-postfix-connrate` - превышение лимита подключения к почтовому серверу;
  * `utm-postscreen-prgrt` - отслеживание нежелательных подключений (PREGREET) к почтовому серверу;
  * `utm-reverse-proxy-conn` - защита от DoS (лимит подключений);
  * `utm-reverse-proxy-req` - защита от DoS (лимит запросов в секунду);
  * `utm-reverse-proxy` - Web Application Firewall (WAF);
  * `utm-roundcube` - авторизация в веб-интерфейсы почтового сервера;
  * `utm-smtp` - авторизация по smtp;
  * `utm-ssh` - авторизация по ssh;
  * `utm-two-factor-codes` - прохождение двухфакторной аутентификации;
  * `utm-vpn-authd` - авторизация по VPN;
  * `utm-vpn-pppoe-authd` - авторизация по VPN PPPoE;
  * `utm-web-interface` - авторизация в административном веб-интерфейсе;
  * `utm-user-cabinet` - авторизация в пользовательском веб-интерфейсе.

</details>

### Формат Syslog

Логи в Syslog-формате начинаются со строки вида:

{% code overflow="wrap" %}
``` 
192.168.1.100 Nov 05 19:30:56 1 daemon warning 2024-11-05T19:30:51+05:00
```
{% endcode %}
где:

* `192.168.1.100` - IP-адрес NGFW отправителя;
* `Nov 05 14:42:25` - время получения события по Syslog;
* `warning` - приоритет сообщения в логах. Другие значения: `info` (информационное сообщение), `notice` (уведомление);
* `2024-11-05T14:36:17+05:00` - время события в Ideco NGFW.

<details>
<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
192.168.1.100	Nov 05 14:42:25 1 daemon warning 2024-11-05T14:36:17+05:00 ngfw-17 suricata - - - flow_id:534238476293026, in_iface:seq:Leth1{3, sensor_name:suricata_debug, event_type:alert, src_ip:192.168.101.25, src_ip_type:local, src_port:36872, src_country:, src_country_code:, src_session_uuid:6103759e-5ad6-48b1-81b5-d15894b005ef, src_user_id:2, src_user_name:user, dest_ip:192.168.101.10, dest_ip_type:local, dest_port:53, dest_country:, dest_country_code:, dest_session_uuid:, dest_user_id:-1, dest_user_name:, proto:UDP, alert.signature_id:1900005, alert.signature:Mining pool, alert.category:Пулы криптомайнеров, alert.severity:2, alert.gid:1, alert.action:blocked, http.hostname:, http.url:, http.http_user_agent:, flow.pkts_toserver:1, flow.pkts_toclient:0, flow.bytes_toserver:81, flow.bytes_toclient:0, flow.start:2024-11-05 09:36:17.714211, flow.end:2024-11-05 09:36:17.714612, flow.age:0, flow.state:, flow.reason:, flow.alerted:0, tcp.tcp_flags:, tcp.tcp_flags_ts:, tcp.tcp_flags_tc:, tcp.cwr:0, tcp.ecn:0, tcp.urg:0, tcp.ack:0, tcp.psh:0, tcp.rst:0, tcp.syn:0, tcp.fin:0, tcp.state:
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `suricata` - название службы;
* `flow_id:534238476293026` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `in_iface:seq:Leth1{3` - содержит идентификатор входящего интерфейса;
* `sensor_name:suricata_debug` - имя экземпляра системы предотвращения вторжений;
* `event_type:alert` - тип события;
* `src_ip:192.168.101.25` - IP-адрес источника;
* `src_port:36872` - порт источника;
* `src_country:` - название местоположения источника;
* `src_country_code:` - ISO-код страны источника;
* `src_session_uuid:6103759e-5ad6-48b1-81b5-d15894b005ef` - внутренний идентификатор сессии Ideco NGFW источника;
* `src_user_id:2` - идентификатор пользователя источника;
* `src_user_name:user`- имя пользователя источника;
* `dest_ip:192.168.101.10` - IP-адрес назначения;
* `dest_port:53` - порт назначения;
* `dest_country:` - название местоположения назначения;
* `dest_country_code:` - ISO-код страны назначения;
* `dest_session_uuid:` - внутренний идентификатор сессии Ideco NGFW назначения;
* `dest_user_id:-1` - идентификатор пользователя назначения;
* `dest_user_name:` - имя пользователя назначения;
* `proto:UDP` - протокол;
* `alert.signature_id:1900005` - ID правила системы предотвращения вторжений;
* `alert.signature:Mining pool` - сообщение из сработавшего правила;
* `alert.category:Пулы криптомайнеров` - описание колонки в веб-интерфейсе **События безопасности**. Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf);
* `alert.severity:2` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы;
* `alert.gid:1` - GID угрозы;
* `alert.action:blocked` - действие по отношению к угрозе (блокировать).

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:

* `http.hostname:` - идентификатор хоста;
* `http.url:` - URL, на который велось обращение;
* `http.http_user_agent:` - информация, идентифицирующая HTTP-клиента.
  
Служебные поля flow (сессии):

* `flow.pkts_toserver:1` - количество пакетов, переданное от клиента к серверу;
* `flow.pkts_toclient:0` - количество пакетов, переданное от сервера к клиенту;
* `flow.bytes_toserver:81` - количество байт, переданное от клиента к серверу;
* `flow.bytes_toclient:0` - количество байт, переданное от сервера к клиенту;
* `flow.start:2024-11-05 09:36:17.714211` - начало;
* `flow.end:2024-11-05 09:36:17.714612` - окончание;
* `flow.age:0` - возраст;
* `flow.state:` - текущее состояние;
* `flow.reason:` - запущена ли IPsec в режиме отладки;
* `flow.alerted:0` - сгенерировался ли поток alert.

Состояние флага [TCP flow(сессии)](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_(%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D0%B1%D0%B8%D1%82%D1%8B)):

* `tcp.tcp_flags:` - значение поля flags в заголовке TCP;
* `tcp.tcp_flags_ts:` -  [timestamp флаги](https://www.atraining.ru/windows-network-tuning/#:~:text=TCP%20Timestamps%20–%20базовая%20низкоуровневая,не%20может%20высчитать%20данные%20значения);
* `tcp.tcp_flags_tc:` - [флаг Truncated response](https://www.rfc-editor.org/rfc/rfc5966);
* `tcp.cwr:0` - флаг TCP-пакета, информирующий отправителя, что получен пакет с установленным флагом ECE (Подробнее в [RFC-3186](https://datatracker.ietf.org/doc/html/rfc3168));
* `tcp.ecn:0` - флаг TCP-пакета, информирующий получателя, что узел способен на явное уведомление  о перегрузке сети;
* `tcp.urg:0` - флаг TCP-пакета, указывающий важность пакета;
* `tcp.ack:0` - флаг TCP-пакета, указывающий, что пакет получен;
* `tcp.psh:0` - флаг TCP-пакета, информирующий получателя, что все данные переданы и можно передать их приложению;
* `tcp.rst:0` - флаг TCP-пакета, указывающий, что соединение завершено в аварийном режиме;
* `tcp.syn:0` - флаг TCP-пакета, отвечающий за установку соединения;
* `tcp.fin:0` - флаг TCP-пакета, указывающий на завершение соединения в штатном порядке;
* `tcp.state:` - [состояния сеанса TCP](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#Состояния_сеанса_TCP).

</details>

<details>

<summary>Файрвол</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 16:50:52 1 daemon notice 2024-11-05T16:50:46+05:00 ngfw-17 ideco-nflog - - - TCP src 192.168.101.25 sport 35468 dst 161.148.164.31 dport 443 table FWD rule 1 action drop
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-nflog` - название службы;
* `TCP` - протокол, принимает значения: UDP, TCP, ICMP, GRE, ESP и AH;
* `src` - IP-адрес источника;
* `sport` - порт источника для UDP и TCP;
* `dst` - IP-адрес назначения;
* `dport` - порт назначения для UDP и TCP;
* `table` - таблица правил, в которой произошло логирование;
* `rule` - ID правила из таблицы;
* `action` - действие, которое произошло.

</details>

<details>

<summary>Контроль приложений</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 16:04:58 1 daemon info 2024-11-05T16:04:51+05:00 ngfw-17 ideco-app-control - - - (flow_info_rules_was_checked) 192.168.101.25:43800 -> 192.168.101.10:53 [Nintendo] = 'DROP'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-app-control` - название службы;
* `192.168.101.25:43800` - IP-адрес источника;
* `192.168.101.10:53 [Nintendo] = 'DROP'` - результат анализа трафика, где  `[Nintendo]` - название приложения, к которому был применен результат. [Список всех приложений](https://static.ideco.ru/static/app_control.pdf).

</details>

<details>

<summary>Контент-фильтр</summary>

Логирование включается в разделе **Сервисы -> Прокси -> Основное**. Просмотр логов доступен в веб-интерфейсе в разделе **Отчеты и журналы -> Журнал веб-доступа**. Название служб для фильтрации: `ideco-content-filter-backend` и `squid`.

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 16:40:56 1 daemon info 2024-11-06T18:40:50+05:00 ngfw-17 squid - - - 192.168.101.25 - - [06/Nov/2024:18:40:50 +0500] "GET https://www.last.fm/ HTTP/1.1" 403 7479 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0" TCP_DENIED:HIER_NONE "Custom deny 2 Запрещенные сайты users.id.2 group.id.1 " "av_name": "-", "av_object_infected": "-", "av_object_size": "-", "av_virus_name": "-"
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `squid` - название службы;
* `192.168.101.25` - IP-адрес пользователя;
* `[06/Nov/2024:18:40:50 +0500] "GET https://www.last.fm/ HTTP/1.1"`:
  * `[06/Nov/2024:18:40:50 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `https://www.last.fm/` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7479` - передано байт (в ответ, включая HTTP-заголовок);
* `Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0` - цифровой отпечаток браузера; 
* `TCP_DENIED:HIER_NONE` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `Custom deny 2 Запрещенные сайты users.id.2 group.id.1`:
  * `2 Запрещенные сайты` - название и номер правила блокировки;
  * `users.id.2` - категория сайта;
  * `group.id.1` - значение поля **Применяется для** в сработавшем правиле.

</details>

<details>
<summary>SSO-аутентификация</summary>

{% code overflow="wrap" %}
```
2024-07-18T16:59:55+05:00 Ideco-NGFW ideco-web-authd - - - Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'web'.
```
{% endcode %}

* `Ideco-NGFW` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-web-authd` - название службы;
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'web'` - тип авторизации веб.

</details>

<details>
<summary>Авторизация через журнал безопасности AD</summary>

{% code overflow="wrap" %}
```
2024-07-18T16:19:39+05:00 Ideco-NGFW ideco-auth-backend - - - Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'log'.
```
{% endcode %}

* `Ideco-NGFW` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'log'` - тип авторизации через журнал безопасности AD.

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 18:12:01 1 daemon info 2024-11-05T18:11:48+05:00 ngfw-17 ideco-web-authd - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'web'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-web-authd` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'web'` - тип авторизации (веб).

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:38:58 1 daemon info 2024-11-05T19:38:46+05:00 ngfw-17 ideco-auth-backend - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'ip'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'ip'` - тип авторизации (IP).

</details>

<details>
<summary>Авторизация по MAC</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:32:47 1 daemon info 2024-11-05T19:32:34+05:00 ngfw-17 ideco-auth-backend - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'mac'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'mac'` - тип авторизации (MAC).

</details>

<details>
<summary>Авторизация по подсетям</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 05 19:30:56 1 daemon info 2024-11-05T19:30:51+05:00 ngfw-17 ideco-auth-backend - - - Subnet 192.168.101.0/24 is authorized as user 'user'. Connection made from None, type 'net'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.101.0/24` - подсеть пользователя;
* `user` - логин пользователя;
* `type 'net'` - тип авторизации (подсеть).

</details>

<details>
<summary>Подключение по VPN</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 12:12:36 1 daemon info 2024-11-06T14:12:24+05:00 ngfw-17 ideco-vpn-authd - - - Subnet 10.128.0.3/32 is authorized as user 'user'. Connection made from '192.168.1.25', type 'pptp'.
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-vpn-authd` - название службы;
* `10.128.0.3/32` - сеть для VPN-подключений;
* `user` - логин пользователя; 
* `192.168.1.25` - IP-адрес, с которого установлено подключение;
* `pptp` - протокол.

</details>

<details>
<summary>Служба fail2ban</summary>

{% code overflow="wrap" %}
```
192.168.1.100 Nov 06 15:14:42 1 daemon info 2024-11-06T17:14:30+05:00 ngfw-17 fail2ban - - - INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-06 17:14:30
```
{% endcode %}

* `ngfw-17` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `fail2ban` - название службы;
* `INFO` или `NOTICE` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-06 17:02:16` - факт обнаружения правил безопасности с указанием группы правил ([utm-vpn-authd]), IP-адреса и даты/времени. Список групп правил: 
  * `utm-dovecot` - авторизация на почтовом сервере через почтовые клиенты;
  * `utm-postfix-connrate` - превышение лимита подключения к почтовому серверу;
  * `utm-postscreen-prgrt` - отслеживание нежелательных подключений (PREGREET) к почтовому серверу;
  * `utm-reverse-proxy-conn` - защита от DoS (лимит подключений);
  * `utm-reverse-proxy-req` - защита от DoS (лимит запросов в секунду);
  * `utm-reverse-proxy` - Web Application Firewall (WAF);
  * `utm-roundcube` - авторизация в веб-интерфейсы почтового сервера;
  * `utm-smtp` - авторизация по smtp;
  * `utm-ssh` - авторизация по ssh;
  * `utm-two-factor-codes` - прохождение двухфакторной аутентификации;
  * `utm-vpn-authd` - авторизация по VPN;
  * `utm-vpn-pppoe-authd` - авторизация по VPN PPPoE;
  * `utm-web-interface` - авторизация в административном веб-интерфейсе;
  * `utm-user-cabinet` - авторизация в пользовательском веб-интерфейсе.

</details>