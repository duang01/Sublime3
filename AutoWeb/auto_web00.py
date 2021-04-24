"""web自动化平台的实现day01"""
import time
from selenium import webdriver

# 实例化浏览器
drive = webdriver.Firefox()
drive.set_window_size(800, 900)

# 请求浏览器，获取响应页面
drive.get("https://www.xueqiu.com")
time.sleep(10)

# 登录页面，定位元素
# drive.find_element_by_xpath('//*[@id="kw"]').send_keys("云打码")
# drive.find_element_by_xpath('//*[@id="su"]').click()
# time.sleep(5)


# 等待输入验证码
# ret = str(input())
# print("请输入验证码：%s" % ret)
# time.sleep(5)
# drive.find_element_by_xpath('//*[@id="code"]').send_keys(ret)

drive.find_element_by_name("q").send_keys("alibab")
time.sleep(3)
drive.find_element_by_xpath('//*[@type="button"]').click()
time.sleep(3)
drive.find_element_by_xpath('//*[contains(text(), "09988")]/../../../..//*[@class="follow__control"]').click()
time.sleep(5)
# 关闭浏览器
drive.close()
# drive.quit()
