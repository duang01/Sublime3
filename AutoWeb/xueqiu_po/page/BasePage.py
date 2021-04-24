from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """为所有页面提供"""

    def __init__(self, driver):
        self.driver: WebDriver = driver

