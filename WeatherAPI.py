# -*- coding: utf-8 -*-

import requests
from datetime import datetime

"""
Метод для получения данных о погоде через запрос на сайт openweathermap.org
Предоставляет класс со следующим функционалом:
- поиск id города, который назвал пользователь;
- формирования списка с данными о погоде на 5 дней;
- формирование словаря с данными о погоде на момент запроса.

Use python 3.11
"""


class WeatherMaker:

    def __init__(self):
        self.app_id = "6458174fba0708611deace21f1e29b77"

    def search_city_id(self, city_name):
        """Функция поиска id города, который назвал пользователь."""
        city = f"{city_name},RU"
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': self.app_id})
        data = res.json()
        city_id = data['list'][0]['id']
        return city_id

    def search_weather(self, city_name='Moscow'):
        """Функция формирования списка с данными о погоде на 5 дней."""
        city_id = self.search_city_id(city_name)
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'lang': 'ru', 'units': 'metric', 'APPID': self.app_id})
        data = res.json()
        weather = []
        for day in data['list']:
            if day['dt_txt'][11:] == '12:00:00':
                weather.append(
                    {"weather": day['weather'][0]['description'],
                     'temp': day['main']['temp'],
                     'date': day['dt_txt'][:-3],
                     'wind': day['wind']['speed'],
                     'city': data['city']['name']}
                )
        return weather

    def search_weather_now(self, city_name='Moscow'):
        """Функция формирование словаря с данными о погоде на момент запроса"""
        city_id = self.search_city_id(city_name)
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'lang': 'ru', 'units': 'metric', 'APPID': self.app_id})
        data = res.json()
        weather = {"weather": data['weather'][0]['description'],
                   'temp': data['main']['temp'],
                   'date': str(datetime.fromtimestamp(data['dt']))[:-3],
                   'wind': data['wind']['speed'],
                   'city': data['name']}
        return weather
