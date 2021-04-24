import os
import time


class APP:
    """ adb  # 安装手机app"""
    def installapk(self, apkpath):
        cmd = 'adb install' + apkpath
        res = os.popen(cmd).read()
        print(res)

    """ adb  # 卸载手机app"""
    def uninstallapk(self, packagename):
        cmd = 'adb uninstall' + packagename
        res = os.popen(cmd).read()
        print(res)

    """ adb  # 等待时间"""
    def sleep(self, t):
        time.sleep(t)

    """adb # 打开APP  # activity:启动入口
    寻找启动入口命令 adb shell dumpsys activity | findstr 包名（net.csdn.csdnplus） | findstr LAUNCHER 
    == net.csdn.csdnplus/.activity.MainActivity
    
    """
    def startapp(self, activity):
        cmd = 'adb shell am start' + ' ' + activity
        res = os.popen(cmd).read()
        print(res)

        """app 点击操作, 两个参数：x 和 y 轴 （339，1257）"""
    def apptap(self, x, y):
        cmd = 'adb shell input tap ' + str(x) + ' ' + str(y)
        res = os.popen(cmd).read()
        self.sleep(3)

    """ app 的输入操作"""
    def appinput(self, s):
        cmd = 'adb shell input text ' + s
        res = os.popen(cmd).read()
        self.sleep(3)

    """adb 输入中文 1.安装ADBKeyboard.apk  2. adb shell am broadcast -a ADB_INPUT_TEXT --es msg"""
    def app_ch_input(self):
        pass

    """adb 截图操作"""
    def screenshot(self, imgname):
        cmd = 'adb shell /system/bin/screencap -p /sdcard/1/screenimg/screencap.png'
        res = os.popen(cmd).read()
        # 保存图片
        cmd = 'adb pull /sdcard/1/screenimg/screencap.png ./img/' + str(imgname)
        res = os.popen(cmd).read()

