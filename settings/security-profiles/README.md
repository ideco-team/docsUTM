# Профили безопасности

Профили безопасности это наборы параметров для фильтрации трафика различными модулями и позволяет настраивать разные политики безопасности независимо друг от друга.

Профили WAF будут использоваться только в публикациях сервисов в разделе [Обратный прокси](settings/services/reverse-proxy.md). Остальные профили - в правилах раздела [Файрвол](/settings/access-rules/firewall.md).\
Один и тот же профиль будет использоваться в нескольких правилах.

## Что позволят делать профили

* [x] Выбирать, какой трафик отправлять на глубокий анализ и фильтрацию. Это позволит уменьшить нагрузку на модули фильтрации.
* [x] Настраивать независимые друг от друга политики безопасности для модулей фильтрации.

{% content-ref url="waf-profiles.md" %}
[waf-profiles.md](waf-profiles.md)
{% endcontent-ref %}

{% content-ref url="application-control.md" %}
[application-control.md](application-control.md)
{% endcontent-ref %}

{% content-ref url="ips-profiles.md" %}
[ips-profiles.md](ips-profiles.md)
{% endcontent-ref %}
