# Создание правила Forward

**Задача:** создать правило Forward для протокола TCP и отредактировать, указав время действия. \
Для правила нужно создать:

* Диапазон IP-адресов (`192.168.0.1-192.168.0.20`);
* Список адресов в качестве источника (`9.9.9.9`, `9.9.9.10`);
* Время действия (с 09:00 по 18:00, с понедельника по пятницу).

{% hint style="info" %}
Все приведенные ниже команды выполняются в bash-терминале.

При использовании curl в командной строке Windows замените все одинарные кавычки двойными, при этом кавычки внутри кавычек необходимо экранировать. Пример:

`--data "{\"login\": \"логин\", \"password\": \"пароль\", \"rest_path\": \"/\"}"`
{% endhint %}

1\. Авторизуйте администратора:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/web/auth/login --data '{"login": "логин", "password": "пароль", "rest_path": "/"}'
```

* `x.x.x.x` - IP-адрес веб-интерфейса Ideco NGFW.

**Ответ на успешный запрос:** 200 ОК

2\. Создайте объект **Диапазон IP-адресов** c `192.168.0.1` по `192.168.0.20`:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/aliases/ip_ranges --data '{"title": "test ip range", "comment": "test ip range", "start": "192.168.0.1", "end": "192.168.0.20"}'
```

**Ответ на успешный запрос:**

```json5
{
    "id": "ip_range.id.2"
}
```

3\. Создайте объект **Список IP-объектов**:

  * Создайте объекты **IP-адрес** для IP `9.9.9.9` и повторите действие для IP `9.9.9.10`. Пример: 

    ```
    curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/aliases/ip_addresses --data '{"comment": "комментарий", "title": "название", "value": "9.9.9.9"}'
    ```

    **Ответ на успешный запрос:**

    ```json5
    {
        "id": "ip.id.3"
    }
    ```

  * Создайте объект типа Список IP-объектов, указав в `values` полученные в прошлом шаге `id` (например: `ip.id.2` и `ip.id.3`): 

    ```
    curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/aliases/lists/addresses --data '{"title": "название", "comment": "комментарий", "values": ["ip.id.2", "ip.id.3"]}'
    ```

    **Ответ на успешный запрос:**

    ```json5
    {
        "id": "address_list.id.2"
    }
    ```

4\. Создайте объект **Время**:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/aliases/time_ranges --data '{"title":"Рабочее время","comment":"пн-пт 09:00-18:00","weekdays":[1,2,3,4,5],"start":"09:00","end":"18:00", "period": null}'
```

**Ответ на успешный запрос:**

```json5
{
    "id": "time_range.id.3"
}
```

5\. Создайте правило файрвола, используя *id* из пунктов 2 и 3:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X POST https://x.x.x.x:8443/firewall/rules/forward --data '{"action": "drop", "comment": "", "destination_addresses": ["ip_range.id.2"], "destination_addresses_negate": false, "destination_ports": ["any"], "enabled": true, "hip_profiles": [], "incoming_interface": "any", "outgoing_interface": "any", "protocol": "protocol.tcp", "source_addresses": ["address_list.id.2"], "source_addresses_negate": false, "timetable": ["any"], "parent_id": "f3ffde22-a562-4f43-ac04-c40fcec6a88c"}'
```

Значение `action`:

  * `accept` - принять пакет; 
  * `drop` - отклонить пакет.

**Ответ на успешный запрос:**

```json5
{
    "id": 2
}
```

6\. Отредактируйте созданное правило, указав время действия:

```
curl -k -c /tmp/cookie -b /tmp/cookie -X PUT https://x.x.x.x:8443/firewall/rules/forward/<id созданного в пункте 5 правила> --data '{"action": "drop", "comment": "", "destination_addresses": ["ip_range.id.2"], "destination_addresses_negate": false, "destination_ports": ["any"], "enabled": true, "hip_profiles": [], "incoming_interface": "any", "outgoing_interface": "any", "protocol": "protocol.tcp", "source_addresses": ["address_list.id.2"], "source_addresses_negate": false, "timetable": ["time_range.id.1"], "parent_id": "f3ffde22-a562-4f43-ac04-c40fcec6a88c"}'
```

**Ответ на успешный запрос:** 200 ОК