# Выгрузка картинок с сайта NASA и публикация их на канале в телеграм.

### Как запустить
#### fetch_apod_images.py
Если необходимо скачать несколько картинок, то вводим в терминал:
```
python fetch_apod_images.py -c {кол-во картинок для скачивания}
```

Если необходимо скачать только одну картинку, то вводим в терминал:
```
python fetch_apod_images.py
```

#### fetch_epic_images.py
Вводим в терминал:
```
python fetch_epic_images.py
```

#### fetch_spacex_images.py
Если необходимо скачать картинки взлета с конкретным ID, то вводим в терминал:
```
python fetch_spacex_images.py -i {номер ID}
```

Если необходимо скачать картинки последнего взлета, то вводим в терминал:
```
python fetch_spacex_images.py
```

#### telegram_bot.py
Если необходимо указать количество часов с какой периодичностью будет поститься каждая картинка, то вводим в терминал:
```
python telegram_bot.py -t {количество часов}
```

Если необходимо, чтобы периодичность, с которой поститься картинка была равна 4 часам, то вводим в терминал:
```
python telegram_bot.py
```

### Структура программы

#### utils.py
Содержит функции по сохранению картинки(save_file) и получению расширения файла(get_extension)

#### fetch_apod_images.py
Сохраняет в папку `./images/` различные случайные картинки NASA по ссылке https://api.nasa.gov/planetary/apod. 

Количество, необходимое для скачивания, указываем в терминале при вызове скрипта (по умолчанию 1 картинка).

Картинки сохраняются с названиями `apod_{индекс картинки}.{формат остается неизменным}`.

#### fetch_epic_images.py
Сохраняет в папку `./images/` эпичные картинки Земли по ссылке https://api.nasa.gov/EPIC/api/natural. 

Картинки сохраняются с названиями `epic_{индекс картинки}.png`.

#### fetch_spacex_images.py
Сохраняет в папку `./images/` картинки взлета ракеты по ссылке https://api.spacexdata.com/v5/launches/. 

ID взлета указываем в терминале при вызове скрипта. Если ID не указано, то сохраняются картинки последнего взлета.

Картинки сохраняются с названиями `spacex_{индекс картинки}.{формат остается неизменным}`.

#### telegram_bot.py
Постит картинки в случайном порядке каждые несколько часов из папки `./images/`.

При запуске скрипта можно указать раз в какое количество будет поститься каждая картинка (по умолчанию 4 часа)

### Как установить
Необходимо получить токен на сайте NASA https://api.nasa.gov/.

Необходимо создать канал, бота и получить токен (https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/).

Создаем файл для переменных окружения `.env` в одной директории с файлом main.py и прописываем в него:
```
NASA_API_KEY=Ваш токен сайта NASA без кавычек и пробелов

TG_TOKEN=Ваш токен телеграм бота без кавычек и пробелов
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```