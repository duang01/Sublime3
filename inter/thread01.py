"""自己实现一个可以迭代的对象--迭代器 """
import time
from  collections import Iterable
from  collections import  Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用 for，那么必须实现__iter__的方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("老二")
classmate.add("老三")

for name in classmate:
    print(name)