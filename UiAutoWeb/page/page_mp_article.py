from time import sleep

from UiAutoWeb import page
from UiAutoWeb.base.web_base import WebBase


class PageMpArticle(WebBase):
    # 1、点击 内容管理
    sleep(5)

    def page_click_content_manage(self):
        self.base_click(page.mp_content_manage)
        sleep(5)

    # 2、点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.mp_publish_article)
        sleep(8)

    # 3、输入 文章标题
    def page_input_title(self, value):
        self.base_input(page.mp_title, value)
        sleep(3)

    # 4、输入 文章内容
    def page_input_content(self, content):
        # 1、切换 iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        sleep(3)

        # 2、输入 内容
        self.base_input(page.mp_content, content)
        sleep(5)

        # 3、回到 默认目录
        self.driver.switch_to.default_content()
        sleep(2)

    # 5、选择  封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)
        sleep(3)

    # 6、选择  频道
    def page_click_channel(self):
        list = ["软件测试", "C++", "PYTHON", "Java", "数据库"]
        click_text = [i for i in list]
        # 调用我们的webpage里的下拉框方法
        self.web_base_click_element(placeholder_text="请选择", click_text=click_text)
        sleep(3)

    # 7、点击  发表
    def page_click_submit(self):
        self.base_click(page.mp_submit)
        sleep(3)

    # 8、获取 发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 9、 组合发布文章业务方法
    def page_mp_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()

