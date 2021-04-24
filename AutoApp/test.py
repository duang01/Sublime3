
from AutoApp.autoapp01 import APP


APP = APP()
# 安装测试
# APP.installapk('./DES/APP')

# 打开APP
APP.startapp('net.csdn.csdnplus/.activity.MainActivity')

# 等待时间
APP.sleep(6)
APP.screenshot(0)

# 点击操作
APP.apptap(339, 1257)
APP.sleep(3)
APP.screenshot('1.png')

APP.apptap(226, 143)
APP.sleep(2)
APP.screenshot('2.png')

# 输入操作
APP.appinput('python')
APP.sleep(3)
APP.screenshot('3.png')

APP.apptap(980, 158)
APP.sleep(3)
APP.screenshot('4.png')
# 卸载测试
# APP.uninstallapk('wangzhe')
