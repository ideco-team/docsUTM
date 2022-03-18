# Версия Ideco UTM 12.X

## **IDECO UTM 12.0 СБОРКА 260 (25.02.2022)**

Обязательно ознакомьтесь с [примечаниями](https://disk.yandex.ru/i/i3qMwQj8YYC5QA) к релизу.

#### Новые возможности

* [Интеграция с сервисом NextDNS](../settings/services/nextdns.md). 
* [Динамическая маршрутизация на базе OSPF](../settings/services/ospf.md). 
* Добавлена возможность возврата на предыдущую версию после обновления в локальном меню.
* Для клиентов, подключенных к Ideco UTM по IKEv2/IPsec, все маршруты передаются автоматически.
* Переработан и улучшен раздел авторизации пользоватей по [IP-адресу/MAC-адресу](../settings/users/authorization/IP-and-MAC-authorization/README.md).
* Добавлена привязка [IP к MAC](../settings/services/dhcp.md#nastroika-dhcp-servera-s-privyazkoi-ip-k-mac) в разделе DHCP.
* Переработан [раздел с сертификатами](../settings/services/certificates/README.md). 
* [Веб-интерфейс Антиспама Касперского](../settings/access-rules/antivirus.md). В функционал Ideco UTM 12.0 добавлена возможность запускать и веб-интерфейс для Антиспама.
* Добавлена возможность отключать созданные правила в [Исключениях прокси](../settings/services/proxy/exclusions.md).
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) обрабатывают поступающий по VPN трафик из внешней сети.
* При обновлении информация из **Журнала событий** раздела [Предотвращения вторжений](../../docsUTM/settings/access-rules/ips.md) не переносится.
* Обновлено ядро платформы до Linux 5.15.
* Не работает создание **исходящих IPSec-подключений** по сертификатам к MikroTik ниже версии 6.45 из-за невозможности использования в сертификатах современных криптоалгоритмов. Но при обновлении на Ideco UTM 12.0 версию, созданные в Ideco UTM 11.0 версии IPSec-подключения, продолжат работу.
* Правила [Предотвращения вторжений](../settings/access-rules/ips.md), [Контроля приложений](../settings/access-rules/application-control.md) и [Ограничение скорости](../settings/access-rules/shaper.md) не обрабатывают трафик между локальными сетями и сетями филиалов. 
***