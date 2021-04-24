import tkinter as tk
from PIL import Image, ImageTk


def onclick():
    global int_val
    print("我被戳了一下。。，",int_val.get())


def click():
    global val           # 设置全局变量

    print("你输入的是：", val.get())


root = tk.Tk()    # 创建一个画板即窗口

# img = Image.open('001.jpg')
# photo = ImageTk.PhotoImage(img)

label_1 = tk.Label(root, text='戳我有惊喜哦！')      # 创建组件
label_2 = tk.Label(root, bitmap='warning').pack()    # 加载内置图片
#label_3 = tk.Label(root,image=photo).pack()           # 加载自定义img图片
label_1.pack()

#按键控件
btn = tk.Button(root, text='戳我@', command=onclick).pack()
btn_1 = tk.Checkbutton(root, text='唱歌', command=click).pack()
btn_2 = tk.Checkbutton(root, text='跳舞', command=click).pack()

int_val = tk.IntVar()
btn_3 = tk.Radiobutton(root, variable=int_val, text='男', value=1, command=onclick).pack()
btn_4 = tk.Radiobutton(root, variable=int_val, text="女", value=2, command=onclick).pack()

#输入框控件
val = tk.StringVar()
#val.set("请输入：")

Entry_1 = tk.Entry(root, textvariable=val).pack()
Entry_2 = tk.Entry(root, textvariable=val, show='*').pack()

btn_5 = tk.Button(root, text='获取输入值', command=click).pack()


#滑动框控件
scale = tk.Scale(root, orient=tk.HORIZONTAL, tickinterval=20, length=200).pack()


root.mainloop()   #每个GUI程序都需要一个主循环
