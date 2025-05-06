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

# Системные требования и источники данных

## Минимальные системные требования

{% hint style="danger" %}
При установке и использовании Ideco NGFW VPP рекомендуется выключить гипертрейдинг, так как опция ухудшает производительность системы.
{% endhint %}

<table><thead><tr><th width="269">Характеристики</th><th>Описание</th></tr></thead>
<tbody>
<tr><td>Процессор</td><td>- Intel x86-64, обязательна поддержка <a href="https://ru.wikipedia.org/wiki/SSSE3">SSSE3</a> и <a href="https://ru.wikipedia.org/wiki/SSE4">SSE4.2 (от 4 ядер);</a> <br>- 6 процессорных ядер, без гипертрейдинга (если есть, нужно отключить); <br>- Не больше 1 NUMA ноды.</td></tr>
<tr><td>Объем оперативной памяти</td><td>- От 16 Гб (в зависимости от количества пользователей).</td></tr>
<tr><td>Дисковая подсистема</td><td>- SSD, объемом 150 Гб или больше.</td></tr>
<tr><td>Сетевые карты</td><td>- Три сетевые карты. <br>Поддерживаемые сетевые карты для Control Plane: <br>- карты на чипах Intel; <br>- Realtek, D-Link и другие. <br>Поддерживаемые сетевые карты для Data Plane: <br>- VirtIO (virtio-pci); <br>- VMware VMXNET3 (vmxnet3); <br>- Intel I710, X710, XL710, X722, XXV710, V710; (i40e); <br>- Intel E810, E822, E823, E830 (ice); <br>- Intel 82576, 82580, I210, I211, I350, I354, DH89xx (igb); <br>- Intel 82598, 82599, X520, X540, X550, X552, X553, E610 (ixgbe).</td></tr>
<tr><td>Гипервизоры</td><td>- VMware; <br>- VirtualBox; <br>- KVM; <br>- Citrix XenServer.</td></tr>
<tr><td>BIOS</td><td>- Поддержка UEFI; <br>- Отключенная опция Secure Boot в UEFI; <br>- Отключенный режим Legacy, может называться CSM (Compatability Support Module).</td></tr>
<tr><td>Дополнительно</td><td>- Монитор и клавиатура.</td></tr>
</tbody></table>

{% hint style="success" %}
На каждый VCE требуется минимум:

* Процессор: 4 ядра.
* Оперативная память: 16 ГБ.
* Дисковое пространство: дополнительное место на SSD в зависимости от нагрузки.
{% endhint %}

## Источники данных

Ideco NGFW VPP может обращаться к адресам для получения данных:

| Тип запроса              | Адрес             |
|--------------------------|-------------------|
| Получение лицензии       | my.ideco.ru       |
| Предотвращение вторжений | suricata.ideco.ru |
| Обновления               | update.ideco.ru   |
| NTP                      | ntp.ideco.ru      |

{% hint style="info" %}
Для корректной работы всех модулей фильтрации Ideco NGFW VPP необходимо, чтобы доступ к вышеуказанным ресурсам был разрешен настройками фильтрации.
{% endhint %}