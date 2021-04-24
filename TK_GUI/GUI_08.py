import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.set_window()
        self.create_top()
        self.create_body()
        self.create_bottom()

    #  设置窗口
    def set_window(self):
        self.root.title("GUI")                      # 设置窗口标题
        self.root.resizable(False, False)            # 设置窗口是否可放大，缩小

    #  创建顶部
    def create_top(self):
        tk.Label(self.root, text="Top").pack()

    #  创建主体
    def create_body(self):

        self.input = tk.StringVar()
        tk.Entry(self.root, textvariable=self.input).pack()

    #  创建底部
    def create_bottom(self):
        tk.Button(self.root, text="Bottom", command=self.onclick).pack()

    #  按钮回调函数
    def onclick(self):
        print(self.input.get())


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()




























