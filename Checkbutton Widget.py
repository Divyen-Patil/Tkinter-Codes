## A python program to creste 3 check buttons and know  which option are selcted by the user

from tkinter import *

class Checkbutton:

    def __init__(self, root):

        self.f = Frame(root, width=500, height = 350)
        self.f.propagate(0)
        self.f.pack()

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        self.c1 = Checkbutton(self.f, bg="yellow",fg="green",font=("Times",40,"bold"), text="Java", variable = self.var1,command=self.dispaly)
        self.c2 = Checkbutton(self.f, bg="yellow",fg="green",font=("Times",40,"bold"), text="Python", variable = self.var2,command=self.dispaly)
        self.c3 = Checkbutton(self.f, bg="yellow",fg="green",font=("Times",40,"bold"), text="C++", variable = self.var3,command=self.dispaly)

        self.c1.place(x=50,y=100)
        self.c2.place(x=200,y=100)
        self.c3.place(x=350,y=100)

    def dispaly(self):

        x = self.var1.get()
        y = self.var2.get()
        z = self.var3.get()

        str = ''

        if x==1:
            str += "Java"

        if y==1:
            str += "Python"

        if z==1:
            str += "C++"

        lbl = Label(text=str, width=200, height=20,font = ("Times"), fg = "blue")
        lbl.place(x=50,y=150)

root = Tk()
mb = Checkbutton(root)
root.mainloop()