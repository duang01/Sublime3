from UiAutoWeb import page
from UiAutoWeb.base.web_base import WebBase
from UiAutoWeb.tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):

    # 1、输入用户名
    def page_input_usname(self, username):
        self.base_input(page.mis_login, username)

    # 2、输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 3、点击登录按钮
    def page_click_login_btn(self):
        # 1、处理js
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)

        # 2、调用点击操作
        self.base_click(page.mis_login_btn)

    # 4、获取 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 4、后台登录业务组合方法
    def page_mis_login(self, username, pwd):
        log.info("正在调用后台管理系统登录业务方法：用户名：{}".format(username))
        self.page_input_usname(username)
        log.info("正在调用后台管理系统登录业务方法：密码：{}".format(pwd))
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 5、后台登录成功依赖 方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用登录依赖业务方法：用户名：{}".format(username))
        self.page_input_usname(username)
        log.info("正在调用登录依赖方法：密码：{}".format(pwd))
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

