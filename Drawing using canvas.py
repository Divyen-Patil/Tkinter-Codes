## A python program to display drawing in canvas .

from tkinter import *

root = Tk()

root.title("Night Drawing")

root.wm_iconbitmap()

c = Canvas(root, bg = "black", height = 700, width = 1200)

## House

c.create_polygon(600,250,700,200,800,250,800,400,600,400,width = 2, fill = "yellow", outline = "red")

c.create_line(600,250,800,250, width = 2, fill = "red")

c.create_rectangle(650,275,750,375, width = 2, fill = "red")

### left side bushes

c.create_arc(0,350,200,450, start = 0,extent = 180, fill = "green")

c.create_arc(200,350,400,450, start = 0,extent = 180, fill = "green")

c.create_arc(400,350,600,450, start = 0,extent = 180, fill = "green")

## Right side bushes

c.create_arc(800,350,1000,450, start = 0,extent = 180, fill = "green")

c.create_arc(1000,350,1200,450, start = 0,extent = 180, fill = "green")

##   River

#c.create_polygon(0,500,200,450,400,550,450,500, width = 2, smooth = 1, fill = "blue", outline = "white")

c.create_polygon(0,500,1200,550,1200,600,0,600, width = 2, smooth = 1, fill = "blue", outline = "white")

###   Moon

c.create_oval(50,50,250,250, width = 2, fill = "white", outline = "white")

#c.create_line(600,150,625,175,650,150, width = 1, fill ="white")

c.create_oval(350,50,360,60, width = 2, fill = "white", outline = "white")

c.create_oval(450,70,460,80, width = 2, fill = "white", outline = "white")

c.create_oval(650,90,660,100, width = 2, fill = "white", outline = "white")

c.create_oval(950,220,960,230, width = 2, fill = "white", outline = "white")

c.create_oval(40,50,50,60, width = 2, fill = "white", outline = "white")

c.create_oval(1050,120,1060,130, width = 2, fill = "white", outline = "white")

c.create_oval(850,150,860,160, width = 2, fill = "white", outline = "white")

c.create_oval(400,170,410,180, width = 2, fill = "white", outline = "white")

c.create_oval(500,230,510,240, width = 2, fill = "white", outline = "white")

c.create_oval(850,50,860,60, width = 2, fill = "white", outline = "white")


##  Text

c.create_text(400,650, text = "Divyen Patil", font = ("Times", 40, "bold", "italic", "underline"), fill = "white")
c.pack()

root.mainloop()