# Регистрация сервера 

{% hint style="info" %}
Для активации лицензии необходима обязательная регистрация сервера в [личном кабинете](https://my.ideco.ru/#/login/?next=/utm/license/).
{% endhint %}

## Онлайн-регистрация

{% hint style="warning" %}
Для привязки лицензии сервер должен иметь выход в интернет.
{% endhint %}

Шаги онлайн-регистрации сервера и привязки лицензии:

1\. Перейдите в веб-интерфейс Ideco NGFW в раздел **Управление сервером -> Лицензия**, выберите **Автоматическое обновление** в качестве способа обновления, нажмите **Сохранить**. 

![](/.gitbook/assets/license.png)

2\. Нажмите **Зарегистрировать**.

3\. В открывшемся окне выберите компанию и нажмите **Добавить**. После добавления нажмите **Обновить информацию о лицензии** для проверки состояния лицензии:

![](/.gitbook/assets/license.gif)

## Оффлайн-регистрация

Шаги оффлайн-регистрации сервера и привязки лицензии:

1\. В веб-интерфейсе Ideco NGFW перейдите в раздел **Управление сервером -> Лицензия** и выберите **Ручная загрузка** в качестве способа обновления.

2\. Скачайте файл со ссылкой на регистрацию сервера, нажав на кнопку:

![](/.gitbook/assets/license1.png)

3\. На устройстве с доступом к интернету перейдите по ссылке из файла, скачанного в пункте 2. Сервер автоматически появится в списке серверов в [MY.IDECO](https://my.ideco.ru/).

4\. Обратитесь к вашему менеджеру для предоставления лицензии. 

5\. В личном кабинете MY.IDECO перейдите в раздел **NGFW -> Лицензирование** и нажмите **Привязать лицензию** рядом с нужным сервером. Пример наименования сервера для оффлайн-регистрации: `UTM (UTM Unknown)`.  

Если была выбрана лицензия, не подходящая для оффлайн-регистрации сервера, то появится ошибка:

![](/.gitbook/assets/initial-setup13.png)

6\. Нажмите на ![](/.gitbook/assets/icon-download.png) напротив названия сервера.

7\. Выберите версию Ideco NGFW:

![](/.gitbook/assets/my-ideco-ngfw.png)

8\. Скачайте файлы, нажав на соответствующие ссылки в открывшейся форме:

![](/.gitbook/assets/my-ideco-ngfw1.png)

9\. В веб-интерфейсе Ideco NGFW перейдите в раздел **Управление сервером -> Лицензия** и загрузите файл с лицензией, скачанный в пункте 8:

![](/.gitbook/assets/license2.png)

## Оффлайн-обновление баз модулей безопасности

Чтобы обновить базы модулей безопасности в режиме оффлайн, перейдите в веб-интерфейс Ideco NGFW в раздел **Управление сервером -> Обновления -> Базы фильтрации** и загрузите скачанные в пункте 8 [Оффлайн-регистрации](/installation/server-registration.md#оффлайн-регистрация) файлы, нажав на соответствующие кнопки:

![](/.gitbook/assets/selfupdate.png)

{% hint style="danger" %}
Базы фильтрации Ideco NGFW могут меняться ежедневно, поэтому при ручной загрузке обновляйте их как можно чаще.
{% endhint %}