# WeatherApp
______
**WeatherApp** - консольная программа для поиска погоды,
создания изображений с погодой и ведением базы данных о погоде. 
Это мой pet project, созданный для изучения программирования и computer science, отработки навыков
работы с языком программирования, с сетевыми запросами, базами данных и библиотекой OpenCV.

***Функционал программы:***

Через консольный интерфейс, пользователь может задать город, в котором ему необходимо узнать погоду,
после выбрать одно из пяти действий:
- Добавить данные о погоде за 5 дней в базу данных.
- Получить данные о погоде за 5 дней из базы данных, они будут выведены на консоль.
- Создать открытку на выбранную дату, она будет показана в новом окне.
- Получить данные о погоде на данный момент, так же будут выведены на консоль. 
- Выйти из программы.

## Установка и запуск

Скачиваем репозиторий со всеми файлами с GitHub.
Создаем виртуальное окружение, но можно в коренную папку, и загружаем туда все необходимые пакеты
с помощью команды: 
``` python
pip install -r requirements.txt
```
Готово, теперь открываем файл `WeatherApp.py` и запускаем его.
Далее, через консольный интерфейс, начинаем взаимодействие.


## Используемые технологии

![version](https://img.shields.io/badge/python-3.11-blue)


![package](https://img.shields.io/badge/requests-2.31.0-violet)
![package](https://img.shields.io/badge/peewee-3.14.0-violet)
![package](https://img.shields.io/badge/OpenCV-4.8.0-violet)

![license](https://img.shields.io/badge/license-Apache__License__V2.0-green)

Так же проект сделан на принципах объектно-ориентированного программирования (ООП).

## Лицензия

Проект разработан с использованием лицензии [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)