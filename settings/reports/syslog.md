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
192.168.1.120 Nov 18 13:38:59 daemon warning 2024-11-18T15:38:54+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|
```
{% endcode %}
где:

* `192.168.1.120` - IP-адрес NGFW отправителя;
* `Nov 18 13:38:59` - время получения события по Syslog;
* `warning` - приоритет сообщения в логах. Другие значения: `info` (информационное сообщение), `notice` (уведомление);
* `2024-11-18T15:38:54+05:00` - время события в Ideco NGFW;
* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `CEF:0` - версия формата CEF;
* `Ideco` - вендор;
* `NGFW` - название продукта;
* `18.0` - версия продукта;
* `0|syslog|0` - идентификатор лога, постоянный для NGFW. Состоит из трех полей: идентификатор типа события, описание события, важность события.

<details>

<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
192.168.1.120 Nov 18 13:38:59 daemon warning 2024-11-18T15:38:54+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731926334 Severity=Warning DeviceProcessName=web-proxy DeviceCustomString1=1881087344384816 DeviceInboundInterface= DeviceProcessName=ideco-ips DeviceCustomString5=alert SourceAddress=192.168.101.25 DeviceCustomString1=local DeviceCustomString1Label=Src IP Type SourcePort=55644 SourceCountry= DeviceCustomString2= DeviceCustomString2Label=Src Country Code DeviceCustomString3=34fbd7c6-716b-4858-bb68-313729b1cad4 DeviceCustomString3Label=Src session UUID SourceUserID=9 SourceUserName=user DestinationAddress=212.70.163.70 DeviceCustomString4=external DeviceCustomString4Label=Dst IP Type DestinationPort=443 DestinationCountry=Латвия DeviceCustomString5=LV DeviceCustomString5Label=Dst Country Code DeviceCustomString6= DeviceCustomString6Label=Dst session UUID DestinationUserID=-1 DestinationUserName= TransportProtocol=TCP DeviceEventClassID=1005404 Message=GeoIP Latvia DeviceEventCategory=GeoIP Страны Восточной Европы Severity=2 DeviceCustomString8=1 DeviceCustomString8Label=Alert GID DeviceCustomString9=blocked DeviceCustomString9Label=Alert action DestinationHostName= RequestUrl= RequestClientApplication= FlexNumber1=1 FlexNumber1Label=Flow packets to server FlexNumber2=0 FlexNumber2Label=Flow packets to client BytesIn=60 BytesOut=0 StartTime=2024-11-18 10:38:54.110294 EndTime=2024-11-18 10:38:54.110969 FlexNumber3=0 FlexNumber3Label=flow DeviceCustomString11= DeviceCustomString11Label=flow.state DeviceCustomString12= DeviceCustomString12Label=flow.reason FlexNumber4=0 FlexNumber4Label=flow.alerted DeviceCustomString14= DeviceCustomString14Label=tcp.tcp_flags DeviceCustomString15= DeviceCustomString15Label=tcp.tcp_flags_ts DeviceCustomString16= DeviceCustomString16Label=tcp.tcp_flags_tc FlexNumber5=0 FlexNumber5Label=tcp.cwr FlexNumber6=0 FlexNumber6Label=tcp.ecn FlexNumber7=0 FlexNumber7Label=tcp.urg FlexNumber8=0 FlexNumber8Label=tcp.ack FlexNumber9=0 FlexNumber9Label=tcp.psh FlexNumber10=0 FlexNumber10Label=tcp.rst FlexNumber11=0 FlexNumber11Label=tcp.syn FlexNumber12=0 FlexNumber12Label=tcp.fin DeviceCustomString17= DeviceCustomString17Label=tcp.state
```
{% endcode %}
где:

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `DeviceCustomString1=1881087344384816` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `DeviceInboundInterface` - идентификатор входящего интерфейса;
* `DeviceProcessName=ideco-ips` - имя экземпляра системы предотвращения вторжений;
* `DeviceCustomString5=alert` - тип события;
* `SourceAddress=192.168.101.25` - IP-адрес источника;
* `DeviceCustomString1=local DeviceCustomString1Label=Src IP Type` - тип IP-адреса источника (`local` - локальный, `external` - внешний);
* `SourcePort=55644` - порт источника;
* `SourceCountry` - название местоположения источника;
* `DeviceCustomString2= DeviceCustomString2Label=Src Country Code` - ISO-код страны источника;
* `DeviceCustomString3=34fbd7c6-716b-4858-bb68-313729b1cad4 DeviceCustomString3Label=Src session UUID` - внутренний идентификатор сессии Ideco NGFW источника; 
* `SourceUserID=9` - идентификатор пользователя источника;
* `SourceUserName=user` - имя пользователя источника;
* `DestinationAddress=212.70.163.70` - IP-адрес назначения;
* `DeviceCustomString4=external DeviceCustomString4Label=Dst IP Type` - тип IP-адреса назначения (`local` - локальный, `external` - внешний);
* `DestinationPort=443` - порт назначения;
* `DestinationCountry=Латвия` - название местоположения назначения; 
* `DeviceCustomString5=LV DeviceCustomString5Label=Dst Country Code` - ISO-код страны назначения;
* `DeviceCustomString6= DeviceCustomString6Label=Dst session UUID` - внутренний идентификатор сессии Ideco NGFW назначения;
* `DestinationUserID=-1` - идентификатор пользователя назначения;
* `DestinationUserName` - имя пользователя назначения;
* `TransportProtocol=TCP` - протокол;
* `DeviceEventClassID=1005404` - ID правила системы предотвращения вторжений;
* `Message=GeoIP Latvia` - сообщение из сработавшего правила;
* `DeviceEventCategory=GeoIP Страны Восточной Европы` - описание колонки в веб-интерфейсе События безопасности;\
  Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf);
* `Severity=2` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы;
* `DeviceCustomString8=1 DeviceCustomString8Label=Alert GID` - GID угрозы;
* `DeviceCustomString9=blocked DeviceCustomString9Label=Alert action` - действие по отношению к угрозе (блокировать).

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:

* `DestinationHostName` - идентификатор хоста;
* `RequestUrl` - URL, на который велось обращение;
* `RequestClientApplication=` - информация, идентифицирующая HTTP-клиента.

Служебные поля flow (сессии):

* `FlexNumber1=1 FlexNumber1Label=Flow packets to server` - количество пакетов, переданное от клиента к серверу;
* `FlexNumber2=0 FlexNumber2Label=Flow packets to client` - количество пакетов, переданное от сервера к клиенту;
* `BytesIn=60` - количество байт, переданное от клиента к серверу;
* `BytesOut=0` - количество байт, переданное от сервера к клиенту;
* `StartTime=2024-11-18 10:38:54.110294` - начало;
* `EndTime=2024-11-18 10:38:54.110969` - окончание;
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
192.168.1.120 Nov 18 14:25:06 daemon info 2024-11-18T16:25:00+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731929100 Severity=Notice DeviceProcessName=ideco-conndrop msg=tcp 6 9 CLOSE src\=192.168.101.25 dst\=151.101.85.188 sport\=58770 dport\=443 src\=151.101.85.188 dst\=192.168.1.120 sport\=443 dport\=58770 [ASSURED] mark\=2 use\=1
```
{% endcode %}
где:

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `tcp 6` - идентификтор протокола в строчном и в десятичном виде;
* `9` - продолжительность conntrack (модуль отслеживания соединения);
* `CLOSE` - состояние соединения;
* `src` - IP-адрес источника;
* `sport` - порт источника для UDP и TCP;
* `dst` - IP-адрес назначения;
* `dport` - порт назначения для UDP и TCP;
* `[ASSURED]` - уведомление, что соединение не будет сброшено при перегрузке conntrack;
* `mark`- маркировка conntrack.

</details>

<details>

<summary>Контент-фильтр</summary>

Логирование включается в разделе **Сервисы -> Прокси -> Основное**. Просмотр логов доступен в веб-интерфейсе в разделе **Отчеты и журналы -> Системный журнал**. Название служб для фильтрации: `ideco-content-filter-backend` и `squid`.

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:56:45 daemon info 2024-11-18T19:56:41+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731941801 Severity=Notice DeviceProcessName=squid msg={10.128.0.5 - - [18/Nov/2024:19:56:41 +0500] "GET http://counter.yadro.ru/hit;argon? HTTP/1.1" 403 7594 "http://argon.pro/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0" TCP_MISS:ORIGINAL_DST "-","av_name": "-","av_object_infected": "-","av_object_size": "7250","av_virus_name": "-","x_infection_found": "-","x_virus_id": "-","x_av_verifed": "-","morph-action": "CheckedOK","morph-dict-id": "-"}
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `10.128.0.5` - IP-адрес пользователя;
* `[18/Nov/2024:19:56:41 +0500] "GET http://counter.yadro.ru/hit;argon? HTTP/1.1"`:
  * `[18/Nov/2024:19:56:41 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `http://counter.yadro.ru/hit;argon?` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7594` - передано байт (в ответ, включая HTTP заголовок);
* `http://argon.pro/` - [HTTP referer](https://ru.wikipedia.org/wiki/HTTP_referer);
* `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0` - цифровой отпечаток браузера; 
* `TCP_MISS:ORIGINAL_DST` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `"av_name": "-"` - название антивируса, если он включен, в примере антивирус отключен;
* `"av_object_infected": "-"` - результат проверки антивирусом, пустое поле - вирус не обнаружен;
* `"av_object_size": "7250"` - размер проверяемого объекта;
* `"av_virus_name": "-"` - название обнаруженного вируса;
* `"x_infection_found": "-"` - подтверждение, что запрос был обработан ICAP-оберткой для антивируса (Касперский);
* `"morph-action": "CheckedOK"` - результат проверки **Морфологическим анализом**;
* `"morph-dict-id": "-"` - название морфологического словаря, указывается в случае запрета **Морфологическим анализом**.

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
* `type 'web'` - тип авторизации (веб).

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
* `type 'log'` - тип авторизации (через журнал безопасности AD).

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
192.168.1.120 Nov 18 12:54:36 daemon info 2024-11-18T14:54:21+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731923661 Severity=Notice DeviceProcessName=ideco-web-authd msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'web'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `user` - логин пользователя;
* `192.168.101.25/32` - IP-адрес пользователя;
* `type 'web'` - тип авторизации (веб).

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 16:51:54 daemon info 2024-11-18T18:51:43+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731937903 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'ip'.
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
192.168.1.10 Nov 18 16:54:35 daemon info 2024-11-18T18:54:21+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731938061 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'mac'.
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
<summary>Авторизация по подсетям</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:08:03 daemon info 2024-11-18T19:07:54+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731938874 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.101.0/24 is authorized as user 'user'. Connection made from None, type 'net'.
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
192.168.1.10 Nov 18 17:16:25 daemon info 2024-11-18T19:16:18+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731939378 Severity=Notice DeviceProcessName=ideco-vpn-authd msg=Start vpn authorization ('user', '192.168.1.25', 'pptp').
192.168.1.10 Nov 18 17:16:25 daemon info 2024-11-18T19:16:18+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731939378 Severity=Notice DeviceProcessName=ideco-vpn-authd msg=Subnet 10.128.0.6/32 is authorized as user 'user'. Connection made from '192.168.1.25', type 'pptp'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `10.128.0.6/32` - сеть для VPN-подключений;
* `user` - логин пользователя;
* `192.168.1.25` - IP-адрес, откуда установлено подключение;
* `pptp` - протокол.

</details>

<details>

<summary>Служба fail2ban</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:27:07 daemon info 2024-11-18T19:26:57+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731940017 Severity=Notice DeviceProcessName=fail2ban msg=INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-18 19:26:57
192.168.1.10 Nov 18 17:27:07 daemon notice 2024-11-18T19:26:57+05:00 ngfw-18 CEF:0|Ideco|NGFW|18.0|0|syslog|0|deviceReceiptTime=1731940017 Severity=Warning DeviceProcessName=fail2ban msg=NOTICE [utm-vpn-authd] Ban 192.168.1.25
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW;
* `INFO` или `NOTICE` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `INFO [utm-web-interface] Found 192.168.1.25 - 2024-11-18 19:26:57` - факт обнаружения правил безопасности с указанием группы правил ([utm-web-interface]), IP-адреса и даты/времени. Список групп правил: 
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
* `NOTICE [utm-vpn-authd] Ban 192.168.1.25` - факт блокировки или разблокировки IP-адреса, где:
  * `Ban` - факт блокировки;
  * `Unban` - факт разблокировки.

</details>

### Формат Syslog

Логи в Syslog-формате начинаются со строки вида:

{% code overflow="wrap" %}
``` 
192.168.1.120 Nov 18 13:40:24 1 daemon warning 2024-11-18T15:40:12+05:00
```
{% endcode %}
где:

* `192.168.1.120` - IP-адрес NGFW отправителя;
* `Nov 18 13:40:24` - время получения события по Syslog;
* `warning` - приоритет сообщения в логах. Другие значения: `info` (информационное сообщение), `notice` (уведомление);
* `2024-11-18T15:40:12+05:00` - время события в Ideco NGFW.

<details>
<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
192.168.1.120 Nov 18 13:40:24 1 daemon warning 2024-11-18T15:40:12+05:00 ngfw-18 suricata - - - flow_id:1344232018329395, in_iface:, sensor_name:ideco-ips, event_type:alert, src_ip:192.168.101.25, src_ip_type:local, src_port:40632, src_country:, src_country_code:, src_session_uuid:34fbd7c6-716b-4858-bb68-313729b1cad4, src_user_id:9, src_user_name:user, dest_ip:212.70.163.70, dest_ip_type:external, dest_port:443, dest_country:Латвия, dest_country_code:LV, dest_session_uuid:, dest_user_id:-1, dest_user_name:, proto:TCP, alert.signature_id:1005404, alert.signature:GeoIP Latvia, alert.category:GeoIP Страны Восточной Европы, alert.severity:2, alert.gid:1, alert.action:blocked, http.hostname:, http.url:, http.http_user_agent:, flow.pkts_toserver:1, flow.pkts_toclient:0, flow.bytes_toserver:60, flow.bytes_toclient:0, flow.start:2024-11-18 10:40:12.378514, flow.end:2024-11-18 10:40:12.379198, flow.age:0, flow.state:, flow.reason:, flow.alerted:0, tcp.tcp_flags:, tcp.tcp_flags_ts:, tcp.tcp_flags_tc:, tcp.cwr:0, tcp.ecn:0, tcp.urg:0, tcp.ack:0, tcp.psh:0, tcp.rst:0, tcp.syn:0, tcp.fin:0, tcp.state:
```
{% endcode %}

где:
* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `suricata` - название службы;
* `flow_id:1344232018329395` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `in_iface` - идентификатор входящего интерфейса;
* `sensor_name:ideco-ips` - имя экземпляра системы предотвращения вторжений;
* `event_type:alert` - тип события;
* `src_ip:192.168.101.25` - IP-адрес источника;
* `src_port:40632` - порт источника;
* `src_country` - название местоположения источника;
* `src_country_code` - ISO-код страны источника;
* `src_session_uuid:34fbd7c6-716b-4858-bb68-313729b1cad4` - внутренний идентификатор сессии Ideco NGFW источника;
* `src_user_id:9` - идентификатор пользователя источника;
* `src_user_name:user`- имя пользователя источника;
* `dest_ip:212.70.163.70` - IP-адрес назначения;
* `dest_port:443` - порт назначения;
* `dest_country:Латвия` - название местоположения назначения;
* `dest_country_code:LV` - ISO-код страны назначения;
* `dest_session_uuid` - внутренний идентификатор сессии Ideco NGFW назначения;
* `dest_user_id:-1` - идентификатор пользователя назначения;
* `dest_user_name` - имя пользователя назначения;
* `proto:TCP` - протокол;
* `alert.signature_id:1005404` - идентификатор правила системы предотвращения вторжений;
* `alert.signature:GeoIP Latvia` - сообщение из сработавшего правила;
* `alert.category:GeoIP Страны Восточной Европы` - описание колонки в веб-интерфейсе События безопасности; \
  Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf).
* `alert.severity:2` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы;
* `alert.gid:1` - GID угрозы;
* `alert.action:blocked` - действие по отношению к угрозе (блокировать).

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:
* `http.hostname` - идентификатор хоста;
* `http.url` - URL, на который велось обращение;
* `http.http_user_agent` - информация, идентифицирующая HTTP-клиента.
  
Служебные поля flow (сессии):

* `flow.pkts_toserver:1` - количество пакетов, переданное от клиента к серверу;
* `flow.pkts_toclient:0` - количество пакетов, переданное от сервера к клиенту;
* `flow.bytes_toserver:60` - количество байт, переданное от клиента к серверу;
* `flow.bytes_toclient:0` - количество байт, переданное от сервера к клиенту;
* `flow.start:2024-11-18 10:40:12.378514` - начало;
* `flow.end:2024-11-18 10:40:12.379198` - окончание;
* `flow.age:0` - возраст;
* `flow.state` - текущее состояние;
* `flow.reason` - запущена ли IPsec в режиме отладки;
* `flow.alerted` 0 - сгенерировался ли поток alert.

Состояние флага [TCP flow(сессии)](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_(%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D0%B1%D0%B8%D1%82%D1%8B)):

* `tcp.tcp_flags` - значение поля flags в заголовке TCP;
* `tcp.tcp_flags_ts` -  [timestamp флаги](https://www.atraining.ru/windows-network-tuning/#:~:text=TCP%20Timestamps%20–%20базовая%20низкоуровневая,не%20может%20высчитать%20данные%20значения);
* `tcp.tcp_flags_tc` - [флаг Truncated response](https://www.rfc-editor.org/rfc/rfc5966);
* `tcp.cwr: 0` - флаг TCP-пакета, информирующий отправителя, что получен пакет с установленным флагом ECE (Подробнее в [RFC-3186](https://datatracker.ietf.org/doc/html/rfc3168));
* `tcp.ecn:0` - флаг TCP-пакета, информирующий получателя, что узел способен на явное уведомление  о перегрузке сети;
* `tcp.urg:0` - флаг TCP-пакета, указывающий важность пакета;
* `tcp.ack:0` - флаг TCP-пакета, указывающий, что пакет получен;
* `tcp.psh:0` - флаг TCP-пакета, информирующий получателя, что все данные переданы и можно передать их приложению;
* `tcp.rst:0` - флаг TCP-пакета, указывающий, что соединение завершено в аварийном режиме;
* `tcp.syn:0` - флаг TCP-пакета, отвечающий за установку соединения;
* `tcp.fin:0` - флаг TCP-пакета, указывающий на завершение соединения в штатном порядке;
* `tcp.state` - [состояния сеанса TCP](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#Состояния_сеанса_TCP).

</details>

<details>

<summary>Файрвол</summary>

Логирование включается в разделе **Правила трафика -> Файрвол -> Логирование**.

{% code overflow="wrap" %}
```
192.168.1.120	Nov 18 13:55:07	1 daemon info 2024-11-18T15:55:00+05:00 ngfw-18 ideco-conndrop - - - tcp 6 7 CLOSE src=192.168.101.25 dst=151.101.236.157 sport=34802 dport=443 src=151.101.236.157 dst=192.168.1.120 sport=443 dport=34802 [ASSURED] mark=2 use=1
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-conndrop` - название службы;
* `tcp 6` - идентификтор протокола в строчном и в десятичном виде;
* `9` - продолжительность conntrack (модуль отслеживания соединения);
* `CLOSE` - состояние соединения;
* `src` - IP-адрес источника;
* `dst` - IP-адрес назначения;
* `sport` - порт источника для UDP и TCP;
* `dport` - порт назначения для UDP и TCP;
* `[ASSURED]` - уведомление, что соединение не будет сброшено при перегрузке conntrack;
* `mark`- маркировка conntrack.

</details>

<details>

<summary>Контент-фильтр</summary>

Логирование включается в разделе **Сервисы -> Прокси -> Основное**. Просмотр логов доступен в веб-интерфейсе в разделе **Отчеты и журналы -> Системный журнал**. Название служб для фильтрации: `ideco-content-filter-backend` и `squid`.

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:50:05 1 daemon info 2024-11-18T19:49:58+05:00 ngfw-18 squid - - - {10.128.0.6 - - [18/Nov/2024:19:49:58 +0500] "GET http://counter.yadro.ru/hit;argon? HTTP/1.1" 403 7594 "http://argon.pro/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0" TCP_MISS:ORIGINAL_DST "-","av_name": "-","av_object_infected": "-","av_object_size": "7250","av_virus_name": "-","x_infection_found": "-","x_virus_id": "-","x_av_verifed": "-","morph-action": "CheckedOK","morph-dict-id": "-"}
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `squid` - название службы;
* `10.128.0.6` - IP-адрес пользователя;
* `[18/Nov/2024:19:49:58 +0500] "GET http://counter.yadro.ru/hit;argon? HTTP/1.1"`:
  * `[18/Nov/2024:19:49:58 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `http://counter.yadro.ru/hit;argon?` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7594` - передано байт (в ответ, включая HTTP заголовок);
* `http://argon.pro/` - [HTTP referer](https://ru.wikipedia.org/wiki/HTTP_referer);
* `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0` - цифровой отпечаток браузера; 
* `TCP_MISS:ORIGINAL_DST` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `"av_name": "-"` - название антивируса, если он включен, в примере антивирус отключен;
* `"av_object_infected": "-"` - результат проверки антивирусом, пустое поле - вирус не обнаружен;
* `"av_object_size": "7250"` - размер проверяемого объекта;
* `"av_virus_name": "-"` - название обнаруженного вируса;
* `"x_infection_found": "-"` - подтверждение, что запрос был обработан ICAP-оберткой для антивируса (Касперский);
* `"morph-action": "CheckedOK"` - результат проверки **Морфологическим анализом**;
* `"morph-dict-id": "-"` - название морфологического словаря, указывается в случае запрета **Морфологическим анализом**.

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
* `type 'web'` - тип авторизации (веб).

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
* `type 'log'` - тип авторизации (через журнал безопасности AD).

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
192.168.1.120 Nov 18 12:47:27 1 daemon info 2024-11-18T14:47:11+05:00 ngfw-18 ideco-web-authd - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'web'.
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-web-authd` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'web'` - тип авторизации (веб).

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 16:42:56 1 daemon info 2024-11-18T18:42:45+05:00 ngfw-18 ideco-auth-backend - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'ip'.
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-web-authd` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'ip'` - тип авторизации (IP).

</details>

<details>
<summary>Авторизация по MAC</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:01:22 1 daemon info 2024-11-18T19:01:14+05:00 ngfw-18 ideco-auth-backend - - - Subnet 192.168.101.25/32 is authorized as user 'user'. Connection made from None, type 'mac'.
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.101.25/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'mac'` - тип авторизации (MAC).

</details>

<details>
<summary>Авторизация по подсетям</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:06:23 1 daemon info 2024-11-18T19:06:08+05:00 ngfw-18 ideco-auth-backend - - - Subnet 192.168.101.0/24 is authorized as user 'user'. Connection made from None, type 'net'.
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-auth-backend` - название службы;
* `192.168.101.0/24` - подсеть пользователя;
* `user` - логин пользователя;
* `type 'net'` - тип авторизации (подсеть).

</details>

<details>

<summary>Подключение по VPN</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:18:04 1 daemon info 2024-11-18T19:17:56+05:00 ngfw-18 ideco-vpn-authd - - - Start vpn authorization ('user', '192.168.1.25', 'pptp').
192.168.1.10 Nov 18 17:18:04 1 daemon info 2024-11-18T19:17:56+05:00 ngfw-18 ideco-vpn-authd - - - Subnet 10.128.0.5/32 is authorized as user 'user'. Connection made from '192.168.1.25', type 'pptp'.
```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `ideco-vpn-authd` - название службы;
* `10.128.0.5/32` - сеть для VPN-подключений;
* `user` - логин пользователя; 
* `192.168.1.25` - IP-адрес, с которого установлено подключение;
* `pptp` - протокол.

</details>

<details>

<summary>Служба fail2ban</summary>

{% code overflow="wrap" %}
```
192.168.1.10 Nov 18 17:22:05 1 daemon info 2024-11-18T19:21:54+05:00 ngfw-18 fail2ban - - - INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-18 19:21:54

```
{% endcode %}

* `ngfw-18` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `fail2ban` - название службы;
* `info` или `notice` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `INFO [utm-vpn-authd] Found 192.168.1.25 - 2024-11-18 19:21:54` - факт обнаружения правил безопасности с указанием группы правил (`[utm-web-interface]`), IP-адреса и даты/времени. Список групп правил: 
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