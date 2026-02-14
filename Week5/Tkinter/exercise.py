from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("GOAT")
root.geometry("350x400")

label_general = Label(root,text="Greatest number of the three!")
label_general.grid(column=0,row=0)

lbl1 = Label(root,text="First number")
lbl1.grid(column=0,row=1)
num1_txtbox= Entry(root)
num1_txtbox.grid(column=1,row=1)

lbl2 = Label(root,text = "Second number")
lbl2.grid(column=0,row=2)
num2_txtbox = Entry(root)
num2_txtbox.grid(column=1,row=2)


lbl3 = Label(root,text="Third number")
lbl3.grid(column=0,row=3)
num3_txtbox = Entry(root)
num3_txtbox.grid(column=1,row=3)

lbl4 = Label(root,text="Result")
lbl4.grid(column=0,row=4)
result_txtbox = Entry(root)
result_txtbox.grid(column=1,row=4)

def emptychecker(value):
    try:
        return float(value)
    except ValueError:
        return
    
def refresh():
    num1_txtbox.delete(0,END)
    num2_txtbox.delete(0,END)
    num3_txtbox.delete(0,END)
    result_txtbox.delete(0,END)
    

def got():
    
    result_txtbox.delete(0,END)
 
    num1 = emptychecker(num1_txtbox.get())
    num2 = emptychecker(num2_txtbox.get())
    num3 = emptychecker(num3_txtbox.get())
    
    if (num1 or num2 or num3)== None:
        messagebox.showinfo("Enter numbers","Please enter all the three numbers.")
        return
    result = max(num1,num2,num3)
    # if num1>num2 and num1>num3:
    #     result_txtbox.insert(0,f"{num1} is the greatest of {num1,num2,num3}")
    # elif num2>num3:
    #     result_txtbox.insert(0,f"{num2} is the greatest of {num1,num2,num3}")
    # else:
    #     result_txtbox.insert(0,f"{num3} is the greatest of {num1,num2,num3}")
    result_txtbox.insert(0,f"{result} is the greatest of {num1},{num2},{num3}")

show_result = Button(root,text = "Show result", command = got)
show_result.grid(column=0,row=5)
refresh_button = Button(root,text = "Refresh", command = refresh)
refresh_button.grid(column=1,row=5)

root.mainloop()
    
    

