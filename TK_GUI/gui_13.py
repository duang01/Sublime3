import shelve
from time import sleep

import pytest
import yaml
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By

# __all__ = ['TestDate']
#
#
# class TestDate:
#     @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./demo.yaml")))
#     def test_data(self, a, b):
#         print(a+b)


# # 自动添加mark标记
# def pytest_collection_modifyitems(session, config, items: list):
#     print(type(items))
#     for item in items:
#         if "add" in item.nodeid:
#             item.add_marker(pytest.mark.add)
#
#         elif "div" in item.nodeid:
#             item.add_marker(pytest.mark.div)
#
#     items.reverse()


class TestWait:
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('https://home.testing-studio.com/')

    @pytest.mark.skip
    def test_wait(self):
        print('hello')
        self.driver.find_element(By.XPATH, '//*[@class="active"]').click()

    @pytest.mark.skip
    def test_chains(self):
        click_element = self.driver.find_element(By.XPATH, '//*[@class="d-button-label"]')
        action = ActionChains(self.driver)
        action.click(click_element)
        action.perform()
        sleep(3)

        '''拖拽的三种方法'''
        # action.drag_and_drop(drag_element, drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        # action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_touch_action(self):
        action1 = TouchActions(self.driver)
        action1.scroll_from_element()

    @pytest.mark.skip
    def test_frame(self):
        self.driver.switch_to.frame("frame的id")
        self.driver.switch_to.window("window的句柄")
        self.driver.switch_to.default_content()   # 切换到默认的frame

    def test_js_scroll(self):
        self.driver.get("www.baidu.com")
        sleep(5)
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        sleep(5)
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(3)

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date'); a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_dae').value='2020-12-30'")
        sleep(5)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))





