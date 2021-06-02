import pytest

from UiAutoWeb.page.page_in import PageIn
from UiAutoWeb.tools.get_driver import GetDriver
from UiAutoWeb.tools.get_log import GetLog
from UiAutoWeb.tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppLogin:
    # 1、初始化
    def setup_class(self):

        # 1、获取driver
        driver = GetDriver.get_app_driver()
        # 2、通过统一入口对象获取 PageAppLogin 对象
        self.app_login = PageIn(driver).page_get_PageAppLogin()

    # 2、结束
    def teardown(self):
        GetDriver.quit_app_driver()

    # 3、app登录业务测试方法
    @pytest.mark.parametrize("app_phone,app_code", read_yaml("app_login.yaml"))
    def test_app_login(self, app_phone, app_code):
        # 调用app 登录测试业务方法
        self.app_login.page_app_login(app_phone, app_code)
        # 断言
        try:
            assert self.app_login.page_is_login_success()
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、截图
            self.app_login.base_img_name()
            self.app_login.base_get_img()
            # 3、抛异常
            raise
