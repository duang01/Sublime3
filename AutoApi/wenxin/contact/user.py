import requests

from AutoApi.wenxin.contact.token import Weixin


class User:
    def creat(self, dict=None, data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=dict,
                            data=data
                          ).json()

