"""对selenuim的常用功能进行封"""
from selenium import webdriver
import time


# 浏览器的初始化操作
class Common(object):

    def __init__(self):
        # 创建浏览器
        self.drive = webdriver.Firefox()
        # 最大化浏览器
        self.drive.maximize_window()

    # 访问地址
    def open_url(self, url):
        self.drive.get(url)
        self.drive.implicitly_wait(10)

    # 定位元素封装
    def locateElement(self, locate_type, value):
        el = None
        if locate_type == 'id':
            el = self.drive.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.drive.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.drive.find_element_by_class_name(value)
        elif locate_type == 'tag':
            el = self.drive.find_element_by_tag_name(value)
        elif locate_type == 'text':
            el = self.drive.find_element_by_link_text(value)
        elif locate_type == 'partial':
            el = self.drive.find_element_by_partial_link_text(value)
        elif locate_type == 'xpath':
            el = self.drive.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.drive.find_element_by_css_selector(value)

        # 返回定位到的元素
        if el is not None:
            return el

    # 元素操作封装
    def click(self, locate_type, value):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()

    # 输入数据的操作
    def input_data(self, locate_type, value, data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行文本操作
        el.send_keys(data)

    # 获取定位到元素中的文本内容
    def get_text(self, locate_type, value):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.text

    # 获取定位到元素中的标签属性
    def get_attr(self, locate_type, value, data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.get_attribute(data)

    def close_driver(self):
        self.drive.quit()

    def __del__(self):
        # 结束时的操作
        time.sleep(3)
        self.drive.quit()


# 判断文件是否自身执行，如果是则运行后面的语句，若是被调用的话，则不执行
if __name__ == '__main__':
    com = Common()
    com.open_url('http://www.baidu.com')
    com.open_url('https://www.csdn.net')
    com.close_driver()




