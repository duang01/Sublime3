import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)


tk.Label(frame, text="这是一个标签", bg="red" ).pack()
tk.Button(frame, text="A", ).pack(side=tk.LEFT)
tk.Button(frame, text="B", ).pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C", ).pack(side=tk.RIGHT, )
tk.Button(frame, text="D", ).pack(side=tk.TOP, fill=tk.BOTH)


frame.pack()

root.mainloop() 