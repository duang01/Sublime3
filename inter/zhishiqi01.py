"""标准的通用装饰器模板"""


def set_func(func):
    def call_func(*args, **kwargs):
        print("------这是权限验证1------")
        print("------这是权限验证2------")
        return func(*args, **kwargs)
    return call_func


@set_func
def test1():
    print("=====test1======")


# test1 = set_func(test1)
test1()


