---
title: Авторизация по IP-адресу
description: null
published: true
date: '2021-05-18T10:44:21.333Z'
tags: null
editor: markdown
dateCreated: '2021-04-02T07:22:21.154Z'
---

# Авторизация по IP-адресу

## Настройка авторизации по IP

Данный тип авторизации предполагает, что авторизация устройства пользователя будет осуществляться по его IP-адресу или IP + MAC-адресу.

{% hint style="info" %}
Пользователи, которые находятся за роутером в локальной сети UTM, не могут авторизоваться по связке IP-адрес - MAC-адрес, так как роутер не обрабатывает трафик уровня L2. Такие пользователи могут авторизоваться только по IP-адресу.
{% endhint %}

Для того чтобы включить авторизацию по IP-адресу для пользователя, необходимо выполнить следующие действия:

1. Перейдите в раздел **Пользователи -&gt; Учетные записи**. 
2. Выберите нужного пользователя из списка и перейдите на вкладку **Основное**. 
3. Поставьте галочку около пункта **Использовать авторизацию по IP**. Также необходимо назначить IP-адрес устройству, с которого пользователь будет получать доступ в сеть Интернет. Форма назначения IP-адреса устройства представлена ниже.

![](../../../.gitbook/assets/ip+mac_01.png)

Для включения дополнительной привязки по MAC-адресу необходимо указать MAC-адрес в соответствующем поле.

{% hint style="info" %}
Вы можете воспользоваться поиском устройств для автоматического создания пользователей при их попытке выхода в Интернет. Для этого воспользуйтесь статьей [Обнаружение устройств](../device-discovery.md).
{% endhint %}

Под одним пользователем можно авторизовать только одно устройство по IP-адресу \(одновременно с данным типом авторизации можно авторизовать еще два устройства любым другим методом авторизации\).

## Добавление группы устройств с авторизацией по IP

Вы можете добавлять пользователей из диапазона IP-адресов (например, из сети, раздаваемой точками доступа по Wi-Fi). Для этого необходимо:

1\. Выбрать группу в дереве пользователей, в которую вы хотите добавить устройства.

2\. Во вкладке **Основное** нажать кнопку **Создать пользователей**.

Откроется окно с настройками создаваемых пользователей. Заполните следующие поля:

1\. **Префикс имени.** Пользователи будут созданы с именем вида "Пользователь IP-адрес".

2\. **Префикс логина.** Пользователи будут созданы с логином вида "user\_ip-адрес".

3\. **IP-адрес первого и последнего пользователей.**

![](../../../.gitbook/assets/add-user-to-group.gif)

В случае, если некоторые IP-адреса из диапазона уже используются другими пользователями Ideco UTM, они будут пропущены при создании.

Пользователи будут созданы с настройками, наследуемыми от группы и указанными\
IP-адресами. Пример группы с добавленными пользователями представлен на скриншоте ниже:

![](../../../.gitbook/assets/auto_user_01.png)