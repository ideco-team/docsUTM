# Версия Ideco UTM 12.X

## **IDECO UTM 12.0 СБОРКА 260 **

Обязательно ознакомьтесь с [примечаниями] к релизу.

#### Новые возможности

* Новая платформа на базе ядра Linux 5.15
* [Добавлена фильтрация баннерной рекламы на уровне DNS](../settings/services/nextdns.md). 
* [Динамическая маршрутизация на базе OSPF](../settings/services/ospf.md). 
* Возможность отката на прошлую версию после обновления в локальном меню.
* Новая версия модуля [Контроль приложений](../settings/access-rules/application-control.md).
* Переработан и улучшен раздел авторизации пользоватей по [IP-адресу/MAC-адресу](../settings/users/authorization/IP-and-MAC-authorization/README.md).
* Привязка [IP к MAC](../settings/services/dhcp.md#nastroika-dhcp-servera-s-privyazkoi-ip-k-mac) в разделе DHCP.
* Переработан [раздел с сертификатами](../settings/services/certificates/README.md). 
* [Веб-интерфейс Антиспама Касперского](../settings/access-rules/antivirus.md). В функционал Ideco UTM 12.0 добавлена возможность запускать и веб-интерфейс для Антиспама.
* Добавлена возможность отключать созданные правила в [Исключениях прокси](../settings/services/proxy/exclusions.md).
  
  
#### Исправления и изменения

* Для клиентов, подключенных к Ideco UTM по IKEv2/IPsec, все маршруты передаются автоматически.
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) обрабатывают поступающий по VPN трафик из внешней сети.
* При обновлении Ideco UTM на версию 12.0 информация из [Журнала событий](../settings/access-rules/ips.md#zhurnal) не переносится.
* Исходящее подключение IPSec к Mikrotik версии ниже 6.45 по сертификатам работать не будет. При этом, подключения, созданные в версии 11.х, продолжат работу.
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) не обрабатывают трафик между локальными сетями и сетями филиалов. 
***