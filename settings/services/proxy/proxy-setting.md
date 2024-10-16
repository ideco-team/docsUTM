---
title: Настройка прокси с одним интерфейсом
description: >-
  При необходимости можно использовать Ideco UTM в качестве прокси-сервера с
  прямыми подключениями клиентов к прокси, с одним интерфейсом.
published: true
date: '2021-06-01T10:33:40.414Z'
tags: proxy
editor: markdown
dateCreated: '2021-04-02T07:26:18.797Z'
---

# Настройка прокси с одним интерфейсом

Для этого необходимо выполнить следующие настройки:

1\. При создании локального интерфейса в разделе **Сервисы -&gt; Сетевые интерфейсы** нужно указать **Шлюз**:

![](../../../.gitbook/assets/gate-local-int9-11.png)

2\. Разрешить прямые подключения к прокси-серверу на вкладке **Сервисы -&gt; Прокси**, выбрав нужный порт из списка:

![](../../../.gitbook/assets/proxy-port.png)

При использовании Ideco UTM в качестве прокси-сервера с прямыми подключениями к прокси, большинство функций будет работать в обычном режиме, но с некоторыми особенностями:

* В правилах межсетевого экрана для пользователей необходимо указывать пути INPUT, вместо FORWARD.
* Глубокий анализ трафика системой предотвращения вторжений и модулем контроля приложений будет осуществляться только для трафика, проходящего через прокси-сервер \(часть правил работать не будет\).
* Исключения из прокси-сервера необходимо делать средствами браузера или маршрутами на конечных устройствах. Настройки на вкладке **Сервисы -&gt; Прокси -&gt; Исключения** применяются только для прозрачного режима работы прокси-сервера.
