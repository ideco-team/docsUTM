---
title: >-
  Одновременное подключение к нескольким провайдерам (балансировка и
  резервирование)
description: 'Настройка резервирования каналов, статической и динамической балансировки.'
published: true
date: '2021-05-18T12:05:40.963Z'
tags: 'network_interface, balancing_and_reserving'
editor: markdown
dateCreated: '2021-04-02T07:23:10.294Z'
---

# Одновременное подключение к нескольким провайдерам

При наличии нескольких подключений к Интернет-провайдерам, можно задействовать их следующими способами:

* Резервирование одного подключения, чтобы при его отключении трафик шел через другие доступные подключения.
* Статическая балансировка трафика между несколькими подключениями. При этом часть пользователей локальной сети будет выходить в сеть Интернет через одного провайдера, часть через другого.
* Динамическая балансировка трафика между несколькими подключениями. При этом подключения будут поочередно переключаться в зависимости от нагрузки, а сессии от всех пользователей будут равномерно распределяться между ними.

## Подготовка

Создайте дополнительное подключение к интернет-провайдеру. Процесс создания подключений описан в статье [Настройка Внешнего Ethernet](ethernet-connection.md). Таким образом, на сервере должно быть минимум два подключения к сети Интернет.

Для работы с трафиком в Ideco UTM важно учитывать 2 момента: маршрутизация и NAT. Это касается как балансировки, так и резервирования.

## Резервирование каналов

Чтобы настроить резервирование, необходимо перейти в раздел **Сервисы -&gt; Балансировка и резервирование** и выбрать режим **Резервирование**.

![](../../.gitbook/assets/backup1.png)

* Приоритет использования подключений задается их порядком в таблице, сверху вниз. Подключение, которое используется в данный момент, отмечено тегом **Используется**.
* Для смены приоритета можно использовать соответствующие элементы управления \(иконки стрелок ![up-down.png](../../.gitbook/assets/up-down.png)\).
* Если сеть Интернет стала недоступна через используемое подключение, то система переключится на более приоритетное, имеющее доступ к сети Интернет.

## Доступ к сети Интернет через определенное подключение к провайдеру \(статическая балансировка\)

Такая схема подключения к нескольким интернет-провайдерам часто применяется в случаях:

* когда некоторые ресурсы в сети Интернет тарифицируются дешевле через другого интернет-провайдера и трафик нужно направить через него;
* когда нужно предоставить доступ к внутренним сетям одного из провайдеров определенным пользователям или группам пользователей.

Для настройки данной схемы подключения выполните следующие действия:

1. Перейдите в раздел меню **Сервисы -&gt; Маршрутизация**. 
2. Добавьте правила маршрутизации для определенного списка ресурсов, трафик к которым необходимо направить через нужное подключение к провайдеру, нажав кнопку **Добавить**.

**Пример правила:**

![](../../.gitbook/assets/rule.png)

В данном примере трафик, направленный к ресурсу **vk. com** от пользователя **Иван Петров**, будет направлен через подключение к провайдеру **Подключение к провайдеру №1**.

## Распределение нагрузки по нескольким подключениям \(динамическая балансировка\)

Для настройки данной схемы подключения выполните следующие действия:

1. Перейти в раздел **Сервисы -&gt; Балансировка и резервирование**. 
2. Выбрать режим работы **Балансировка**.

![](../../.gitbook/assets/balancing1.png)

Для равномерного распределения сессий между подключениями необходимо указать значение **Полосы пропускания** - максимальной скорости Интернета по тарифам ваших провайдеров. По умолчанию, полоса пропускания имеет значение - 100 Мбит/с. Сервер автоматически будет балансировать трафик в зависимости от загрузки подключений.

{% hint style="info" %}
Создавать маршруты или выполнять еще какие-либо настройки для балансировки трафика не требуется. Трафик прокси-сервера также будет балансироваться автоматически.
{% endhint %}

