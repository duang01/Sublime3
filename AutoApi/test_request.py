import jsonpath
import pytest
import requests
import logging
from hamcrest import *
from jsonschema import validate


class TestRequests(object):

    # logging.basicConfig()
    #
    # # def test_get(self):
    # #
    # #     r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
    # #     logging.info(r)
    # #     print(r.text)

    def test_hamcrest(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200

        assert_that(r.json()['category_list']['categories'][0]['name']), equal_to('霍格沃兹测试学院公众号')


if __name__ == '__main__':
    pytest.main(['-s', 'test_request.py'])
