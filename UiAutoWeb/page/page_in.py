from UiAutoWeb.page.page_app_article import PageAppArticle
from UiAutoWeb.page.page_app_login import PageAppLogin
from UiAutoWeb.page.page_mis_audit import PageMisAudit
from UiAutoWeb.page.page_mis_login import PageMisLogin
from UiAutoWeb.page.page_mp_article import PageMpArticle
from UiAutoWeb.page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取 PageMpLogin 对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取 PageMpArticle 对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取 PageMisLogin 对象
    def page_get_PageMisLogin(self):
        return  PageMisLogin(self.driver)

    # 获取 PageMisAudit 对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

    # 获取 PageAppLogin 对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    # 获取 PageAppArticle 对象
    def page_get_PageAppArticle(self):
        return PageAppArticle(self.driver)
