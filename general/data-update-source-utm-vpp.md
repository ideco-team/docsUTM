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

## Минимальные системные требования

<table><thead><tr><th width="269">Комплектующие</th><th>Системные требования</th></tr></thead><tbody><tr><td>Процессор</td><td>Intel x86-64, обязательна поддержка <a href="https://ru.wikipedia.org/wiki/SSSE3">SSSE3</a> и <a href="https://ru.wikipedia.org/wiki/SSE4">SSE4.2</a>. Минимум 6 процессорных ядер, без гипертрейдинга (если есть, нужно отключить). Не больше 1 NUMA ноды</td></tr><tr><td>Объем оперативной памяти</td><td>от 16 Гб (в зависимости от количества пользователей)</td></tr><tr><td>Дисковая подсистема</td><td>SSD, объемом 150 Гб или больше</td></tr><tr><td>Сетевые карты</td><td>Минимум три сетевые карты. <br>Поддерживаемые сетевые карты для Control Plane: <br>- карты на чипах Intel; <br>- Realtek, D-Link и другие. <br>Поддерживаемые сетевые карты для Data Plane: <br>- VirtIO (virtio-pci);<br>- VMware VMXNET3 (vmxnet3);<br>- Intel 82540, 82545, 82546 (e1000);<br>- Intel 82571, 82572, 82573, 82574, 82583, ICH8, ICH9, ICH10, PCH, PCH2, I217, I218, I219 (e1000e);<br>- Intel X710, XL710, X722, XXV710 (i40e);<br>- Intel E810, E822, E823 (ice);<br>- Intel 82573, 82576, 82580, I210, I211, I350, I354, DH89xx (igb);<br>- Intel 82598, 82599, X520, X540, X550 (ixgbe).</td></tr><tr><td>Гипервизоры</td><td>VMware, VirtualBox, KVM, Citrix XenServer</td></tr><tr><td>Дополнительно</td><td>Монитор и клавиатура</td></tr></tbody></table>

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
Для корректной работы всех модулей фильтрации Ideco NGFW VPP необходимо, чтобы доступ к вышеуказанным ресурсам был разрешён настройками фильтрации.
{% endhint %}
