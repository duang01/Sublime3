from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from workwx.workmain.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        #self.wait_for_click('username')
        # sendkeys 元素 id = username  memberAdd_english_name
        sleep(5)
        self.find(By.ID, 'username').send_keys("老李")
        self.find(By.ID, 'memberAdd_english_name').send_keys("李三赖")
        self.find(By.ID, 'memberAdd_acctid').send_keys("123456")
        self.find(By.ID, 'memberAdd_phone').send_keys("18500001650")
        sleep(2)
        self.find(By.CSS_SELECTOR, '.js_member_editor_form>div:nth-child(3) a:nth-child(3)').click()
        sleep(2)
        # self.find(By.CSS_SELECTOR, '#__dialog__7057__ >div>div: nth-child(3) a: nth-child(2)').click()
        # self.switch_to_alert()
        return True

