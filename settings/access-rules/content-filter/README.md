---
description: Контентная фильтрация реализована на основе данных о веб-трафике, получаемых от модуля проксирования веб-трафика. Позволяет блокировать доступ к различным интернет-ресурсам.
---

# Контент-фильтр

{% hint style="success" %}
Название службы раздела _Контент-фильтра_: `ideco-content-filter-backend.service`. \
Список имен служб для других разделов доступен по [ссылке](/settings/server-management/terminal.md).

Для записи логов поставьте флаг строке **Включить журналирование** в разделе **Сервисы -> Прокси -> Основное**.
{% endhint %}

**Контент-фильтр** проверяет наличие сайта, который хочет открыть пользователь, в списках ресурсов Ideco NGFW. Если адрес находится в этих списках, то применяются настроенные правила фильтрации.

Контент-фильтр состоит из четырех вкладок: правила, пользовательские категории, морфологические словари и настройки:

{% content-ref url="rules.md" %}
[rules.md](rules.md)
{% endcontent-ref %}

{% content-ref url="custom-categories.md" %}
[custom-categories.md](custom-categories.md)
{% endcontent-ref %}

{% content-ref url="morphological-dictionaries.md" %}
[morphological-dictionaries.md](morphological-dictionaries.md)
{% endcontent-ref %}

{% content-ref url="settings.md" %}
[settings.md](settings.md)
{% endcontent-ref %}

{% hint style="info" %}
HTTPS-сайты без расшифровки трафика фильтруются только по домену (а не по полному URL), правила категории **Файлы** на них также применить невозможно. Для полной фильтрации HTTPS создайте правила расшифровки HTTPS-трафика нужных категорий.
{% endhint %}

{% hint style="warning" %}
Для фильтрации по IP-адресам используйте [Файрвол](/settings/access-rules/firewall.md).

Фильтрация по IP-адресам в **Контент-фильтре** будет работать:

* Для HTTP-запросов к IP-адресам напрямую;
* Для расшифрованных HTTPS-запросов к IP-адресам;
* Для HTTPS-запросов к ресурсам, сертификат которых содержит IP-адрес в поле Common Name сертификата.

**Файрвол** анализирует пакет на сетевом уровне (L3), а **Контент-фильтр** - на прикладном уровне (L7). Информация об IP-адресах на прикладном уровне (L7) неточная, поэтому для блокировки IP-адресов нужно использовать **Файрвол**.

{% endhint %}

Подробная информация о методах фильтрации HTTPS представлена в статье:

{% content-ref url="filtering-https-traffic.md" %}
[filtering-https-traffic.md](filtering-https-traffic.md)
{% endcontent-ref %}

Порядок действий для изменения страницы блокировки Контент-фильтра описан в статье:

{% content-ref url="block-page.md" %}
[block-page.md](block-page.md)
{% endcontent-ref %}

{% hint style="info" %}
Процесс блокировки ресурсов, взаимодействующих с чат-ботами, описан в [статье](/recipes/popular-recipes/block-chat-bot.md)
{% endhint %}
