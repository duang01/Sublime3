import logging

import requests
import time
from AutoApi.wenxin.contact.token import Weixin
import pystache

from AutoApi.wenxin.contact.user import User
from AutoApi.wenxin.contact.utils import Utils


class TestUser:
    depart_id = 3
    @classmethod
    def setup_class(cls):
        # todo: create depart
        cls.user = User()

    def test_mustache(self):
        te = str(time.time()).replace(".", "")[0:11]
        uid = "Abod"+te
        mobile = te
        data = str(Utils.parse("user_create.json", {
            "userid": uid,
            "name": uid,
            "alias": uid,
            "title": "校长",
            "email": uid+"@qq.com",
            "mobile": mobile
                                                     }))
        data = data.encode("UTF-8")

        r = self.user.creat(data=data)
        logging.debug(r)
        assert r['errcode'] == 0

    # def test_get_user(self):
    #     logging.debug(Utils.parse("user_create.json", {"name": "Abod", "title": "校长", "email": "12@1.com"}))

    def test_create(self):
        te = str(time.time()).replace(".", "")[0:11]
        uid = "Aoo"+te
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@gzdev.com"
        }
        r = User().creat(data)
        logging.debug(r)
        assert r['errcode'] == 0

