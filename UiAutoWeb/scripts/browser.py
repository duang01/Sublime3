"""
    目标：
        1、多线程应用
        2、不同浏览器的使用和启动参数
"""

# 1、导包
from selenium import webdriver
import threading
from time import sleep


# 封装操作脚本
def get_baidu(driver):
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.quit()


# 2、封装drive
def get_driver(browser):
    # 定义一个空变量
    cap = None

    # 判断浏览器类型
    if browser == "chrome":
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == "firefox":
        cap = webdriver.DesiredCapabilities.FIREFOX.copy()

    # 修改默认平台名称
    cap['platform'] = "WINDOWS"

    # 返回driver
    return webdriver.Remote("http://127.0.0.1:4444/wd/hub", cap)


# 3、遍历多线程
# 3.1 定义浏览器列表
browserName = ['chrome', 'firefox']

# 3.2 遍历浏览器列表
for browser in browserName:
    driver = get_driver(browser)

    # 3.3 实例化线程及启动
    threading.Thread(target=get_baidu, args=(driver,)).start()






