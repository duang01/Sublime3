
import threading
import time
lock = threading.Lock()   #创建一个线程锁（互斥锁），解决多个线程中线程执行错乱问题
                            #全局解释器锁（GIL）:不管CPU核心数量是多少，都保证python程序中同一时间点只能执行一个线程；可以使用多进程解决这个问题
'''
def run(name):
    print(name,"线程执行了")
    time.sleep(5)

#程序执行时，程序本身就是一个线程，叫主线程；手动创建的线程叫子线程，主线程的执行中不会等待子线程执行完毕，就会直接执行后面的代码
#创建线程
t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))

t1.start()          #启动线程
t2.start()


t1.join()               #设置子线程执行完毕之后在执行主线程内容
t2.join()


print("执行完毕！")'''

num = 100

#线程锁的目的：保证在运行的线程执行完毕在执行其它线程
def run(name):
    lock.acquire()             #设置线程锁
    global num               #设置为全局变量
    num = num - 1
    print("线程",num,"执行了，目前num的值为：",num)
    lock.release()             # 释放线程锁

  #创建并启动100个线程
for i in range(100):
    t = threading.Thread(target=run,args=(i+1,))
    t.start()