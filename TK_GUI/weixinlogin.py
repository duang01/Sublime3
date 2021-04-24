import shelve

import pytest
from jmespath import Options
from selenium import webdriver

'''企业微信登录测试类'''


class TestWeiXinLogin:
    def setup(self):
        self.driver.implicitly_wait(5)
        option = Options()
        option.debugger_address = '127.0.0.1:9233'
        self.driver = webdriver.Chrome(options=option)
        self.db = shelve.open("cookies")

    def teardown(self):
        self.db.close()
        self.driver.quit()

    def test_login_save_cookies(self):
        self.db["cookies"] = self.driver.get_cookies()  # 获取cookies保存到shelve数据库中
        self.driver.get(url="http://www.baidu.com")
        self.driver.find_element_by_id("kw").click()

    def test_login_get_cookies(self):
        self.driver.get(url="https://www.sina.cn")
        cookie = self.db["cookies"]
        for _cookie in cookie:            # 从cookies 列表中删除过期字段等
            if "expiry" in _cookie and not isinstance(_cookie["expiry"], int):
                _cookie["expiry"] = round(_cookie["expiry"])
            self.driver.add_cookie(_cookie)

        self.driver.get(url="http://www.huya.com")



