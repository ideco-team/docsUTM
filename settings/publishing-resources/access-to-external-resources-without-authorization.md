---
title: Доступ до внешних ресурсов без авторизации
description: >-
  При необходимости можно разрешить доступ к внешним ресурсам не авторизованным
  пользователям.
published: true
date: '2021-07-08T11:41:22.365Z'
tags: null
editor: markdown
dateCreated: '2021-04-02T07:24:48.279Z'
---

# Доступ до внешних ресурсов без авторизации

Также можно разрешить доступ к сети Интернет без фильтрации и авторизации на Ideco UTM некоторым IP-адресам и сетям (**осторожно используйте эту возможность!**).

Для доступа к внешним ресурcам для авторизации введите их IP-адрес или сеть в настройках по следующей инструкции.

Аналогичным образом для открытия доступа определенным хостам внутренней сети без авторизации укажите их IP-адреса.

1\. Исключить внешние ресурсы (IP-адреса или сети) из обработки прокси сервера. В разделе **Сервисы -> Прокси -> Исключения** в **Сети назначения** добавить эти ресурсы.

2\. В консоли UTM ([доступ по SSH](../access-rules/admins.md)) ввести команду:

`mcedit /usr/bin/ideco-firewall`

3\. Между строками:

`iptables -A FORWARD -m state --state INVALID -j DROP`

`iptables -A FORWARD -j forward_sys_rules`

Вписать строки:

`iptables -A FORWARD -d [ip/маска] -j ACCEPT`

`iptables -A FORWARD -s [ip/маска] -j ACCEPT`

Для диапазона IP адресов ввести:

`iptables -I FORWARD 1 -p udp -m iprange --dst-range [первый ip]-[последний ip] -m state --state`&#x20;

`iptables -I FORWARD 1 -p udp -m iprange --src-range [первый ip]-[последний ip] -j ACCEPT`

**Например:**&#x20;

`iptables -I FORWARD 1 -p udp -m iprange --dst-range`` `**`10.0.0.1-10.0.0.200`**` ``-m state --state`&#x20;

`iptables -I FORWARD 1 -p udp -m iprange --src-range`` `**`10.0.0.1-10.0.0.200`**` ``-j ACCEPT`

4\. Сохраните файл.

5\. Перезагрузите Ideco UTM.
