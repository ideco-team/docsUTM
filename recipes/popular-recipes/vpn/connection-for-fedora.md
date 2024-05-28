# Инструкция по созданию подключения в Fedora

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

## Протокол IKEv2/IPsec 

### Установка пакетов

Для поддержки подключения по IPsec для NetworkManager установите пакет **NetworkManager-strongswan**:

```bash
sudo dnf -y install NetworkManager-strongswan
```

<details>
<summary>Окружение рабочего стола GNOME</summary>

Для настройки IPsec-подключения через графический интерфейс установите пакет **NetworkManager-strongswan-gnome**:

```bash
sudo dnf -y install NetworkManager-strongswan-gnome
```

</details>

<details>
<summary>Окружение рабочего стола KDE</summary>

Для настройки IPsec-подключения через графический интерфейс установите пакет **plasma-nm-strongswan**:

```bash
sudo dnf -y install plasma-nm-strongswan
```

</details>

### Hастройка IKEv2/IPsec-подключения

1\. Перед настройкой IPsec-подключения загрузите на устройство корневой сертификат Ideco NGFW (включая всю цепочку доверия) или **ISRG_ROOT_X1** сертификат при использовании сертификата Let`s encrypt.

{% hint style="warning" %}
Файл сертификата должен находится в общедоступном каталоге.

Если загрузить корневой сертификата NGFW(включая всю цепочку доверия) в каталог \
`/etc/strongswan/ipsec.d/cacerts`, то не потребуется указывать сертификат при настройке подключения.

Если в системе уже имеется **ISRG_ROOT_X1** сертификат, то загружать его отдельно не требуется.

При настройке подключения в Fedora 40 **не требуется** загружать **ISRG_ROOT_X1** сертификат, поскольку он уже есть в системе. Сертификат находится в каталоге \
`/etc/ssl/certs`
{% endhint %}

2\. Перейдите в настройки VPN-подключений на компьютере и выберите тип **IKEV2**.

3\. Заполните поля:

* **Название** - название VPN-подключения;
* **Address** - доменное имя шлюза для VPN-подключения;
* **Certificate** - сертификат, загруженный на шаге 1;
* **Authentication** - EAP;
* **Username** - имя пользователя на Ideco NGFW;
* **Password** - пароль пользователя на Ideco NGFW.

![](/.gitbook/assets/connection-for-fedora1.png)

4\. Нажмите **Применить** и подключитесь к Ideco NGFW.


