---
description: >-
    В статье рассказывается о работе и создании профилей Антивируса в Ideco NGFW.
---
# Антивирус

{% hint style="success" %}
Название службы раздела **Антивирус**: `ideco-av-backend`. \
Список имен служб для других разделов доступен по [ссылке](/settings/server-management/terminal/README.md).
{% endhint %}

Антивирус в продукте создан на базе Kaspersky Anti-Virus Software Development Kit. Для включения модуля перейдите в раздел **Профили безопасности -> Антивирус**:

![](/.gitbook/assets/antivirus.png)

Антивирус приобретается отдельно от Ideco NGFW, использование может быть ограничено условиями лицензии. Для покупки обратитесь в [отдел продаж](https://ideco.ru/kontakty).

{% hint style="info" %}
Корпоративные ключи, предназначенные для других продуктов Лаборатории Касперского, нельзя использовать для активации антивируса.
{% endhint %}

**Антивирус** связан с прокси-сервером и **Контент-фильтром**, поэтому фильтрует веб-трафик при выполнении следующих условий:

* В разделе [**Контент-фильтр**](/settings/access-rules/content-filter/README.md) настроена расшифровка веб-трафика. HTTPS-сайт проверяется только в случае расшифровки HTTPS-трафика **Контент-фильтром**. Рекомендации по настройке фильтрации HTTPS представлены в [статье](/settings/access-rules/content-filter/filtering-https-traffic.md);
* Веб-ресурс не находится в списках исключений прокси-сервера по назначению;
* Пользователь, к которому поступает трафик, не добавлен в исключения прокси-сервера по источнику.

Чтобы трафик фильтровался модулем **Антивирус**, создайте правило в разделе [**Контент-фильтр**](/settings/access-rules/content-filter/rules.md), содержащее нужный профиль **Антивируса**.

{% hint style="danger" %}
Если профиль не добавлен в правила **Контент-фильтра**, трафик не будет фильтроваться **Антивирусом**.
{% endhint %}

Результат проверки трафика антивирусом представлен в [Журнале веб-трафика](/settings/reports/web-traffic-log.md).

## Профили

Для создания профиля выполните действия:

1\. Нажмите **Добавить** и заполните поля на вкладке **Настройки**:

![](/.gitbook/assets/antivirus3.png)

<details>

<summary>Расшифровка полей</summary>

* **Название** - название профиля;
* **Комментарий** - произвольный текст, поясняющий цель действия профиля. Значение не должно быть длиннее 255 символов;
* **Настройки эвристического анализа** - включение методов для обнаружения новых и неизвестных вредоносных программ:
  * **Уровень глубины**:
    * Легкий - уровень сканирования поверхностный;
    * Средний - уровень сканирования средний (уровень по умолчанию);
    * Глубокий - уровень сканирования детализированный;
    * Максимальный - уровень сканирования максимально детализированный.
  
**Важно**: Чем выше уровень, тем больше ресурсов системы требуется и дольше длится сканирование.

* **Дополнительно**:
  * **Максимальное время проверки** - время в секундах на проверку одного файла;
  * **Максимальный размер проверяемого файла** - максимальный объем проверяемого файла в МБ.
* **Блокировать вредоносные ссылки** - проверка URL по базе вредоносных ссылок Web Malicious URL Filtering (WMUF);
* **Блокировать скачивание файла при неудачной проверке** - блокирование файла при неудачной проверке.

</details>

2\. Перейдите на вкладку **Блокировка вредоносного контента** и укажите контент, который должен быть заблокирован:

![](/.gitbook/assets/antivirus4.png)

<details>

<summary>Тип блокируемого контента</summary>

* **Документ, содержащий макрос** - объект, содержащий макросы Microsoft Office;
* **Зашифрованный объект** - объект, защищенный алгоритмом шифрования;
* **Парольные архивы** - запароленный архив;
* **Вредоносное ПО** - вредоносные инструменты, трояны, неопознанное вредоносное ПО высокой или средней опасности и другие категории, указанные в [дереве классификации](https://encyclopedia.kaspersky.com/knowledge/the-classification-tree/);
* **Условно опасное ПО** - рекламное ПО (Adware), порнографическое (Pornware) или потенциально опасное (Riskware), указанное в [дереве классификации](https://encyclopedia.kaspersky.com/knowledge/the-classification-tree/).

Тип блокируемого контента в файловом формате (**Архивные файлы**, **Исполняемые файлы**, **Мультимедиа файлы**, **Офисные файлы**, **Текстовые файлы**, **Файлы баз данных**, **Файлы веб-архивов**) и **Прочие форматы** указаны в таблице **Подробное описание типов файлов** ниже.

</details>

<details>

<summary>Подробное описание типов файлов</summary>

| Категория | Подкатегория | Формат | Описание | Расширение | MIME-тип |
|----------|-------------|--------|-------------|------------|------|
| Текстовые файлы |  | GENERAL_CSV | Comma-separated Values | csv | text/csv |
| Текстовые файлы |  | GENERAL_HTML | HyperText Markup Language or fragments of HTML | htm; html | text/html |
| Текстовые файлы |  | GENERAL_HTML_STRICT | HyperText Markup Language standalone document (generally with doctype or html tags) | htm; html | text/html |
| Текстовые файлы |  | GENERAL_TXT | Plain Text | txt | text/plain |
| Текстовые файлы |  | GENERAL_XML | Extensible Markup Language (XML) | xml | text/xml; application/xml |
| Текстовые файлы |  | TEXT_REG | Windows registry editor script | reg |  |
| Мультимедиа файлы | Audio | AUDIO_AAC | Advanced Audio Coding | aac; m4a | audio/aac; audio/mp4 |
| Мультимедиа файлы | Audio | AUDIO_AC3 | AC3 multichannel audio | ac3 | audio/ac3 |
| Мультимедиа файлы | Audio | AUDIO_APE | Monkey&apos; s Audio (APE) | ape | audio/x-monkeys-audio; application/x-extension-ape |
| Мультимедиа файлы | Audio | AUDIO_CDA | CD digital Audio | cda | application/x-cdf |
| Мультимедиа файлы | Audio | AUDIO_FLAC | Free Lossless Audio Codec (FLAC) | flac | audio/x-flac; application/x-flac; audio/flac |
| Мультимедиа файлы | Audio | AUDIO_MIDI | MIDI | mid; midi | audio/mid |
| Мультимедиа файлы | Audio | AUDIO_MKA | Matroska Audio | mka | audio/x-matroska |
| Мультимедиа файлы | Audio | AUDIO_MP3 | MPEG-1 Layer 3 | mp3 | audio/x-mpeg; audio/mp3; audio/x-mp3; audio/mpeg3; audio/x-mpeg3; audio/mpeg; audio/x-mpg; audio/x-mpegaudio |
| Мультимедиа файлы | Audio | AUDIO_OGG | OGG Vorbis Audio | ogg | audio/x-ogg; application/x-ogg |
| Мультимедиа файлы | Audio | AUDIO_RA | RealAudio | rm; ra; ravb | audio/vnd.rn-realaudio |
| Мультимедиа файлы | Audio | AUDIO_WAV | Microsoft Wave | wav | audio/x-wav |
| Мультимедиа файлы | Audio | AUDIO_WEB_M | WebM Audio | webm; weba | audio/webm |
| Мультимедиа файлы | Audio | AUDIO_WMA | Windows Media Audio | wma |  |
| Мультимедиа файлы | Image | IMAGE_BMP | Windows Bitmap (DIB) | bmp | image/bmp |
| Мультимедиа файлы | Image | IMAGE_CDR | Corel Draw | cdr |  |
| Мультимедиа файлы | Image | IMAGE_EMF | Windows Meta-File | emf; wmf |  |
| Мультимедиа файлы | Image | IMAGE_EPS | Post-Script Format | eps | application/postscript |
| Мультимедиа файлы | Image | IMAGE_GIF | GIF | gif | image/gif |
| Мультимедиа файлы | Image | IMAGE_JPEG | JPEG/JFIF | jpg; jpe; jpeg; jff | image/jpeg |
| Мультимедиа файлы | Image | IMAGE_PNG | Portable Graphics | png | image/png |
| Мультимедиа файлы | Image | IMAGE_PSD | Adobe Photoshop | psd |  |
| Мультимедиа файлы | Image | IMAGE_TIFF | Targa Image File Format | tif; tiff | image/tif; image/tiff |
| Мультимедиа файлы | Image | IMAGE_WEBP | WebP | webp | image/webp |
| Мультимедиа файлы |  | MULTIMEDIA_SWF | ShockWave Flash | swf | application/x-shockwave-flash |
| Мультимедиа файлы | Video | VIDEO_3GPP | MPEG4 ISO format | 3gp; 3g2; 3gp2; 3p2 |  |
| Мультимедиа файлы | Video | VIDEO_ASF | Microsoft Container | asf; wmv | video/x-ms-asf |
| Мультимедиа файлы | Video | VIDEO_AVI | Audio/Video Interleave | avi | video/avi; video/msvideo; video/x-msvideo |
| Мультимедиа файлы | Video | VIDEO_BIK | Bink Video | bik |  |
| Мультимедиа файлы | Video | VIDEO_DIVX | MPEG4 | divx; mp4; m4v | video/mp4; video/divx; video/x-m4v |
| Мультимедиа файлы | Video | VIDEO_F4V | f4v | f4v | video/x-flv |
| Мультимедиа файлы | Video | VIDEO_FLV | Adobe Flash Video | flv | video/x-flv; video/mp4; video/x-m4v |
| Мультимедиа файлы | Video | VIDEO_MKV | Matroska Video | mkv | video/x-matroska |
| Мультимедиа файлы | Video | VIDEO_MOV | Apple Quicktime | mov; qt | video/quicktime |
| Мультимедиа файлы | Video | VIDEO_RM | RealMedia CB/VB | rm; rmvb | video/vnd.rn-realvideo |
| Мультимедиа файлы | Video | VIDEO_RTMP | Real Time Messaging Protocol Message |  | application/x-fcs |
| Мультимедиа файлы | Video | VIDEO_VOB | MPEG1 (VCD) / MPEG2 (DVD) format | vob; dat; mpg; mpeg | video/mpeg; video/dvd; video/x-vob |
| Мультимедиа файлы | Video | VIDEO_WEB_M | WebM Video | webm | video/webm |
| Исполняемые файлы | Executable | EXECUTABLE_APK | Android Application Package | apk | application/vnd.android.package-archive |
| Исполняемые файлы | Executable | EXECUTABLE_APPLE_SCRIPT | AppleScript Files | scpt; AppleScript |  |
| Исполняемые файлы | Executable | EXECUTABLE_BAT | Command Line Script | cmd; bat | application/x-msdos-batch |
| Исполняемые файлы | Executable | EXECUTABLE_COM | COM - MS-DOS Application | com |  |
| Исполняемые файлы | Executable | EXECUTABLE_DEB | Debian Software Package | deb | application/x-deb |
| Исполняемые файлы | Executable | EXECUTABLE_DEX | Dalvik Executable Format | dex; odex |  |
| Исполняемые файлы | Executable | EXECUTABLE_DOS | "DOS |  Win-16 |  OS/2 - all executables based on exe except PE" | exe; dll | application/octet-stream; application/x-msdownload; application/exe; application/x-exe; application/dos-exe; vms/exe |
| Исполняемые файлы | Executable | EXECUTABLE_DOS_NE_RESOURCE | "DOS |  Win-16 |  OS/2 - NE Resource Only Library" | dll; fon | application/octet-stream; application/x-msdownload; application/exe; application/x-exe; application/dos-exe; vms/exe |
| Исполняемые файлы | Executable | EXECUTABLE_ELF | Executable and Linkable Format | o; so; elf; prx |  |
| Исполняемые файлы | Executable | EXECUTABLE_JAVA | Java Class File | class |  |
| Исполняемые файлы | Executable | EXECUTABLE_JS | JavaScript | js | text/javascript; application/javascript |
| Исполняемые файлы | Executable | EXECUTABLE_MACHO | Mach object file format |; o; dylib |  |
| Исполняемые файлы | Executable | EXECUTABLE_MSI | Microsoft Installer Archive | msi |  |
| Исполняемые файлы | Executable | EXECUTABLE_PYC | Python Bytecode | pyc; pyo |  |
| Исполняемые файлы | Executable | EXECUTABLE_RPM | RPM Package | rpm | application/x-rpm |
| Исполняемые файлы | Executable | EXECUTABLE_SCRIPTS | Unix Scripts | sh; pl |  |
| Исполняемые файлы | Executable | EXECUTABLE_VBS | Visual Basic Script | vbs; vb | text/vbscript |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE | Win32 PE | exe; dll; ocx; scr | application/octet-stream; application/x-msdownload; application/exe; application/x-exe; vms/exe; application/x-winexe |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE_DLL | Win32 PE Dynamic Library | dll; ocx; scr | application/octet-stream; application/x-msdownload; application/x-exe |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE_EXE | Win32 PE Executable File | exe | application/octet-stream; application/exe; application/x-exe; vms/exe; application/x-winexe |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE_EXEUI | Win32 PE Executable File for Windows GUI/CUI and POSIX Subsystems | exe | application/octet-stream; application/exe; application/x-exe; vms/exe; application/x-winexe |
| Исполняемые файлы | .Net | EXECUTABLE_WIN32PE_ILLIBRARY | Win32 PE .Net IL Library | exe; dll; ocx; scr | application/octet-stream; application/x-msdownload; application/exe; application/x-exe |
| Исполняемые файлы | .Net | EXECUTABLE_WIN32PE_ILONLY | Win32 PE .Net IL (Only) | exe; dll; ocx; scr | application/octet-stream; application/x-msdownload; application/exe; application/x-exe |
| Исполняемые файлы | .Net | EXECUTABLE_WIN32PE_NET | Win32 PE .Net | exe; dll; scr | application/octet-stream; application/x-msdownload; application/exe; application/x-exe |
| Исполняемые файлы | .Net | EXECUTABLE_WIN32PE_NET_RESOURCE_WITH_POSSIBLE_TRIVIAL_CODE | Win32 PE .Net Resource Only Library (May contain trival code) | dll | application/octet-stream; application/x-msdownload; application/x-exe |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE_RESOURCE | Win32 PE Resource Only Library | dll | application/octet-stream; application/x-msdownload; application/x-exe |
| Исполняемые файлы | Windows | EXECUTABLE_WIN32PE_SYS | Win32 PE File for Native Subsystem | sys | application/octet-stream |
| Исполняемые файлы | Windows | EXECUTABLE_WINDOWS_SHELLLINK | MS Windows shell links | lnk |  |
| Офисные файлы | Microsoft Office | MSOFFICE_DOC | Microsoft Word Document 97-2003 | doc | application/msword |
| Офисные файлы | Microsoft Office | MSOFFICE_DOCM | Microsoft Word Macro-Enabled Document | docm | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| Офисные файлы | Microsoft Office | MSOFFICE_DOCX | Microsoft Word Document | docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| Офисные файлы | Microsoft Office | MSOFFICE_DOT | Microsoft Word Template 97-2003 | dot | application/msword |
| Офисные файлы | Microsoft Office | MSOFFICE_DOTM | Microsoft Word Macro-Enabled Template | dotm | application/vnd.openxmlformats-officedocument.wordprocessingml.template |
| Офисные файлы | Microsoft Office | MSOFFICE_DOTX | Microsoft Word Template | dotx | application/vnd.openxmlformats-officedocument.wordprocessingml.template |
| Офисные файлы | Microsoft Office | MSOFFICE_POTM | Microsoft PowerPoint Macro-Enabled Template | potm | application/vnd.openxmlformats-officedocument.presentationml.template |
| Офисные файлы | Microsoft Office | MSOFFICE_POTX | Microsoft PowerPoint Template | potx | application/vnd.openxmlformats-officedocument.presentationml.template |
| Офисные файлы | Microsoft Office | MSOFFICE_PPSM | Microsoft PowerPoint Macro-Enabled Slide Show | ppsm | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| Офисные файлы | Microsoft Office | MSOFFICE_PPSX | Microsoft PowerPoint Slide Show | ppsx | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| Офисные файлы | Microsoft Office | MSOFFICE_PPT | Microsoft PowerPoint Presentation 97-2003 | ppt; pot; pps | application/vnd.ms-powerpoint |
| Офисные файлы | Microsoft Office | MSOFFICE_PPTM | Microsoft PowerPoint Macro-Enabled Presentation | pptm | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| Офисные файлы | Microsoft Office | MSOFFICE_PPTX | Microsoft PowerPoint Presentation | pptx | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| Офисные файлы | Microsoft Office | MSOFFICE_PUB | Microsoft Publisher Document | pub | application/vnd.ms-publisher |
| Офисные файлы | Microsoft Office | MSOFFICE_SCRAP | Microsoft Shell Scrap Object | shs; shb |  |
| Офисные файлы | Microsoft Office | MSOFFICE_XLAM | Microsoft Excel Macro-Enabled Add-in | xlam | application/vnd.ms-excel.addin.macroEnabled |
| Офисные файлы | Microsoft Office | MSOFFICE_XLS | Microsoft Excel Document 97-2003 | xsl | application/vnd.ms-excel |
| Офисные файлы | Microsoft Office | MSOFFICE_XLSB | Microsoft Excel Binary Document | xlsb | application/vnd.ms-excel.sheet.binary |
| Офисные файлы | Microsoft Office | MSOFFICE_XLSM | Microsoft Excel Macro-Enabled Document | xlsm | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| Офисные файлы | Microsoft Office | MSOFFICE_XLSX | Microsoft Excel Document | xlsx | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| Офисные файлы | Microsoft Office | MSOFFICE_XLTM | Microsoft Excel Macro-Enabled Template | xltm | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| Офисные файлы | Microsoft Office | MSOFFICE_XLTX | Microsoft Excel Template | xltx | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| Офисные файлы |  | OFFICE_EML | Outlook Express Message | eml | message/rfc822 |
| Офисные файлы |  | OFFICE_MSG | Microsoft Outlook Message | msg | application/vnd.ms-outlook |
| Офисные файлы |  | OFFICE_MSOFFICE | MS Office documents | doc; xls; ppt; dot; pot | application/msword; application/vnd.ms-excel; application/vnd.ms-powerpoint; application/vnd.ms-* |
| Офисные файлы |  | OFFICE_MSOFFICE_MACRO | Office 2007 macro enabled docs | docm; xlsm; pptm; ppsm; dotm | application/vnd.openxmlformats* |
| Офисные файлы |  | OFFICE_ODP | OpenDocument Presentation | odp | application/vnd.oasis.opendocument.presentation |
| Офисные файлы |  | OFFICE_ODS | OpenDocument Spreadsheet | ods | application/vnd.oasis.opendocument.spreadsheet |
| Офисные файлы |  | OFFICE_ODT | OpenDocument Text | odt | application/vnd.oasis.opendocument.text |
| Офисные файлы |  | OFFICE_ONE | Microsoft OneNote Document | one | application/msonenote |
| Офисные файлы |  | OFFICE_ONEPKG | Microsoft OneNote Package | onepkg | application/msonenote |
| Офисные файлы |  | OFFICE_OPENXML | Open XML documents | docx; xlsx; pptx; dotx; potx | application/vnd.openxmlformats*; application/vnd.ms-word*; application/vnd.ms-excel*; application/vnd.ms-powerpoint; application/onenote |
| Офисные файлы |  | OFFICE_PDF | Adobe Acrobat | pdf | application/pdf |
| Офисные файлы |  | OFFICE_PST | MS Outlook Personal Folders | pst; ost | application/vnd.ms-outlook |
| Офисные файлы |  | OFFICE_RTF | Rich Text Format | rtf | text/rtf; application/rtf |
| Офисные файлы |  | OFFICE_SXW | OpenOffice.org 1.0 Writer Document | sxw | application/vnd.sun.xml.writer |
| Офисные файлы |  | OFFICE_VDX | Microsoft Visio Drawing XML | vdx; vsx; vtx | application/vnd.ms-visio |
| Офисные файлы |  | OFFICE_VSD | Microsoft Visio Diagram | vsd; vss; vst | application/vnd.ms-visio |
| Офисные файлы |  | OFFICE_XPS | Open XML Paper Specification | xps; oxps | application/oxps; application/vnd.ms-xpsdocument |
| Офисные файлы |  | OFFICE_XSN | Microsoft InfoPath Template Form | xsn | application/vnd.ms-infopath |
| Файлы баз данных |  | DATABASE_ACCDB | Microsoft Access Database | accdb; accde; accdr | application/msaccess |
| Файлы баз данных |  | DATABASE_ACCDC | Microsoft Access Signed Package | accdc | application/msaccess |
| Файлы баз данных |  | DATABASE_MDB | Microsoft Access 2003 Database | mdb | application/msaccess |
| Архивные файлы |  | ARCHIVE_ARJ | Arj archive | arj | application/x-arj |
| Архивные файлы |  | ARCHIVE_7Z | 7-zip archive | 7z*; 7-z |  |
| Архивные файлы |  | ARCHIVE_ACE | ACE archive | ace | application/x-ace-compressed |
| Архивные файлы |  | ARCHIVE_BZIP2 | BZIP2 archive | bz; bz2; tbz; tbz2 | application/x-bzip |
| Архивные файлы |  | ARCHIVE_CAB | Windows Cabinet | cab |  |
| Архивные файлы |  | ARCHIVE_DMG | Apple Disk Image | dmg; smi; img | application/x-apple-diskimage |
| Архивные файлы |  | ARCHIVE_GZIP | Gzip archive | gz; tgz | application/x-gzip |
| Архивные файлы |  | ARCHIVE_ISO | ISO-9660 CD Disk | iso |  |
| Архивные файлы |  | ARCHIVE_JAR | Java (ZIP) archive | jar |  |
| Архивные файлы |  | ARCHIVE_LZIP | Lzip archive | lz | application/x-lzip |
| Архивные файлы |  | ARCHIVE_RAR | RAR archive | rar |  |
| Архивные файлы |  | ARCHIVE_TAR | Tar archive | tar | application/x-tar |
| Архивные файлы |  | ARCHIVE_XAR | Extensible archive format | xar |  |
| Архивные файлы |  | ARCHIVE_Z | Z (compress) archive | Z | application/x-compress |
| Архивные файлы |  | ARCHIVE_ZIP | ZIP archive | zip | application/zip |
| Файлы веб-архивов |  | TEXT_CHM | Microsoft Compiled HTML Help | chm | application/x-chm |
| Файлы веб-архивов |  | TEXT_MHT | MHTML Document | mht; mhtml |  |
| Прочие форматы |  | CRYPTO_CAT | Security Catalogue Information | cat |  |

</details>

3\. Для подтверждения создания профиля нажмите **Добавить**.

На вкладке также можно настроить **Максимальную вложенность архива**:

![](/.gitbook/assets/antivirus2.png)

В поле укажите целое число от 0 до 1000, где 0 — бесконечное количество вложенностей (0 указано по умолчанию). Для запрета вложенных архивов укажите в поле значение 1.

{% hint style="warning" %}
Если пользователь скачивает архив, вложенность которого превышает указанное в настройке число, то может возникнуть ошибка:
* при включении **Блокировать скачивание файла при неудачной проверке** файл будет заблокирован;
* при отключении **Блокировать скачивание файла при неудачной проверке** файл будет скачан.
{% endhint %}

Функция проверки вложенности не работает с запароленными архивами. Этот тип контента можно заблокировать при создании профиля на вкладке **Тип блокируемого контента**.

## Обновление баз

На вкладке можно посмотреть информацию о последнем обновлении баз антивируса Касперского:

![](/.gitbook/assets/antivirus5.png)

## Проверка работы антивируса

Попробуйте скачать тестовые файлы с сайта: [https://www.eicar.org/download-anti-malware-testfile](https://www.eicar.org/download-anti-malware-testfile/).

В случае правильной настройки браузер выведет ошибку доступа:

![](/.gitbook/assets/antivirus1.png)

Для проверки блокировки вредоносных ссылок воспользуйтесь ссылкой [http://www.kaspersky.com/test/wmuf](http://www.kaspersky.com/test/wmuf).