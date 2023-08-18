# Разрешить интернет всем

Данный режим используется для диагностики неполадок.

Активный режим **Разрешить интернет всем** автоматически не отключается и работает, пока его не отключить.

При этом:

* не будут работать правила [файрвола](../settings/access-rules/firewall.md);
* не будет происходить фильтрация трафика;
* не будет производиться сбор веб-статистики;
* не будет доступа к серым IP-адресам за UTM из внешней сети;
* пользователям будет разрешен доступ в интернет без авторизации.

Включить данный режим можно двумя способами:

1\. Через веб-интерфейс.\
Для этого нажмите на иконку технической поддержки в верхней правой части окна![](../.gitbook/assets/icon-help.png) и в открывшемся окне переведите ползунок активации режима в положение **Активно.**

![](../.gitbook/assets/allow-int.gif)

2\. Через локальное меню.\
Для этого введите номер пункта **6. Включить режим Разрешить интернет всем** и нажмите **Enter** для применения настройки.