# 这是基本类
import time


class BasePage(object):

    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)
        time.sleep(3)

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 获取网页标题
    def get_title(self):
        return self.driver.title

    # 关闭
    def quit_browser(self):
        self.driver.quit()