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

<table><thead><tr><th width="218.33333333333331">Комплектующие</th><th>Минимальные системные требования</th></tr></thead><tbody><tr><td>Процессор</td><td> Intel x86-64, обязательна поддержка <a href="https://ru.wikipedia.org/wiki/SSSE3">SSSE3</a> и <a href="https://ru.wikipedia.org/wiki/SSE4">SSE4.2</a>. Минимум 6 ядер, без гипертрединга (если есть, нужно отключить). Не больше 1 NUMA ноды</td></tr><tr><td>Объем оперативной памяти</td><td>от 16 Гб (в зависимости от количества пользователей)</td></tr><tr><td>Дисковая подсистема</td><td>SSD, объемом 150 Гб или больше</td></tr><tr><td>Сетевые карты</td><td>Минимум три сетевые карты. Поддерживаемые карты: VirtIO (virtio-pci), Intel X710 (i40e), Intel I210 (igb), Intel 82599ES (ixgbe), VMware VMXNET3 (vmxnet3)</td></tr><tr><td>Гипервизоры</td><td>VMware, Microsoft Hyper-V (2-го поколения), VirtualBox, KVM, Citrix XenServer</td></tr><tr><td>Дополнительно</td><td>Монитор и клавиатура</td></tr><tr><td>Замечания</td><td>Обязательна поддержка UEFI. Не поддерживаются программные RAID-контроллеры (интегрированные в чипсет). Для виртуальных машин необходимо использовать фиксированный, а не динамический размер хранилища и оперативной памяти.</td></tr></tbody></table>

## Источники обновления данных

Ideco UTM VPP получает обновления из следующих источников:

* Получение лицензии: my.ideco.ru;
* Предотвращение вторжений: suricata.ideco.ru;
* Обновления: update.ideco.ru;
* NTP: ntp.ideco.ru.

{% hint style="info" %}
Для корректной работы всех модулей фильтрации Ideco UTM VPP, необходимо чтобы доступ к вышеуказанным ресурсам, был разрешён настройками фильтрации.
{% endhint %}
