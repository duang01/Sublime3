# json.dumps  将python数据类型转化为json数据类型
# json.loads  将json数据类型转化为python数据类型

import json
import unittest


data = {'id': 1, 'name': '51zxw', 'password': '66666'}
# print(type(data))
#
# json_str = json.dumps(data)
# print(type(json_str))
# print(json_str)
#
# data1 = json.loads(json_str)
# print(data1)
# print(type(data1))

# json 文件处理
# 写入JSON 数据到文件             将python数据类型转化为json数据类型文件并存储为data.json 文件
# with open('data.json','w') as f:
#     json.dump(data,f)


# 读取json数据文件                 将json文件读取出来并转化为python数据类型
with open('data.json', 'r') as f:
    data2 = json.load(f)
    print(data2)
    print(type(data2))