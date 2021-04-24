# 定义一个英雄类
class Hero(object):

    # count = 0
    # 构造类方法   类方法的调用 类名.类方法 如 Hero.lei()
    @classmethod
    def lei(cls):

        print("这是一个类方法 %d")

    # 静态方法 通过类.静态方法名()调用  如 Hero.jin()
    @staticmethod
    def jin():
        print("这是一个静态方法")

    # 构造方法

    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def __str__(self):
        return "名字：%s；血量:%d; 攻击力：%d" % (self.name, self.hp, self.atk)

    def __del__(self):
        print("结束了---")

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new 方法会被自动调用
        print("创建对象，分配空间")
        # 2.为对象 分配空间
        ret = super().__new__(cls)
        # 3.返回对象的引用
        return ret


her0 = Hero("Tom", 100, 50)
print(her0.name, end="**")
print(her0.hp, end="**")
print(her0.atk, end="**")
Hero.jin()
Hero.lei()
print(her0)






























