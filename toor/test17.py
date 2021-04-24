from tkinter import *            #导入GUI界面库
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # self.helloLabel = Label(self,text='Hello world!')
        # self.helloLabel.pack()
        # self.quitButton = Button(self,text='Quit',command=self.quit)
        # self.quitButton.pack()
        self.alterButton = Button(self,text='Hello',command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)


app = Application()
app.master.title('Hello world')
app.mainloop()