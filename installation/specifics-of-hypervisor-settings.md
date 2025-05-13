# Настройка гипервизора

{% hint style="success" %}
Ideco NGFW совместим с указанными гипервизорами:

* Microsoft Hyper-V (2-го поколения).
* VMware (Workstation и ESXi) версии не ниже 6.5.0.
* VirtualBox версии не ниже 7.0.0.
* KVM версии не ниже 1.2.0.
* Proxmox VE.
* Citrix XenServer.
{% endhint %}

**Обязательные условия для работы Ideco NGFW:**

* Тип ОС для создания виртуальной машины: **Linux Fedora 64 bit**.
* Минимальный объем жесткого диска: **150 ГБ**.
* Минимальное количество оперативной памяти: **16 ГБ**.
* Минимальное количество ядер: **4**.
* Видеопамять (VRAM): 16 Мб.
* Включение режима UEFI.
* Отключение опции Secure Boot в UEFI.
* Отключение режима Legacy загрузки (он также может называться CSM).
* Внутренние часы виртуальной машины должны быть настроены на хранение времени в временной зоне UTC.

**Для максимальной производительности рекомендуем:**

* Режим работы кэша виртуального диска: writeback. Хранилище должно гарантировать сохранность данных после завершения команды фиксации кэша.
* Настроить паравиртуализованный источник энтропии (Random Number Generator (RNG)).
* Настроить паравиртуализованные часы и таймер.
* Убедиться, что виртуальные процессоры, использующиеся для виртуальной машины, располагаются на одной физической NUMA-ноде.
* Гипервизор с аппаратной виртуализацией (вложенная виртуализация не требуется).

{% hint style="warning" %}
Если при установке Ideco NGFW появилось окно с текстом **Installation in BIOS mode is not supported**, необходимо проверить включение режима UEFI в настройках.
{% endhint %}

## VMware ESXi 6.7

{% hint style="info" %}
При установке Ideco NGFW на хосты кластера с разными поколениями процессоров укажите в настройках EVC самое старое поколение процессора из хостов, соответствующее минимальным системным требованиям для установки.
{% endhint %}

<details>
<summary>Настройка</summary>

Перед установкой Ideco NGFW:
* Загрузите образ, скачанный с [MY.IDECO](https://my.ideco.ru/), на VMware ESXi. При настройке виртуальной машины потребуется указать его путь.
* Увеличьте размер видеопамяти для виртуальной машины до 16 МБ.
* Используйте виртуальные сетевые адаптеры **vmxnet3**.

1\. Создайте виртуальную машину:

![](/.gitbook/assets/specifics-of-hypervisor-settings4.png)

2\. Укажите **Имя** виртуальной машине и установите остальные настройки как на скриншоте:

 ![](/.gitbook/assets/specifics-of-hypervisor-settings5.png)

3\. Выберите хранилище для виртуальной машины:

![](/.gitbook/assets/specifics-of-hypervisor-settings6.png)

4\. Установите размер оперативной памяти **16ГБ** и размер диска **150ГБ**. После выберите в поле **CD/DVD Drive** Datastore ISO file и укажите путь к загрузочному образу:
   
![](/.gitbook/assets/specifics-of-hypervisor-settings7.png)

5\. Включите **UEFI** на вкладке **VM Options**, выбрав в поле **Firmware** EFI:

![](/.gitbook/assets/specifics-of-hypervisor-settings8.png)

6\. Нажмите **Finish**:

![](/.gitbook/assets/specifics-of-hypervisor-settings9.png)

</details>

## VMware Workstation 17.0

<details>
<summary>Настройка</summary>

Перед установкой Ideco NGFW:
* Увеличьте размер видеопамяти для виртуальной машины до 16 МБ.
* Используйте виртуальные сетевые адаптеры **vmxnet3**.

1\. Создайте виртуальную машину, нажав **Create a New Virtual Machine**:

![](/.gitbook/assets/specifics-of-hypervisor-settings12.png)

2\. Укажите загрузочный ISO-образ:

![](/.gitbook/assets/specifics-of-hypervisor-settings13.png)

3\. Выберите гостевую операционную систему **Linux** и в раскрывающемся списке укажите тип **Fedora 64-bit**:

![](/.gitbook/assets/specifics-of-hypervisor-settings14.png)

4\. Укажите имя виртуальной машины и директорию для создания виртуального диска:

![](/.gitbook/assets/specifics-of-hypervisor-settings15.png)

5\. Укажите размер вирутального жесткого диска **150ГБ**:
   
![](/.gitbook/assets/specifics-of-hypervisor-settings16.png)

6\. Выберите **Customize Hardware** для изменения настроек виртуальной машины:

![](/.gitbook/assets/specifics-of-hypervisor-settings17.png)

7\. Укажите размер виртуальной оперативной памяти **16384МБ**:

![](/.gitbook/assets/specifics-of-hypervisor-settings18.png)

8\. Укажите количество ядер процесса равное 4:

![](/.gitbook/assets/specifics-of-hypervisor-settings19.png)

9\. Выйдите из меню и нажмите **Finish** для окончания настройки:

![](/.gitbook/assets/specifics-of-hypervisor-settings20.png)

10\. Перейдите в окно виртуальной машины и нажмите **Edit virtual machine settings**:

![](/.gitbook/assets/specifics-of-hypervisor-settings21.png)

11\. Перейдите на вкладку **Options**:

![](/.gitbook/assets/specifics-of-hypervisor-settings22.png)

12\. Выберите опцию **Advanced** и установите для параметра Firmware Type значение **UEFI**:

![](/.gitbook/assets/specifics-of-hypervisor-settings23.png)

13\. Нажмите **OK** для завершения настройки виртуальной машины.

</details>

## Citrix XenServer

<details>
<summary>Настройка</summary>

Если xenserver не загружается с установочного образа:

1\. Выполните команду `xe vm-list`. Она отобразит список виртуальных машин на xenserver.

2\. Выберите виртуальную машину с NGFW и запомните ее UUID.

3\. Выполните команду. После этого начнется загрузка с установочного носителя:
``` 
xe vm-param-set uuid=<UUID> HVM-boot-policy=BIOS\ order HVM-boot-params:order=dc
```

</details>

## VirtualBox 7.0.12

<details>
<summary>Настройка</summary>

* По умолчанию при создании виртуальной машины создается 1 сетевая карта с типом подключения **NAT**.

1\. Укажите **Имя** виртуальной машины (ВМ), выберите директорию для ВМ и установите путь до загрузочного образа NGFW. Остальные параметры установите как на скриншоте:

![](/.gitbook/assets/specifics-of-hypervisor-settings24.png)

2\. Установите размер оперативной памяти ВМ (**16 ГБ**) и нажмите **Включить EFI**:
    
![](/.gitbook/assets/specifics-of-hypervisor-settings25.png)

3\. Создайте виртуальный жесткий диск под ВМ (Объем не меньше **150ГБ**):

![](/.gitbook/assets/specifics-of-hypervisor-settings26.png)

4\. Нажмите **Готово**

</details>

## KVM

<details>
<summary>Настройка</summary>

1\. При установке Ideco NGFW выберите тип операционной системы - **Fedora**

2\. На пятом шаге (virtm-manager) установки обязательно включите опцию **Проверить конфигурацию перед установкой** и нажмите кнопку **Готово**.

![](/.gitbook/assets/specifics-of-hypervisor-settings27.png)

3\. Для дисков и сетевых карт измените интерфейс на **virtio.**

4\. Выберите режим кеширования. Если диски имеют формат qcow2 или raw, используйте **writeback**. Если используется другой формат дисков, проконсультируйтесь у своего системного администратора или в нашей технической поддержке.

5\. В появившемся окне на вкладке **Обзор** в поле Firmware выберите пункт **UEFI x86\_64:/usr/share/OVMF/OVMF\_CODE.fd**. Выбор этого пункта включит **UEFI** и выключит опцию **Secure Boot**.

![](/.gitbook/assets/specifics-of-hypervisor-settings28.png)

Если пункта **UEFI x86\_64:/usr/share/OVMF/OVMF\_CODE.fd** нет в списке, доустановите пакет ovmf. В Ubuntu этот пакет устанавливается командой `sudo apt install ovmf`.
</details>

## Proxmox

{% hint style="success" %}
Видеоинструкцию по установке Ideco NGFW на Proxmox смотрите по ссылкам:
* [Rutube](https://rutube.ru/video/33b94fd8c7ca7262da0f8f6282d75548/)
* [Youtube](https://youtu.be/ntYvS5Yz6dk?si=DK9VENP46g9DjcPE)
{% endhint %}

<details>
<summary>Настройка</summary>

1\. Нажмите **Создать ВМ**, введите имя машины:

![](/.gitbook/assets/proxmox.png)

2\. В разделе **ОС** выберите хранилище и заполните поля:

![](/.gitbook/assets/proxmox1.png)

* **ISO-образ** - образ с нужной версией NGFW.
* **Гостевая ОС**:
  * **Тип** - Linux.
  * **Версия** - 6.х - 2.0 Kernel.

3\. В разделе **Система** заполните поля:

![](/.gitbook/assets/proxmox2.png)

* **BIOS** - OVMF.
* **Хранилище EFI** - хранилище для UEFI-диска.
* **Предварительная загрузка ключей** - отключите опцию.

4\. В разделе **Диски** укажите нужный размер диска (не меньше 150 ГБ) и выберите хранилище для NGFW:

![](/.gitbook/assets/proxmox3.png)

Проверьте свободное место на диске.

5\. В разделе **Процессор** укажите количество сокетов и ядер (от четырех ядер) и выберите тип, который поддерживает SSE 4.2:

![](/.gitbook/assets/proxmox4.png)

6\. В разделе **Память** укажите объем оперативной памяти (не менее 16 ГБ):

![](/.gitbook/assets/proxmox5.png)

7\. В разделе **Сеть** в поле **Сетевой мост** выберите сетевой мост для локального интерфейса:

![](/.gitbook/assets/proxmox6.png)

Рекомендуем отключить опцию **Сетевой экран**, чтобы облегчить настройку и отладку файрвола в Ideco NGFW и избежать конфликтов обработки трафика.

8\. В разделе **Подтверждение** проверьте заданные настройки и нажмите **Готово**:

![](/.gitbook/assets/proxmox7.png)

Рекомендуем отключить опцию **Запуск после создания**, так как потребуется добавить еще одно сетевое устройство.

9\. Для работы NGFW также понадобится мост на сетевой интерфейс, чтобы получить доступ в интернет. Нажмите на созданную виртуальную машину, выберите **Оборудование -> Добавить -> Сетевое устройство** и добавьте мост, соответствующий выбранному ранее коммутатору:

![](/.gitbook/assets/proxmox8.png)

</details>

## Microsoft Hyper-V

{% hint style="success" %}
Видеоинструкцию по установке Ideco NGFW на Microsoft Hyper-V смотрите по ссылкам:
* [Rutube](https://rutube.ru/video/17bf175e041bc159a1868a76936d69df/)
* [Youtube](https://www.youtube.com/watch?v=238bs_4ObPY)
{% endhint %}

* Поддерживается только второе поколение виртуальных машин под Windows Server 2012 R2 или выше.
* Отключите опцию **Secure Boot** (безопасная загрузка).
* Используйте обычный виртуальный сетевой адаптер (Network Adapter).

{% hint style="info" %}
Шаги по установке Ideco NGFW после создания загрузочного USB-накопителя можно прочитать в статье [Установка](installation-process.md).
{% endhint %}