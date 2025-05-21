---
description: >-
  В разделе представлена общая информация об особенностях авторизации пользователей в Ideco NGFW VPP.
---

{% hint style="success" %}
Название службы раздела **Авторизация**: `ideco-auth-backend`. \
Список служб для других разделов доступен по [ссылке](/settings/server-management/terminal.md).
{% endhint %}

# Настройка авторизации пользователей

Авторизация необходима при работе как во внешней сети, так и в локальной.

Сетевое устройство (хост) может получить доступ в интернет через VPP с контролем трафика только после авторизации под учетной записью пользователя.

{% hint style="warning" %}
По умолчанию в таблице **Правила трафика -> Файрвол -> FORWARD** настроено системное правило, блокирующее весь трафик. Для доступа пользователей в интернет необходимо [создать разрешающие правила](/settings/access-rules/firewall.md).
{% endhint %}

Реализовано несколько способов авторизации:

{% content-ref url="ip-mac-authorization.md" %}
[ip-mac-authorization.md](ip-mac-authorization.md)
{% endcontent-ref %}

{% content-ref url="authorization-by-subnet.md" %}
[authorization-by-subnet.md](authorization-by-subnet.md)
{% endcontent-ref %}

{% hint style="info" %}
Настройка авторизации через журнал безопасности Active Directory описана в [статье](/settings/users/active-directory/README.md).
{% endhint %}
