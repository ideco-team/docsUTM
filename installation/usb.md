# Подготовка загрузочного диска

{% hint style="info" %}
При записи ISO образа вся информация с USB накопителя будет удалена.
{% endhint %}

{% hint style="info" %}
Подробнее об установке Ideco UTM после создания загрузочного диска можно прочитать в статье [Установка](installation-process.md).
{% endhint %}

Для установки на отдельный сервер нужно подготовить загрузочный USB диск.

## В среде Windows

1\. Скачайте программу [Rufus](https://rufus.ie/ru/) и запустите скачанный файл.

2\. Выберите нужный USB диск в пункте **Устройство**:

![](https://docs.ideco.dev/\~gitbook/image?url=https%3A%2F%2F4217941192-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzELp0pTlLMmCAnvEjR2o%252Fuploads%252Fgit-blob-1e4512526f8648b3aa9a77315c267b2ef0a2087d%252Fpreparation-boot-disk1.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=ef0a52f65e4134cd14debfc9e4f563deb2a1535f43d0d6a8749d43ce86d41ae1)

3\. Выберите метод загрузки **Диск или ISO образ**.

4\. Нажмите на кнопку **Выбрать** и откройте скачанный образ Ideco UTM.

5\. Нажмите **Старт** и в появившемся окне выберите пункт **Запись в режиме DD-образ**.

6\. В диалоговом окне подтвердите запись на USB диск.

Шаги по установке Ideco UTM описаны в статье [Процесс установки](https://docs.ideco.dev/v/v15/installation/installation-process).

### В среде Linux <a href="#v-srede-linux" id="v-srede-linux"></a>

Создать загрузочный USB диск в Linux можно двумя способами:

#### С помощью программы gnome-disks: <a href="#s-pomoshyu-programmy-gnome-disks" id="s-pomoshyu-programmy-gnome-disks"></a>

![](https://docs.ideco.dev/\~gitbook/image?url=https%3A%2F%2F4217941192-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FzELp0pTlLMmCAnvEjR2o%252Fuploads%252Fgit-blob-21db6ca1d5c73d00b07c769971f4eb2a5902d35f%252Fgnome-disks3.png%3Falt%3Dmedia\&width=768\&dpr=4\&quality=100\&sign=a9262c0056d0c82cf3d27b92cef67596a47a83320d46854a1e57d763669bec47)

#### Вручную в терминале: <a href="#vruchnuyu-v-terminale" id="vruchnuyu-v-terminale"></a>

1.  Проверьте целостность образа (хеш-сумма должна совпадать с суммой в личном кабинете):

    Copy

    ```
    md5sum <путь_к_скачанному_загрузочному_образу>
    8c872cb6b720f6fd6683107681645156  /home/ideco/IdecoUTM.iso
    ```
2.  Найдите USB-носитель в системе:

    Copy

    ```
    lsblk --nodeps  -o name,size,fstype,tran,model,mountpoint /dev/sd*

    NAME  SIZE FSTYPE TRAN MODEL        MOUNTPOINT
    sdx   7,5G        usb  USB_DISK_3.0 
    sdx1  7,5G vfat                     /run/media/ideco/D661-82E2
    ```
3.  Отмонтируйте файловую систему:

    Copy

    ```
    sudo umount <точка_монтирования>
    sudo umount /run/media/ideco/D661-82E2
    ```
4.  Запишите образ на носитель:

    Copy

    ```
    sudo dd if=<путь_к_загрузочному_образу> of=<имя_устройства> bs=1M oflag=direct status=progress
    sudo dd if=/home/ideco/IdecoUTM.iso of=/dev/sdx bs=1M oflag=direct status=progress
    ```
5.  Подготовьте носитель к извлечению:

    Copy

    ```
    sudo eject <имя_устройства>
    sudo eject /dev/sdx
    ```
