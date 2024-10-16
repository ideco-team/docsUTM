---
title: Предотвращение вторжений
description: Система обнаружения и предотвращения вторжений
published: true
date: '2021-07-14T09:36:12.186Z'
tags: ids_ips
editor: markdown
dateCreated: '2021-04-02T07:24:39.377Z'
---

# Предотвращение вторжений

{% hint style="info" %}
Система предотвращения вторжений доступна только в **Enterprise версии Ideco UTM** для пользователей с активной подпиской на обновления.&#x20;
{% endhint %}

**Система предотвращения вторжений** (IDS/IPS, Intrusion detection system / Intrusion prevention system) предназначена для обнаружения, журналирования и предотвращения атак злоумышленников на сервер, интегрированные службы (почта, веб-сайт и др.) и, защищаемую интернет-шлюзом, локальную сеть.

Правила блокировки трафика включают в себя блокирование активности троянских программ, spyware, бот-сетей, клиентов p2p и **торрент-трекеров**, вирусов, сети **TOR** (используемой для обхода правил фильтрации), анонимайзеров и т.д.

Настроить службу можно на вкладке **Правила доступа -> Предотвращение вторжений.**

Передвинув выключатель (слева от названия раздела) вправо или влево можно соответственно включить/выключить службу предотвращения вторжений.

![](../../.gitbook/assets/suricata-on-off.gif)

Для добавления правила нажмите кнопку **Добавить** и в поле **Подсеть** добавьте локальные сети, обслуживаемые UTM. Как правило, это сети локальных интерфейсов UTM, а также маршрутизируемые на них сети удаленных сегментов локальной сети вашего предприятия.&#x20;

{% hint style="info" %}
Ни в коем случае не указывайте сети, принадлежащие внешним сетевым интерфейсам UTM и внешним сетям. Указанные здесь сети участвуют в правилах службы предотвращения вторжения как локальные, характеризуя трафик в/из локальных сетей. Локальный межсегментный трафик не исключается из проверок системы.
{% endhint %}

Опция **Хранить записи журнала** позволяет выбрать время хранения логов системы.

При использовании системы предотвращения вторжений **не рекомендуется** использовать внутренние DNS-серверы для компьютеров сети, т.к. система анализирует проходящие через нее DNS-запросы и определяет по ним зараженные устройства. В случае использования внутреннего домена AD, рекомендуется на компьютерах указывать DNS-сервер Ideco UTM в качестве единственного DNS-сервера, а в настройках DNS-сервера на UTM указать Forward-зону для локального домена.

## Журнал

В подразделе **Журнал** можно просмотреть последние 100 строк логов предупреждения системы предотвращения вторжений.

![](../../.gitbook/assets/suricata\_journal.png)

Полные логи системы находятся на сервере в каталоге: `/var/log/suricata/fast.log`:

* команда `journalctl -u ideco-suricata`введенная в разделе **Терминал** выведет лог работы службы;
* команда `less /var/log/suricata/fast.log` введенная в разделе **Терминал** выведет лог срабатывания правил.

## Правила

На вкладке **Правила** доступны для просмотра и включения/отключения группы правил системы предотвращения вторжений. При включении/отключении группы правил настройки применяются мгновенно без необходимости перезапускать службу.

## Исключения

Есть возможность отключить определенные правила системы предотвращения вторжений, в случае их ложных срабатываний или по другим причинам.

![](../../.gitbook/assets/suricata-except.png)

На вкладке **Исключения** можно добавить ID правила (его номер, см. пример анализа логов ниже).

{% hint style="info" %}
Внимание! Со временем при обновлении баз ID правил могут меняться.&#x20;
{% endhint %}

## Пример анализа логов

### Пример 1

Предупреждение системы предотвращения вторжений:

`04/04/2017-19:31:14.341627 [Drop] [**] [1:2008581:3] ET P2P BitTorrent DHT ping request [**] [Classification: Запросы на скомпрометированные ресурсы] [Priority: 1] {UDP} 10.130.0.11:20417 -> 88.81.59.137:61024`

**Расшифровка полей:**

* `04/04/2017-19:31:14.341627` — дата и время события.
* `[Drop]` — действие системы, `Drop` — пакет блокирован, любая другая информация в этом поле означает `Alert`, информирование.
* `[1:2008581:3]` — ID правила в группе (ID содержится между знаками `:`). В случае, если правило необходимо добавить в исключения, нужно добавить туда номер `2008581`.
* `[Classification: Запросы на скомпрометированные ресурсы]` — трафик категоризирован правилами группы "Запросы на скомпрометированные ресурсы"

Таким образом, на вкладке **Правила** можно открыть найденную группу и в ней найти сработавшее правило по его ID: `drop udp $HOME_NET any -> $EXTERNAL_NET any (msg:"ET P2P BitTorrent DHT ping request"; content:"d1|3a|ad2|3a|id20|3a|"; depth:12; nocase; threshold: type both, count 1, seconds 300, track by_src; reference:url,wiki.theory.org/BitTorrentDraftDHTProtocol; reference:url,doc.emergingthreats.net/bin/view/Main/2008581; classtype:policy-violation; sid:2008581; rev:3;)`

По ссылке (после url, в данном примере: doc.emergingthreats.net/bin/view/Main/2001891) можно получить дополнительную информацию о сработавшем правиле.

`10.130.0.11:20417 -> 88.81.59.137:61024` — IP-адрес, с которого (в локальной сети), на который была попытка соединения.

{% hint style="info" %}
Можно проанализировать IP-адрес, с которым была попытка подозрительного соединения, через [whois](https://www.nic.ru/whois/).
{% endhint %}

### Пример 2

Предупреждение системы предотвращения вторжений:

`07/03/2015-14:52:07.654757 [Drop] [**] [1:2403302:1942] ET CINS Active Threat Intelligence Poor Reputation IP group 3 [**] [Classification: Misc Attack] [Priority: 2] {UDP} 24.43.1.206:10980 -> 192.168.10.14:32346`

Для более подробного анализа логов с IP компьютера 192.168.10.14 в консоли сервера выполняем команду:

`grep "10.80.1.13:" /var/log/suricata/fast.log`

Получаем достаточно большое количество строк с блокировками соединений с IP-адресами, классифицируемыми разными категориями опасности.

В результате анализа ПО на компьютере была обнаружена и удалена adware-программа, на которую не реагировал локально установленный антивирус.

## Как исключить узел из обработки системой IDS/IPS

**Задача:** Необходимо исключить из обработки узел `192.168.154.7`.

**Решение:**&#x20;

1. В файл `/var/opt/ideco/suricata-backend/custom.rules` необходимо добавить следующую строку: `pass ip 192.168.154.7 any <> any any (sid:1;)`. Для редактирования этого файла перейдите в раздел **Терминал** и введите команду `mcedit /var/opt/ideco/suricata-backend/custom.rules`.&#x20;
2. Затем в разделе **Терминал** выполнить команду `systemctl restart ideco-suricata-backend`.

{% hint style="warning" %}
При создании нескольких ручных правил **обязательно** изменяйте ID-правила (sid:2;), иначе система предотвращения вторжений прекратит работу из-за наличия нескольких правил с одним sid.
{% endhint %}

## Технические требования

Для работы системы предотвращения вторжений требуются значительные вычислительные ресурсы. Предпочтительным являются многоядерные (4 и более ядер) процессоры. Минимальное количество оперативной памяти для использования системы: 8 Гб.

После включения системы желательно проконтролировать, что мощности вашего процессора достаточно для проверки следующего через шлюз трафика.

В разделе **Мониторинг -> Графики загруженности**. Параметр средняя загрузка (за 1, 5 и 15 минут) не должен быть больше, чем количество физических ядер установленного процессора.