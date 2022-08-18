## A python program to crate a horizontal scroll bar attach it to a text widget to view the texrt from left and right

from tkinter import * 

class Myscrollbar:

    def __init__(self,root):

        self.t = Text(root, width=100,height=10,wrap=NONE)

        for i in range(50):
            self.t.insert(END, "This is divyen patil")

        self.t.pack(side=TOP, fill=X)

        self.h = Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)
        self.t.configure(xscrollcommand=self.h.set)

        self.h.pack(side=BOTTOM, fill=X)

root = Tk()
ms = Myscrollbar(root)
root.mainloop()
