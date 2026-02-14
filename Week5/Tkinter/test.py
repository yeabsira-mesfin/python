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
        return int(value)
    except ValueError:
        messagebox.showinfo("Invalid Input", "Please enter an integer only.")
        return None

def operate(op):
    num3_txtbox.delete(0, END)
    num1 = intvalid(num1_txtbox.get())
    num2 = intvalid(num2_txtbox.get())
    
    if num1 is None or num2 is None:
        return
    
    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        if num2 == 0:
            messagebox.showinfo("Division by zero", "Cannot divide by zero.")
            return
        result = num1 / num2
    
    num3_txtbox.insert(0, result)

add_button = Button(root, text="Add", command=lambda: operate("add"))
sub_button = Button(root, text="Sub", command=lambda: operate("sub"))
mul_button = Button(root, text="Mul", command=lambda: operate("mul"))
div_button = Button(root, text="Div", command=lambda: operate("div"))


add_button.grid(row=4, column=0)
sub_button.grid(row=4,column=1)
mul_button.grid(column=0, row=5)
div_button.grid(column=1,row=5)

root.mainloop()
