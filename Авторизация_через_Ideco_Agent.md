# Авторизация через Ideco Agent

Для управления доступом в интернет пользователей с установленной
специализированной программой-агентом. Доступ будет обеспечен
только в то время, когда пользователь авторизован с помощью этой
программы. Программа должна быть установлена на рабочей станции
пользователя или запускаться с удаленного сервера при входе в
систему.

Для авторизации с помощью программы-агента необходимо загрузить
программу с локального web-сайта и сохранить ее в произвольный
каталог. Получить программу-авторизатор Ideco Agent можно на странице
авторизации при входе в систему, в меню справа, как показано ниже
(ссылка появится при включении возможности авторизации через
программу-агент в разделе Сервисы - Авторизация пользователей).

  

Необходимым условием успешной авторизации с помощью IdecoAgent является
указание в настройках сетевой карты в качестве шлюза и в качестве
сервера DNS локального адреса интернет-шлюза Ideco UTM. При
необходимости нужно разрешить в межсетевом экране подключение на
сетевой порт 800/TCP из внутренней сети.

После запуска программы необходимо ввести логин и пароль пользователя.
Состояние авторизации отображается иконкой в системном лотке.
Возможные состояния представлены в следующей таблице.

<div class="table-wrap">

Индикация статуса соединения в Ideco-агент

</div>

![](attachments/1278079/1441882.png)

Программа не активна

![](attachments/1278079/1441881.png)

Идет подключение к серверу

![](attachments/1278079/1441880.png)

Доступ в интернет разрешен

![](attachments/1278079/1441879.png)

Сработал лимит предупреждения

![](attachments/1278079/1441878.png)

Сработал лимит отключения

![](attachments/1278079/1441877.png)

Произошла ошибка. Доступ в интернет запрещен.

В контекстном меню иконки доступны пункты, описанные в таблице ниже.

<div class="table-wrap">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Пункт меню</th>
<th>Значение</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Подключить</td>
<td><p>Отображение диалога подключения.</p>
<p><br />
</p></td>
</tr>
<tr class="even">
<td>Отключить</td>
<td>Отключиться от сервера.</td>
</tr>
<tr class="odd">
<td>Информация</td>
<td><p>Отобразить информацию о подключении к интернет.</p>
<p><br />
</p></td>
</tr>
<tr class="even">
<td>Запускаться при входе в систему</td>
<td>Установить автоматический запуск программы при входе в Windows.</td>
</tr>
<tr class="odd">
<td>О программе</td>
<td><p>Вывод информации о программе авторизации.</p>
<p><br />
</p></td>
</tr>
</tbody>
</table>

</div>

<div>

<div>

  - При использовании Ideco Agent в домене Active Directory
    рекомендуется расположить IdecoAgent.exe на общем
    сетевом ресурсе и установить в политике входа в домен запуск
    приложения IdecoAgent.exe с ключом domain. Таким образом, запуск
    агента будет централизован, и не потребуется его установка на
    каждый компьютер.
  - При смене локального адреса Ideco UTM обязательно нужно повторно
    скачать Ideco Agent с сайта, поскольку локальный адрес сервера
    встраивается в приложение при скачивании.

</div>

</div>

**

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" data-align="left">

![](images/icons/bullet_blue.gif)
[agent\_12.png](attachments/1278079/1441876.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_6.png](attachments/1278079/1441877.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_5.png](attachments/1278079/1441878.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_4.png](attachments/1278079/1441879.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_3.png](attachments/1278079/1441880.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_2.png](attachments/1278079/1441881.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent\_1.png](attachments/1278079/1441882.png) (image/png)  
![](images/icons/bullet_blue.gif)
[download\_agent.png](attachments/1278079/6062176.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent1.png](attachments/1278079/6062181.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent2.png](attachments/1278079/6062182.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent3.png](attachments/1278079/6062183.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent1.png](attachments/1278079/6062178.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent2.png](attachments/1278079/6062179.png) (image/png)  
![](images/icons/bullet_blue.gif)
[agent3.png](attachments/1278079/6062180.png) (image/png)  
![](images/icons/bullet_blue.gif)
[profile.png](attachments/1278079/6062185.png) (image/png)  
![](images/icons/bullet_blue.gif)
[profile.png](attachments/1278079/6062184.png) (image/png)  
![](images/icons/bullet_blue.gif) [Скачать
agent.png](attachments/1278079/11436165.png) (image/png)  
![](images/icons/bullet_blue.gif) [логин и
пароль.png](attachments/1278079/11436167.png) (image/png)  
![](images/icons/bullet_blue.gif) [Инфа о
квоте.png](attachments/1278079/11436168.png) (image/png)  
![](images/icons/bullet_blue.gif) [О
прграмме.png](attachments/1278079/11436169.png) (image/png)  
![](images/icons/bullet_blue.gif) [о
проге.png](attachments/1278079/11436171.png) (image/png)  

</div>
