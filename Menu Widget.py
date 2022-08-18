### A python program to create a menu bar and adding File and Edit menus with some menu items 

from tkinter import *

class Mymenudemo:
    
    def __init__(self, root):

        self.menubar = Menu(root)

        root.config(menu = self.menubar)
        self.filemenu = Menu(root, tearoff=0)

        self.filemenu.add_command(label = "New", command=self.donothing)
        self.filemenu.add_command(label = "Open", command=self.donothing)
        self.filemenu.add_command(label = "Save", command=self.donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label = "exit", command=root.destroy)

        self.menubar.add_cascade(label="File", menu = self.filemenu)

        self.editmenu = Menu(root, tearoff=0)

        self.editmenu.add_command(label = "Cut", command=self.donothing)
        self.editmenu.add_command(label = "Copy", command=self.donothing)
        self.editmenu.add_command(label = "Paste", command=self.donothing)


        self.menubar.add_cascade(label="Edit", menu = self.editmenu)

    def donothing(self):
        pass

root = Tk()
root.title("Menu bar demonstration")
obj = Mymenudemo(root)
root.mainloop()
        


