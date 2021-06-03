import pytest
from ApiAutoTest import api
from ApiAutoTest.api.api_mp import ApiMp
from ApiAutoTest.tools.get_log import GetLog
from ApiAutoTest.tools.read_yaml import read_yaml
from ApiAutoTest.tools.tools import Tools

log = GetLog.get_logger()


class TestMp:
    # 1、初始化
    def setup_class(self):
        # 1、获取ApiMp对象
        self.mp = ApiMp()

    # 2、登录接口测试方法
    @pytest.mark.parametrize("mobile,code", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, mobile, code):
        # 1、调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        # 打印输出结果
        print("登录的结果为：", r.json())
        try:
            # 提取token
            Tools.common_token(r)
            # 响应断言
            Tools.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 3、发布文章测试接口方法
    def test01_mp_article(self, title=api.title, content=api.content, channel_id=api.channel_id):
        # 1、调用发布文章接口
        r = self.mp.api_mp_article(title, content, channel_id)
        # 提取 id 为后面的文章审核做依赖参数
        api.article_id = r.json().get("data").get("id")
        # 2、打印输出结果
        print("发布文章成功后id值为", api.article_id)
        try:
            # 3、断言
            Tools.common_assert(r, status_code=201)
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、抛异常
            raise

