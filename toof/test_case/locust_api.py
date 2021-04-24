from locust import HttpLocust, TaskSet, task

'''
执行命令：cmd中 locust -f D:\Atools\Sublime3\toof\test_case\locust_api.py 
查看报告地址：localhost:8089
'''


class UserBehavior(TaskSet):
    @task(2)
    def test_user(self):
        self.client.get('/users/', auth=('duang01', '123456'))

    @task(1)
    def test_groups(self):
        self.client.get('/groups/', auth=('duang01', '123456'))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

