# Подключение пользователей \(client-to-site\)

Для того чтобы получить доступ извне \(из дома, отеля, другого офиса\) к локальной сети предприятия, которая находится за Ideco UTM, можно подключиться по VPN с этой машины \(компьютера или мобильного устройства\) к серверу Ideco UTM.

Для clien-to-site VPN наш сервер поддерживает четыре протокола туннельных соединений: [IKEv2](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/IPSec_IKEv2/README.md), [SSTP,](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/SSTP/README.md) [L2TP/IPSec](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/L2TP_IPSec/README.md), PPTP.

В целях безопасности не рекомендуется использовать протокол PPTP \(он оставлен для совместимости с устаревшими операционными системами и оборудованием, а также для авторизации в локальной сети, где нет требований к строгому шифрованию трафика\).

**Рекомендуемым в плане скорости и безопасности является протокол** [**IKEv2**](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/IPSec_IKEv2/README.md)**.**

Инструкции по настройке сервера и клиентов:

[Подключение по VPN IKEv2/IPSec](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/IPSec_IKEv2/README.md)

[Подключение по VPN SSTP](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/SSTP/README.md)

[Подключение по VPN L2TP/IPsec](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/L2TP_IPSec/README.md)

Вы можете использовать веб-кабинет пользователя для раздачи инструкций по созданию пользовательских VPN-подключений:

[Веб-кабинет пользователя](https://github.com/ideco-team/docsUTM/tree/54be5c28981601375569bdca6ef75ead87808b16/Веб-кабинет_пользователя/README.md).

