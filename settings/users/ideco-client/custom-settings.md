---
description: >-
  Как сделать индивидуальные настройки Ideco Client
---

С помощью конфигурационного файла можно гибко контролировать доступ пользователей через Ideco Clinet, предотвращать изменения важных параметров и обеспечивать соответствие требованиям безопасности.

# Возможности

* Управление профилями Ideco Client через конфигурационный файл;
* Запрет на создание новых профилей (убирает элемент в интерфейсе);
* Запрет сохранять пароль (убирает элемент в интерфейсе);
* Запрет редактирования профиля;
* Установка профиля по умолчанию;
* Автоматический запуск профиля;
* Поддержка Windows, Linux и Mac.

# Виды поддерживаемых профилей

Поддерживаются три типа профилей:

<details>

<summary>Password – требует ввода логина и пароля вручную</summary>

* Если `read_only: false`, то **Логин** всегда отображается в интерфейсе и достуен для редактирования.
* Если login задан в файле конфигурации, его значение должно отображаться в поле **Логин**.
* Если `read_only: true`, профиль нельзя редактировать, но при подключении должен появляться диалог для ввода логина и пароля.
* Автоподключение запрещено `autoconnect=false`, так как пароли не хранятся.
* Если в файле конфигурации указано `type: "password"` и `autoconnect: true`, служба отклонит конфигурацию и запишет ошибку в логи.
* Пользователь может сохранить логин и пароль, если администратор не запретил `deny_save_profile_password=false`.
* Связывание пользовательских данных с файлом конфигурации осуществляется по id.

</details>

<details>

<summary>SSO – использует учетные данные системы</summary>

* Для SSO-профиля поле **Логин** отсутствует в файле конфигурации и не отображается в интерфейсе Ideco Client поскольку аутентификация выполняется автоматически с использованием учетной записи операционной системы.
* Параметры SSO-профиля задаются администратором и не могут быть изменены пользователем.
* Автоподключение возможно `autoconnect=true`, так как аутентификация не требует ввода пароля.
* Если службе не удается выполнить аутентификацию, то в логи будет записана ошибка, а пользователю выведено соответствующее уведомление.
* Связывание профиля с учетной записью пользователя выполняется на основе механизма SSO, без сохранения паролей.

</details>

<details>

<summary>Device – служебный профиль для автоматических подключений</summary>

* Не отображается в интерфейсе Ideco Client.
* Аутентификация осуществляется автоматически, используя идентификатор устройства (MAC, UUID, сертификат).
* Все параметры профиля `server`, `enable_device_vpn`, `cert_data` задаются администратором и не могут быть изменены пользователем.
* Автоподключение всегда включено `autoconnect=true`, так как профиль предназначен для устройств без интерактивного входа.
* В случае ошибки подключения информация запишется в логи.

</details>

# Настройки файла конфигурации

{% hint style="info" %}
Конфигурация задается администратором в json-формате.
{% endhint %}

`profiles` - обязательное поле, без него конфигурация не будет работать.

`gui_client_options` - обязательное поле. Управляет поведением графического интерфейса через модификатор `true` или `false`:

   * `"deny_save_profile_password": true`- запрещает сохранение пароля.
   * `"deny_create_profiles": false`- запрещает создание новых профилей.

## Настройки профилей

`source": "json` - обязательное поле для всех типов профилей.

`id` - уникальный идентификатор профиля. Только для профилей типа Password.

`name` - уникальное название профиля. Только для профилей типа Device и SSO.

`data` - содержит данные для каждого типа профиля:
   * `type` - определяет тип профиля: password, sso или device.
   * `login` - логин пользователя. Только для Password.
   * `server` - адрес сервера. Для всех типов профилей.
   * `enable_device_vpn": true` - активирует DeviceVPN. Только для Device.
   * `cert_data` - путь до корневого сертификата. Только для Device.

`profile_options` - управляет поведением профиля через модификатор `true` или `false`:
   * `autoselect` – устанавливает профиль по умолчанию. Профиль, для которого в  файле конфигурации установлен параметр `autoselect: true`, будет выбран в качестве профиля по умолчанию при запуске клиента. Если этот параметр задан для нескольких профилей, приоритетным станет последний профиль в порядке следования кода конфигурации.
   * `"autoconnect": true` – автоматически подключает профиль при запуске Ideco Client.
   * `"read_only": true` – делает профиль неизменяемым для пользователя.

## Примеры файлов конфигураций

<details>

<summary>Профиль Password</summary>
```
{
    "profiles": [
        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90a0ac6",
            "source": "json",
            "name": "Profile123",
            "data": {
                "login": "user1",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options": {
                "autoselect": true,
                "autoconnect": false,
                "read_only": false
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
</details>

<details>

<summary>Профиль SSO</summary>
```
{
    "profiles": [
        {
            "name": "SSO Profile",
            "source": "json",
            "data": {
                "type": "sso",
                "server": "google.ru"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": false
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
</details>

<details>

<summary>Профиль Device</summary>
```
{
    "profiles": [
        {
            "name": "Device Profile",
            "source": "json",
            "data": {
                "type": "device",
                "enable_device_vpn": true,
                "cert_data": ":/../cert/devicevpn-1.pem",
                "server": "10.1.0.8"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": false
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
</details>

<details>

<summary>Структура конфигурационного файла с несколькими профилями</summary>

В данном примере используется один SSO-профиль, один Device-профиль и два Password-профиля.

```
{
    "profiles":
    [

              {
            "name": "some string name device",
            "source": "json",
            "data":
            {
                "type": "device",
                "enable_device_vpn": true,
                "cert_data" : ":/../cert/devicevpn-1.pem",
                "server": "10.1.0.8"
            },
            "profile_options":
            {
                "autoselect": false,
                "autoconnect": false,
                "read_only": false
            }
        },

        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90a0ac6",
            "source": "json",
            "name": "some string name 1",
            "data":
            {
                "login": "user1",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options":
            {
                "autoselect": true,
                "autoconnect": false,
                "read_only": false
            }
        },

        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90a0ac7",
            "source": "json",
            "name": "some string name 2",
            "data":
            {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options":
            {
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        },

        {
            "name": "some string name sso",
            "source": "json",
            "data":
            {
                "type": "sso",
                "server": "google.ru"
            },
            "profile_options":
            {
                "autoselect": false,
                "autoconnect": false,
                "read_only": false
            }
        }
    ],
    "gui_client_options":
    {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
</details>

# Применение файла конфигурации

1\. Создайте .json файл на машине пользователя и задайте конфуигурацию.

2\. Завершите все процессы IdecoClient. Это необходимо для корректного запуска клиента с новыми настройками.

3\. Установите конфигурацию.

{% hint style="info" %}
Путь к .json файлу конфигурации должен быть абсолютным. Например: C:\Program Files\Ideco\test.json
{% endhint %}

Windows - запустите командную строку с правами администратора и зайдйте конфигурацию:
```
IdecoClient.exe --set-json-config="путь_до_файла_конфигурации"
```
Linux или Mac - откройте терминал и введите команду:
```
sudo IdecoClient --set-json-config="путь_до_файла_конфигурации"
```
3\. Ideco Client выполнит анализ файла.

* Если нет ошибок - сохранит в реестре данные файла конфигурации.
* Если есть ошибки - отправит ответ в Ideco Client список ошибок.

<details>

<summary>Возможные причины ошибок</summary>

* Файл недоступен для чтения;
* Файл конфигурации пустой;
* Файл превышает 1 Мб;
* Файл содержит неопознанные параметры, например опечатки;
* В файле отсутствуют обязательные поля `profiles` и `gui_client_options`;
* Более одного профиля имеет опцию автовыбора;
* Более одного профиля имеет опцию автоподключения;
* Если профиль имеет опцию автоподключения, но не имеет опции автовыбора;
* Наличие более одного DeviceVPN-профиля.
* Идентификаторы не уникальны.

</details>

# Работа с конфигурацией

Удалить конфигурацию:
```
IdecoClient.exe --reset-json-config True
Linux: sudo IdecoClient --reset-json-config True
```

Получить и вывести конфигурацию в консоль:
```
Windows: IdecoClient.exe --print-json-config True
Linux или Mac: sudo IdecoClient --print-json-config True 
```

