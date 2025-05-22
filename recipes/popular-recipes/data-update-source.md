# Источники данных

Ideco NGFW может обращаться к адресам для получения данных:

<table><thead><tr><th width="300">Тип запроса</th><th>Адрес</th></tr></thead><tbody>
<tr><td>Отсылка уведомлений в личный кабинет/телеграм-бот</td><td>alerts.v19.ideco.dev</td></tr>
<tr><td>Обновление баз Контент-фильтра</td><td>content-filter.v19.ideco.dev</td></tr>
<tr><td>Отсылка анонимной статистики</td><td>gatherstat.v19.ideco.dev</td></tr>
<tr><td>Обновления баз GeoIP</td><td>ip-list.v19.ideco.dev</td></tr>
<tr><td>Обмен информации о лицензии</td><td>license.v19.ideco.dev</td></tr>
<tr><td>Отправка отчетов по почте</td><td>send-reports.v19.ideco.dev</td></tr>
<tr><td>Обновления сигнатур IDS/IPS</td><td>suricata.v19.ideco.dev</td></tr>
<tr><td>Обновления системы</td><td>sysupdate.v19.ideco.dev</td></tr>
<tr><td>Синхронизация времени</td><td>ntp.ideco.ru</td></tr>
<tr><td>Получение сертификатов Let's Encrypt</td><td>acme-v02.api.letsencrypt.org</td></tr>
<tr><td>Антивирус Касперского (обновление баз)</td><td>Серверы с <a href="https://support.kaspersky.ru/common/start/6105">официального сайта</a> Лаборатории Касперского</td></tr>
</tbody></table>

Часть запросов к указанным выше серверам может быть перенаправлена на mcs-vm.ideco.ru, update.ideco.ru, storage.yandexcloud.net.

{% hint style="warning" %}
Для корректной работы всех модулей фильтрации Ideco NGFW необходимо, чтобы доступ к вышеуказанным ресурсам был разрешен настройками фильтрации.

Учитывайте при обновлении, что `v19` в домене соответствует версии Ideco NGFW. Эту часть можно заменить символом `*` при настройке фильтрации (пример: `license.*.ideco.dev`).
{% endhint %}