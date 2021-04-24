from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from workwx.register import Register


class Login:
    # 因为这里还需要driver来访问地址、所以选择复用
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # 扫描二维码功能
    def scanf(self):
        pass

    # 提供注册页面链接
    def goto_register(self):
        # 点击注册，返回注册页面
        # 元素 login_registerBar_link
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()

        return Register(self._driver)
