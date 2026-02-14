from tkinter import *

root = Tk()
root.title("How to change your background")
root.geometry("350x400")

def change_bg(color):
    b1.configure(foreground="black")
    b2.configure(foreground="black")
    b3.configure(foreground="black")
    b4.configure(foreground="black")
    if color == "red":
        root.configure(background ="red")
        b1.configure(foreground="red")
    elif color == "green":
        root.configure(background="green")
        b2.configure(foreground="green")
    elif color == "blue":
        root.configure(background = "blue")
        b3.configure(foreground = "blue")
    else:
        root.configure(background = "yellow")
        b4.configure(foreground = "yellow")
        
b1 = Button(root, text = "Red",font = "Helvetica 16 bold italic", command=lambda: change_bg("red"), width=10)
b1.grid(column = 0, row=0)

b2 = Button(root,text = "Green",font = "Helvetica 16 bold italic",command=lambda: change_bg("green"), width=10)
b2.grid(column=1, row=0)

b3 = Button(root,text="Blue",font = "Helvetica 16 bold italic", command=lambda: change_bg("blue"), width=10)
b3.grid(column=0, row=1)

b4 = Button(root,text="Yellow", font = "Helvetica 16 bold italic", command=lambda: change_bg("yellow"), width=10)
b4.grid(column=1,row=1)

root.mainloop()