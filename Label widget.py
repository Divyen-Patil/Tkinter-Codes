###  A pyton program to diaplay a label upon clicking a push  button

from tkinter import *

class Mybutton:

    def __init__(self, root):
        
        self.f = Frame(root, width = 500, height = 350)

        self.f.propagate(0)

        self.f.pack()

        self.b1 = Button(self.f, text = "Click me", width=12,height=2,command=self.buttonclick)

        self.b2 = Button(self.f, text = "Close", height=2, width=15,command = quit)

        self.b1.grid(row = 0, column=1)
        self.b1.grid(row = 0, column=2)

    def buttonclick(self):

        self.label = Label(self.f, text = "Welcome to python", width = 20, height = 2, font=("Tomes",20,"bold","underline"),fg="blue")
        self.label.grid(row=2,column=0)


root = Tk()

mb = Mybutton(root)

root.mainloop()

