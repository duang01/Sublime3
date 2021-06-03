from locust import TaskSet, HttpLocust


"""1、定义任务"""


# 1、登录
def login(session):
    # 请求post方法
    r = session.client.post(url="/bms/login", data={"username": "admin", "password": "123456"})
    # 查看登录结果 json
    print(r.json())
    print("正在调用登录方法")


# 2、打开首页
def index(session):
    # 调用get方法
    r = session.client.get(url="/bms/index")
    # 查看结果。text方法解析
    print(r.text)


# 3、查询用户信息
def user(session):
    # 调用get方法
    r = session.client.get(url="/bms/profile")
    # 查看信息
    print(r.text)


# 4、退出登录
def logout(session):
    # 调用post方法
    r = session.client.post(url="/bms/logout")
    # 查看结果
    print(r.json())
    print("正在执行退出登录操作")


"""2、定义任务集"""


class TaskTest(TaskSet):
    # 复写 tasks 属性  10 和 1 为权重
    tasks = {index: 10, user: 1}

    # 初始化执行方法
    def on_start(self):
        login(self)

    # 结束执行方法 只运行一次
    def on_stop(self):
        logout(self)


"""3、定义用户类"""


class UserRun(HttpLocust):
    # 复写 task_set
    task_set = TaskTest

    # 定义一个host
    host = "http://182.92.81.159:1880"

    # 最小延迟时间  毫秒为单位
    min_wait = 1000

    # 最大延迟时间
    max_wait = 3000

    # 权重， 默认为10
    weight = 10
