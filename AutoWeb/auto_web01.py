"""我是一个人呐 还是一个人呐  为何还是一个人啊
1.基于selenium 网络自动化获取疫情信息
2.

"""
import random,os, time

# a = """5555abd dkiekjkK Kwelk5555"""
#
# b = [1, ['w', 'we', 'ewe'], 2, 'ad']
# # print(type(a))
# # a1 = a[:-1:2]
# # print(a1)
# # print(type(a1))
# # a2 = a.find('e')
# # print(a2)
# # a3 = a.capitalize()
# # print(a3)
# # a4 = a.title()
# # print(a4)
# # for c in b:
# #     print(c)
# #
# # print('*'*50)
# # index = 0
# # l = len(b)
# # while index < l:
# #     value = b[index]
# #     print(value)
# #
# #     index += 1
#
#
# my_list = []
#
# for i in range(6):
#     value = random.randint(-10, 50)
#     my_list.append(value)
#     my_list.sort(reverse=True)
#
# print(my_list)
#
# # 一个学校3间办公室让8个老师随机进到办公室
laoshi = "ABCDEFGH"
school = [[], [], []]

for c in laoshi:
    index = random.randint(0, 2)
    school[index].append(c)

print(school)

for i, value in enumerate(school):
    print(i, value)
#


def gic(name, age):
    """

    :param name:
    :param age:
    """
    print("name:" % name)
    print("age:" % age)

# # 匿名函数


# f = lambda name: print("name:%s" % name)
# f("wangwu")


(lambda name, age: print("name:%s" % name, "age:%s" % age))("zhagnsan", 18)

print((lambda a, b: a+b)(10, 20))

# # 列表推导式
my_list = [i for i in range(1, 101)]
print(my_list)

my_list = ["haha" for i in range(30)]
print(my_list)

# my_list = []
for i in range(1, 51):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)


my_list = [i for i in range(1, 51) if i % 2 == 0]
print(my_list)

# 创建文件
# file = open("log.txt", "w")
# file.write("hello nihao")

# 重命名文件
# os.rename('log.txt', 'langx')

# 获取当前的绝对路径
ret = os.getcwd()
print(ret)

# 改变当前默认的目录
os.chdir("../")
print(os.getcwd())

# 获取当前目录列表
my_list = os.listdir()
print(my_list)

# 创建和删除文件夹
os.mkdir("wenjian")
time.sleep(5)
os.rmdir('wenjian')

# 批量修改文件名
''' 
    1.当前目录创建一个文件夹
    2、指定默认目录
    3、创建批量文件
'''


# os.mkdir("批量文件")
os.chdir("批量文件")
print(os.getcwd())
for i in range(1, 11):
    f = open('hm%d.txt' % i, 'w')
    f.close()

# print("文件创建完成--")
#
os.chdir("./批量文件")
mylist = os.listdir()
for filename in mylist:
    print(filename)
    filename1 = filename.replace(".txt", "[中国].txt")
    os.rename(filename, filename1)

















