
'''a =[1,2,5,6,4,645,6,34,54,5,5]
maxx = max(a)
print(maxx)
'''
'''a=23
b=3
c=a/b
print( round(c,3))
'''
#import random  #生成随机数
#from urllib import request
#import os
#a=random.random()
#import webbrowser

#os.system("C:")
#webbrowser.open("http://www.baidu.com")

'''fh1 =open(r'D:\Atools\Sublime3\toor\001.txt',"a")  # r-- read 读取  w-- 写入 a--追加  fh1--文件句柄，用来控制文件
#data = fh1.readlines()
data2 = fh1.write("假如时光倒流我")  #如果文件存在，就重新写入；如果文件不存在；新建文件再写入
#print(data[3])
print(data2)

#for i in fh1:  #读取大文件
 #   print(i)

fh1.close()                        # 文件操作完毕后一定要关闭文件io资源
'''
##文件分为两大类：1.文本文件   2.二进制文件
fh = open(r'D:\Atools\Sublime3\toor\007.jpg',"rb")
data = fh.read()
print(data)

fh1 = open(r'D:\Atools\Sublime3\toof\003.jpg',"wb")
fh1.write(data)
fh.close()
fh1.close()
