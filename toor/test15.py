# json 数据结构的学习 {key:value,key:value......}

import json

#json 转字符串
j = '{"city":"北京","name":"熊猫"}'
p = json.loads(j)
print(p)
print(type(p))


#字典转json

dictt = {"city":"湖南","name":"辣椒"}
ss = json.dumps(dictt,ensure_ascii=False)
print(ss)
print(type(ss))


'''
encode()
decode()
ascii
gb2312
gbk
unicode
utf-8
python3中字符串的两种类型：bytes ,str ;str存储unicode类型，bytes存储byte类型（二进制）

'''

#字符串转byte(encode)------编码
a = "中华人民共和国万岁！"
b = a.encode("utf-8")   #转成字节码
print(b)

#byte转字符串（unicode）-----解码
c = b.decode("utf-8")
print(c)

#编码方式和解码方式必须一致

'''
至此2019-7-5 0:30 python基础部分学习完毕，
                    历时17天，每晚1-2小时。

1.数据挖掘---爬虫（爬虫框架，数据清洗，数据库）
2.web编程---网站（前端，web框架，数据库）
3.数据分析--（数学，统计学，行业知识，数学挖掘）
---------------------------------------------------前行目标：测开+数据分析

'''