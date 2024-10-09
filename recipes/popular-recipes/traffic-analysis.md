# Анализ трафика хостов

Для анализа трафика на компьютерах или NGFW используйте утилиту `tcpdump`. На Ideco NGFW утилита используется в разделе **Управление сервером -> Терминал**.

{% hint style="info" %}
Утилита `tcpdump` предустановлена в продукт Ideco NGFW. 
{% endhint %}

## Описание использования утилиты и ключи tcpdump

{% hint style="info" %}
Для работы `tcpdump` требует прав суперпользователя.

При запуске `tcpdump` без каких-либо ключей/параметров произойдет перехват всех пакетов через интерфейс по умолчанию.

Для просмотра всех ключей утилиты введите `tcpdump -h`.

Для более гибкого использования утилиты используйте комбинацию ключей.

**Например:**

Для вывода и разбора только 5 захваченных пакетов с интерфейса `eth1` введите:

```bash
tcpdump -i eth1 -c 5
```

{% endhint %}

### Использование tcpdump с применением ключей

<details>

<summary>Просмотр списка сетевых интерфейсов</summary>

Для просмотра введите в терминале:

```bash
tcpdump -D
```

**Пример вывода утилиты:**

```bash
1.eth0
2.nflog (Linux netfilter log (NFLOG) interface)
3.nfqueue (Linux netfilter queue (NFQUEUE) interface)
4.eth1
5.any (Pseudo-device that captures on all interfaces)
6.lo [Loopback]
```
</details>

<details>

<summary>Захват пакетов, проходящих через определенный интерфейс</summary>

Для захвата пакетов с интерфейса `eth1` введите:

```bash
tcpdump -i eth1
```

**Пример вывода утилиты:**

```bash
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
01:06:09.278817 IP vagrant-ubuntu-trusty-64 > 10.0.0.51: ICMP echo request, id 4761, seq 1, length 64
01:06:09.279374 IP 10.0.0.51 > vagrant-ubuntu-trusty-64: ICMP echo reply, id 4761, seq 1, length 64
01:06:10.281142 IP vagrant-ubuntu-trusty-64 > 10.0.0.51: ICMP echo request, id 4761, seq 2, length 6
```

**Полезная информация:**

* Ключ `-v` увеличивает количество отображаемой информации о пакетах (добавляется протокол, флаги пакета)
* Ключ `-vv` дает еще более подробную информацию (полный разбора пакета и вывод в терминал).

**Пример использования с ключами:**

```bash
tcpdump -i eth1 -v
```

```bash
tcpdump -i eth1 -vv
```

</details>

<details>

<summary>Вывод и захват только определенного числа пакетов</summary>

Для захвата и разбора 5 пакетов с интерфейса по-умолчанию введите:

```bash
tcpdump -c 5
```

**Пример вывода утилиты:**

```bash
04:19:07.675216 IP 10.0.2.15.22 > 10.0.2.2.50422: Flags [P.], seq 2186733178:2186733278, ack 204106815, win 37232, length 100
04:19:07.675497 IP 10.0.2.2.50422 > 10.0.2.15.22: Flags [.], ack 100, win 65535, length 0
04:19:07.675747 IP 10.0.2.15.22 > 10.0.2.2.50422: Flags [P.], seq 100:136, ack 1, win 37232, length 36
04:19:07.675902 IP 10.0.2.2.50422 > 10.0.2.15.22: Flags [.], ack 136, win 65535, length 0
04:19:07.676142 IP 10.0.2.15.22 > 10.0.2.2.50422: Flags [P.], seq 136:236, ack 1, win 37232, length 100
5 packets captured
```

</details>

### Использование tcpdump c применением фильтров

Список часто используемых фильтров `tcpdump`:

* `port` - фильтрация пакетов по номеру порта;
* `host` - фильтрация исходящих и входящих пакетов по IP-адресу;
* `src` - фильтрация пакетов по IP-адресу источника;
* `dst` - фильтрация пакетов по IP-адресу назначения.

Для фильтрации по определенному протоколу укажите его в качестве фильтра:

* `tcp` - фильтрация пакетов с протоколом `TCP`;
* `udp` - фильтрация пакетов с протоколом `UDP`;
* `icmp` - фильтрация пакетов с протоколом `ICMP`;
* `arp` - фильтрация пакетов с протоколом `ARP`.

Для комбинирования фильтров используйте логические операторы:

* `and` - пакет выведется при совпадении условий у всех указанных фильтров;
* `or` - пакет выведется при совпадении условий у одного указанного фильтра;
* `not` - инвертирует условие фильтра.

<details>

<summary>Фильтрация пакетов по 80 порту</summary>

Для фильтрации введите:

```bash
tcpdump port 80
```

**Пример вывода утилиты:**

```bash
23:54:24.978612 IP 10.0.0.1.53971 > 10.0.0.50.80: Flags [SEW], seq 53967733, win 65535, options [mss 1460,nop,wscale 5,nop,nop,TS val 256360128 ecr 0,sackOK,eol], length 0
23:54:24.978650 IP 10.0.0.50.80 > 10.0.0.1.53971: Flags [S.E], seq 996967790, ack 53967734, win 28960, options [mss 1460,sackOK,TS val 5625522 ecr 256360128,nop,wscale 6], length 0
23:54:24.978699 IP 10.0.0.1.53972 > 10.0.0.50.80: Flags [SEW], seq 226341105, win 65535, options [mss 1460,nop,wscale 5,nop,nop,TS val 256360128 ecr 0,sackOK,eol], length 0
23:54:24.978711 IP 10.0.0.50.80 > 10.0.0.1.53972: Flags [S.E], seq 1363851389, ack 226341106, win 28960, options [mss 1460,sackOK,TS val 5625522 ecr 256360128,nop,wscale 6], length 0
```

</details>

<details>

<summary>Фильтрация пакетов по хосту с IP-адресом 10.0.2.15</summary>

Для фильтрации введите:

```bash
tcpdump host 10.0.2.15
```

**Пример вывода утилиты:**

```bash
03:48:06.087509 IP 10.0.2.15.22 > 10.0.2.2.50225: Flags [P.], seq 3862934963:3862934999, ack 65355639, win 37232, length 36
03:48:06.087806 IP 10.0.2.2.50225 > 10.0.2.15.22: Flags [.], ack 36, win 65535, length 0
03:48:06.088087 IP 10.0.2.15.22 > 10.0.2.2.50225: Flags [P.], seq 36:72, ack 1, win 37232, length 36
03:48:06.088274 IP 10.0.2.2.50225 > 10.0.2.15.22: Flags [.], ack 72, win 65535, length 0
03:48:06.088440 IP 10.0.2.15.22 > 10.0.2.2.50225: Flags [P.], seq 72:108, ack 1, win 37232, length 36
```

</details>

<details>

<summary>Фильтрация пакетов по IP-адресу назначения 8.8.8.8</summary>

Для фильтрации введите:

```bash
tcpdump dst 8.8.8.8
```

**Пример вывода утилиты:**

```bash
17:32:19.642154 IP desktop > dns.google: ICMP echo request, id 1, seq 1, length 64
17:32:20.644231 IP desktop > dns.google: ICMP echo request, id 1, seq 2, length 64
17:32:21.645715 IP desktop > dns.google: ICMP echo request, id 1, seq 3, length 64
17:32:22.647387 IP desktop > dns.google: ICMP echo request, id 1, seq 4, length 64
17:32:23.648814 IP desktop > dns.google: ICMP echo request, id 1, seq 5, length 64
```

</details>

<details>

<summary>Фильтрация пакетов по протоколу ICMP</summary>

Для фильтрации введите:

```bash
tcpdump icmp
```

**Пример вывода утилиты:**

```bash
04:03:47.408545 IP vagrant-ubuntu-trusty-64 > 10.0.0.51: ICMP echo request, id 2812, seq 75, length 64
04:03:47.408999 IP 10.0.0.51 > vagrant-ubuntu-trusty-64: ICMP echo reply, id 2812, seq 75, length 64
04:03:48.408697 IP vagrant-ubuntu-trusty-64 > 10.0.0.51: ICMP echo request, id 2812, seq 76, length 64
04:03:48.409208 IP 10.0.0.51 > vagrant-ubuntu-trusty-64: ICMP echo reply, id 2812, seq 76, length 64
04:03:49.411287 IP vagrant-ubuntu-trusty-64 > 10.0.0.51: ICMP echo request, id 2812, seq 77, length 64
```

</details>

<details>

<summary>Фильтрация пакетов с интерфеса eth1 c IP-адресом источника 10.0.0.1 и 80 портом назначения</summary>

Для фильтрации введите:

```bash
tcpdump -i eth1 src 10.0.0.1 and dst port 80
```

**Пример вывода утилиты:**

```bash
00:18:17.155066 IP 10.0.0.1.54222 > 10.0.0.50.80: Flags [F.], seq 500773341, ack 2116767648, win 4117, options [nop,nop,TS val 257786173 ecr 5979014], length 0
00:18:17.155104 IP 10.0.0.1.54225 > 10.0.0.50.80: Flags [S], seq 904045691, win 65535, options [mss 1460,nop,wscale 5,nop,nop,TS val 257786173 ecr 0,sackOK,eol], length 0
00:18:17.157337 IP 10.0.0.1.54221 > 10.0.0.50.80: Flags [P.], seq 4282813257:4282813756, ack 1348066220, win 4111, options [nop,nop,TS val 257786174 ecr 5979015], length 499: HTTP: GET / HTTP/1.1
00:18:17.157366 IP 10.0.0.1.54225 > 10.0.0.50.80: Flags [.], ack 1306947508, win 4117, options [nop,nop,TS val 257786174 ecr 5983566], length 0
```

</details>

<details>

<summary>Фильтрация пакетов по всем доступным протоколам, кроме ICMP</summary>

Для фильтрации введите:

```bash
tcpdump not icmp
```

**Пример вывода утилиты:**

```bash
17:45:34.847882 IP desktop.48552 > 149.154.167.41.https: Flags [P.], seq 3991504547:3991504748, ack 499514727, win 248, options [nop,nop,TS val 1585771305 ecr 4205201964], length 201
17:45:34.918383 IP 149.154.167.41.https > desktop.48552: Flags [.], ack 201, win 7509, options [nop,nop,TS val 4205203056 ecr 1585771305], length 0
17:45:34.919444 IP 149.154.167.41.https > desktop.48552: Flags [.], seq 1:1229, ack 201, win 7509, options [nop,nop,TS val 4205203056 ecr 1585771305], length 1228
17:45:34.919475 IP desktop.48552 > 149.154.167.41.https: Flags [.], ack 1229, win 239, options [nop,nop,TS val 1585771377 ecr 4205203056], length 0
17:45:34.919778 IP 149.154.167.41.https > desktop.48552: Flags [P.], seq 1229:2457, ack 201, win 7509, options [nop,nop,TS val 4205203056 ecr 1585771305], length 1228
17:45:34.919804 IP desktop.48552 > 149.154.167.41.https: Flags [.], ack 2457, win 239, options [nop,nop,TS val 1585771377 ecr 4205203056], length 0
17:45:34.923322 IP 149.154.167.41.https > desktop.48552: Flags [P.], seq 2457:2845, ack 201, win 7509, options [nop,nop,TS val 4205203061 ecr 1585771305], length 388
17:45:34.923351 IP desktop.48552 > 149.154.167.41.https: Flags [.], ack 2845, win 239, options [nop,nop,TS val 1585771381 ecr 4205203061], length 0
17:45:35.644804 IP desktop.49669 > _gateway.domain: 65295+ PTR? 41.167.154.149.in-addr.arpa. (45)
```

</details>

<details>

<summary>Сохранение дампа захваченных пакетов в файл в формате .pcap</summary>

Для сохранения дампа в файл `out.pcap` введите:

```bash
tcpdump -w out.pcap
```

</details>

{% hint style="info" %}

Для анализа захваченных пакетов в формате `.pcap` используйте [Wireshark](https://www.wireshark.org/).

{% endhint %}

### Примеры использования с Ideco NGFW

<details>

<summary>Проверка работы IPsec-туннелей</summary>

**Позволяет понять причину неработоспособности IPsec-туннеля.**

1. Для проверки прохождения трафика на всех интерфейсах головного офиса по порту 4500 введите:

```bash
tcpdump -i any port 4500 -ttttnnn
```

2. Для проверки прохождения трафика на всех интерфейсах филиала по порту 500 введите:

```bash
tcpdump -i any port 500 -tttnnn
```

</details>

