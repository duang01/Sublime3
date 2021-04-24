from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.users_index=0
        self.groups_index=0

    @task
    def test_users(self):
        users_id = self.locust.id[self.users_index]
        url = '/users/'+str(users_id)+'/'
        self.client.get(url, auth=('duang01', '123456'))
        self.users_index = (self.users_index+1) % len(self.locust.id)

    @task
    def test_groups(self):
        groups_id = self.locust.id[self.groups_index]
        url = '/groups/'+str(groups_id)+'/'
        self.client.get(url, auth=('duang01', '123456'))
        self.groups_index = (self.groups_index+1) % len(self.locust.id)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    id = [1, 2]
    min_wait = 3000
    max_wait = 6000
    host = '127.0.0.1:8000'


'''
运行命令；locust -f D:\Atools\Sublime3\toof\test_case\locust_api_groups.py --no-web -c 5 -r 1 -t 15s
查看报告地址：localhost:8089
'''
