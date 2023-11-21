# IPsec

{% hint style="success" %}
Название службы раздела **IPsec**: `ideco-ipsec-backend`; `strongswan`. \
Список служб для других разделов доступен по [ссылке](../../server-management/terminal.md).

Нужна помощь при настройке Ideco UTM? Получите быстрый ответ от [чат-бота](https://gpt-docs.ideco.ru/) нашей документации!
{% endhint %}

{% hint style="info" %}
Особенность работы некоторых Cisco: Если в подключении site2site активную сторону представляет Cisco и Child_SA закрывается, то пассивная сторона не сможет отправить пакет в сторону Cisco, пока Cisco не создаст новый Child_SA.
{% endhint %}

{% hint style="danger" %}
При обновлении на версию 15.Х может пропасть соединение IPsec с типом аутентификации PSK. Для настройки соединения перейдите в режим редактирование и подберите тип идентификатора.
{% endhint %}

{% content-ref url="branch-office-and-main-office.md" %}
[branch-office-and-main-office.md](branch-office-and-main-office.md)
{% endcontent-ref %}

{% content-ref url="devices.md" %}
[devices.md](devices.md)
{% endcontent-ref %}