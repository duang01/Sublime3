from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import xlrd


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    # 登录pange 元素维护
    username = (By.ID, "username")
    password = (By.ID, "pass")
    login_btn = (By.ID, "loginBtn")

    def set_username(self, username):   # 输入用户名
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)

    def set_password(self, password):   # 输入密码
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)

    def click_login(self):         # 点击登录
        loginbtn = self.driver.find_element(*LoginPage.login_btn)
        loginbtn.click()


class Test_Login(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.drive = webdriver.Firefox()
        self.drive.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    # tearDown 清理
    def tearDown(self):
        self.drive.close()

    # 1、打开登录页
    def test_Login(self):
        self.drive.get(self.base_url)

    # 2、初始化登录page
    login_page = BasePage.LoginPage(self.drive)

    # 3、输入用户名
    # 4、输入密码
    # 5、点击登录按钮






















