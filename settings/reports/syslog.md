---
description: >-
  Включение этого модуля дает возможность передавать все системные сообщения
  (syslog) Ideco NGFW в сторонние коллекторы (Syslog Collector) или в
  SIEM-системы.
---

# Syslog

{% hint style="success" %}
Название службы раздела **Syslog**: `ideco-monitor-backend`. \
Список служб для других разделов доступен по [ссылке](/settings/server-management/terminal.md).
{% endhint %}

## Пересылка системных сообщений

Чтобы настроить пересылку системных сообщений, перейдите в раздел **Отчеты и журналы -> Syslog** и выполните действия:

1\. Укажите IP-адрес сервера-коллектора (любой локальный "серый" или публичный "белый" IP-адрес);

2\. В поле **Порт** укажите любой порт из диапазона от 1 до 65535;

3\. Выберите формат передаваемых системных сообщений (Syslog или CEF);

4\. Выберите протокол передачи системных логов - TCP или UDP;

5\. Нажмите **Сохранить** и переведите опцию в верхней части страницы в положение включен:

![](/.gitbook/assets/remote-syslog.png)

{% hint style="info" %}
Рекомендуется передавать логи по протоколу TCP, так как он гарантирует доставку и соблюдает последовательность сообщений.
{% endhint %}

## Расшифровка передаваемых логов

### Формат CEF

Логи в CEF-формате всегда начинаются со строки вида:

{% code overflow="wrap" %}
``` 
2024-04-02T14:20:01+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|
```
{% endcode %}
где:

* `2024-04-02T14:16:22+05:00` - время события в Ideco NGFW;
* `ideco-ngfw` - hostname сервера NGFW, заданный в левом верхнем углу веб-интерфейса;
* `CEF:0` - версия формата CEF;
* `Ideco` - вендор;
* `NGFW` - название продукта (может меняться в зависимости от продукта);
* `17.0` - версия продукта (может меняться в зависимости от версии);
* `0|syslog|0` - три поля - идентификатор типа события, описание события, важность события. Идентификатор лога, постоянный для NGFW.

<details>

<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
2024-04-02T14:16:22+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712049382 Severity=Warning DeviceProcessName=web-proxy DeviceCustomString1=1831848834213181 DeviceInboundInterface=seq:Leth8{3 DeviceProcessName=suricata_debug DeviceCustomString5=alert SourceAddress=192.168.100.17 DeviceCustomString1=local DeviceCustomString1Label=Src IP Type SourcePort=49777 SourceCountry= DeviceCustomString2= DeviceCustomString2Label=Src Country Code DeviceCustomString3=70977265-245b-44f7-8281-b0e26cae1c46 DeviceCustomString3Label=Src session UUID SourceUserID=59 SourceUserName=192.168.100.17 DestinationAddress=52.185.211.133 DeviceCustomString4=external DeviceCustomString4Label=Dst IP Type DestinationPort=443 DestinationCountry=США DeviceCustomString5=US DeviceCustomString5Label=Dst Country Code DeviceCustomString6= DeviceCustomString6Label=Dst session UUID DestinationUserID=-1 DestinationUserName= TransportProtocol=TCP DeviceEventClassID=1006202 Message=Windows Telemetry DeviceEventCategory=Телеметрия Windows Severity=3 DeviceCustomString8=1 DeviceCustomString8Label=Alert GID DeviceCustomString9=blocked DeviceCustomString9Label=Alert action DestinationHostName= RequestUrl= RequestClientApplication= FlexNumber1=3 FlexNumber1Label=Flow packets to server FlexNumber2=1 FlexNumber2Label=Flow packets to client BytesIn=390 BytesOut=66 StartTime=2024-04-02 09:16:22.885262 EndTime=2024-04-02 09:16:22.887440 FlexNumber3=0 FlexNumber3Label=flow DeviceCustomString11= DeviceCustomString11Label=flow.state DeviceCustomString12= DeviceCustomString12Label=flow.reason FlexNumber4=0 FlexNumber4Label=flow.alerted DeviceCustomString14= DeviceCustomString14Label=tcp.tcp_flags DeviceCustomString15= DeviceCustomString15Label=tcp.tcp_flags_ts DeviceCustomString16= DeviceCustomString16Label=tcp.tcp_flags_tc FlexNumber5=0 FlexNumber5Label=tcp.cwr FlexNumber6=0 FlexNumber6Label=tcp.ecn FlexNumber7=0 FlexNumber7Label=tcp.urg FlexNumber8=0 FlexNumber8Label=tcp.ack FlexNumber9=0 FlexNumber9Label=tcp.psh FlexNumber10=0 FlexNumber10Label=tcp.rst FlexNumber11=0 FlexNumber11Label=tcp.syn FlexNumber12=0 FlexNumber12Label=tcp.fin DeviceCustomString17= DeviceCustomString17Label=tcp.state
```
{% endcode %}
где:

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `DeviceCustomString1=1831848834213181` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `DeviceInboundInterface=seq:Leth8{3` - содержит идентификатор входящего интерфейса;
* `DeviceProcessName=suricata_debug` - имя экземпляра системы предотвращения вторжений;
* `DeviceCustomString5=alert` - тип события;
* `SourceAddress=192.168.100.17` - IP-адрес источника;
* `DeviceCustomString1=local DeviceCustomString1Label=Src IP Type` - тип IP-адреса источника (`local` - локальный, `external` - внешний); 
* `SourcePort=49777` - порт источника;
* `SourceCountry=` - название местоположения источника;
* `DeviceCustomString2= DeviceCustomString2Label=Src Country Code` - ISO-код страны источника;
* `DeviceCustomString3=70977265-245b-44f7-8281-b0e26cae1c46 DeviceCustomString3Label=Src session UUID` - внутренний идентификатор сессии Ideco NGFW источника; 
* `SourceUserID=59` - идентификатор пользователя источника;
* `SourceUserName=192.168.100.17` - имя пользователя источника;
* `DestinationAddress=52.185.211.133` - IP-адрес назначения;
* `DeviceCustomString4=external DeviceCustomString4Label=Dst IP Type` - тип IP-адреса назначения (local - локальный, external - внешний);
* `DestinationPort=443` - порт назначения;
* `DestinationCountry=США` - название местоположения назначения; 
* `DeviceCustomString5=US DeviceCustomString5Label=Dst Country Code` - ISO-код страны назначения;
* `DeviceCustomString6= DeviceCustomString6Label=Dst session UUID` - внутренний идентификатор сессии Ideco NGFW назначения;
* `DestinationUserID=-1` - идентификатор пользователя назначения;
* `DestinationUserName=` - имя пользователя назначения;
* `TransportProtocol=TCP` - протокол;
* `DeviceEventClassID=1006202` - ID правила системы предотвращения вторжений;
* `Message=Windows Telemetry` - сообщение из сработавшего правила;
* `DeviceEventCategory=Телеметрия Windows` - описание колонки в веб-интерфейсе События безопасности;\
  Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf).
* `Severity=3` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы.

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:

* `DestinationHostName=` - идентификатор хоста;
* `RequestUrl= - url`, на который велось обращение;
* `RequestClientApplication=` - информация, идентифицирующая HTTP-клиента.

Служебные поля flow (сессии):

* `FlexNumber1=3 FlexNumber1Label=Flow packets to server` - количество пакетов, переданное от клиента к серверу;
* `FlexNumber2=1 FlexNumber2Label=Flow packets to client` - количество пакетов, переданное от сервера к клиенту;
* `BytesIn=390` - количество байт, переданное от клиента к серверу;
* `BytesOut=66` - количество байт, переданное от сервера к клиенту;
* `StartTime=2024-04-02 09:16:22.885262` - начало;
* `EndTime=2024-04-02 09:16:22.887440` - окончание;
* `FlexNumber3=0 FlexNumber3Label=flow` - возраст;
* `DeviceCustomString11= DeviceCustomString11Label=flow.state` - текущее состояние;
* `DeviceCustomString12= DeviceCustomString12Label=flow.reason` - запущена ли IPsec в режиме отладки;
* `FlexNumber4=0 FlexNumber4Label=flow.alerted` - сгенерировался ли поток alert.

Состояние флага [TCP flow (сессии)](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_(%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D0%B1%D0%B8%D1%82%D1%8B)):

* `DeviceCustomString14= DeviceCustomString14Label=tcp.tcp_flags` - значение поля flags в заголовке TCP;
* `DeviceCustomString15= DeviceCustomString15Label=tcp.tcp_flags_ts` -  [timestamp флаги](https://www.atraining.ru/windows-network-tuning/#:~:text=TCP%20Timestamps%20–%20базовая%20низкоуровневая,не%20может%20высчитать%20данные%20значения);
* `DeviceCustomString16= DeviceCustomString16Label=tcp.tcp_flags_tc` - [флаг Truncated response](https://www.rfc-editor.org/rfc/rfc5966);
* `FlexNumber5=0 FlexNumber5Label=tcp.cwr 0` - флаг TCP-пакета, информирующий отправителя, что получен пакет с установленным флагом ECE (Подробнее в [RFC-3186](https://datatracker.ietf.org/doc/html/rfc3168));
* `FlexNumber6=0 FlexNumber6Label=tcp.ecn 0` - флаг TCP-пакета, информирующий получателя, что узел способен на явное уведомление о перегрузке сети;
* `FlexNumber7=0 FlexNumber7Label=tcp.urg 0` - флаг TCP-пакета, указывающий важность пакета;
* `FlexNumber8=0 FlexNumber8Label=tcp.ack 0` - флаг TCP-пакета, указывающий, что пакет получен;
* `FlexNumber9=0 FlexNumber9Label=tcp.psh 0` - флаг TCP-пакета, информирующий получателя, что все данные переданы и можно передать их приложению;
* `FlexNumber10=0 FlexNumber10Label=tcp.rst 0` - флаг TCP-пакета, указывающий, что соединение завершено в аварийном режиме;
* `FlexNumber11=0 FlexNumber11Label=tcp.syn 0` - флаг TCP-пакета, отвечающий за установку соединения;
* `FlexNumber12=0 FlexNumber12Label=tcp.fin 0` - флаг TCP-пакета, указывающий на завершение соединения в штатном порядке;
* `DeviceCustomString17= DeviceCustomString17Label=tcp.state` - [состояния сеанса TCP](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#Состояния_сеанса_TCP).

</details>

<details>

<summary>Файрвол</summary>

{% code overflow="wrap" %}
```
2024-04-02T14:20:01+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712049601 Severity=Warning DeviceProcessName=ideco-nflog msg=TCP      src 192.168.100.17   sport 48300 dst 1.1.1.1          dport 443   table FWD  rule  2    action drop
```
{% endcode %}
где:

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `TCP` - протокол. Это поле принимает значения UDP, TCP, ICMP, GRE, ESP и AH;
* `src` - IP-адрес источника;
* `dst` - IP-адрес назначения;
* `sport` - порт источника для UDP и TCP;
* `dport` - порт назначения для UDP и TCP;
* `table` - таблица правил, в которой произошло логирование;
* `rule` - ID правила из таблицы;
* `action` - действие, которое произошло.

</details>

<details>

<summary>Контроль приложений</summary>

{% code overflow="wrap" %}
```
2024-04-02T14:27:57+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712050077 Severity=Notice DeviceProcessName=ideco-app-control msg=(flow_info_rules_was_checked) 192.168.100.17:49873 -> 162.159.138.232:443 [Discord] \= 'DROP'. 
```
{% endcode %}

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `flow_info_rules_was_checked` - идентификатор процесса;
* `192.168.100.17:49873` - IP-адрес источника;
* `162.159.138.232:443 [Discord] \= 'DROP'` - результат анализа трафика, где  `[Discord]` - название приложения, к которому был применен результат. [Список всех приложений](https://static.ideco.ru/static/app_control.pdf).

</details>

<details>

<summary>Контент-фильтр</summary>

Просмотр логов доступен в веб-интерфейсе в разделе **Мониторинг -> Журналы**. Название служб для фильтрации: ideco-content-filter-backend и squid ().

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
2024-04-03T13:00:38+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712131238 Severity=Notice DeviceProcessName=squid msg=192.168.100.17 - - [03/Apr/2024:13:00:38 +0500] "GET https://love.ru/znakomstva/ekaterinburg/ HTTP/1.1" 403 7519 "https://www.google.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36" TCP_DENIED:HIER_NONE "Custom deny 8 znakomstva extended.id.23 user.id.3 " "av_name": "-", "av_object_infected": "-", "av_object_size": "-", "av_virus_name": "-" 
```
{% endcode %}

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `192.168.100.17` - IP-адрес пользователя;
* `[03/Apr/2024:13:00:38 +0500] "GET https://love.ru/znakomstva/ekaterinburg/ HTTP/1.1"`:
  * `[03/Apr/2024:13:00:38 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `https://love.ru/znakomstva/ekaterinburg/` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7519` - передано байт (в ответ, включая HTTP заголовок);
* `"https://www.google.com/"` - [HTTP referer](https://ru.wikipedia.org/wiki/HTTP_referer);
* `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"` - цифровой отпечаток браузера; 
* `TCP_DENIED:HIER_NONE` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `"Custom deny 8 znakomstva extended.id.23 user.id.3 "`:
  * `Custom deny 8 znakomstva` - описание и номер правила блокировки;
  * `extended.id.23` - категория сайта;
  * `user.id.3` - значение поля **Применяется для** в сработавшем правиле.

</details>

<details>

<summary>Аутентификация через веб-интерфейс</summary>

{% code overflow="wrap" %}
```
2024-04-02T14:51:36+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712051496 Severity=Notice DeviceProcessName=fail2ban msg=INFO [utm-web-interface] Found 192.168.100.17 - 2024-04-02 14:51:36
2024-04-02T14:51:36+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712051496 Severity=Warning DeviceProcessName=fail2ban msg=NOTICE [utm-web-interface] Ban 192.168.100.17
```
{% endcode %}

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `INFO` или `NOTICE` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `INFO [utm-web-interface] Found 192.168.100.17 - 2024-04-02 14:51:36` - факт обнаружения правил безопасности с указанием группы правил ([utm-web-interface]), IP-адреса и даты/времени. Список групп правил: 
  * `utm-dovecot`;
  * `utm-postfix-connrate.conf`;
  * `utm-postscreen-prgrt.conf`;
  * `utm-reverse-proxy.conf`;
  * `utm-roundcube.conf`;
  * `utm-smtp.conf`;
  * `utm-ssh.conf`;
  * `utm-two-factor-codes.conf`;
  * `utm-vpn-authd.conf`;
  * `utm-vpn-pppoe-authd.conf`;
  * `utm-web-interface.conf`;
  * `utm-wireguard-backend.conf`.
* `NOTICE [utm-web-interface] Ban 192.168.100.17` - факт блокировки или разблокировки IP-адреса, где:
  * `Ban` - факт блокировки;
  * `Unban` - факт разблокировки.

</details>

<details>

<summary>SSO-аутентификация</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:11:40+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721304700 Severity=Notice DeviceProcessName=ideco-web-authd msg=Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'web'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
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
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'log'` - тип авторизации через журнал безопасности AD.

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:26:34+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721305594 Severity=Notice DeviceProcessName=ideco-web-authd msg=User 'Sanek' has been successfully authorized in web interface from IP '192.168.205.254'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `Sanek` - логин пользователя;
* `192.168.205.254` - IP-адрес пользователя;

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:29:18+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721305758 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'ip'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'ip'` - тип авторизации по IP.

</details>

<details>
<summary>Авторизация по MAC</summary>

{% code overflow="wrap" %}
```
2024-07-18T17:32:26+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721305946 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'mac'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'mac'` - тип авторизации по MAC.

</details>

<details>
<summary>Авторизация по подсети</summary>

{% code overflow="wrap" %}
```
2024-07-18T20:52:27+05:00 Ideco-NGFW CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1721317947 Severity=Notice DeviceProcessName=ideco-auth-backend msg=Subnet 192.168.205.0/24 is authorized as user 'Sanek'. Connection made from None, type 'net'.
```
{% endcode %}

* `deviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `192.168.205.0/24` - подсеть, по которой происходит авторизация;
* `Sanek` - логин пользователя;
* `type 'net'` - тип авторизации по подсети.


</details>

<details>

<summary>Подключение по VPN</summary>

{% code overflow="wrap" %}
```
2024-04-02T14:49:34+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712051374 Severity=Notice DeviceProcessName=ideco-vpn-authd msg=Start vpn authorization ('user',  '192.168.100.17',  'pptp').
2024-04-02T14:49:34+05:00 ideco-ngfw CEF:0|Ideco|NGFW|17.0|0|syslog|0|deviceReceiptTime=1712051374 Severity=Notice DeviceProcessName=ideco-vpn-authd msg=Subnet 10.128.240.8/32 is authorized as user 'user'. Connection made from '192.168.100.17',  type 'pptp'.
```
{% endcode %}

* `DeviceReceiptTime` - время события в системе NGFW, может не совпадать с временем получения события по Syslog;
* `Severity` - важность события (Emergency, Alert', Critical, Error, Warning, Notice, Informational, Debug);
* `DeviceProcessName` - название службы NGFW (unit);
* `Start vpn authorization ('user',  '192.168.100.17',  'pptp')` - факт запроса на авторизацию с информацией о запрашиваемом подключении, где:
  *  `user` - логин пользователя;
  *  `192.168.100.17` - IP-адрес, откуда установлено подключение;
  *  `pptp` - протокол.
* `Subnet 10.128.240.8/32 is authorized as user 'user'` - факт успешной авторизации с локальным IP-адресом.

</details>

### Формат Syslog

<details>
<summary>Предотвращение вторжений</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Dec 14 15:48:38		daemon	warning		timestamp:2022-12-14 10:48:34.808465+00:00,flow_id:1189034483406353,in_iface:seq:Leth1:3:m,sensor_name:suricata_debug,event_type:alert,src_ip:192.168.100.11,src_port:61790,src_country:,src_country_code:,src_session_uuid:7100d1c8-017f-4cbf-8b78-482839300211,src_user_id:2,src_user_name:a.istomina,dest_ip:192.168.100.2,dest_port:53,dest_country:,dest_country_code:,dest_session_uuid:,dest_user_id:-1,dest_user_name:,proto:UDP,alert.signature_id:1003892,alert.signature:Windows Telemetry,alert.category:Telemetry Windows,alert.severity:3,alert.gid:1,alert.action:blocked,http.hostname:,http.url:,http.http_user_agent:,flow.pkts_toserver:1,flow.pkts_toclient:0,flow.bytes_toserver:73,flow.bytes_toclient:0,flow.start:2022-12-14 10:48:34.808465+00:00,flow.end:2022-12-14 10:48:35.580143+00:00,flow.age:0,flow.state:,flow.reason:,flow.alerted:0,tcp.tcp_flags:,tcp.tcp_flags_ts:,tcp.tcp_flags_tc:,tcp.cwr:0,tcp.ecn:0,tcp.urg:0,tcp.ack:0,tcp.psh:0,tcp.rst:0,tcp.syn:0,tcp.fin:0,tcp.state:
```
{% endcode %}

где:
* `192.168.100.2` - IP-адрес NGFW отправителя;
* `Dec 14 15:48:38` - время получения события по Syslog;	
* `timestamp: 2022-12-14 10:48:34.808465+00:00` - время события в системе предотвращения вторжений, может не совпадать с временем получения события по Syslog;
* `flow_id: 1189034483406353` - внутренний идентификатор системы предотвращения вторжений flow (сессии);
* `in_iface: seq:Leth1:3:m` - содержит идентификатор входящего интерфейса;
* `sensor_name: suricata_debug` - имя экземпляра системы предотвращения вторжений;
* `event_type: alert` - тип события;
* `src_ip: 192.168.100.11` - IP-адрес источника;
* `src_port: 61790` - порт источника;
* `src_country:` - название местоположения источника;
* `src_country_code:` - ISO-код страны источника;
* `src_session_uuid: 7100d1c8-017f-4cbf-8b78-482839300211` - внутренний идентификатор сессии Ideco NGFW источника;
* `src_user_id: 2` - идентификатор пользователя источника;
* `src_user_name: a.istomina`- имя пользователя источника;
* `dest_ip: 192.168.100.2` - IP-адрес назначения;
* `dest_port: 53` - порт назначения;
* `dest_country:` - название местоположения назначения;
* `dest_country_code:` - ISO-код страны назначения;
* `dest_session_uuid:` - внутренний идентификатор сессии Ideco NGFW назначения;
* `dest_user_id: -1` - идентификатор пользователя назначения;
* `dest_user_name:` - имя пользователя назначения;
* `proto: UDP` - протокол;
* `alert.signature_id: 1003892` - ID правила системы предотвращения вторжений;
* `alert.signature: Windows Telemetry` - сообщение из сработавшего правила;
* `alert.category: Telemetry Windows` - описание колонки в веб-интерфейсе События безопасности; \
  Соответствие *alert.category:* -> *alert.signature* описаны в [файле](https://static.ideco.ru/static/alert.category%20-%20alert.signature.pdf).
* `alert.severity: 3` - уровень угрозы, может принимать значения 1, 2, 3 и 256, где 1 - самый высокий уровень угрозы.

Служебные поля результата анализа HTTP-трафика. Заполняются, если в процессе анализа трафика был определен HTTP-протокол:
* `http.hostname:` - идентификатор хоста;
* `http.url:` - url, на который велось обращение;
* `http.http_user_agent:` - информация, идентифицирующая HTTP-клиента.
  
Служебные поля flow (сессии):

* `flow.pkts_toserver :1` - количество пакетов, переданное от клиента к серверу;
* `flow.pkts_toclient: 0` - количество пакетов, переданное от сервера к клиенту;
* `flow.bytes_toserver: 73` - количество байт, переданное от клиента к серверу;
* `flow.bytes_toclient: 0` - количество байт, переданное от сервера к клиенту;
* `flow.start: 2022-12-14 10:48:34.808465+00:00` - начало;
* `flow.end: 2022-12-14 10:48:35.580143+00:00` - окончание;
* `flow.age: 0` - возраст;
* `flow.state:` - текущее состояние;
* `flow.reason:` - запущена ли IPsec в режиме отладки;
* `flow.alerted:` 0 - сгенерировался ли поток alert.

Состояние флага [TCP flow(сессии)](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#%D0%A4%D0%BB%D0%B0%D0%B3%D0%B8_(%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D0%B1%D0%B8%D1%82%D1%8B)): 

* `tcp.tcp_flags:` - значение поля flags в заголовке TCP;
* `tcp.tcp_flags_ts:` -  [timestamp флаги](https://www.atraining.ru/windows-network-tuning/#:~:text=TCP%20Timestamps%20–%20базовая%20низкоуровневая,не%20может%20высчитать%20данные%20значения);
* `tcp.tcp_flags_tc:` - [флаг Truncated response](https://www.rfc-editor.org/rfc/rfc5966);
* `tcp.cwr: 0` - флаг TCP-пакета, информирующий отправителя, что получен пакет с установленным флагом ECE (Подробнее в [RFC-3186](https://datatracker.ietf.org/doc/html/rfc3168));
* `tcp.ecn: 0` - флаг TCP-пакета, информирующий получателя, что узел способен на явное уведомление  о перегрузке сети;
* `tcp.urg: 0` - флаг TCP-пакета, указывающий важность пакета;
* `tcp.ack: 0` - флаг TCP-пакета, указывающий, что пакет получен;
* `tcp.psh: 0` - флаг TCP-пакета, информирующий получателя, что все данные переданы и можно передать их приложению;
* `tcp.rst: 0` - флаг TCP-пакета, указывающий, что соединение завершено в аварийном режиме;
* `tcp.syn: 0` - флаг TCP-пакета, отвечающий за установку соединения;
* `tcp.fin: 0` - флаг TCP-пакета, указывающий на завершение соединения в штатном порядке;
* `tcp.state:` - [состояния сеанса TCP](https://ru.wikipedia.org/wiki/Transmission_Control_Protocol#Состояния_сеанса_TCP).

</details>

<details>

<summary>Файрвол</summary>

{% code overflow="wrap" %}
```
ноя 24 09:36:27 ideco-ngfw ideco-nflog[691]: UDP      src 192.168.100.12   sport 137   dst 40.125.122.151   dport 137   table FWD  rule  1    action accept
```
{% endcode %}

* `UDP` - протокол, принимает значения UDP, TCP, ICMP, GRE, ESP и AH;
* `src` - IP-адрес источника;
* `dst` - IP-адрес назначения;
* `sport` - порт источника для UDP и TCP;
* `dport` - порт назначения для UDP и TCP;
* `table` - таблица правил, в которой произошло логирование;
* `rule` - ID правила из таблицы *rule*;
* `action` - действие, которое произошло.

</details>

<details>

<summary>Контроль приложений</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:00:15	1	user	err		2023-01-12T11:00:14+05:00 ideco-ngfw app-control 2027 - - (flow_info_rules_was_checked) 192.168.100.11:52514 -> 192.168.100.2:53 [Amazon] = 'DROP'. 
```
{% endcode %}

* `2027` - идентификатор процесса;
* `192.168.100.11:52514` - IP-адрес источника;
* `192.168.100.2:53 [Amazon] = 'DROP'` - результат анализа трафика, где  `[Amazon]` - название приложения, к которому был применен результат. [Список всех приложений](https://static.ideco.ru/static/app_control.pdf).

</details>

<details>

<summary>Контент-фильтр</summary>

Просмотр логов доступен в веб-интерфейсе в разделе **Мониторинг -> Журналы**. Название служб для фильтрации: ideco-content-filter-backend и squid.

Пример блокировки ресурса:

{% code overflow="wrap" %}
```
192.168.101.130    Mar 31 14:56:57    1    daemon    info        2023-03-31T14:56:56+05:00 ideco-ngfw squid 5950 - - 192.168.101.131 - - [31/Mar/2023:14:56:56 +0500] "GET https://www.igromania.ru/? HTTP/1.1" 403 7455 "https://yandex.ru/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0" TCP_DENIED:HIER_NONE "Custom deny 8 Игры extended.id.21 group.id.1 " 
```
{% endcode %}

* `5950` - идентификатор процесса;
* `192.168.101.131` - IP-адрес пользователя;
* `[31/Mar/2023:14:56:56 +0500] "GET https://www.igromania.ru/? HTTP/1.1`:
  * `[31/Mar/2023:14:56:56 +0500]` - дата/время события блокировки;
  * `GET` - метод;
  * `https://www.igromania.ru/?` - URL заблокированного ресурса;
  * `HTTP/1.1` - протокол.
* `403` - код состояния HTTP;
* `7455` - передано байт (в ответ, включая HTTP заголовок);
* `https://yandex.ru/` - [HTTP referer](https://ru.wikipedia.org/wiki/HTTP_referer);
* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0` - цифровой отпечаток браузера; 
* `TCP_DENIED:HIER_NONE` - техническое сообщение от [squid](http://wiki.squid-cache.org/SquidFaq/SquidLogs#Squid_result_codes);
* `Custom deny 8 Игры extended.id.21 group.id.1`:
  * `Custom deny 8 Игры` - описание и номер правила блокировки;
  * `extended.id.21` - категория сайта;
  * `group.id.1` - значение поля **Применяется для** в сработавшем правиле.

</details>

<details>

<summary>Аутентификация через веб-интерфейс</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:02:15	1	daemon	info		2023-01-12T11:02:14+05:00 ideco-ngfw fail2ban.filter 779 - - INFO [utm-web-interface] Found 192.168.100.1 - 2023-01-12 11:02:14 
192.168.100.2	Jan 12 11:02:36	1	daemon	notice		2023-01-12T11:02:35+05:00 ideco-ngfw fail2ban.actions 779 - - NOTICE [utm-web-interface] Ban 192.168.100.1 

```
{% endcode %}

* `info` или `notice` - приоритет сообщения в логах в виде информационного сообщения или уведомления;
* `779` - идентификатор процесса;
* `INFO [utm-web-interface] Found 192.168.100.1 - 2023-01-12 11:02:14` - факт обнаружения правил безопасности с указанием группы правил (`[utm-web-interface]`), IP-адреса и даты/времени. Список групп правил: 
  * `utm-dovecot`;
  * `utm-postfix-connrate.conf`;
  * `utm-postscreen-prgrt.conf`; 
  * `utm-reverse-proxy.conf`;
  * `utm-roundcube.conf`;
  * `utm-smtp.conf`;
  * `utm-ssh.conf`;
  * `utm-two-factor-codes.conf`;
  * `utm-vpn-authd.conf`;
  * `utm-vpn-pppoe-authd.conf`;
  * `utm-web-interface.conf`;
  * `utm-wireguard-backend.conf`.
* `NOTICE [utm-web-interface] Ban 192.168.100.1` - факт блокировки или разблокировки IP-адреса, где:
  * `Ban` - факт блокировки;
  * `Unban` - факт разблокировки.

</details>

<details>

<summary>Подключение по VPN</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:10:06	1	local0	info		2023-01-12T11:10:05+05:00 ideco-ngfw ideco-vpn-authd 1356 - - Start vpn authorization ('user_1', '192.168.100.11', 'pptp'). 
192.168.100.2	Jan 12 11:10:06	1	local0	info		2023-01-12T11:10:05+05:00 ideco-ngfw ideco-vpn-authd 1356 - - Subnet 10.128.187.17/32 is authorized as user 'user_1'. Connection made from '192.168.100.11', type 'pptp'.
```
{% endcode %}

* `1356` - идентификатор процесса;
* `Start vpn authorization('user_1', '192.168.100.11', 'pptp')` - факт запроса на авторизацию с информацией о запрашиваемом подключении, где:
  *  `user_1` - логин пользователя; 
  *  `192.168.100.11` - IP-адрес, откуда установлено подключение;
  *  `pptp` - протокол.
* `Subnet 10.128.187.17/32` - факт успешной авторизации с локальным IP-адресом.

</details>

<details>
<summary>Веб-авторизация</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:20:06	1	local0	info		2023-01-12T11:20:05+05:00 ideco-ngfw ideco-web-authd 1665 - - Subnet 192.168.100.10/32 is authorized as user 'user'. Connection made from None, type 'web'
```
{% endcode %}

* `1665` - идентификатор процесса;
* `192.168.100.10/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'web'` - тип авторизации веб.

</details>

<details>
<summary>SSO-аутентификация</summary>

{% code overflow="wrap" %}
```
2024-07-18T16:59:55+05:00 Ideco-NGFW ideco-web-authd - - - Subnet 192.168.205.254/32 is authorized as user 'Sanek'. Connection made from None, type 'web'.
```
{% endcode %}

* `Ideco-NGFW` - название сервера;
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

* `Ideco-NGFW` - название сервера;
* `192.168.205.254/32` - IP-адрес пользователя;
* `Sanek` - логин пользователя;
* `type 'log'` - тип авторизации через журнал безопасности AD.

</details>

<details>
<summary>Авторизация по IP</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:20:06	1	local0	info		2023-01-12T11:20:05+05:00 ideco-ngfw ideco-web-authd 1665 - - Subnet 192.168.100.49/32 is authorized as user 'user-1717140295.828113'. Connection made from None, type 'ip_permanent'.
```
{% endcode %}

* `1665` - идентификатор процесса;
* `192.168.100.49/32` - IP-адрес пользователя;
* `'user-1717140295.828113'` - логин пользователя;
* `type 'ip_permanent'` - тип авторизации IP с постоянной авторизацией.

</details>

<details>
<summary>Авторизация по MAC</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:20:06	1	local0	info		2023-01-12T11:20:05+05:00 ideco-ngfw ideco-auth-backend 3660 - - Subnet 192.168.100.10/32 is authorized as user 'user'. Connection made from None, type 'mac'.
```
{% endcode %}

* `3660` - идентификатор процесса;
* `192.168.100.10/32` - IP-адрес пользователя;
* `user` - логин пользователя;
* `type 'mac'` - тип авторизации MAC.

</details>

<details>
<summary>Авторизация по подсетям</summary>

{% code overflow="wrap" %}
```
192.168.100.2	Jan 12 11:20:06	1	local0	info		2023-01-12T11:20:05+05:00 ideco-ngfw ideco-auth-backend 3660 - - Subnet 192.168.100.0/24 is authorized as user 'user'. Connection made from None, type 'net'.
```
{% endcode %}

* `3660` - идентификатор процесса;
* `192.168.100.0/24` - подсеть пользователя;
* `user` - логин пользователя;
* `type 'net'` - тип авторизации подсеть.

</details>