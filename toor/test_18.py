"""
        需求：
        1.小明 体重 75.8公斤
        2.小明每次跑步减肥0.5公斤
        3.小明每次吃东西增重1公斤

"""


class Person:
    # 使用形参可以简化类属性
    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我得名字是%s, 体重是%.2f公斤" % (self.name, self.weight)
    # TODO 小李开发跑步和吃的方法

    def run(self):

        self.weight -= 0.5
        print("%s 爱跑步，跑步锻炼身体和减肥; 体重是 %.2f" % (self.name, self.weight))

    def eat(self):

        self.weight += 1
        print("%s 是个吃货，先吃再减也不错; 体重是 %.2f" % (self.name, self.weight))


xiaoming = Person("小明", 75)

xiaoming.run()
xiaoming.eat()

print(xiaoming)
