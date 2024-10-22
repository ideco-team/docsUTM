# Особенности создания профилей

Принцип создания профилей **Контроля приложений** в 18 версии Ideco NGFW аналогичен принципу создания правил **Контроля приложений** в более ранних версиях: все протоколы и приложения, которые не были запрещены, остаются разрешены.

{% hint style="info" %}
С 18 версии NGFW правила Файрвола, которые блокировали трафик за счет перехвата DNS в предыдущих версиях, не смогут его блокировать. Чтобы это исправить, создайте и включите правила с профилями IPS и DPI в разделе **Правила трафика -> Файрвол -> INPUT**.
{% endhint %}

Для удобства настройки модуля фильтрации рекомендуем объединить пользователей в несколько групп/подгрупп (например, в соответствии с организационной структурой компании) и настроить профиль **Контроля приложений** отдельно для каждой группы.

## Создание профилей и добавление в правила **Файрвола**

**Пример**. Необходимо ограничить доступ к социальным сетям пользователям группы "Бухгалтерия".

### Создание профиля Контроля приложений

1\. Перейдите в раздел **Профили безопасности -> Контроль приложений** и нажмите **Добавить**.

2\. Заполните **Название**, **Комментарий** (необязательно) и добавьте профиль:

![](/.gitbook/assets/application-control6.png)

3\. Нажмите в столбце **Управление** на ![](/.gitbook/assets/icon-edit.png), затем **Доступ к приложениям**. 

4\. Выберите **Социальные сети** (при необходимости используйте поиск). Появится строка с выбором действия:

![](/.gitbook/assets/application-control7.png)

5\. Примените действие **Запретить** рядом со строкой поиска и нажмите **Применить**. Действие применится к выбранным приложениям:

![](/.gitbook/assets/application-control21.png)

{% hint style="info" %}
К неизвестным источникам по умолчанию применяется действие **Разрешить** (доступно для редактирования).
{% endhint %}

6\. Нажмите **Сохранить**.

### Добавление профиля в правила Файрвола

1\. Перейдите в раздел **Правила трафика -> Файрвол -> FORWARD** и нажмите **Добавить**.

2\. Заполните поля:

![](/.gitbook/assets/application-control8.png)

* **Протокол** - выберите протокол, соответствующий трафику, который требуется фильтровать с помощью профиля **Контроля приложений**;
* **Источник** - выберите **Адрес**, **Зону** и **HIP-профиль** источника трафика;
* **Назначение** - выберите **Адрес** и **Зону** назначения трафика;
* **Действие** - выберите **Разрешить**.

3\. Включите опцию **Контроль приложений** и в разделе **Профили для фильтрации** из раскрывающегося списка выберите профиль, запрещающий социальные сети сотрудникам бухгалтерии.

4\. Включите правило или оставьте его выключенным.

5\. Нажмите **Добавить**.

6\. При включенной опции **Перехват пользовательских DNS-запросов** создайте аналогичное правило INPUT.

## Иерархическая структура Профилей контроля приложений

Один из вариантов корректного применения политик безопасности к вложенной структуре пользователей - построение иерархической структуры профилей **Контроля приложений**: 

* Профили для самой большой группы пользователей запрещают наибольшее количество протоколов и приложений;
* Профили для более мелких групп пользователей повторяют запрет для самой большой группы пользователей, но точечно разрешают определенные приложения и протоколы для конкретных подгрупп;
* Профили для конкретных пользователей разрешают определенные протоколы и приложения, необходимые этим конкретным пользователям. В этих профилях также остаются запреты, которые должны сохраниться для этих пользователей.

{% content-ref url="structure.md" %}
[structure.md](structure.md)
{% endcontent-ref %}

Чтобы настроить фильтрацию трафика, для которого в таблице FORWARD нет правил, воспользуйтесь инструкцией:

{% content-ref url="no-rules.md" %}
[no-rules.md](no-rules.md)
{% endcontent-ref %}