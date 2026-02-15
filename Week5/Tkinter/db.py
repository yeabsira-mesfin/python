from tkinter import *
import pyodbc
import pandas.io.sql as psql

root = Tk()
root.title("Dept List")
root.geometry("300x300")

label1 =Label(root, text ="Deptno")
label1.grid(row =1, column =0)

num1_txtbx =Entry(root)
num1_txtbx.grid(row =1, column =1)

label2 =Label(root, text ="Dname")
label2.grid(row =2, column =0)

num2_txtbx =Entry(root)
num2_txtbx.grid(row =2, column =1)

label3 =Label(root, text ="Loc")
label3.grid(row =3, column =0)

num3_txtbx =Entry(root)
num3_txtbx.grid(row =3, column =1)

def result():
    cxn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',server = 'YEABSIRA',database='python',Trusted_Connection='yes')
    cursor = cxn.cursor()
    m1=int(num1_txtbx.get())
    m2=num2_txtbx.get()
    m3=num3_txtbx.get()
    print (f"insert into dept(deptno,dname,loc) values({str(m1)} {m2} {m3}")
    cursor.execute("insert into dept(deptno,dname,loc) values("+str(m1)+','+"'"+m2+"'"+','+"'"+m3+"'"+")")
    cursor.commit()
    print ('1 row inserted')
    cxn.close()

def delete_dept():
    cxn = pyodbc.connect(
        driver='{ODBC Driver 17 for SQL Server}',
        server='YEABSIRA',
        database='python',
        Trusted_Connection='yes'
    )
    cursor = cxn.cursor()

    deptno = int(num1_txtbx.get())

    cursor.execute("DELETE FROM dept WHERE deptno = ?", (deptno,))
    cxn.commit()

    print(cursor.rowcount, "row(s) deleted")
    cxn.close()


calculate_button =Button(root, text="Insert", command= result)
calculate_button.grid(row =4, column =0,columnspan=2)

delete_button = Button(root, text="Delete")
delete_button.grid(row=4, column=2)



root.mainloop()