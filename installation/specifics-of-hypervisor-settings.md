# Настройка гипервизора

{% hint style="warning" %}
Для установки Ideco NGFW нужно включить режим UEFI в настройках виртуальной машины.
{% endhint %}

{% hint style="info" %}
**Обязательные условия для работы Ideco NGFW:**

* Поддержка UEFI;
* Отключить режим Legacy загрузки (он также может называться CSM);
* Отключить опцию Secure Boot в UEFI.
{% endhint %}

Ideco NGFW поддерживает работу на следующих гипервизорах:

* VMware (Workstation и ESXi) версии не ниже 6.5.0;
* Microsoft Hyper-V (2-го поколения);
* VirtualBox версии не ниже 7.0.0;
* KVM версии не ниже 1.2.0;
* Citrix XenServer.

## Общие рекомендации

* Тип ОС для создания виртуальной машины: **Linux Fedora 64 bit**;
* Минимальный размер жесткого диска: **150 ГБ**;
* Минимальное количество оперативной памяти: **16 ГБ**;
* Внутренние часы ВМ должны быть настроены на хранение времени во временной зоне UTC.

{% hint style="warning" %}
Если при установке Ideco NGFW появилась ошибка с текстом **Требуется не менее 16 ГБ оперативной памяти** и при этом указан рекомендуемый размер оперативной памяти, то уменьшите размер ресурсов, выделенных под видеопамять, до минимального.
{% endhint %}

{% hint style="info" %}
Если при установке Ideco NGFW появилось окно с надписью **Installation in BIOS mode is not supported**, проверьте включение режима UEFI в настройках виртуальной машины. 
{% endhint %}

## Microsoft Hyper-V 

* Поддерживается только второе поколение виртуальных машин под Windows Server 2012 R2 или выше; 
* Отключите опцию **Secure Boot** (безопасная загрузка);
* Используйте обычный виртуальный сетевой адаптер (Network Adapter).

**Видеоинструкция по настройке виртуальной машины**:

{% embed url="https://www.youtube.com/watch?v=238bs_4ObPY" %}
<!-- https://www.youtube.com/watch?v=238bs_4ObPY -->

## VMware ESXi 6.7

* Перед установкой Ideco NGFW увеличьте размер видеопамяти для виртуальной машины до 16 МБ;
* Используйте виртуальные сетевые адаптеры **vmxnet3**.

<details>
<summary>Настройка</summary>

Перед установкой Ideco NGFW загрузите образ, скачанный с [MY.IDECO](https://my.ideco.ru/), на VMware ESXi. При настройке виртуальной машины потребуется указать его путь.

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

{% hint style="info" %}
При установке Ideco NGFW на хосты кластера с разными поколениями процессоров укажите в настройках EVC самое старое поколение процессора из хостов, соответствующее минимальным системным требованиям для установки.
{% endhint %}


## VMware Workstation 17.0

* Перед установкой Ideco NGFW увеличьте размер видеопамяти для виртуальной машины до 16 МБ;
* Используйте виртуальные сетевые адаптеры **vmxnet3**.

<details>
<summary>Настройка</summary>

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

1\. Выполните команду `xe vm-list`. Она отобразит список виртуальных машин на xenserver;

2\. Выберите виртуальную машину с NGFW и запомните ее UUID;

3\. Выполните команду:
``` 
xe vm-param-set uuid=<UUID> HVM-boot-policy=BIOS\ order HVM-boot-params:order=dc
```

После 3 шага начнется загрузка с установочного носителя.

</details>

## VirtualBox 7.0.12
* По умолчанию при создании виртуальной машины создается 1 сетевая карта с типом подключения **NAT**.

<details>
<summary>Настройка</summary>

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

4\. Для дисков используйте режим кеширования **writeback**, если диски хранятся в qcow2 или raw-файлах.\
Если нет - проконсультируйтесь у администратора хранилища или нашей технической поддержки относительно выбора режима кеширования.

5\. В появившемся окне на вкладке **Обзор** в поле Firmware выберите пункт **UEFI x86\_64:/usr/share/OVMF/OVMF\_CODE.fd**. Выбор этого пункта включит **UEFI** и выключит опцию **Secure Boot**.

![](/.gitbook/assets/specifics-of-hypervisor-settings28.png)

Если пункта **UEFI x86\_64:/usr/share/OVMF/OVMF\_CODE.fd** нет в списке, доустановите пакет ovmf. В Ubuntu этот пакет устанавливается командой `sudo apt install ovmf`.
</details>

Далее начнется установка Ideco NGFW на виртуальную машину. Подробнее об установке в статье [Установка](installation-process.md)


{% hint style="info" %}
При возможных проблемах проверьте соответствие параметров виртуальной машины [общим рекомендациям](#obshie-rekomendacii).
{% endhint %}