"""    基于天气的api  'https://www.sojson.com/api/weather.html'"""

#  1.接口地址url: https://www.sojson.com/open/api/weather/json.shtml

import requests
from urllib import parse

data = {'city': '北京'}
city = parse.urlencode(data).encode('utf-8')            # 对汉字进行一个编码的转码处理
url01 = 'http://t.weather.sojson.com/api/weather/city/101030100'

r = requests.get(url01)
# print(r.text)
# print(r.status_code)
response_data = r.json()
print(response_data['cityInfo'])
# print(response_data['data'])
print(response_data['message'])
# print(response_data['date'])

print("星期:" + response_data['data']['forecast'][0]['week'])
print("日期:" + response_data['data']['forecast'][0]['ymd'])
print("日出:" + response_data['data']['forecast'][0]['sunrise'])
print("最高:" + response_data['data']['forecast'][0]['high'])
print("最低:" + response_data['data']['forecast'][0]['low'])
print("落日:" + response_data['data']['forecast'][0]['sunset'])
print("天气:" + response_data['data']['forecast'][0]['type'])
print("风向:" + response_data['data']['forecast'][0]['fx'])
print("风力:" + response_data['data']['forecast'][0]['fl'])
print("注意:" + response_data['data']['forecast'][0]['notice'])

print("-------------@---------------@-------------@------------------@----------------------------")
print("星期:" + response_data['data']['forecast'][1]['week'])
print("日期:" + response_data['data']['forecast'][1]['ymd'])
print("日出:" + response_data['data']['forecast'][1]['sunrise'])
print("最高:" + response_data['data']['forecast'][1]['high'])
print("最低:" + response_data['data']['forecast'][1]['low'])
print("落日:" + response_data['data']['forecast'][1]['sunset'])
print("天气:" + response_data['data']['forecast'][1]['type'])
print("风向:" + response_data['data']['forecast'][1]['fx'])
print("风力:" + response_data['data']['forecast'][1]['fl'])
print("注意:" + response_data['data']['forecast'][1]['notice'])
