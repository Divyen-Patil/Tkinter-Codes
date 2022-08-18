### A python program to create two spin box and retrive the values displayed in the spin boxes when the user clicks on the push button

from tkinter import *

class Myspinbox:

    def __init__(self, root):

        self.f = Frame(root, width = 500, height=350)
        self.f.propagate(0)
        self.f.pack()

        self.val1 = IntVar()
        self.val2 = StringVar()

        self.s1 = Spinbox(self.f, from_=5, to=15,textvariable=self.val1,width=15,fg="blue",bg="yellow",font=("Times", 14,"bold"))
        self.s2 = Spinbox(self.f, values = ("Mumbai","Delhi","Hyderabad","Rajasthan","kolkatta","banglore"),
        textvariable=self.val2,width=15,fg="blue",bg="yellow",font=("Times", 14,"bold"))

        self.b1 = Button(self.f, text = "Get values from the spinbox",command=self.display)

        self.s1.place(x=50,y=50)
        self.s2.place(x=50,y=100)
        self.b1.place(x=50,y=150)

    def display(self):

        a = self.val1.get()
        b = self.val2.get()

        lbl1 = Label(text = "Selected value is : "+str(a)).place(x=50,y=200)
        lbl2 = Label(text = "Selected city is : "+str(b)).place(x=50,y=220)

root = Tk()
mb = Myspinbox(root)
root.mainloop()