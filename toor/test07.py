''''#创建一个类

class Dog(object):

    typee = "宠物"  #类变量（属性）

    #初始化方法
    def __init__(self,name,age,color):            #定义一个类和属性
        self.name = name                          #实例变量（属性）
        self.age = age
        self.color = color

    #普通方法
    def eat(self):
        print(self.name,"狗狗在啃骨头！")

    def run(self,speed):
        print(self.name,"狗狗在飞快的跑",speed)


#实例化对象
dog = Dog("小花",3,"白色")
dog.color = "红色"
print(dog.color)
dog.eat()
dog.run("3m/s")
'''

'''类的封装'''
'''
class Card(object):

    def __init__(self,num,pwd,ban):
        self.num = num
        self.pwd = pwd
        self.__ban = ban     #私有属性（只能在类的内部被访问）

    def cun(self):
        print("存款！")

    def getBan(self,numm,pwdd):
        if numm==self.num and pwdd == self.pwd:
            return self.__ban
        else:
            return "输入错误！"


card = Card("1000","123456",1000) #开卡

print(card.getBan("1000","123456"))
#print(card._Card__ban)    #不安全
'''

# 异常的处理

a =[12,55,623,5,0,65,33]

for i in a:
    print("0--------0",i)




    try:                                 #写可能会报错或者异常的代码

        print(i/3)
    except Exception as e:                      # 捕获try语句里面的异常，Exception 就是捕获到的异常对象
        print("出现错误：",e)
    else:
        print("-------------正常")                #没有异常时执行的语句
    finally:
        print("==本次结束==")                       #无论是否异常，都会执行的语句




