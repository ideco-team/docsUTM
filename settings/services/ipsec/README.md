# IPsec

{% hint style="success" %}
Название службы раздела **IPsec**: `ideco-ipsec-backend`; `strongswan`. \
Список служб для других разделов доступен по [ссылке](../../server-management/terminal.md).

Особенность работы некоторых Cisco: Если в подключении site2site активную сторону представляет Cisco и Child_SA закрывается, то пассивная сторона не сможет отправить пакет в сторону Cisco, пока Cisco не создаст новый Child_SA.
{% endhint %}

## Выбор алгоритмов шифрования на удалённых устройствах

При настройке сторонних устройств необходимо явно указать алгоритмы шифрования, используемые для подключения. \
Ideco UTM не поддерживает устаревшие и небезопасные алгоритмы (MD5, SHA1, AES128, DES, 3DES, blowfish и др.). \
При конфигурировании сторонних устройств можно указать несколько поддерживаемых алгоритмов одновременно, так как не все устройства поддерживают современные алгоритмы.

<details>

<summary>Список алгоритмов и пример использования</summary>

* **Phase 1 (IKE):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (hash, целостность):
    * для **AES256-GCM** - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для **AES256**, по приоритету: **SHA512, SHA256**.
  * prf (функция генерации случайных значений):
    * как правило, настраивается автоматически, в зависимости от выбора алгоритмов integrity (поэтому в примере [ниже](connecting-devices.md#primer-nastroiki-podklyucheniya-pfsense-k-ideco-utm-po-ipsec-predstavlen-na-skrinshotakh-nizhe) значение prf: PRF-HMAC-SHA512);
    * для AES-GCM может потребоваться указать явно. В этом случае по приоритету: **AESXCBC, SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman):
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**.
  * Таймауты: 
    * **Lifetime**: 14400 сек;
    * **DPD Timeout** (для L2TP/IPsec): 40 сек;
    * **DPD Delay**: 30 сек.
* **Phase 2 (ESP):**
  * encryption (шифрование):
    * **AES256-GCM**;
    * **AES256**.
  * integrity (целостность):
    * для **AES256-GCM** - не требуется, поскольку проверка целостности встроена в AEAD-алгоритмы;
    * для **AES-256**, по приоритету: **SHA512, SHA384, SHA256**.
  * DH (Группа Diffie-Hellman, PFS). **ВНИМАНИЕ! если не указать, подключаться будет, но не сработает rekey через некоторое время**:
    * **Curve25519 (group 31)**;
    * **ECP256 (group 19)**;
    * **modp4096 (group 16)**;
    * **modp2048 (group 14)**;
    * **modp1024 (group 2)**. 
  * Таймаут:  
    * **Lifetime**: 3600 сек.

**Пример:**

* **Phase 1 (IKE)** (нужна одна из строк)**:**
  * AES256-GCM\PRF-HMAC-SHA512\Curve25519;
  * AES256\SHA512\PRF-HMAC-SHA512\ECP384;
  * AES256\SHA256\PRF-HMAC-SHA256\MODP2048.
* **Phase 2 (ESP)** (нужна одна из строк)**:**
  * AES256-GCM\ECP384;
  * AES256\SHA256\MODP2048.

Пример настройки подключения pfSense к Ideco UTM по IPsec:

![](/.gitbook/assets/site-to-site-ideco-mikrotik1.png)

![](/.gitbook/assets/site-to-site-ideco-mikrotik2.png)

</details>

{% content-ref url="branch-office-and-main-office.md" %}
[branch-office-and-main-office.md](branch-office-and-main-office.md)
{% endcontent-ref %}

{% content-ref url="devices.md" %}
[devices.md](devices.md)
{% endcontent-ref %}

{% content-ref url="site-to-site/README.md" %}
[site-to-site/README.md](site-to-site/README.md)
{% endcontent-ref %} 
