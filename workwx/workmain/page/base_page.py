from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _drive = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            # options = Options()
            # options.debugger_address = '127.0.0.1:2933'

            self._driver = webdriver.Firefox()
            # self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
            # sleep(10)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
            sleep(15)

    def find(self, by, locator):     # 封装find方法、传入定位方式和元素即可操作
        return self._driver.find_element(by, locator)

    def wait_for_click(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def switch_to_alert(self):
        return self._driver.switch_to.alert.text()





