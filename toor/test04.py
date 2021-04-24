#循环结构学习

a = [1,2,5,68,87,56,62,35,99]
max = a[0]
for x in range(0,len(a)-1):
    if max <= a[x+1]:
        max = a[x+1]

print(max)

