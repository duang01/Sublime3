import os
import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from UiAutoWeb.config import BASE_PATH
from UiAutoWeb.tools.get_log import GetLog

log = GetLog.get_logger()


class Base:

    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver: {}".format(driver))
        """解决driver"""
        self.driver = driver

    # 查找元素 方法
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认 30s
        :param poll: 查找元素频率， 默认 0.5s
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param value: 要输入的值
        """
        # 1、获取元素
        el = self.base_find(loc)
        # 2、清空操作
        log.info("正在对元素：{}执行清空数据".format(loc))
        el.clear()
        # 3、输入操作
        log.info("正在对：{}元素输入数据：{}".format(loc, value))
        el.send_keys(value)

    # 点击  方法封装
    def base_click(self, loc):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        """
        log.info("正在点击元素：{}".format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取  元素文本
    def base_get_text(self, loc):
        """
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :return: 返回元素的文本值
        """
        log.info("正在获取元素文本信息：{}".format(loc))
        return self.base_find(loc).text

    # 截图 命名的方法（很重要）
    def base_img_name(self):
        """可在image_time构建你想要的名字"""
        image_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        png_path = BASE_PATH + os.sep + "image" + os.sep
        err_png = png_path + image_time + '.png'
        return err_png

    # 截图方法
    def base_get_img(self, file_name):
        log.error("断言出错，执行截图操作！！！")
        # 1、调用截图的方法
        self.driver.get_screenshot_as_file(file_name)
        log.error("断言结果写入allure报告中>>>")
        # 2、调用图片写入报告方法
        self.__base_write_img(file_name)

    # 将图片写入报告方法（私有）
    def __base_write_img(self, file_name):

        # 1、获取图片文件流
        with open(file_name, 'rb') as f:

            # 2、调用allure.attach附加方法,即将图片写入报告
            allure.attach(f.read(), "错误截图", attachment_type=allure.attachment_type.PNG)





