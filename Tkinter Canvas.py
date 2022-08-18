### A Gui program that demonstrate the creation of various shapes in canvas

from tkinter import *

root = Tk()

c = Canvas(root, bg="red", height=700, width = 1200, cursor = "hand2")

id = c.create_line(50,50,200,50,200,150,width = 4,fill = "white")

id = c.create_oval(100,100,400,300,width = 5, fill = "White", outline = "black", activefill = "green")

id = c.create_polygon(10,10,200,200,300,200, width = 4, fill = "green", outline = "black", smooth = "1", activefill = "blue")

id = c.create_rectangle(500,200,700,600, width = "4", fill = "gray", outline = "black", activefill = "yellow")

fnt = ("Times", 40, "bold italic underline")
id = c.create_text(500,100, text = "My Canvas", font = fnt, fill="yellow", activefill="green")

c.pack()

root.mainloop()