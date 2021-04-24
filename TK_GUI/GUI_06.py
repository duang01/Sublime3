import tkinter as tk


def callback(a):
    print("被点击了", a.get())

def creat_view():
    val = tk.StringVar()
    tk.Entry(root, textvariable=val).pack()
    tk.Button(root, text="btn", command=lambda: callback(val)).pack()

root =tk.Tk()
creat_view()



root.mainloop()