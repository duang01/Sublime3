'''
    自动化测试框架设计思路：基于关键字驱动和数据驱动来实现，通过对selenum进行二次封装，将常用的功能
    和内容封装形成类对象，将这个类对象作为一个工具提供的类，然后结合unitest或者pytest来进行测试用例
    的一个整合，或者是通过exls、yaml、ddt的形式做数据驱动的文件读写，通过这种文件读写的形式结合关键字
    的调用来实现一系列的流程，再通过写入的操作将测试用例的执行内容以断言的结果作为测试用例执行通过与否
    的一个标准，然后写入到相应的结果报告中
'''
from selenium import webdriver
from ddt import ddt, data, unpack


@ddt
class TestKeyWords(object):
    # 初始化
    def __init__(self, url, browser_type):
        self.open_browser(browser_type)
        self.driver.get(url)

    # 调用浏览器
    def open_browser(self, browser_type):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print("type error")

    # 元素定位方法二次封装
    @data('sv', 'se', 'se')
    @unpack
    def locator(self, locator_type, value):
        if locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'name':
            el = self.driver.find_element_by_name(value)
            return el

    # 封装元素操作
    # 文本输入   需输入locator_type:定位方法; value:定位的元素值
    def input_text(self, locator_type, value, text):
        self.locator(locator_type, value).send_keys(text)

    # 点击操作    需输入locator_type:定位方法; value:定位的元素值
    def click_elment(self, locator_type, value):
        self.locator(locator_type, value).click()


if __name__ == '__main__':
    tk = TestKeyWords('http://www.baidu.com', 'firefox')
    tk.input_text('id', 'kw', '霍格沃兹')
    tk.click_elment('id', 'su')