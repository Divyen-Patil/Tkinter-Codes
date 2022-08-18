##  A python program to display image in the canvas

from tkinter import *

root =Tk()

c = Canvas(root, bg = "white", height = 700, width = 1200)

file1 = PhotoImage(file="")
file2 = PhotoImage(file = "")

id = c.create_image(500,200, anchor = NE, image = file1, activeimage = file2)

id = c.create_text(500,500, text = "This is a thrilling photo", font = ("Times", 40, "bold", "underline"), fill ="blue")
c.pack()

root.mainloop()