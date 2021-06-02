from time import sleep

from UiAutoWeb import page
from UiAutoWeb.base.web_base import WebBase


class PageMisAudit(WebBase):
    # 文章 id
    article_id = None

    # 1、点击 信息管理
    def page_click_info_manage(self):
        # 1、强制等待
        sleep(3)
        # 2、点击信息管理
        self.base_click(page.mis_info_manage)

    # 2、点击 内容审核
    def page_click_content_audit(self):
        # 1、强制等待
        sleep(3)
        # 2、点击内容审核
        self.base_click(page.mis_content_audit)

    # 3、输入 文章标题
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    # 4、输入 文章频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 5、选择 状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    # 6、点击 查询
    def page_click_find(self):
        # 1、点击查询按钮
        self.base_click(page.mis_find)
        # 2、强制等待
        sleep(3)

    # 7、获取 文章id  -->用于断言使用
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 8、点击 通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 9、点击 确认
    def page_click_confirm_pass(self):
        # 1、暂停时间
        sleep(3)
        # 2、点击确认
        self.base_click(page.mis_confirm_pass)

    # 10、文章审核 业务组合方法
    def page_mis_audit(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取的文章id为：", self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 11、组装 断言 业务操作方法
    def page_assert_audit(self):
        # 1、等待状态转化时间
        sleep(3)
        # 2、修改状态 --> 审核通过
        self.page_click_status(click_text="审核通过")
        # 3、点击 查询按钮
        self.page_click_find()
        # 4、判断当前页面是否存在指定元素 并返回结果
        return self.web_base_is_exist(self.article_id)

