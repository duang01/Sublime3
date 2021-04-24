import logging

import pytest
import requests

from AutoApi.wenxin.contact.token import Weixin
from AutoApi.wenxin.contact.utils import Utils


class TestDepartment:

    @pytest.mark.parametrize("name", ["因缘研究院", "福利研究院", "天文研究院"])
    def test_create(self, name, token):
        data = {
            "name": name+Utils.udid(),
            "parentid": 4,
            "order": 1,

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                      params = {"access_token": token}, json=data
                      ).json()

        logging.debug(r)
        assert r["errcode"] == 0

    def test_create_order(self, token):
        data = {
            "name": "信用研发中心",
            "parentid": 2,
            "order": 3,

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": token}, json=data
                          ).json()

        logging.debug(r)

