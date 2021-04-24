#numpy的使用；ndarray n维数组
import numpy as np

#创建数组 array
data1 = [6,4,5,0,1]
D1 = np.array(data1)           #创建一维数组
print(D1)

data2 = [[1,2,3,4,5,6,],[7,8,9,10,11,15]]
D2 = np.array(data2)
print(D2)

D3 = np.ones((4,10))
print(D3)
D4 = np.zeros((3,10))
print(D4)

D0 = D1*2
print(D0)

n1  = np.arange(1,20,2)
print(n1)
n1[2:5] = 10
print(n1[2:5])
print(D2[0,3])
