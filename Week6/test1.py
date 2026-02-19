import xlsxwriter,xlrd,os

wb = xlsxwriter.Workbook("D:\\Python\\MyOwnPractices\\python\\Week6\\ano.csv")
ws = wb.add_worksheet()

row = 1
column = 0
ws.write("A1","Emp Name")
ws.write("B1", "Emp No")
ws.write("C1", "Dept No")
ws.write("D1","Salary")
content = ["Viva", "Ronaldo", "Run", "Down", "The", "Wing", "Hear United","Sing"] 

print("csv file created")

wb.close()