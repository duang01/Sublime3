import os

path = 'D:\\Atools\\Sublime3\\ApiAutoTest\\report\\'
lex = '.json'

filelist = os.listdir(path)
for f in filelist:
    if lex in f:
        print(f)
        del_file = path + f
        os.remove(del_file)
        print("已经删除：", del_file)
