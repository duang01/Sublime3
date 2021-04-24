from PO_web.basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SearchPage(BasePage):
    input_id = (By.ID, 'kw')
    click_id = (By.ID, 'su')

    # 对搜索框进行内容输入
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text)
        time.sleep(3)

    # 点击查询按钮，实现本次搜索
    def click_elemet(self):
        self.locator(self.click_id).click()

    # 检查函数
    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_elemet()


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    driver = webdriver.Firefox()
    sp = SearchPage(driver)
    sp.check(url, 'lol')
