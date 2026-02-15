from tkinter import *
from tkinter import messagebox,simpledialog
# import tkinter as tk
from tkinter.ttk import *
# # window = Tk()
# # window.title("Welcome to all! ")
# # window.geometry('100x100')
# # print("Before mainloop")
# # window.mainloop()
# # print("After mainloop")
# window = Tk()
# window.title("Welcome ot Hps app")
# lbl = Label(window,text ="Welcome to all")
# lbl.grid(column=1,row=1,padx=50, pady=50)
# window.geometry('300x300')
# window.mainloop()
# window = Tk()
# window.title("Welcome to all")
# lbl1 = Label(window,text="Enter first Name: ")
# en1 = Entry(window)
# lbl1.grid(column=0, row=0,padx= 20,pady=20)
# en1.grid(column=1,row=0)

# lbl2 = Label(window,text="Enter Second Name: ")
# en2 = Entry(window)
# lbl2.grid(column=0, row=1)
# en2.grid(column=1,row=1)

# but1 = Button(window,text="Submit")
# but2 = Button(window,text="Reset")
# but1.grid(column = 0, row=2)
# but2.grid(column = 1, row=2)

# lbl3 = Label(window,text="Result: ")
# en3 = Entry(window)
# lbl3.grid(column = 0, row=4)
# en3.grid(column=1,row=4)
# window.geometry('350x350')

# window.mainloop()
# window = Tk()
# window.title("Welcome to my app")
# window.geometry('350x400')
# lbl = Label(window,text="Hello")
# lbl.grid(column=0,row=0)
# btn = Button(window,text="Click Moi")
# btn.grid(column=0,row=2)
# window.mainloop()

# window = Tk()
# window.title("This is my mini app!")
# window.geometry('360x400')
# lbl = Label(window,text="Hello")
# lbl.grid(column=0, row=0, padx=0, pady=0)

# def clicked():
#     lbl.configure(text="Button was clicked")
    
# btn = Button(window,text="Click Me", command=clicked)
# btn.grid(column=1,row=0)
# window.mainloop()


# window = Tk()
# window.title("Welcome to my mini app")

# window.geometry("350x400")

# lbl = Label(window,text="Hey there")
# lbl.grid(column=0, row = 0)

# box = Entry(window,width=10)
# box.grid(column=1,row=0)

# def clicked():
#     lbl.configure(text="Button was clicked")
    
# btn = Button(window,text="Click me", command=clicked)
# btn.grid(column=2,row=0)
# window.mainloop()

# window = Tk()

# window.title("This is my app!")
# window.geometry("350x400")

# combo = Combobox(window)
# combo["values"] = (1,2,3,4,5,"Text")
# combo.current(1)
# combo.grid(column=0,row=0)
# window.mainloop()

# window = Tk()
# window.title("This is my app")
# window.geometry("350x400")

# chk_state = BooleanVar()
# # chk_state.set(False)

# chk = Checkbutton(window,text="Choose", var=chk_state)
# chk.grid(column=0,row=0)
# window.mainloop()

# window = Tk()
# window.title("This is the app!")
# window.geometry("350x400")
# rad1 = Radiobutton(window,text="First",value=1)
# rad2 = Radiobutton(window,text="Second",value=2)
# rad3 = Radiobutton(window,text="Third",value=3)

# rad1.grid(column=0,row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=3,row=0)

# window.mainloop()

# window = tk.Tk()
# window.title("Welcome to my app!")
# window.geometry("350x400")
# selected = tk.IntVar()

# rad1 = ttk.Radiobutton(window,value=1,text="First",variable=selected)
# rad2 = ttk.Radiobutton(window,value=2,text="Second",variable=selected)
# rad3 = ttk.Radiobutton(window,value=3,text="Third",variable=selected)

# def clicked():
#     print(selected.get())
# btn = tk.Button(window,text="Click me", command=clicked)

# rad1.grid(column=0,row=0)
# rad2.grid(column=1,row=0)
# rad3.grid(column=2,row=0)
# btn.grid(column=1,row=1)
# window.mainloop()

# window = Tk()
# window.title("Message Box")
# window.geometry("350x400")
# def clicked():
#     messagebox.showinfo("Message title","You have a notification from message box please click okay :)")

# btn = Button(window,text="Click here", command=clicked)
# btn.grid(column=0,row=0)
# window.mainloop()

# window = Tk()
# window.title("Welcome to spinbox!")
# window.geometry("350x400")
# spin = Spinbox(window,from_=0,to=100,width=0)
# spin.grid(column=0,row=0)
# window.mainloop()

# answer = messagebox.askokcancel("Question","Do you want to open this file?")
# answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
# answer = messagebox.askyesno("Question","Do you like Python?")
# answer = messagebox.askyesnocancel("Question", "Continue playing?")

application_window = Tk()

answer = simpledialog.askstring("Input", "What is your first name?",parent=application_window)
messagebox.showinfo("Your first name is ", answer)
answer = simpledialog.askinteger("Input", "What is your age?",parent=application_window,minvalue=0, 
maxvalue=100)
messagebox.showinfo("Your age is ", answer)
answer = simpledialog.askfloat("Input", "What is your salary?",parent=application_window,minvalue=0.0, 
maxvalue=100000.0)
messagebox.showinfo("Your salary is ", answer)