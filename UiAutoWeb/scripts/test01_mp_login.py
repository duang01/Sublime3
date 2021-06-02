
from time import sleep
import pytest
from UiAutoWeb import page, tools
from UiAutoWeb.page.page_in import PageIn
from UiAutoWeb.tools.del_data import DelData
from UiAutoWeb.tools.get_driver import GetDriver
from UiAutoWeb.tools.get_log import GetLog
from UiAutoWeb.tools.read_yaml import read_yaml


log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)

        # 2、通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 1、调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        # 1、调用业务方法
        self.mp.page_mp_login(username, code)
        # 2、断言
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error("断言出错！！！ 错误信息：{}".format(e))
            sleep(3)

            # 截图
            self.mp.base_get_img(file_name=self.mp.base_img_name())

            # 抛异常
            raise
