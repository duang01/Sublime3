"""正则表达式 的常见使用        """
import requests
import re
'''
import re

# 常用的方法
re.compile()            # 预先编译匹配
re.match()              # 从头找一个
re.findall()            # 找所有
re.search()             # 只找一个
re.sub()                # 替换

""" 需要注意的有 """

re.findall("a(.*?)b", "str")    # 能够返回括号中的内容，括号前后的内容起到定位和过滤的效果

'''


class CSDN:
    def __init__(self):
        self.start_url = "https://www.csdn.net"
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    def parse_url(self, url):    # 发送请求
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str):
        pass

    def run(self):  # 实现主要逻辑
        # 1. start_url
           pass
        # 2. 发送请求，获取响应

        # 3. 提取数据
        # 4. 保存相应内容



