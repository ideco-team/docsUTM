# Версия Ideco UTM 12.X

## **IDECO UTM 12.0 СБОРКА 260**


#### Новые возможности

* Новая платформа на базе ядра Linux 5.15.
* Добавлена возможность создать правило авторизации только по [MAC-адресу](/settings/users/authorization/IP-and-MAC-authorization/mac.md).
* Добавлена [фильтрация баннерной рекламы](../settings/services/nextdns.md) на уровне DNS. 
* Добавлена динамическая маршрутизация на базе [OSPF](../settings/services/ospf.md). 
* Добавлена возможность отката на прошлую версию после обновления.
* Добавлено резервирование [IP к MAC](../settings/services/dhcp.md#nastroika-dhcp-servera-s-privyazkoi-ip-k-mac) в разделе DHCP.
* Добавлена возможность запускать веб-интерфейс для [Антиспама](../settings/access-rules/antivirus.md).
* Добавлена возможность отключать созданные правила в [Исключениях прокси](../settings/services/proxy/exclusions.md).
  
  
#### Исправления и изменения

* Для клиентов, подключенных к Ideco UTM по IKEv2/IPsec, маршруты передаются автоматически.
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) обрабатывают поступающий по VPN трафик из внешней сети.
* При обновлении Ideco UTM на версию 12.0 информация из раздела Предотвращение вторжений -> [Журнал](../settings/access-rules/ips.md#zhurnal) теряется.
* Исходящее подключение IPSec к Mikrotik версии ниже 6.46 по сертификатам работать не будет. При этом, подключения, созданные в версии 11.х, продолжат работу.
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) перестали обрабатывать трафик между локальными сетями и сетями филиалов. 
* Переработан [раздел с сертификатами](../settings/services/certificates/README.md). 
* Переработан и улучшен раздел авторизации пользоватей по [IP-адресу/MAC-адресу](../settings/users/authorization/IP-and-MAC-authorization/README.md).
* Новая версия модуля [Контроль приложений](../settings/access-rules/application-control.md).
***