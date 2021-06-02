from UiAutoWeb import page
from UiAutoWeb.base.app_base import AppBase
from UiAutoWeb.tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppArticle(AppBase):
    # 1、查找指定的频道
    def page_click_channel(self, click_text):
        # 1、调用 从右向左滑动方法
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    # 2、查找指定的文章
    def page_click_article(self, title):
        # 调用从下到上的滑动方法
        self.app_base_down_wipe_up(page.app_article, click_text=title)

    # 3、查找文章业务的方法
    def page_app_article(self, click_text, title):
        # 1、调用查找频道
        log.info("正在调用查看文章的业务方法 所属频道：{}，文章标题{}".format(click_text, title))
        self.page_click_channel(click_text)
        # 2、调用查找文章
        self.page_click_article(title)
