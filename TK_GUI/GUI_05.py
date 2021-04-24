import tkinter as tk

parent = tk.Tk()
parent.title("Find & Replace")

tk.Label(parent, text="Find:", bg="yellow").grid(row=0, column=0, sticky="ew")
tk.Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky="we", columnspan=9)
tk.Button(parent, text="Find", bg="green").grid(row=0, column=10, sticky="ew")
parent.grid_columnconfigure(0, weigh=1)
parent.grid_columnconfigure(2, weigh=1)
parent.grid_columnconfigure(10, weigh=1)

tk.Label(parent, text="Replace:", bg="yellow").grid(row=1, column=0, sticky="ew")
tk.Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky="we", columnspan=9)
tk.Button(parent, text="Find All", bg="blue").grid(row=1, column=10, sticky="ew")
tk.Button(parent, text="Replace", bg="yellow").grid(row=2, column=10, sticky="ew")
tk.Button(parent, text="Replace All", bg="green").grid(row=3, column=10, sticky="ew")


tk.Checkbutton(parent, text="Match whole word only").grid(row=2, column=1, ipadx=2, sticky=tk.W)
tk.Checkbutton(parent, text="Match Case").grid(row=3, column=1, ipadx=2, sticky=tk.W)
tk.Checkbutton(parent, text="Wrap around").grid(row=4, column=1, ipadx=2, sticky=tk.W)

tk.Label(parent, text="Direction:").grid(row=2, column=2, columnspan=4, padx=2, pady=2, sticky="w")
tk.Radiobutton(parent, text="UP", value=1).grid(row=3, column=2, columnspan=2, sticky="w")
tk.Radiobutton(parent, text="DOWN", value=2).grid(row=4, column=2, columnspan=2, sticky="W")

tk.Scale(parent, orient=tk.HORIZONTAL, tickinterval=20, length=200, bg="red").grid(row=5, column=1)

parent.mainloop()



