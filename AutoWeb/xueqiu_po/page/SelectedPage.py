from AutoWeb.xueqiu_po.page.BasePage import BasePage


class SelectedPage(BasePage):
    def select(self, keyword, market):
        self.driver.find_element_by_css_selector(".option .search_droppdowm input").send_keys(keyword)
        self.driver.find_element_by_xpath('//*[@class=segfcdg_sd]//li[contains(text(), "%s")]' % market).click()


