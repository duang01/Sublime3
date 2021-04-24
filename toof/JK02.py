import requests
import json
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

url01 = "https://www.zhihu.com/explore"
url02 = "http://www.baidu.com"
url03 = "https://www.12306.cn"
url04 = "http://www.httpbin.org"

# 请求头的定制
# from_data = {'user':'51xuw','password':'8888'}
# header = {'user-agent':'Mozilla/5.0'}
# r = requests.post(url01+'/post',data=from_data,headers = header)
# print(r.text)
# print(r.json)

'''
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0'}
r = requests.get(url01,headers=header)
print(r.text)
'''

# cookie 的设置
# cookie = {'user':'51zxw'}
# r=requests.get(url01+'/cookie',cookies=cookie)
# print(r.text)

# 具体用法
# r = requests.get(url02)
# print(r.cookies)           # 获取cookie
# print(type(r.cookies))     # 查看coolie类型
# for key, value in r.cookies.items():          # 循环遍历打印cookie
#     print(key+':'+value)

# 文件上传    使用参数files 提交文件数据。
# file = {'file':open('data.json','rb')}
# r = requests.post(url02+'/post',files=file)
# print(r.text)
#

'''
#会话对象 session对象存储特定用户会话所需的属性及配置信息，解决接口之间的依赖关系
#   1.生成会话对象
s = requests.Session()

#   2.设置cookie
r = s.get(url03+'/cookies/set/user/51zxw')
print(r.text)

#   3.获取cookie
r=s.get(url03+'/cookies')
print(r.text)

'''

# SSL证书验证和代理设置
# 1.证书验证
# r = requests.get('https://www.12306.cn', verify=False)         # 不想验证证书用 verify = False 参数
# print(r.text)

'''
#        2.代理设置
proxi = {'http':'http://219.141.153.41:80'}          #设置代理地址
r = requests.get(url03+'/get',proxies = proxi)
print(r.text)

'''

# #身份认证
# #basic采用的是base64加密算法
# r = requests.get(url04+'/basic-auth/51zxw/8888', auth=HTTPBasicAuth('51zxw', '8888'))
# print(r.text)
# print(r.status_code)

# #digest保证数据的安全性，采用MD5的加密算法
# r = requests.get(url04+'/digest-auth/auth/zxw/6666',auth=HTTPDigestAuth('zxw','6666'))
# print(r.text)
# print(r.status_code)


# 流式处理           返回多个值
r = requests.get(url04+'/stream/10', stream=True)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(data['id'])



