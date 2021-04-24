# This sample code uses the Appium python client
# Then you can paste this into a file and simply run with Python
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from appium import webdriver
import pytest
import time

from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu(object):

    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print("---> setup class 在该类中只执行一次")
        cls.driver = cls.init_appium()
        cls.driver = cls.restart_app()

    def setup_method(self):
        print("---> setup method 运行在每一条用例执行前")
        self.driver = TestXueQiu.driver


    """
    业务：进入雪球首页-->进入雪球的基金页(不是第一个)，对它及它的右侧的每个新闻栏目、执行上滑5次
            进入下个栏目用从右边到左边滑动
            *****请使用相对坐标、务使用绝对坐标、提高兼容性
    """

    def test_swipe_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()

        list = self.get_cell_list()
        print(list)
        range_times1 = len(list)-list.index('基金')
        self.swipe_your_icon(range_times1)
        list_new = self.get_cell_list()
        print(list_new)
        range_times2 = len(list_new) - list_new.index(list[-1])
        self.swipe_your_icon(range_times2)

    def swipe_your_icon(self, num):
        size = self.driver.get_window_size()      # {"width":"1088", "height":"2040"}
        action = TouchAction(self.driver)
        for y in range(num):

            for i in range(5):
                action.press(x=size['width']*0.8,
                             y=size['height']*0.8).move_to(x=size['width']*0.2, y=size['height']*0.2).release().perform()
                time.sleep(3)

                action.press(x=size['width'] * 0.9,
                             y=size['height'] * 0.5).move_to(x=size['width'] * 0.2, y=size['height'] * 0.2).release().perform()
                time.sleep(3)

    def get_cell_list(self):
        # 获取后面的元素列表
        cells = self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text != '']")
        cell_list = []
        for i in cells:
            cell_list.append(i.text)
            # print(cell_list)
            # print(cell_list.index())
            return cell_list

    def test_webview(self):
        '''对webview的测试'''
        self.driver.find_elements_by_accessibility_id("A股开户").click()
        self.driver.find_elements_by_accessibility_id("立即开户")
        # 显示等待,在模拟器上可以实现
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MobileBy.ACCESSIBILITY_ID, '立即开户'))

    def teardown_method(self):
        self.driver.quit()

    @classmethod
    def init_appium(cls):
        caps = {}

        caps["platformName"] = "Android"

        caps['platformVersion'] = '9'
        caps['deviceName'] = '79d70e23'

        # app信息
        caps['appPackage'] = 'com.xueqiu.android'  # 包名
        caps['appActivity'] = '.view.WelcomeActivityAlias'  # 启动名

        # 输入法
        caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
        caps['resetKeyboard'] = 'true'  # 运行结束后删除appium键盘
        caps['noReset'] = 'true'  # 不做应用清除.

        # 启动appium应用服务
        driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        driver.implicitly_wait(10)  # 添加一个隐性等待时间
        return driver

