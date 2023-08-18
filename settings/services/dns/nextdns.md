# NextDNS

NextDNS является облачным поставщиком услуг DNS в Интернете, используемый\
для блокировки онлайн-трекеров, фильтрации баннеров и прочей рекламы. А также ограничения доступа к нежелательным сайтам по доменным именам через черные и белые списки.

У NextDNS имеются различные [тарифы](https://nextdns.io/pricing), среди которых есть и бесплатный. Этот тариф подойдет для предприятий малого бизнеса или школ.

{% hint style="warning" %}
Данный тариф имеет ограничение по количеству запросов в месяц, после превышения этого количества, фильтрация со стороны NextDNS будет прекращена, но резолвинг имен продолжит работать.
{% endhint %}

{% hint style="success" %}
Данная интеграция была внедрена в Ideco UTM для предоставления возможности использовать сервис NextDNS всем пользователям, находящимся в локальных сетях Ideco UTM.
{% endhint %}

## Настройка NextDNS на Ideco UTM

{% hint style="info" %}
Для использования сервиса NextDNS, необходимо предварительно в нем [зарегистрироваться](https://my.nextdns.io). Без регистрации можно использовать пробный аккаунт, действующий в течение 7 дней, с последующим удалением.
{% endhint %}

Для интеграции Ideco UTM с NextDNS, необходимо:

1\. Необходимо зайти на сайт https://my.nextdns.io/`nextDNS-id`/setup

![Первичное окно настройки NextDNS](../../../.gitbook/assets/nextdns\_first\_configuration.png)

2\. Перейдите в раздел **Сервисы -> DNS**.

3\. Нажать на флаг с **NextDNS** и вставить в поле ID из личного кабинета, как показано\
на скриншоте:

![](../../../.gitbook/assets/nextdns\_paste\_id\_in\_dns.png)

4\. Нажать на кнопку **Сохранить**.

После сохранения настроек, все имеющиеся в вашем личном кабинете NextDNS правила фильтрации начнут действовать на исходящие DNS-запросы от пользователей\
из локальных сетей Ideco UTM.

{% hint style="info" %}
При возникновении проблем с интеграцией NextDNS, обратитесь\
в [техническую поддержку](../../../general/technical-support.md) Ideco UTM.

При возникновении трудностей с настройкой или проблем с работой\
самого NextDNS, обратитесь в техническую поддержку NextDNS.
{% endhint %}