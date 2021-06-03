from locust import TaskSet, HttpLocust

# 1、定义一任务
"""注：普通函数，必须有一个形参"""

"""
1、登录
 URL:HTTP://182.92.81.159:1880/bms/login
 请求方式：post
 请求参数：{"username": "admin", "password": "123456"}
2、首页
 URL：http://182.92.81.159:1880/bms/index
 请求方式：get
3、获取用户信息
 URL：http://182.92.81.159:1880/bms/profile
 请求方式：get
4、退出
 URL：http://182.92.81.159:1880/bms/logout
 请求方式：post
"""
# 1、任务一 说话
def say(params):
    print("正在说话")

# 2、任务二 唱歌
def sing(params):
    print("正在唱歌")


# 2、定义任务集
""" 注：一个类，必须继承 TaskSet, 复写tasks 
            --格式为列表或字典，值 为任务函数名"""
class TaskTest(TaskSet):
    # 复写tasks
    tasks = [say, sing]

# 3、定义用户类
""" 注： 一个类，必须继承 HttpLocust ,
        --复写 task_set 参数，值为任务集类名称"""
class RunUser(HttpLocust):
    # 复写 task_set 参数
    task_set = TaskTest
    # 指定域名
    host = "http://localhost"
