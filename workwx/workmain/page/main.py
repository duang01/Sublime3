from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from workwx.workmain.page.add_member import AddMember
from workwx.workmain.page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        # click add member
        #el = ".index_service_cnt_itemWrap:nth-child(1)"
        # 元素 .index_service_cnt_itemWrap:nth-child(1)  .index_service_cnt_itemWrap:nth-child(3)
        #self.wait_for_click('.index_service_cnt_itemWrap:nth-child(1)')
        sleep(10)
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()

        return AddMember(self._driver)

    def goto_join_member(self):
        # 元素 .index_service_cnt_itemWrap:nth-child(3)
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(3)').click()
        return True
