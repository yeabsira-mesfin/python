from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Arithmetic Calculator")
root.geometry("350x400")
label1 = Label(root,text="First", font = "Helvetica 16 bold italic")
label1.grid(column=0,row=1)

num1_txtbox = Entry(root)
num1_txtbox.grid(column=1,row=1)

label2 = Label(root,text="Second", font="Helvetica 16 bold italic")
label2.grid(column=0,row=2)

num2_txtbox = Entry(root)
num2_txtbox.grid(column=1,row=2)

label3 = Label(root,text="Result",font="Helvetica 16 bold italic")
label3.grid(column=0,row=3)

num3_txtbox = Entry(root)
num3_txtbox.grid(column=1,row=3)

def intvalid(value):
    try:
        return float(value)
    except ValueError:
        messagebox.showinfo("Invalid Input","Please enter numbers only!") 
        return None

def addF():
    num3_txtbox.delete(0,END)
    num1 = intvalid(num1_txtbox.get())
    num2 = intvalid(num2_txtbox.get())
    if num1 is None or num2 is None:
        return
    sum = num1 + num2
    num3_txtbox.insert(0,sum)
    
def subF():
    num3_txtbox.delete(0,END)
    num1 = intvalid(num1_txtbox.get())
    num2 = intvalid(num2_txtbox.get())
    if num1 is None or num2 is None:
        return
    diff = num1-num2
    num3_txtbox.insert(0,diff)
    
def mulF():
    num3_txtbox.delete(0,END)
    num1 = intvalid(num1_txtbox.get())
    num2 = intvalid(num2_txtbox.get())
    if num1 is None or num2 is None:
        return
    mul = num1*num2
    num3_txtbox.insert(0,mul)

def divF():
    num3_txtbox.delete(0,END)
    num1 = intvalid(num1_txtbox.get())
    num2 = intvalid(num2_txtbox.get())
    if num1 is None or num2 is None:
        return
    if num2 !=0:
        num3_txtbox.insert(0,num1/num2)
    else:
        messagebox.showinfo("Divison by zero","You can't divide a number by zero.")
        
add_button = Button(root,text="Addition",command=addF,font="Helvetica 10 bold italic",width=10)
add_button.grid(row=4, column=0)

diff_button = Button(root,text="Subtraction", command=subF,font="Helvetica 10 bold italic",width=10)
diff_button.grid(row=4,column=1)

mult_button = Button(root,text="Multiplication", command=mulF,font="Helvetica 10 bold italic",width=10)
mult_button.grid(column=0, row=5)

div_button = Button(root,text="Divison",command=divF,font="Helvetica 10 bold italic",width=10)

div_button.grid(column=1,row=5)

root.mainloop()
