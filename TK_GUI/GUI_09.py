from tkinter import *

content = "汉皇重色思倾国，御宇多年求不得，杨家有女初长成，养在深闺人未识。\
          天生丽质难自弃，一朝选在君王侧。回眸一笑百媚生，六宫粉黛无颜色。"

root = Tk()
root.geometry("400x600")

top = LabelFrame(root, text="这是Lable")
top.pack(padx=8, pady=8, ipadx=4, ipady=4)

# 创建一个Lable
Label(top, text=content, bg="blue").pack()

bottom = LabelFrame(root, text="这是Message")
bottom.pack()

# 创建一个Message
Message(bottom, text=content, bg="green").pack()

# 下拉菜单
op_list = ["选项1", "选项2", "选项3"]
val = StringVar()
val.set(op_list[0])


# 指定数字范围
val_range = StringVar()
val_range.set(0)
Spinbox(root, textvariable=val_range, from_=-10, to=10).pack()

# 指定列表范围
Spinbox(root, value=op_list).pack()


OptionMenu(root, val, *op_list).pack()


root.mainloop()