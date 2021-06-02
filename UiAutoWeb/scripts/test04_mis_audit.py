import pytest

from UiAutoWeb import page
from UiAutoWeb.page.page_in import PageIn
from UiAutoWeb.tools.get_driver import GetDriver
from UiAutoWeb.tools.read_yaml import read_yaml


class TestMisAudit:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、获取统一的入口类对象
        self.page_in = PageIn(driver)
        # 3、调用 登录成功依赖方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4、获取 PageMisAudit 对象
        self.audit = self.page_in.page_get_PageMisAudit()

    # 2、结束
    def teardown(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3、审核文章的 测试业务 方法
    @pytest.mark.parametrize("title,channel", read_yaml("mis_audit.yaml"))
    def test_mis_audit(self, title, channel):
        # 调用 审核文章业务方法
        self.audit.page_mis_audit(title, channel)
        # 断言
        self.audit.page_assert_audit()
