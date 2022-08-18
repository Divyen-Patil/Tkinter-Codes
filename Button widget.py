###   A python program to create a push  button and bind it with an event handler function

from tkinter import * 

def buttonclick(self):
    print("You have clicked me")

root = Tk()

f = Frame(root, height=200, width=300)

f.propagate(0)

f.pack()

b = Button(f, text="My button", height = 2, width=15,bg="yellow", fg="blue", activebackground="green", activeforeground="red")
b.pack()

b.bind("<Button-1>", buttonclick)
root.mainloop()