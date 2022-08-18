### A python program to create a menu bar and adding File and Edit menus with some menu items 

from tkinter import *
from tkinter import filedialog

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

    def open_file(self):
        self.filename = filedialog.askopenfilename(parent=root,title="Select a file",
        filetypes=(("Python files ","*.py"),("All files", "*.*")))

        if self.filename != None:
            f = open(self.filename,"r")

            contents = f.read()
            self.t = Text(root, width=80, height=20,wrap=WORD)
            self.t.pack()
            self.t.insert(1.0, contents)
            f.close()

    def save_file(self):
        self.filename = filedialog.asksaveasfilename(parent=root,defaultextension=".txt")

        if self.filename != None:
            f = open(self.filename, "w")
            contents = str(self.t.get(1.0, END))
            f.write(contents)
            f.close()




root = Tk()
root.title("Menu bar demonstration")
obj = Mymenudemo(root)
root.mainloop()
        


