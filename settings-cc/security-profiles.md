# Профили безопасности

Профили безопасности представляют собой наборы параметров, которые используются для фильтрации трафика различными модулями. Это позволяет настраивать разные политики безопасности независимо друг от друга.

В Ideco Center можно управлять профилями безопасности для всех подключенных Ideco NGFW одновременно. 

Созданные в Ideco Center профили безопасности можно редактировать только в Ideco Center, в интерфейсе Ideco NGFW они доступны только для просмотра: 

* Таблица профилей **Контроля приложений**:

![](/.gitbook/assets/security-profiles1.png)

* Таблица профилей **Предотвращения вторжений**:

![](/.gitbook/assets/security-profiles2.png)

* Таблица профилей **Web Application Firewall**:

![](/.gitbook/assets/security-profiles3.png)

Созданные в Ideco Center профили **Контроля приложений** и **Предовращения вторжений** доступны для добавления при создании правил **[Файрвола](/settings-cc/policies-and-objects.md#fairvol)** в NGFW:

<img src="/.gitbook/assets/security-profiles5.png" alt="" data-size="original">

## Контроль приложений

В разделе **Профили безопасности -> Контроль приложений** можно создавать профили, которые определяют, разрешен ли пользователю доступ к выбраным приложениям и протоколам. Для определения протоколов приложений используется глубокий анализ трафика (Deep Packet Inspection — DPI).

![](/.gitbook/assets/security-profiles6.png)

{% hint style="success" %}
Принцип создания и настройки профилей в Ideco Center соответствуют принципам Ideco NGFW. Подробное описание в статье [Контроль приложений](/settings/security-profiles/application-control.md).

Миграция профилей **Контроля приложений** с версии 17 на версию 18 в Ideco Center осуществляется независимо от Ideco NGFW. Рекомендуем сначала обновить Ideco Center, а затем Ideco NGFW.
{% endhint %}

## Web Application Firewall

Использование WAF-профилей позволит настроить параметры защиты для опубликованных веб-ресурсов. Профиль создается в разделе **Профили безопасности -> Web Application Firewall**.

![](/.gitbook/assets/cc-waf-profiles1.png)

{% hint style="success" %}
Для удобной настройки **Web Application Firewall** на Ideco NGFW, соединенных с Ideco Center, создайте профиль WAF на Ideco Center и используйте его в Ideco NGFW. Подробное описание в статье [Web Application Firewall](/settings/security-profiles/waf-profiles.md).
{% endhint %}
