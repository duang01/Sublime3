#景区卖票，解决不同窗口卖同一张票的情况

import threading
import datetime     #获取当前时间

num =100

#卖票
def sale(name):
    global num
    num = num -1
    print(name,"卖出一张票，还剩：",num,"张！")

#售票窗口（2个线程表示）
while 1==1:
    if num > 0:
        ta = threading.Thread(target=sale,args=("A窗口",))
        tb = threading.Thread(target=sale, args=("B窗口",))
        ta.start()
        tb.start()

    else:
        break
print("票已卖完！请稍后再购买！")
now = datetime.datetime.now()          #获取当前日期
print(now)

'''
d=datetime.datetime(2019,10,1,12,40,45)          #获取指定的日期
print(d)
'''

#日期转字符串
now = datetime.datetime.now()
A = now.strftime("%Y-%m-%d %H:%M:%S")
print(A)


#字符串转日期
s = "2019-08-04 23:40:59"
e=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(e)