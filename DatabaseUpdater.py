# -*- coding: utf-8 -*-

import peewee

"""
Метод для создания и формирования базы данных. 
Имеет следующий функционал:
- обновление данных о погоде в таблице;
- вывод данных из таблицы на консоль.

Use python 3.11
"""

db = peewee.SqliteDatabase('DB.db')
"""Создание базы данных через ORM peewee."""


class DataBase(peewee.Model):
    """Создание таблицы с необходимыми полями."""
    date = peewee.CharField()
    temp = peewee.CharField()
    weather = peewee.CharField()
    wind = peewee.CharField()
    city = peewee.CharField()

    class Meta:
        database = db


DataBase.create_table()


class DatabaseUpdater:
    """Класс для управления базой данных."""

    def __init__(self, weather_data, database=DataBase):
        """
        :param weather_data: Данные о погоде.
        :param database: Таблица, в которую будут внесены или вынуты данные.
        """
        self.database = database
        self.weather_data = weather_data

    def updata(self):
        """Обновление данных таблицы"""
        self.database.delete().execute()
        data = []
        for weath in self.weather_data:
            data.append(
                {
                    'date': weath['date'],
                    'temp': weath['temp'],
                    'weather': weath['weather'],
                    'wind': weath['wind'],
                    'city': weath['city']
                }
            )
        data_in_db = self.database.insert_many(data).execute()
        return True

    def view_all_data(self):
        """Функция вывода данных на консоль из таблицы."""
        for line in self.database.select():
            print(f'Дата: {line.date}, температура воздуха: {line.temp} градусов цельсия, '
                  f'{line.weather}, ветер: {line.wind} м/с, город: {line.city}.')
