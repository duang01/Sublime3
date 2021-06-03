from ApiAutoTest import api
from ApiAutoTest.tools.get_log import GetLog

log = GetLog.get_logger()


class Tools:
    # 1、提取token
    @classmethod
    def common_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        # 追加请求头信息
        api.headers['Authorization'] = "Bearer" + token
        log.info("提取token到headers的headers:{}".format(api.headers))
        print("添加token后的headers为：", api.headers)

    # 2、断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info("公共断言方法-->status_code".format(status_code))
        # 断言状态码
        assert status_code == response.status_code
        # 断言响应信息
        assert "OK" == response.json().get("message")
