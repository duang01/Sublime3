from selenium import webdriver
import time

# 创建一个浏览器对象
drive = webdriver.Firefox()

# 设置浏览器的尺寸
size = drive.get_window_size()  # 获取浏览器尺寸
print(size)
time.sleep(3)

drive.set_window_size(800, 400)
size = drive.get_window_size()
print("已设置好浏览器尺寸")
time.sleep(3)

# 获取窗口位置
position = drive.get_window_position()
print(position)

# 设置访问的地址
url = 'http://www.baidu.com'
url2 = 'https://www.csdn.net'
time.sleep(3)

# 访问需要的地址
drive.get(url)
time.sleep(3)
drive.get(url2)
time.sleep(3)

# 前进和后退操作
drive.back()
print("后退一步:访问%s" % drive.current_url)
time.sleep(2)
drive.forward()
print("前进一步: 访问%s" % drive.current_url)
time.sleep(2)

# 保存快照操作
# data = drive.get_screenshot_as_png()
# with open('baidu.jpg', 'wb') as f:
#     f.write(data)

# 获取所有窗口的句柄
handle_list = drive.window_handles

# 切换句柄,通过句柄的下标索引解决
drive.switch_to.window(handle_list[1])

# 关闭浏览器
drive.close()

