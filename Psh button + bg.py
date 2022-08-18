## A PYTHON prgram to create three push buttons and change the background of the frame according to the button clicked by the user

from tkinter import *

class Mybutton:

    def __init__(self, root):
        self.f = Frame(root, height = 400, width = 500)

        self.f.propagate(0)
        self.f.pack()

        self.b1 = Button(self.f, text = "red", height=2,width=15,command = lambda:self.buttonclick(1))
        self.b2 = Button(self.f, text = "green", height=2,width=15,command = lambda:self.buttonclick(2))
        self.b3 = Button(self.f, text = "blue", height=2,width=15,command = lambda:self.buttonclick(3))

        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

    def buttonclick(self, num):
        if num==1:
            self.f["bg"] = "red"

        if num ==2:
            self.f["bg"] = "green"

        if num==3:
            self.f["bg"] = "blue"

root = Tk()

mb = Mybutton(root)

root.mainloop()