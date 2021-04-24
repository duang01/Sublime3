import tkinter as tk

root = tk.Tk()

f1 = tk.Frame(root)
f2 = tk.Frame(root)

tk.Label(f1, text='左1').pack()
tk.Label(f1, text='左2').pack()
tk.Label(f1, text='左3').pack()
tk.Label(f1, text='左4').pack()

tk.Button(f2, text="右一").pack(side="right", padx=10)
tk.Button(f2, text="右二").pack(side="left", ipadx=10)
tk.Button(f2, text="右三", bg="red").pack(side="left", padx=10, pady=10, ipadx=10, ipady=10 )

f1.pack(side="left")
f2.pack(side="left")

root.mainloop()