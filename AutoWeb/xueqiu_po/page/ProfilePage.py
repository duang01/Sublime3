from AutoWeb.xueqiu_po.page.BasePage import BasePage
from AutoWeb.xueqiu_po.page.SelectedPage import SelectedPage


class ProfilePage(BasePage):

    def login(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})
        self.driver.add_cookie({"name": "", "value": ""})

        print(self.driver.get_cookies())
        self.driver.refresh()

    def gotoselected(self):
        return SelectedPage(self.driver)