### A python program to create entry widget for entering user name and password and display the entered text

from tkinter import *

class Myentry:

    def __init__(self, root):
        
        self.f = Frame(root, width=500, height=350)
        self.f.propagate(0)
        self.f.pack()

        self.l1 = Label(text = "Enter the username : ")
        self.l2 = Label(text = "Enter your Password : ")

        self.e1 = Entry(self.f, width = 25, fg="blue",bg="yellow",font=("arial", 14))
        self.e2 = Entry(self.f, width = 25, fg="blue",bg="yellow",show="*")

        self.e1.bind("<Return>", self.display)
        self.e2.bind("<Return>", self.display)

        self.l1.place(x=50,y=100)
        self.e1.place(x=200,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=200,y=150)

    def display(self, event):
        str1 = self.e1.get()
        str2 = self.e2.get()

        lbl1 = Label(text = "Your username is : "+str1).place(x=50, y=200)
        lbl2 = Label(text = "Your username is : "+str2).place(x=50, y=220)

root = Tk()
mb = Myentry(root)
root.mainloop()