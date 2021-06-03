
from ApiAutoTest.tools.read_yaml import read_yaml


""" 公共变量 """
# 1、请求域名
host = "http://ttapi.research.itcast.cn"
# 2、请求信息头
headers = {"Content-Type": "application/json"}

# 3、提取的文章id值
article_id = None
# 4、接收分布文章读取的数据
data_article = read_yaml("mp_article.yaml")
print(data_article)
# 文章title
title = data_article[0][0]
# 文章内容
content = data_article[0][1]
# 文章所属频道id
channel_id = data_article[0][2]
# 文章所属频道
channel = data_article[0][3]
