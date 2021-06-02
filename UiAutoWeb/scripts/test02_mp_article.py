import pytest

from UiAutoWeb import page
from UiAutoWeb.page.page_in import PageIn
from UiAutoWeb.tools.get_driver import GetDriver
from UiAutoWeb.tools.read_yaml import read_yaml


class TestMpArticle:
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)

        # 2、获取统一入口类对象
        self.page_in = PageIn(driver)

        # 3、获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()

        # 4、获取PageMpArticle 页面对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 2、结束
    def teardown(self):
        # 1、关闭driver
        GetDriver.quit_web_driver()

    # 3、测试发布文章的方法
    @pytest.mark.parametrize("title,content", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content):
        # 1、调用 发布文章 业务方法
        self.article.page_mp_article(title, content)

        # 2、查看断言信息
        print("发布文章结果为：", self.article.page_get_info())
