import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuApp(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        cls.driver = cls.init_app()
        
        el1 = cls.driver.find_element_by_id("user_profile_icon")
        el1.click()

    def setup_method(self):
        print("setup_method 在每个用例执行之前执行一次")
        # 获取启动的appium的driver实例、用于后续每个case的driver
        self.driver = WebDriver
        self.driver = TestXueqiuApp.driver

        el2 = self.driver.find_element_by_id("tv_login")
        el2.click()

    def install_app(self):
        pass

    def init_app(self):
        # server 启动参数
        desired_caps = {}

        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '79d70e23'

        # app信息
        desired_caps['appPackage'] = 'com.myzaker.ZAKER_Phone'  # 包名
        desired_caps['appActivity'] = 'com.myzaker.ZAKER_Phone.view.LogoActivity'  # 启动名

        # 输入法
        desired_caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
        desired_caps['resetKeyboard'] = 'true'  # 运行结束后删除appium键盘
        desired_caps['noReset'] = 'true'  # 不做应用清除.

        # 启动appium应用服务
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(5)  # 添加一个隐性等待时间

    def test_01(self):
        action = TouchAction(self.driver)
        action.press(x=100, y=100).move_to(x=500, y=500).release().perform()    # 按住一个点滑动到某个点

        pass