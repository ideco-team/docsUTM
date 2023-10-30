---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Системные требования и источники обновления данных

## Системные требования

<table><thead><tr><th width="224.39043824701196">Комплектующие</th><th>Минимальные системные требования</th></tr></thead><tbody><tr><td>Процессор</td><td>Intel x86-64, обязательна поддержка <a href="https://ru.wikipedia.org/wiki/SSSE3">SSSE3</a> и <a href="https://ru.wikipedia.org/wiki/SSE4">SSE4.2</a>. Минимум 6 ядер, без гипертрединга (если есть, нужно отключить). Не больше 1 NUMA ноды</td></tr><tr><td>Объем оперативной памяти</td><td>от 16 Гб (в зависимости от количества пользователей)</td></tr><tr><td>Дисковая подсистема</td><td>SSD, объемом 150 Гб или больше</td></tr><tr><td>Сетевые карты</td><td>Минимум три сетевые карты. Поддерживаемые сетевые карты для Control Plane интерфейса: карты на чипах Intel, Realtek, D-Link и другие. Поддерживаемые сетевые карты для Data Plane интерфейсов: VirtIO (virtio-pci), Intel X710 (i40e), Intel I210 (igb), Intel 82599ES (ixgbe), VMware VMXNET3 (vmxnet3).</td></tr><tr><td>Гипервизоры</td><td>VMware, Microsoft Hyper-V (2-го поколения), VirtualBox, KVM, Citrix XenServer</td></tr><tr><td>Дополнительно</td><td>Монитор и клавиатура</td></tr></tbody></table>

{% hint style="info" %}
**Обязательные условия для работы с Ideco NGFW VPP:**

1. Обязательная поддержка UEFI;
2. Для виртуальных машин необходимо использовать фиксированный, а не динамический размер хранилища и оперативной памяти;
3. Отключить режим Legacy загрузки, он может называться CSM (Compatability Support Module);
4. Отключить опцию Secure Boot в UEFI.
{% endhint %}

## Источники обновления данных

Ideco NGFW VPP получает обновления из следующих источников:

* Получение лицензии: my.ideco.ru;
* Предотвращение вторжений: suricata.ideco.ru;
* Обновления: update.ideco.ru;
* NTP: ntp.ideco.ru.

{% hint style="info" %}
Для корректной работы всех модулей фильтрации Ideco NGFW VPP, необходимо чтобы доступ к вышеуказанным ресурсам, был разрешён настройками фильтрации.
{% endhint %}
