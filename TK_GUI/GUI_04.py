import tkinter as tk

root = tk.Tk()

tk.Label(root, text="账号").grid(row=0, sticky="ew")
tk.Label(root, text="密码").grid(sticky="EW")

tk.Entry(root).grid(row=0, column=1, sticky="ew")
tk.Entry(root).grid(row=1, column=1, sticky="WE")

tk.Button(root,text="登录", bg="green").grid(row=2, column=0, columnspan=2, sticky="ew" )

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
