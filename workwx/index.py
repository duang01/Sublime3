import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from workwx.Xiazai import Xiazai
from workwx.login import Login
from workwx.register import Register


class Index:

    def __init__(self):

        self._driver = webdriver.Firefox()
        self._driver.get('https://work.weixin.qq.com/wework_admin/')

    # 前往企业登录页
    def goto_login(self):
        # 点击首页企业登录功能
        # 定位元素  .index_top_operation_loginBtn
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)

    # 前往注册页面
    def goto_register(self):
        # 点击首页立即注册功能
        # 元素： index_head_info_pCDownloadBtn
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    @pytest.mark.skip
    def goto_xiazai(self):
        # 点击首页下载功能
        # 元素： index_top_operation_registerBtn
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_registerBtn').click()
        return Xiazai(self._driver)
