
#多进程的实现，解决GIL问题  实现多任务同一时间执行
import time
from multiprocessing import Process

def run(name):
    print(name,"进程执行了！")
    time.sleep(5)

if __name__ == '__main__':

    #创建进程
    p1 = Process(target=run,args=("p1",))
    p2 = Process(target=run,args=("p2",))
    p3 = Process(target=run,args=("p3",))
    p4 = Process(target=run,args=("p4",))
    #p5 = Process(target=run,args=("p5",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    #p5.start()