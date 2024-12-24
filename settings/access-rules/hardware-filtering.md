# Аппаратная фильтрация

На вкладке можно настроить пакетную фильтрацию трафика на основе сетевых и физических адресов отправителей и (или) получателей. Пакеты будут блокироваться на аппаратном уровне без участия центрального процессора, c использованием вычислительных мощностей сетевой карты.

В Ideco NGFW блокировка будет происходить в соответствии с выбранным режимом фильтрации. Одновременно может работать фильтрация по MAC-адресу источника или один из видов фильтрации по IP.

Созданные на вкладке правила применяются сразу ко всем поддерживаемым сетевым адаптерам, найденным в системе.

## Список поддерживаемых сетевых карт

| PCI-идентификатор | Модель адаптера |
|-------------------|-----------------|
| 0x8086:0x0CF8 | Ethernet Controller X710 Intel(R) FPGA Programmable Acceleration Card N3000 for Networking |
| 0x8086:0x0D58 | Ethernet Controller XXV710 Intel(R) FPGA Programmable Acceleration Card N3000 for Networking |
| 0x8086:0x1572 | Ethernet Controller X710 for 10GbE SFP+ |
| 0x8086:0x1574 | Ethernet Controller XL710 Emulation |
| 0x8086:0x1580 | Ethernet Controller XL710 for 40GbE backplane |
| 0x8086:0x1581 | Ethernet Controller X710 for 10GbE backplane |
| 0x8086:0x1583 | Ethernet Controller XL710 for 40GbE QSFP+ |
| 0x8086:0x1584 | Ethernet Controller XL710 for 40GbE QSFP+ |
| 0x8086:0x1585 | Ethernet Controller X710 for 10GbE QSFP+ |
| 0x8086:0x1586 | Ethernet Controller X710 for 10GBASE-T |
| 0x8086:0x1587 | Ethernet Controller XL710 for 20GbE backplane |
| 0x8086:0x1588 | Ethernet Controller XL710 for 20GbE backplane |
| 0x8086:0x158A | Ethernet Controller XXV710 for 25GbE backplane |
| 0x8086:0x158B | Ethernet Controller XXV710 for 25GbE SFP28 |
| 0x8086:0x15FF | Ethernet Controller X710 for 10GBASE-T |
| 0x8086:0x104F | Ethernet Controller X710 for 10 Gigabit backplane |
| 0x8086:0x104E | Ethernet Controller X710 for 10 Gigabit SFP+ |
| 0x8086:0x0DD2 | Ethernet Network Adapter I710 |

## Создание правил

{% hint style="info" %}
Администратор может создать не более 2500 правил каждого типа фильтрации.
{% endhint %}

Созданные правила отображаются в таблице в зависимости от выбранного режима фильтрации:

![](/.gitbook/assets/hardware-filtering1.png)

Чтобы создать правило определенного типа, выполните действия:

1\. Выберите режим фильтрации, нажмав на кнопку в левом верхнем углу:

![](/.gitbook/assets/hardware-filtering.png)

* По MAC-адресу источника;
* По IP-адресу источника;
* По IP-адресу назначения;
* По IP-адресу источника и назначения.

2\. Нажмите **Добавить** и заполните поля:

<details>
<summary>Фильтрация по MAC-адресу источника</summary>

![](/.gitbook/assets/hardware-filtering2.png)

* **MAC-адрес** - введите физический адрес источника трафика;
* **Протокол** - введите [номер](https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml) протокола сетевого уровня. **Не указывайте протокол IPv4** (значение 2048), для фильтрации  на сетевом уровне используйте правила *По IP-адресу источника*, *По IP-адресу назначения*, *По IP-адресу источника и назначения*;
* **Коментарий** - поле необязательное.

</details>

<details>
<summary>Фильтрация по IP-адресу источника</summary>

![](/.gitbook/assets/hardware-filtering3.png)

* **IP-адрес источника** - введите IP-адрес источника трафика;
* **Коментарий** - поле необязательное.

</details>

<details>
<summary>Фильтрация по IP-адресу назначения</summary>

![](/.gitbook/assets/hardware-filtering4.png)

* IP-адрес назначения - введите IP-адрес назначения трафика;
* Коментарий - поле необязательное.

</details>

<details>
<summary>Фильтрация по IP-адресу источника и назначения</summary>

![](/.gitbook/assets/hardware-filtering5.png)

* **IP-адрес источника** - введите IP-адрес источника трафика;
* **IP-адрес назначения** - введите IP-адрес назначения трафика;
* **Коментарий** - поле необязательное.

</details>

3\. Нажмите **Добавить**.

4\. Включите правило или оставьте его выключенным.

{% hint style="info" %}
Отключить аппаратную фильтрацию можно, выключив опцию **Файрвол** в соответствующем разделе.
{% endhint %}