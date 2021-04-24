from AutoWeb.xueqiu_po.page.BasePage import BasePage


class SearchPage(BasePage):
    """使用xpath定位元素常用contains表达式  具体使用：xpath=('//*[contains(text(),"文本")]')
    例：//*[contains(text(),"09988")]/../../../..//*[@class="follow__control"]
    """
    def follow(self, keyword):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]/../../../..//*[@class="follow__control"]' % keyword).click()
        return self
