# name1 = 'tom'
# name2 = 'jerry'
# name = 'errlod'
#


import os


# print('two boys are {} and {}'.format(name1, name2))
# print(f'my name is {name.islower()}')
# print(f'1+1 = {1+1}')

# try:
#     num1 = int(input("请输入一个除数"))
#     num2 = int(input("请输入一个被除数"))
#     a = num1/num2
#     print(a)
# except SyntaxError:
#     print("这是一个SyntaxError异常")
# except ValueError:
#     print("这是一个值异常")
# except ZeroDivisionError:
#     print("不能为0")

# 新建文件夹和文件
import random
import time


print(os.getcwd())
if not os.path.exists("./b"):
    os.mkdir("b")
if not os.path.exists("./b/test.txt"):
    f = open("./b/test.txt", "w")
    f.write("hello os to  be  num01")
    f.close()
else:
    num = random.randint(0, 10)
    f = open("./b/test.txt", "a")
    f.write('\r\n'+f'你好呀 boys{num}')   # 追加文字
    f.write('\r\n 是你呀 girl {}'.format(num))
    f.close()


print(os.getcwd())




