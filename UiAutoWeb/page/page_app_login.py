from time import sleep
from UiAutoWeb import page
from UiAutoWeb.base.app_base import AppBase
from UiAutoWeb.tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppLogin(AppBase):
    # 1、输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 2、输入 验证码
    def page_input_code(self, code):
        self.base_input(page.app_code, code)

    # 3、点击 登录按钮
    def page_click_login_btn(self):
        sleep(2)
        self.base_click(page.app_login_btn)

    # 4、判断 页面是否存在
    def page_is_login_success(self):
        sleep(2)
        return self.app_base_is_exist(page.app_me)

    # 5、组合业务 登录方法
    def page_app_login(self, app_phone, app_code):
        log.info("正在调用app应用登录方法，手机号：{};验证码：{}".format(app_phone, app_code))
        self.page_input_phone(app_phone)
        self.page_input_code(app_code)
        self.page_click_login_btn()

    # 6、组合业务依赖 登录成功方法
    def page_app_login_success(self, app_phone='13812345679', app_code='246811'):
        log.info("依赖登录成功的方法，手机号：{};验证码：{}".format(app_phone, app_code))
        self.page_input_phone(app_phone)
        self.page_input_code(app_code)
        self.page_click_login_btn()
