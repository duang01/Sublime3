from time import sleep

from selenium.webdriver.common.by import By

from UiAutoWeb.base.base import Base


class WebBase(Base):
    """以下为web项目专属方法: 注意细节 ’{}’.format()的动态替换"""

    # 根据显示文本点击指定元素-->针对于下拉框
    def web_base_click_element(self, placeholder_text, click_text):
        # 1、点击父选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)

        # 2、暂停
        sleep(2)

        # 3、点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        # 1、组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2、找元素
        try:
            # 1、找元素，最长10s
            self.base_find(loc, timeout=10)
            # 2、输出找到元素
            print("找到：{}元素啦！").format(loc)
            # 3、返回ture
            return True
        except:
            # 1、输出未找到信息
            print("没有找到：{}元素哎！").format(loc)
            # 2、返回false
            return False
