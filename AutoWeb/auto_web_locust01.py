from locust import  HttpLocust, TaskSet, task
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Discuz_Task(TaskSet):

    @task(1)
    def index(self):
        self.client.get("www.baidu.com")


class Discuz_Locust(HttpLocust):

    task_set = Discuz_Task
    host = "http://192.168.1.201.8888"
    min_wait = 1000
    max_wait = 2000


class TestHome(object):
    def setup(self):
        # 选择浏览器，对多浏览器操作通过Remote
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.FIREFOX)