# -*- coding: utf-8 -*-

from DatabaseUpdater import DatabaseUpdater
from ImageMaker import ImageMaker
from WeatherAPI import WeatherMaker

"""
Консольный интерфейс для работы пользователя с WeatherApp.
Use python 3.11
"""


def weather_on_image(weather_data):
    """Функция формирования и показа изображения с погодой на выбранную пользователем дату."""
    choice_date = int(input(
        'За какую дату вы хотите получить открытку?\n'
        f'1 - {weather_data[0]["date"]}\n'
        f'2 - {weather_data[1]["date"]}\n'
        f'3 - {weather_data[2]["date"]}\n'
        f'4 - {weather_data[3]["date"]}\n'
        f'5 - {weather_data[4]["date"]}\n'
        '>>> '
    ))
    show_weather = ImageMaker(weather_data, choice_date)
    show_weather.image_make()
    show_weather.view_image()


def run():
    """
    Функция обрабатывает сообщения пользователя через заготовленные шаблоны взаимодействия.
    """
    try:
        choice_city = str(input('Введите город в котором хотите узнать погоду: '))
        weather = WeatherMaker()
        while True:
            weather_data = weather.search_weather(choice_city)
            db = DatabaseUpdater(weather_data=weather_data)
            choice = int(input(
                'Это приложение о погоде, выберете вариант действия:\n'
                '1 - добавить данные о погоде за 5 дней в базу данных.\n'
                '2 - получить данные о погоде за 5 дней из базы данных.\n'
                '3 - создать открытку.\n'
                '4 - получить данные о погоде на данный момент.\n'
                '5 - выход из программы.\n'
                '>>> '
            ))
            if choice == 1:
                db.updata()
                print('Данные о погоде добавлены в базу данных.')
            elif choice == 2:
                db.view_all_data()
            elif choice == 3:
                weather_on_image(weather_data)
            elif choice == 4:
                weather_now = weather.search_weather_now(choice_city)
                print(f'Дата: {weather_now["date"]}, температура воздуха: {weather_now["temp"]} градусов цельсия, '
                      f'{weather_now["weather"]}, ветер: {weather_now["wind"]} м/с, город: {weather_now["city"]}.')
            elif choice == 5:
                exit()
            else:
                print('Неверное действие. Попробуйте еще раз.')
                continue
    except Exception:
        print('Произошла ошибка, возможно вы ввели неправильный город. Попробуйте еще раз.')
        run()


if __name__ == '__main__':
    run()
