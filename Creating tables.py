###  A GUI program to display a table wieth several rows and columns

from tkinter import *

class Mytable:

    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_cols):
                self.e = Entry(root, width=20,fg="blue",font = ("Arial", 16,"bold"))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


lst = [(1,"Divyen Patil", "Dharangaon",10000),
        (2,"Yash Patil", "Dharangaon",20000),
        (3,"Lucky Pawar", "Mumbai",30000),
        (4,"Pratik Pawar","Songad",40000)]

total_rows = len(lst)
total_cols = len(lst[0])

root = Tk()
mt = Mytable(root)
root.mainloop()