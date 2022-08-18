### A python program to create radio button and know which button is selected by the user  

from tkinter import *

class Myradio:

    def __init__(self, root):

        self.f = Frame(root, height=350,width=500)
        self.f.propagate(0)
        self.f.pack()

        self.var = IntVar()

        self.r1 = Radiobutton(self.f, bg="yellow",fg="green",font=("Georgia", 20,"underline"),text="Male",variable=self.var,value=1,command=self.display)
        self.r2 = Radiobutton(self.f, bg="yellow",fg="green",font=("Georgia", 20,"underline"),text="Female",variable=self.var,value=2,command=self.display)

        self.r1.place(x=50,y=100)
        self.r2.place(x=200,y=100)

    def display(self):
        x = self.var.get()

        str = ''
        if x==1:
            str += "You selected : Male"

        if x==2:
            str += "You selected : Female"

        lbl = Label(text = str, fg = "blue").place(x=50,y=150,width=200,height=20)

root = Tk()
mb = Myradio(root)
root.mainloop()