### A python program to create a list box with universities names and display the selected universities names in a text box

from tkinter import *

class Listboxdemo:

    def __init__(self, root):

        self.f = Frame(root,width=500,height=350)
        self.f.propagate(0)
        self.f.pack()

        self.lbl = Label(self.f, text="click one or more of the universities below", font=("Calibri",14))
        self.lbl.place(x=50,y=50)

        self.lb = Listbox(self.f,font=("Arial",12,"bold"),height=10,selectmode=MULTIPLE)
        self.lb.place(x=50,y=100)

        for i in ["Stanford university","Oxford university","Howard university","SPPU university","Cambridge university"]:
            self.lb.insert(END, i)
        
        self.lb.bind("<<ListboxSelect>>", self.on_select)

        self.t = Text(self.f, width=40,height=10, wrap=WORD)
        self.t.place(x=300, y=100)

    def on_select(self, event):

        self.lst = []

        indexes = self.lb.curselection()

        for i in indexes:
            self.lst.append(self.lb.get(i))

        self.t.delete(0.0, END)
        self.t.insert(0.0,self.lst)

root = Tk()
root.title("Demonstration of listbox")
obj = Listboxdemo(root)
root.mainloop()




