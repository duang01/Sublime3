from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from AutoWeb.xueqiu_po.page.MainPage import Mainpage
import logging

from AutoWeb.xueqiu_po.page.ProfilePage import ProfilePage
from AutoWeb.xueqiu_po.testcase.BaseTestCase import BaseTestCase


class TestXueQiu(BaseTestCase):
    # def __init__(self):
    #     self.main = Mainpage(self.driver)
    #     self.driver = webdriver.Firefox()

    def setup(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main = Mainpage(self.driver)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_search(self):
        self.main.search("alibaba").follow("09988")
        #todo: add assertion

    def test_profile(self):
        profile = ProfilePage(self.driver)        # 篡改cookies 绕过验证吗登录
        profile.login()
        selected = profile.gotoselected()         # 进入自选股页面
        selected.select("alibaba", "09988")       # 对自选股页面的输入数据

        self.driver.get("https://xueqiu.com/setting/user")

    def test_log(self):

        self.log.warning("warning demo")
        self.log.debug("debug demo")




