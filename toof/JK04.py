"""----@基于unittest 的一个接口测试封装@----"""

import unittest
import requests
from urllib import parse
from time import sleep


class WeatherTest(unittest.TestCase):
    def setUp(self):

        self.url = 'https://www.sojson.com/blog/349.html'

    def test_weather_tianjin(self):
        r = requests.get(self.url)
        result = r.json()

        self.assertEqual(result['status'], 200)
        sleep(3)

    # def test_weather_param_error(self):


if __name__ == '__main__':
    unittest.main()