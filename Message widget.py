###  A python program to display a message in the frame    

from tkinter import *

class Mymessage:

    def __init__(self, root):

        self.f = Frame(root, height = 350, width = 500)

        self.f.propagate(0)

        self.f.pack()

        self.m = Message(self.f, text="My name is divyen patil i have coded this program",
        width=200, font = ("Times", 20 ,"bold", "underline"),fg = "black")

        self.m.pack(side=TOP)

root = Tk()
mm = Mymessage(root)
root.mainloop()