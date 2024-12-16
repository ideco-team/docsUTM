---
description: >-
  В статье описан принцип создания правил авторизации по IP и MAC в Ideco NGFW.
---

# IP и MAC авторизация

В Ideco NGFW можно создать правила авторизации по IP, MAC и IP+MAC. 

Правила **IP и MAC авторизации** создают аналогичную привязку в [DHCP-сервере](/settings/services/dhcp.md#nastroika-dhcp-servera-s-privyazkoi-ip-k-mac) Ideco NGFW. Но если одни и те же IP- и MAC-адреса будут использоваться во включенных правилах DHCP-сервера, то правила DHCP-сервера будут выполняться в первую очередь.

Созданные в разделе **Авторизация -> IP и MAC авторизация** правила отражаются в [карточке пользователя](/settings/users/user-tree/customization-of-users.md).

Для настройки IP и MAC авторизации выполните действия:

1\. В разделе **Авторизация -> IP и MAC авторизация** нажмите **Добавить**.

2\. Создать правило привязки **IP и MAC авторизации**:

![](/.gitbook/assets/authorization5.png)

При наличии большого количества правил привязки в таблице воспользуйтесь кнопкой **Фильтры**.

3\. Если вы хотите обеспечить непрерывный доступ в интернет, даже если пользователь не активен, установите флаг **Постоянно авторизован**.

Статьи об авторизации пользователей только по IP- или MAC-адресу:

{% content-ref url="ip-authorization.md" %}
[ip-authorization.md](ip-authorization.md)
{% endcontent-ref %}

{% content-ref url="mac-authorization.md" %}
[mac-authorization.md](mac-authorization.md)
{% endcontent-ref %}