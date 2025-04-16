---
description: >-
  Как скачать, установить и запустить Ideco Client на Linux.
---

# Установка и настройка Ideco Client на Linux

## Особенности работы Ideco Client на Linux

* Ideco Client гарантированно работает на Alt Linux, РЕД ОС, Astra Linux, Fedora, Ubuntu. Для остальных дистрибутивов работа не гарантируется;

* [HIP-профили](/settings/users/hip-profiles.md) на стороне агента поддерживаются **не в полном объеме**:

{% tabs %}

{% tab title="Доступные HIP-профили" %}

* ОС;
* процесс.

{% endtab %}

{% tab title="Недоступные HIP-профили" %}

* антивирус;
* домен;
* межсетевой экран;
* реестр (всегда только Windows);
* службы (всегда только Windows);
* пакет обновлений Knowledge Base (всегда только Windows).

{% endtab %}

{% endtabs %}

* Для проверки запуска процесса с заданным именем в системе (ZTNA) используется функция:

```
bool os_specific::isProcessExist(const std::string &processName)
```
Длина строки `processName` составляет не более 15 символов. Если название процесса длиннее, оно будет обрезано до максимально доступного числа символов. В этом случае проверка не будет выполнена корректно.

## Скачивание

{% tabs %}

{% tab title="Для администратора" %}

Перейдите в раздел **Пользователи -> Ideco-Client**, переведите опцию **Ideco Client** в положение **Включен**, нажмите **Скачать под Linux**:

![](/.gitbook/assets/ideco-client5.png)

{% endtab %}

{% tab title="Для пользователя" %}

Перейдите в личный кабинет пользователя и нажмите **Скачать под Linux**:

![](/.gitbook/assets/ideco-client7.png)

{% endtab %}

{% endtabs %}

## Установка

Для установки Ideco Client на Linux выполните действия:

1\. Перейдите в папку со скачанным файлом установки Ideco Client:

```bash
cd "Путь до директории с установочным файлом"
```

2\. Предоставьте файлу разрешение на исполнение, выполнив в терминале команду:

```bash
chmod +x IdecoAgent.sh
```

3\. Запустите файл установки Ideco Client:

```bash
./IdecoAgent.sh
```

4\. После установки проверьте статус службы IdecoService, выполнив команду:

```bash
systemctl status IdecoService.service
```

5\. Убедитесь, что служба IdecoService запущена и работает:

![](/.gitbook/assets/ideco-client-linux2.png)

{% hint style="info" %}
Для добавления службы в автозагрузку выполните команду:

```bash
systemctl enable IdecoService.service
```

{% endhint %}

{% hint style="warning" %}
Для корректной работы Ideco Client на Astra Linux удалите настройку службы IdecoService:

```bash
sudo rm /etc/systemd/system/IdecoService.service
```

{% endhint %}

## Настройка профиля для первого запуска

Перед подключением к Ideco NGFW по внешнему IP-адресу или доменному имени без сертификата Let’s Encrypt импортируйте корневой сертификат Ideco NGFW на компьютер и убедитесь, что срок действия сертификата на домен или IP-адрес составляет **825 дней**.

Если срок действия сертификата превышает 825 дней, [загрузите](/settings/services/certificates/upload-ssl-certificate-to-server.md) на Ideco NGFW сертификат со сроком действия, не превышающим 825 дней, или [перевыпустите](/settings/services/certificates/README.md#процесс-перевыпуска-сертификата) автоматически сгенерированный сертификат.

Для импорта корневого сертификата на конкретный дистрибутив воспользуйтесь статьями:

* [Установка корневого сертификата на Astra Linux](https://wiki.astralinux.ru/tandocs/dobavlenie-sobstvennyh-sertifikatov-v-os-linux-302022798.html);
* [Установка корневого сертификата на Alt Linux](https://www.altlinux.org/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BA%D0%BE%D1%80%D0%BD%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE_%D1%81%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%B0);
* [Установка корневого сертификата на Red OS](https://redos.red-soft.ru/base/redos-7_3/7_3-security/7_3-ext-szi/7_3-cpro/7_3-certs-cryptopro/?nocache=1729509457983);
* [Установка корневого сертификата на Ubuntu/Debian](https://manuals.gfi.com/en/kerio/connect/content/server-configuration/ssl-certificates/adding-trusted-root-certificates-to-the-server-1605.html).

## Первый запуск

1\. Запустите Ideco Client.

2\. Введите данные:

![](/.gitbook/assets/ideco-client-linux3.png)

* **Имя профиля** - может не совпадать с логином и будет использоваться при выборе профиля для авторизации;
* **Пароль** - укажите пароль пользователя;
* **Логин** и **Хост** - укажите логин и хост в зависимости от количества доменов, в которые введен NGFW:

<details>
<summary>NGFW введен в один домен</summary>

Введите **логин** в домене, в качестве **хоста** укажите домен или IP-адрес.

![](/.gitbook/assets/ideco-client-linux4.png)

</details>

<details>
<summary>NGFW введен в несколько доменов</summary>

Введите **логин** в формате **имя_домена/имя_пользователя**, в качестве **хоста** укажите **IP NGFW**.

![](/.gitbook/assets/ideco-client-linux5.png)

</details>

3\. Нажмите **Сохранить**.

4\. Для авторизации выберите профиль пользователя из выпадающего списка и нажмите **Авторизоваться**:

![](/.gitbook/assets/ideco-client-linux6.png)

## Редактирование профиля

1\. Перейдите в раздел **Настройки**, кликнув по ![](/.gitbook/assets/icon-gear2.png).

2\. Выберите профиль для редактирования, нажав ![](/.gitbook/assets/icon-edit.png), и внесите изменения в поля формы.

3\. Сохраните изменения в полях формы, нажав кнопку **Сохранить**.