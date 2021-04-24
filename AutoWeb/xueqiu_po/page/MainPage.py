from AutoWeb.xueqiu_po.page.BasePage import BasePage
from AutoWeb.xueqiu_po.page.SearchPage import SearchPage


class Mainpage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_xpath('//*[@type="button"]').click()
        return SearchPage(self.driver)
