---
title: Пересылка системных сообщений
description: >-
  Включение этого модуля даёт возможность передавать все системные сообщения
  (syslog) Ideco UTM в сторонние коллекторы (Syslog Collector) или в
  SIEM-системы.
published: true
date: '2021-06-07T11:34:50.771Z'
tags: syslog
editor: markdown
dateCreated: '2021-04-02T07:23:05.580Z'
---

# Syslog

## Пересылка системных сообщений

В качестве коллектора можно указывать любой локальный «серый» или публичный «белый» IP-адрес.

В поле **Порт** укажите любой порт из диапазона от 1 до 65535.

![](/.gitbook/assets/syslog.gif)

{% hint style="info" %}
Передача системных сообщений происходит согласно RFC-5424 (транспорт UDP).
{% endhint %}
