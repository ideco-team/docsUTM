# Исключения 

Правила в разделе **Исключения** отключают из обработки системы [Предотвращения вторжений](README.md), [Контроля приложений](application-control.md) и [Ограничение скорости](shaper.md) и данные по ним не попадают в монитор трафика.

![](../../../.gitbook/assets/suricata1.png) 

Созданные исключения удалят объект из обработки правил на вкладке **Правила**.

Если после исключения объекта из обработки, доступ к ресурсу не появился, проверьте не блокируется ли DNS запрос. Для этого перейдите в раздел **Предотвращение вторжений -> Журнал**. Если запрос блокируется, то в журнале срабатываний наведите на строку и нажмите ![](../../../.gitbook/assets/icon-lock.png).