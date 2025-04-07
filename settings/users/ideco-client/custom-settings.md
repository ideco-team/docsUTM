---
description: >-
  В статье рассказывается, как модифицировать Ideco Client, если необходимы индивидуальные правила работы с пользовательскими профилями. 
---

# Кастомная настройка Ideco Client

Для авторизации пользователей Ideco Client использует профили, состоящие из логина и пароля. По умолчанию пользователь может создавать, удалять, редактировать профили и сохранять пароль для автоматической авторизации. Кастомная настройка позволит администратору создавать готовые конфигурации, а также ограничить права пользователей на управление профилями.


## Возможности кастомной настройки

* Запрет на создание новых профилей;
* Запрет на сохранение пароля;
* Запрет на редактирование профиля;
* Установка профиля по умолчанию;
* Автоматическое подключение выбранного профиля при запуске Ideco Client.

## Параметры файла конфигурации

Файл конфигурации создается администратором на пользовательской машине в формате .json, устанавливается через командную строку/терминал и поддерживает два типа профилей:

* Password - пользователь подключается по логину и паролю (только для Windows);
* SSO - пользователь для подключения использует данные системы.

Пример файла конфигурации, в котором заданы Password-профиль и SSO-профиль:

```
{
    "profiles":
    [

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

<details>

<summary>Описание настроек конфигурационного файла</summary>

* `"profiles"` - обязательное поле, без него конфигурация не будет работать;
* `"id"` - обязательный уникальный идентификатор профиля, который администратор придумывает и задаёт вручную. Используется для идентификации профиля при редактировании. Не передается в NGFW. Только для Password;
* `"source": "json"` - обязательное поле для всех типов профилей;
* `"name"` - уникальное название профиля;
* `"data"` - содержит данные для каждого типа профиля:
    * `"login"` - логин пользователя. Только для Password;
    * `"type"` - определяет тип профиля: password или sso;
    * `"server"` - адрес сервера. Для всех типов профилей.
* `"profile_options"` - настройки профиля:
    * `"autoselect"` - отвечает за установку профиля по умолчанию:
        * `true` - профиль будет выбран в качестве профиля по умолчанию при запуске Ideco Client;
        * `false` - профиль не выбран в качестве профиля по умолчанию.
    * `"autoconnect"` - отвечат за автоподключение профиля при запуске Ideco Client:
        * `true` - профиль будет автоматически подключаться при запуске Ideco Client;
        * `false` - профиль не будет автоматически подключаться при запуске Ideco Client.
    * `"read_only"` - отвечает за то, может ли пользователь редактировать или удалять профиль:
        * `true` - профиль нельзя редактировать или удалять;
        * `false` - профиль можно редактировать или удалять.
* `"gui_client_options"` - обязательное поле. Управляет поведением графического интерфейса:
    * `"deny_save_profile_password"`- разрешает или запрещает сохранение пароля:
        * `true` - пользователь не сможет сохранить пароль. Ideco Client будет запрашивать пароль при каждом подключении;
        * `false` - пользователь может сохранять пароль в Ideco Client.
    * `"deny_create_profiles"`- разрешает или запрещает создание новых профилей:
        * `true`- пользователь может создавать новые профили в Ideco Client;
        * `false`- пользователь не сможет создавать новые профили в Ideco Client.

</details>

Особенности работы профилей:

{% tabs %}

{% tab title="Password" %}

* Если логин пользователя задан в файле конфигурации в поле `"login"`, то его значение будет отображаться в поле Логин в Ideco Client;
* Если `"deny_save_profile_password": true`, то автоподключение должно быть запрещено `"autoconnect": false`, так как пароли не хранятся;
* Если `"deny_save_profile_password": true` и `"autoconnect": true`, то служба отклонит конфигурацию и запишет ошибку в логи;
* Если у нескольких профилей будет задан параметр автовыбора `"autoselect": true`, то выбран будет самый нижний профиль в файле конфигурации;
* Связывание пользовательских данных с файлом конфигурации осуществляется по `"id"` пользователя.

{% endtab %}

{% tab title="SSO" %}

* Для SSO-профиля `"login"` отсутствует в файле конфигурации и поле Логин не отображается в интерфейсе Ideco Client, поскольку аутентификация выполняется автоматически с использованием учетной записи операционной системы;
* Параметры SSO-профиля задаются администратором и не могут быть изменены пользователем;
* Автоподключение возможно `"autoconnect": true`, так как аутентификация не требует ввода пароля;
* Если службе не удается выполнить аутентификацию, то в логи будет записана ошибка, а пользователю - выведено соответствующее уведомление;
* Связывание профиля с учетной записью пользователя выполняется на основе механизма SSO, без сохранения паролей.

{% endtab %}

{% endtabs %}

## Применение файла конфигурации

1\. Создайте .json файл на машине пользователя.

2\. Задайте необходимую конфигурацию.

3\. Завершите все процессы Ideco Client. Это необходимо для корректного запуска с новыми настройками.

4\. Установите конфигурацию.

{% hint style="info" %}
Путь к .json файлу конфигурации должен быть абсолютным. Например: C:\Program Files\Ideco\test.json
{% endhint %}

{% tabs %}

{% tab title="Windows" %}

Откройте командную строку от имени администратора и выполните команду:

```
IdecoClient.exe --set-json-config="путь_до_файла_конфигурации"
```

{% endtab %}

{% tab title="Linux или MacOS" %}

Откройте терминал и выполните команду:

```
sudo IdecoClient --set-json-config="путь_до_файла_конфигурации"
```

{% endtab %}

{% endtabs %}


5\. Ideco Client выполнит анализ файла:

* Если нет ошибок - сохранит в реестре данные файла конфигурации;
* Если есть ошибки - отправит в лог службы список ошибок.

<details>

<summary>Возможные причины ошибок</summary>

* Файл недоступен для чтения;
* Файл конфигурации пустой;
* Размер файла превышает 1 Мб;
* Файл содержит неопознанные параметры, например опечатки;
* В файле отсутствуют обязательные поля `"profiles"` и `"gui_client_options"`;
* Более одного профиля имеет опцию автовыбора `"autoselect": true`;
* Более одного профиля имеет опцию автоподключения `"autoconnect": true`;
* Если профиль имеет опцию автоподключения `"autoconnect": true`, но не имеет опции автовыбора `"autoselect": true`;
* В файле конфигурации в рамках Password-профиля указано `"deny_save_profile_password": true` и `"autoconnect": true`;
* Поля `"name"` или `"id"` не уникальны.

</details>

## Работа с конфигурацией

Получить и вывести конфигурацию в консоль:

{% tabs %}

{% tab title="Windows" %}

Откройте командную строку с правами администратора и выполните команду:

```
IdecoClient.exe --print-json-config True
```

{% endtab %}

{% tab title="Linux или MacOS" %}

Откройте терминал и выполните команду:

```
sudo IdecoClient --print-json-config True
```

{% endtab %}

{% endtabs %}

Удалить конфигурацию:

{% tabs %}

{% tab title="Windows" %}

Откройте командную строку с правами администратора и выполните команду:

```
IdecoClient.exe --reset-json-config True
```

{% endtab %}

{% tab title="Linux или MacOS" %}

Откройте терминал и выполните команду:

```
sudo IdecoClient --reset-json-config True
```

{% endtab %}

{% endtabs %}

### Примеры настроек файла конфигурации

<details>

<summary>Запретить пользователю редактировать преднастроенный профиль</summary>

![](/.gitbook/assets/custom-settings1.png)

Профиль **some string name 2** создан в файле конфигурации и его запрещено редактировать или удалять, так как у него стоит настройка `"read_only": true`.

Профили **some string name 1** и **some string name 3** созданы пользователем самостоятельно и их можно редактировать или удалять.

```
{
    "profiles": [
        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6",
            "source": "json",
            "name": "some string name 2",
            "data": {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
* `"profiles":` - обязательное поле, без него конфигурация не будет работать;
* `"id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6"` - уникальный идентификатор профиля. Только для Password.
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 2"` - название профиля some string name 2;
* `"data":` - содержит данные профиля:
    * `"login": "user2"` - логин пользователя user2;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"gui_client_options":` - управляет поведением графического интерфейса:
    * `"deny_save_profile_password": false` - так как false, то пользователь может сохранять пароль в Ideco Client;
    * `"deny_create_profiles": false` - так как false, то пользователь может вручную создавать новые профили в Ideco Client.

</details>

<details>

<summary>Задать профиль, который будет выбран по умолчанию при запуске Ideco Client</summary>

Файл конфигурации содержит два профиля **some string name 1** и **some string name 2**. Чтобы профилем по умолчанию был выбран **some string name 1**, в файле конфигурации у данного профиля, необходимо указать `"autoselect": true`.


![](/.gitbook/assets/custom-settings4.png)

Настройка файла конфигурации:

```
{
    "profiles": [
        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6",
            "source": "json",
            "name": "some string name 2",
            "data": {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        },

        {
            "id": "a78cb502-f0d5-4ce5-84ab-a127a90a0ac7",
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
                "read_only": true
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": false
    }
}
```
* `"profiles":` - обязательное поле, без него конфигурация не будет работать;
* `"id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6"` - уникальный идентификатор профиля. Только для Password;
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 2"` - название профиля some string name 2;
* `"data":` - содержит данные профиля:
    * `"login": "user2"` - логин пользователя user2;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"id": "a78cb502-f0d5-4ce5-84ab-a127a90a0ac7"` - уникальный идентификатор профиля. Только для Password;
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 1"` - название профиля some string name 1;
* `"data":` - содержит данные профиля:
    * `"login": "user1"` - логин пользователя user1;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": true` - так как true, профиль будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"gui_client_options":` - управляет поведением графического интерфейса:
    * `"deny_save_profile_password": false` - так как false, то пользователь может сохранять пароль в Ideco Client;
    * `"deny_create_profiles": false` - так как false, то пользователь может вручную создавать новые профили в Ideco Client.

</details>

<details>

<summary>Создать три профиля, которые нельзя изменить или удалить. Запретить создавать новые профили</summary>

Файл конфигурации содержит три профиля **some string name 1**, **some string name 2**, **some string name 3** Чтобы их нельзя было отредактировать или удалить, всем профилям необходимо указать `"read_only": true`.
Чтобы запретить пользователю создавать новые профили необходимо указать: `"deny_create_profiles": true`.

![](/.gitbook/assets/custom-settings5.png)

Настройка файла конфигурации:

```
{
    "profiles": [
        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6",
            "source": "json",
            "name": "some string name 2",
            "data": {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        },

        {
            "id": "a78cb502-f0d5-4ce5-84ab-a127a90a0ac7",
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
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        },

        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7asd4123",
            "source": "json",
            "name": "some string name 2",
            "data": {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
            },
            "profile_options": {
                "autoselect": false,
                "autoconnect": false,
                "read_only": true
            }
        }
    ],
    "gui_client_options": {
        "deny_save_profile_password": true,
        "deny_create_profiles": true
    }
}
```
* `"profiles":` - обязательное поле, без него конфигурация не будет работать;

* `"id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6"` - уникальный идентификатор профиля.
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 2"` - название профиля some string name 2;
* `"data":` - содержит данные профиля:
    * `"login": "user2"` - логин пользователя user2;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"id": "a78cb502-f0d5-4ce5-84ab-a127a90a0ac7"` - уникальный идентификатор профиля;
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 1"` - название профиля some string name 1;
* `"data":` - содержит данные профиля:
    * `"login": "user1"` - логин пользователя user1;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * ``"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"id": "a78cb502-f0d5-4ce5-84ab-aaf7asd4123"` - уникальный идентификатор профиля;
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 1"` - название профиля some string name 1;
* `"data":` - содержит данные профиля:
    * `"login": "user1"` - логин пользователя user1;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": true` - так как true, запрещает редактировать и удалять профиль.
* `"gui_client_options":` - управляет поведением графического интерфейса:
    * `"deny_save_profile_password": false` - так как false, то пользователь может сохранять пароль в Ideco Client;
    * `"deny_create_profiles": true` - так как true, то пользователь не сможет создавать новые профили в Ideco Client.

</details>

<details>

<summary>Запретить сохранять пароль. Ideco Client будет запрашивать пароль при каждом подключении</summary>

Чтобы запретить пользователюю сохранять пароль в Ideco Client, необходимо в файле конфигурации указать `"deny_save_profile_password": true`. 

![](/.gitbook/assets/custom-settings2.png)

Настройка файла конфигурации:

```
{
    "profiles": [
        {
            "id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6",
            "source": "json",
            "name": "some string name 2",
            "data": {
                "login": "user2",
                "type": "password",
                "server": "10.20.30.40"
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
* `"profiles":` - обязательное поле, без него конфигурация не будет работать;
* `"id": "a78cb502-f0d5-4ce5-84ab-aaf7a90kkac6"` - уникальный идентификатор профиля. Только для Password;
* `"source": "json"` - обязательное поле, без него конфигурация не будет работать;
* `"name": "some string name 2"` - название профиля some string name 2;
* `"data":` - содержит данные профиля:
    * `"login": "user2"` - логин пользователя user2;
    * `"type": "password"` - тип профиля Password;
    * `"server": "10.20.30.40"` - IP-адрес сервера Ideco NGFW.
* `"profile_options":` - настройки профиля:
    * `"autoselect": false` - так как false, профиль не будет профилем по умолчанию;
    * `"autoconnect": false` - так как false, профиль не будет подключаться автоматически при запуске Ideco Client;
    * `"read_only": false` - так как true, запрещает редактировать и удалять профиль.
* `"gui_client_options":` - управляет поведением графического интерфейса;
    * `"deny_save_profile_password": true` - так как true, то пользователь не может сохранять пароль в Ideco Client;
    * `"deny_create_profiles": false` - так как false, то пользователь может вручную создавать новые профили в Ideco Client.

</details>