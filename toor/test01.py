#encoding:utf-8
#运算符有优先级的
#容器

'''list1=[1,2,3,4,5,6,"hello","假如"] #定义一个列表
del list1[2]
list1.pop(1)
list1.insert(1,666)
list1[3]=10
print(list1)
print(len(list1))
'''
#a={"name":"张三","age":"23","hoppy":"打球"}#
import os

'''a={1,2,3,4,5,6}
b={4,5,6,7,8,9}

print(a-b) #集合的差
print(a|b) #集合的并集
print(a&b) #集合的交集
print(a^b) #集合的对称差'''

####
#三种结构 ：顺序结构， 循环结构 ，选择结构
#
#一；IF结构
cunkuan=int(input("请输入你的银行存款（万）："))
zizhu=int(input("请输入你老爸给你资助你多少钱（万）："))

if cunkuan>100:
	print("可以买宝马啦！")
	print("好开心@@@！")
	if zizhu>50:
		print("买宝马740")
	elif zizhu>30:
		print("买宝马520")
	elif zizhu>20:
		print("买宝马320")
	else:
		print("去二手市场买宝马")

elif cunkuan>60:
	print("买丰田")

elif cunkuan>30:
	print("买二手撤")

else:
	print("还是骑车吧@@@！")


