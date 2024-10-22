---
description: >-
  Инструкция актуальна для Alt Linux 10.2.
---

# Инструкция по созданию VPN-подключения в Alt Linux

{% hint style="info" %}
Перед настройкой VPN-подключения перейдите в раздел **Пользователи -> VPN-подключения -> Доступ по VPN** и создайте разрешающее VPN-подключение правило.
{% endhint %}

{% hint style="warning" %}
Не рекомендуем использовать для VPN-подключений кириллические логины.
{% endhint %}

## Протокол IKEv2/IPsec

**Настройка Ideco NGFW:**

1\. Перейдите в раздел **Пользователи -> VPN-подключения -> Основное**.

2\. Установите опцию **Подключение по IKEv2/IPsec** и заполните поле **Домен и IP-адрес**:

![](/.gitbook/assets/vpn-authorization8.png)

3\. Скачайте корневой сертификат Ideco NGFW в разделе **Сервисы -> Сертификаты -> Загруженные сертификаты** в веб-интерфейсе NGFW или в личном кабинете пользователя по кнопке **Скачать корневой сертификат**.

Корневой сертификат потребуется для настройки подключения рабочей станции пользователя, если не был получен корневой сертификат через Let\`s Encrypt. При необходимости перенесите файл сертификата на рабочую станцию.\
Если для VPN-подключения используется сертификат, выданный Let\`s Encrypt, то установка корневого сертификата на устройство не требуется.

**Cоздание подключения Alt Linux:**

1\. Откройте терминал сочетанием клавиш Ctrl+Alt+T и установите необходимые пакеты:

```bash
apt-get update && apt-get dist-upgrade && apt-get install NetworkManager-strongswan NetworkManager-strongswan-gnome strongswan strongswan-charon-nm strongswan-testing
```

2\. Установите корневой сертификат на рабочую станцию:

```bash
cp root-ca.crt /etc/pki/ca-trust/source/anchors/ && update-ca-trust
```

* `root-ca.crt` - путь к сертификату.

3\. Перейдите в **Соединения VPN** и нажмите **Настроить VPN**:

![](/.gitbook/assets/connection-for-alt-linux.png)

4\. Добавьте новое VPN-подключение:

![](/.gitbook/assets/connection-for-alt-linux1.png)

5\. Выберите тип VPN-подключения `IPsec/IKEv2 (strongswan)` и нажмите **Создать**:

![](/.gitbook/assets/connection-for-alt-linux2.png.png)

6\. Заполните необходимые поля для создания VPN-подключения, как на скриншоте:

* Address - адрес шлюза;
* Authentication - тип аутентификации;
* Username - логин пользователя на Ideco NGFW;
* Password - пароль пользователя на Ideco NGFW.

![](/.gitbook/assets/connection-for-alt-linux3.png.png)

7\. Заполните параметры шифрования, как на скриншоте, и нажмите **Сохранить**:

![](/.gitbook/assets/connection-for-alt-linux4.png.png)

8\. Включите созданное VPN-подключение:

![](/.gitbook/assets/connection-for-alt-linux5.png.png)

</details>