import tkinter as tk

root = tk.Tk()

tk.Label(root, text="单击").pack()


def callback(event):
    print("EventType=", event.type)
    # print("keysym=", event.keysym)
    print("Num", event.num)


frame = tk.Frame(root, bg="red", width=100, height=80)
frame.bind("<Button-1>", callback)
frame.bind("<Button-2>", callback)
frame.bind("<Button-3>", callback)
frame.bind("<Double-Button-1>", callback)
frame.bind("<Triple-Button-1>", callback)

# root.bind("<Keypress-a>", callback)

frame.pack()

root.mainloop()