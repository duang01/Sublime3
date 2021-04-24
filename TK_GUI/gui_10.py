from tkinter import *

root = Tk()

list_var0 = StringVar()
list_var0.set(["GO", "Python", "Java", "JavaScript"
              "c", "C++", "PHPHOHOHOHPHPHPHPHHPHPHPPHPHPHPPHPHPHPPHPHPP"])

"创建窗口顶部的菜单栏对象"
menu_bar = Menu(root)

"将菜单栏对象设置给根窗口"
root["menu"] = menu_bar         # 等价于 root.config(menu=menu_bar)

"创建“文件”联级菜单"
file_menu = Menu(menu_bar, tearoff=0)
"在菜单栏上添加菜单标签，并将该标签与对应的联级菜单关联起来"
menu_bar.add_cascade(label="文件", menu=file_menu)

"在 文件 菜单中添加菜单项"
file_menu.add_command(label="新建", accelerator="Ctrl+N")
file_menu.add_command(label="打开", accelerator='Ctrl+O')
file_menu.add_command(label="保存", accelerator="Ctrl+S")

'添加分割线'
file_menu.add_separator()
file_menu.add_command(label="退出", accelerator="Ctrl+F4")

about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="关于", menu=about_menu)
about_menu.add_command(label="关于")
about_menu.add_command(label="帮助")

'#创建滚动条//分别创建x,y方向两个滚动条，orient属性设置起滚动方向'
y_bar = Scrollbar(root, orient=VERTICAL)
x_bar = Scrollbar(root, orient=HORIZONTAL)


'添加一个列表框'
list_box = Listbox(root, listvariable=list_var0, selectmode=EXTENDED, yscrollcommand=y_bar.set,
                   xscrollcommand=x_bar.set, height=5)
'EXTENDED ；BROWSE ; SINGLE ; MULTIPLE 四个参数'

y_bar["command"] = list_box.yview
x_bar["command"] = list_box.xview

'设置布局方位'
y_bar.pack(side=RIGHT, fill=Y)
x_bar.pack(side=BOTTOM, fill=X)
list_box.pack(anchor=NW, fill=BOTH, expand=YES)

root.mainloop()
