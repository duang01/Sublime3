import requests

from ApiAutoTest import api
from ApiAutoTest.tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:
    # 1、初始化

    def __init__(self):
        # 1、登录 URL
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("后台登录URL：{}".format(self.url_login))
        # 2、查询文章url
        self.url_article = api.host + "/mis/v1_0/articles"
        log.info("后台查询文章URL：{}".format(self.url_article))
        # 3、审核文章URL
        self.url_audit = api.host + "/mis/v1_0/articles"
        log.info("后台审核文章URL：{}".format(self.url_audit))

    # 2、登录
    def api_mis_login(self, account, password):
        # 1、组装数据
        data = {"account": account, "password": password}
        log.info("调用登录URL数据：{}".format(data))
        # 2、调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3、查询文章
    def api_mis_search(self):
        # 1、参数数据
        data = {"title": api.title, "channel": api.channel}
        log.info("调用查询文章URL数据：{}".format(data))
        # 2、调用get方法
        return requests.get(url=self.url_article, params=data, headers=api.headers)

    # 4、审核文章
    def api_mis_audit(self):
        """
        :param: article_id 发布文章时获取
        :return: 响应数据
        """
        # 1、参数数据
        data = {"article_id": [1, 2], "status": 2}
        log.info("调用审核文章URL数据：{}".format(data))
        # 2、调用put方法
        return requests.put(url=self.url_audit, json=data, headers=api.headers)



