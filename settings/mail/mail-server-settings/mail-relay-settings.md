# Настройка почтового релея

{% hint style="warning" %}
NGFW не поддерживает кириллические почтовые домены.
{% endhint %}

Ретрансляция входящей почты с внешнего IP-адреса Ideco NGFW (с зарегистрированным доменом и настроенными записями у регистратора и провайдера) на другой сервер для отправки и доставки почты.

Перед настройкой почтового релея убедитесь что на Ideco NGFW включен почтовый сервер.

Для настройки почтового релея добавьте в поле **Relay-домены** запись вида: `mydomain.ru|10.20.30.40`, где:

* `mydomain.ru` - почтовый домен, зарегистрированный в Интернете на публичный адрес Ideco NGFW;
* `10.20.30.40` - адрес почтового сервера в локальной сети.

![](../../../.gitbook/assets/relay-domens.png)

При настройке почтового релея на Ideco NGFW принципиально, чтобы основной почтовый домен Ideco отличался от Relay-домена. Для этого в поле **Основной почтовый домен** в настройках почтового сервера нужно прописать вымышленный домен, не совпадающий с зарегистрированным. Таким образом можно указать несколько Relay-доменов для нескольких разных серверов в локальной сети. Все почтовые домены должны быть ассоциированы с внешним адресом сервера Ideco NGFW (A и MX записи в DNS-зоне).

При такой схеме Ideco NGFW будет пропускать проходящую через себя почту прямо на почтовый сервер в локальной сети. Попутно письма могут проверяться спам. Для этого включите соответствующие сервисы в веб-интерфейсе Ideco NGFW.

Ideco NGFW будет принимать почту, адресованную только для указанного Relay-домена. Любая другая почта будет отвергнута сервером, таким образом, возможность получения открытого почтового релея при настройке исключена.