---
description: Система обнаружения и предотвращения вторжений
---

# Предотвращение вторжений

{% hint style="info" %}
Система предотвращения вторжений доступна только в **Enterprise версии Ideco UTM** для пользователей с активной подпиской на обновления.

Правила **Предотвращения вторжений**, [Контроля приложений](application-control.md) и [Ограничение скорости](shaper.md) не обрабатывают трафик между локальными сетями и сетями филиалов.
{% endhint %}

**Система предотвращения вторжений** (IDS/IPS, Intrusion detection system / Intrusion prevention system) предназначена для обнаружения, журналирования и предотвращения атак злоумышленников на сервер, интегрированные службы (почта, веб-сайт и др.) и, защищаемую интернет-шлюзом, локальную сеть.

Правила блокировки трафика включают в себя блокирование активности троянских программ, spyware, бот-сетей, клиентов p2p и **торрент-трекеров**, вирусов, сети **TOR** (используемой для обхода правил фильтрации), анонимайзеров и т.д.

Настроить службу можно на вкладке **Правила доступа -> Предотвращение вторжений.**

Передвинув выключатель (слева от названия раздела) вправо или влево можно соответственно включить/выключить службу предотвращения вторжений.

![](/.gitbook/assets/suricata-on-off.gif)

Для добавления правила нажмите кнопку **Добавить** и в поле **Подсеть** добавьте локальные сети, обслуживаемые UTM. Как правило, это сети локальных интерфейсов UTM, а также маршрутизируемые на них сети удаленных сегментов локальной сети вашего предприятия.

{% hint style="info" %}
Ни в коем случае не указывайте сети, принадлежащие внешним сетевым интерфейсам UTM и внешним сетям. Указанные здесь сети участвуют в правилах службы предотвращения вторжения как локальные, характеризуя трафик в/из локальных сетей. Локальный межсегментный трафик не исключается из проверок системы.
{% endhint %}

Опция **Хранить записи журнала** позволяет выбрать время хранения логов системы.

![](/.gitbook/assets/keep-logs.gif)

При использовании системы предотвращения вторжений **не рекомендуется** использовать внутренние DNS-серверы для компьютеров сети, т.к. система анализирует проходящие через нее DNS-запросы и определяет по ним зараженные устройства. В случае использования внутреннего домена AD, рекомендуется на компьютерах указывать DNS-сервер Ideco UTM в качестве единственного DNS-сервера, а в настройках DNS-сервера на UTM указать Forward-зону для локального домена.

## Журнал

В подразделе **Журнал** можно просмотреть логи предупреждения системы предотвращения вторжений.

![](/.gitbook/assets/suricata-logi.png)

* Поле **Результат анализа** отображает действие системы, `Blocked` — пакет блокирован, любая другая информация в этом поле означает `Allowed`, информирование.
* В поле **Уровень угрозы** могут отображаться следующие значения:
  * 1 - <mark style="background-color:red;">критично</mark>;
  * 2- <mark style="background-color:orange;">опасно</mark>;
  * 3 - <mark style="background-color:yellow;">предупреждение</mark>;
  * 4 - не распознано;
  * 255 - не классифицировано.

При наведении на колонку **ID** в строке с правилом, появится кнопка **Добавить в исключения**, при нажатии на которую сигнатура будет добавлена в  исключения.

Скачайте CSV-файл с логами системы предотвращения вторжений за определенный период по соответствующей кнопке. 

<details>

<summary>Действия для корректного отображения информации из CSV-файла в MS Excel</summary>

1\. Откройте CSV-файл в MS Excel и выделите весь первый столбец.

2\. Перейдите во вкладку **Данные** и нажмите кнопку **Текст по столбцам**. 

3\. В открывшемся окне выберите **с разделителями** и нажмите **Далее**:

![](/.gitbook/assets/suricata.png)

4\. В блоке **Символом-разделителем является:**  выберите **запятая** и нажмите **Далее**:

![](/.gitbook/assets/suricata2.png)

5\. В блоке **Формат данных столбца** выберите **Текстовый** и нажмите **Готово**:

![](/.gitbook/assets/suricata3.png)

</details>

## Правила

На вкладке **Правила** доступны для просмотра и включения/отключения группы правил системы предотвращения вторжений. При включении/отключении группы правил настройки применяются мгновенно без необходимости перезапускать службу.


<details>
 
<summary>История изменений правил</summary>
 
**26.10.2022:**
* Удалена отдельная категория правил **Список НКЦКИ** \
  Источник данных атакующих НКЦКИ остается в составе баз, являясь частью *Черного списка IP-адресов*
 
**21.10.2022:**
* Удалена группа **Активные ботнеты** \   Актуальные угрозы блокируются с помощью *Чёрных списков IP-адресов*
 
</details> 

## Исключения

Вы можете отключить определенные правила системы предотвращения вторжений, в случае их ложных срабатываний или по другим причинам.

![](/.gitbook/assets/suricata-except.png)

На вкладке **Исключения** можно добавить ID правила (его номер, см. пример анализа логов ниже).

{% hint style="info" %}
Внимание! Со временем при обновлении баз ID правил могут меняться.
{% endhint %}

<details>

<summary>Пример анализа логов</summary>

Предупреждение системы предотвращения вторжений:

![](/.gitbook/assets/ex2suricata.png)

Таким образом, на вкладке **Правила** можно открыть найденную группу и в ней найти сработавшее правило по его ID:

`drop dns $HOME_NET any -> any any (msg:"ET DNS Query for .cc TLD"; dns.query; content:".cc"; endswith; fast_pattern; classtype:bad-unknown; sid:2027758; rev:5; metadata:affected_product Any, attack_target Client_Endpoint, created_at 2019_07_26, deployment Perimeter, former_category DNS, signature_severity Minor, updated_at 2020_09_17;)`

{% hint style="info" %}
Можно проанализировать IP-адрес, с которым была попытка подозрительного соединения, через [whois](https://www.nic.ru/whois/).
{% endhint %}

</details>

<details>

<summary>Как исключить узел из обработки системой IDS/IPS</summary>

**Задача:** Необходимо исключить из обработки узел `192.168.154.7`.

**Решение:**

1. В файл `/var/opt/ideco/suricata-backend/custom.rules` необходимо добавить следующую строку: `pass ip 192.168.154.7 any <> any any (sid:1;)`. Для редактирования этого файла перейдите в раздел **Терминал** и введите команду `mcedit /var/opt/ideco/suricata-backend/custom.rules`.
2. Затем в разделе **Терминал** выполнить команду `systemctl restart ideco-suricata-backend`.

{% hint style="warning" %}
При создании нескольких ручных правил **обязательно** изменяйте ID-правила (sid:2;), иначе система предотвращения вторжений прекратит работу из-за наличия нескольких правил с одним sid.
{% endhint %}

</details>

<details>

<summary>Технические требования</summary>

Для работы системы предотвращения вторжений требуются значительные вычислительные ресурсы. Предпочтительным являются многоядерные (4 и более ядер) процессоры. Минимальное количество оперативной памяти для использования системы: 8 Гб.

После включения системы желательно проконтролировать, что мощности вашего процессора достаточно для проверки следующего через шлюз трафика.

В разделе **Мониторинг -> Графики загруженности**. Параметр средняя загрузка (за 1, 5 и 15 минут). Подробнее о [Load Average](https://habr.com/ru/company/vk/blog/335326/).

</details>