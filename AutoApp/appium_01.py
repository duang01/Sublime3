from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 导入显示等待包


# server 启动参数
desired_caps = {}


# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '79d70e23'

# app信息
desired_caps['appPackage'] = 'com.myzaker.ZAKER_Phone'     # 包名
desired_caps['appActivity'] = 'com.myzaker.ZAKER_Phone.view.LogoActivity'               # 启动名

# 输入法
desired_caps['unicodeKeyboard'] = 'true'               # 支持中文输入，而且不会乱跳
desired_caps['resetKeyboard'] = 'true'                 # 运行结束后删除appium键盘
desired_caps['noReset'] = 'true'                       # 不做应用清除.

# 启动appium应用服务
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)    # 添加一个隐性等待时间

'''定位方法'''
driver.find_element_by_id("com.myzaker.ZAKER_Phone:id/cover_pic").click()
driver.swipe(479, 1340, 479, 799)
'''用显示等待来等待某个元素的出现，当作断言'''
# WebDriverWait(driver, 5).until(
#     lambda x: x.find_element_by_class_name("android.widget.ImageView[2]", "NOT FIND THIS!")
# )

# driver.find_elements_by_class_name("android.widget.ImageView")[2].click()
'''获取webview页面，切换到webview再定位'''
# ret = driver.contexts
# print(ret)

'''toast弹窗内容定位'''

driver.find_element_by_xpath('//*[contains(@text,"热点")]').click()
# driver.find_elements_by_accessibility_id()
# driver.find_elements_by_android_uiautomator(u'UiSelector().resourceId("permission_allow_button").text("文本")')
driver.find_element_by_xpath(u'//*[contains(@text,"订阅")]').click()
driver.find_element_by_xpath(u'//*[@text="精读"]').click()
driver.find_element_by_xpath('//*[contains(@text,"热点")]').click()
driver.find_element_by_id('com.myzaker.ZAKER_Phone:id/title').click()
driver.swipe(479, 1340, 479, 799)
'''# 滑屏操作'''
# driver.swipe(882, 834, 320, 821)

'''按键操作'''
driver.press_keycode(4)

driver.find_element_by_id("com.myzaker.ZAKER_Phone:id/banner_img").click()
driver.swipe(479, 1340, 479, 799)
driver.press_keycode(4)
driver.press_keycode(4)


driver.quit()

