from selenium import webdriver
import appium.webdriver

from UiAutoWeb import page


class GetDriver:
    # 1、声明web driver变量
    __web_drive = None

    # 1.2、声明 app driver变量
    __app_driver = None

    # 2、获取driver 方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是为空
        if cls.__web_drive is None:
            # 设置driver操作
            # 获取浏览器
            cls.__web_drive = webdriver.Firefox()
            cls.__web_drive.implicitly_wait(10)
            # 最大化浏览器
            cls.__web_drive.maximize_window()
            # 打开url
            cls.__web_drive.get(url)

        # 返回driver
        return cls.__web_drive

    # 3、退出driver 方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_drive:
            # 退出操作
            cls.__web_drive.quit()
            # 置空操作
            cls.__web_drive = None

    # 获取app_driver
    @classmethod
    def get_app_driver(cls):
        # 判断app_driver 为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '9'
            desired_caps['deviceName'] = page.advice

            # app信息
            desired_caps['appPackage'] = page.appPackage  # 包名
            desired_caps['appActivity'] = page.appActivity  # 启动名

            # 输入法
            desired_caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
            desired_caps['resetKeyboard'] = 'true'  # 运行结束后删除appium键盘
            desired_caps['noReset'] = 'true'  # 不做应用清除.

            # 设置app_driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app_driver
    @classmethod
    def quit_app_driver(cls):
        # 1、判断app_driver 不为空
        if cls.__app_driver:
            # 退出 __app_driver
            cls.__app_driver.quit()
            # 将__app_driver 置空
            cls.__app_driver = None


