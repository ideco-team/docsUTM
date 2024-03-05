# Настройки

Для добавления правила нажмите **Добавить** и в поле **Подсеть** укажите локальные сети, обслуживаемые NGFW (сети локальных интерфейсов NGFW, маршрутизируемые на них сети удаленных сегментов локальной сети предприятия).

{% hint style="warning" %}
**Не указывайте** сети, принадлежащие внешним сетевым интерфейсам NGFW и внешним сетям. Указанные здесь сети участвуют в правилах службы предотвращения вторжения как локальные. Локальный межсегментный трафик не исключается из проверок системы.
{% endhint %}

{% hint style="warning" %}
При работе службы предотвращения вторжений **не используйте** сторонние DNS-серверы для компьютеров, т.к служба определяет зараженные устройства по DNS-запросам, проходящим через нее. \
При использовании внутреннего домена AD рекомендуется:

* В компьютерах указать DNS-сервер Ideco NGFW в качестве единственного DNS-сервера;
* В настройках DNS-сервера на NGFW указать Forward-зону для локального домена.
{% endhint %}