from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    # 初始化driver
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        # 填表单
        # 定位表单元素 id=corp_name  manager_name
        self._driver.find_element(By.ID, 'corp_name').send_keys("小易资源")
        self._driver.find_element(By.ID, 'manager_name').send_keys("老王")
        sleep(5)
        self._driver.quit()
        return True

