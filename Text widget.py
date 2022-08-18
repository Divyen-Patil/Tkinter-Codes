## A python program to create a text widget with a vertical scroll bar attached to it.
## also,highlight the first line of the text and dispaly image in the text widget

from tkinter import *

class Mytext:

    def __init__(self, root):


        self.t = Text(root, width = 20, height=5, font=("Times",10,"bold"),fg="blue",bg="yellow",wrap = WORD)

        self.t.insert(END, "Text widget\nThe text is inserted into text widget\nThis is second line\nThis is third line\n")

        self.t.pack(side=LEFT)

        self.img = PhotoImage(file="")
        self.t.image_create(END, image = self.img)

        self.t.tag_add("Start", "1.0", "1.11")
        self.t.tag_configure("start", background="red", foreground="white",font = ("Lucida console", 20,"bold","underline"))

        self.s = Scrollbar(root, orient=VERTICAL,command=self.t.yview)
        self.t.configure(yscrollcommand=self.s.set)
        self.s.pack(side=RIGHT,fill=Y)

root = Tk()
mt = Mytext(root)
root.mainloop()