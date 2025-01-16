---
description: Создание и управление учетными записями пользователей.
---

# Учетные записи

В веб-интерфейсе Ideco NGFW пользователи отображаются в виде дерева и могут быть организованы в группы с неограниченной вложенностью. Дерево учетных записей доступно в разделе **Пользователи -> Учетные записи**. 

Группа **Ideco Device VPN** автоматически создается при установке NGFW, объединяющая пользователей, подключившихся через Device VPN. Имя пользователя такой группы импортируется из поля `Common name` пользовательского сертификата.

В Ideco NGFW реализован принцип наследования, которое позволяет задавать и изменять общие параметры для всех пользователей группы через родительскую группу. Это упрощает управление и настройки для всей группы одновременно.

{% hint style="info" %}
Все пользователи Ideco NGFW по умолчанию входят в группу **Все**. Если при создании какого-либо правила в параметрах будет выбрана группа **Все**, правило будет распространяться на всех пользователей NGFW.
{% endhint %}

Цвет пиктограммы пользователя зависит от состояния учетной записи пользователя:

<table><thead><tr><th width="200" align="center">Состояние учетной записи пользователя</th><th>Описание</th></tr></thead><tbody><tr><td align="center"><img src="/.gitbook/assets/icon-green.png" alt="icon-green.png" data-size="line"></td><td>В данный момент пользователь прошел процедуру авторизации, и ему был предоставлен доступ в интернет</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-yellow.png" alt="icon-yellow.png" data-size="line"></td><td>В <a href="customization-of-users.md">настройках пользователей</a> выбран запрет на авторизацию</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-account.png" alt="icon-account.png" data-size="line"></td><td>В данный момент пользователь не прошел процедуру авторизации, и ему не был предоставлен доступ в интернет</td></tr></tbody></table>

Элементы управления в дереве пользователей:

<table><thead><tr><th width="200" align="center">Обозначение</th><th>Описание</th></tr></thead><tbody><tr><td align="center"><img src="/.gitbook/assets/icon-add-user.png" alt=""></td><td>Создать учетную запись пользователя</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-folder.png" alt=""></td><td>Создать группу</td></tr><tr><td align="center"><img src="/.gitbook/assets/icon-delete2.png" alt=""></td><td>Удалить учетную запись пользователя или группу</td></tr></tbody></table>

Пример дерева пользователей:

![](/.gitbook/assets/tree.png)