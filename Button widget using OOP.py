## A python program to create a push button and bind it with an event handler function using command option  ########

from tkinter import *

class MyButton:

    def __init__(self,root):
        self.f = Frame(root, height = 200, width = 300)
        self.f.propagate(0)

        self.f.pack()

        self.b = Button(self.f, text="My button", height = 2, width=15,bg="yellow", fg="blue", activebackground="green", activeforeground="red",command = self.buttonclick)

        self.b.pack()

    def buttonclick(self):
        print("You have clicked me")

root = Tk()

mb = MyButton(root)

root.mainloop()