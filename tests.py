import unittest
from unittest import TestCase
from unittest.mock import Mock

from DatabaseUpdater import DatabaseUpdater
from ImageMaker import ImageMaker
from WeatherAPI import WeatherMaker

_test_data_now = [{'city': 'Борисоглебск',
                   'date': '2043-07-13 15:00',
                   'temp': '23.99',
                   'weather': 'ясно',
                   'wind': '2.57'}]

_test_data = [{'city': 'Пермь',
               'date': '2023-07-28 15:00:00',
               'temp': 23.99,
               'weather': 'ясно',
               'wind': 2.57},
              {'city': 'Пермь',
               'date': '2023-07-29 15:00:00',
               'temp': 26.3,
               'weather': 'ясно',
               'wind': 2.12},
              {'city': 'Пермь',
               'date': '2023-07-30 15:00:00',
               'temp': 26.51,
               'weather': 'ясно',
               'wind': 3.52},
              {'city': 'Пермь',
               'date': '2023-07-31 15:00:00',
               'temp': 23.1,
               'weather': 'небольшой дождь',
               'wind': 3.01},
              {'city': 'Пермь',
               'date': '2023-08-01 15:00:00',
               'temp': 20.64,
               'weather': 'дождь',
               'wind': 3.05}]


class Tests(TestCase):

    def test_put_data_in_database(self):
        """Тест обновления базы данных."""
        test = DatabaseUpdater(weather_data=_test_data)
        self.assertTrue(test.updata())

    def test_create_image(self):
        """Тест на создание правильного изображения."""
        image = ImageMaker(_test_data_now)
        image.image_make()
        with open('result.jpg', 'rb') as img_file:
            f = img_file.read()
            bit_result = bytearray(f)
        with open('for_tests/result.jpg', 'rb') as img_file:
            f = img_file.read()
            bit_answer = bytearray(f)
        self.assertEqual(bit_result, bit_answer)

    def test_get_weather(self):
        """
        Тест на работу метода по получению данных о погоде.
        Поиск по сети заменен Mock-функцией для независимости тестирования.
        """
        weather = WeatherMaker()
        weather.search_weather_now = Mock(return_value=_test_data_now)
        weather_now = weather.search_weather_now()
        self.assertEqual(weather_now, _test_data_now)


if __name__ == '__main__':
    unittest.main()
