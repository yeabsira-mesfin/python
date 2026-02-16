import xlsxwriter,xlrd,os

# wb = xlsxwriter.Workbook("D:\\Python\\MyOwnPractices\\python\\Week5\\XML\\test.xls")
# ws = wb.add_worksheet()
# ws.write("A1","Emp Name")
# ws.write("B1","Emp No")
# ws.write("C1","Dept No")
# ws.write("D1","Salary")

# print("Excel file created")
# wb.close()

# wb = xlsxwriter.Workbook("D:\\Python\\MyOwnPractices\\python\\Week5\\XML\\TestCSV.csv")
# ws = wb.add_worksheet()

# ws.write("A1","Emp Name")
# ws.write("B1", "Emp No")
# ws.write("C1","Dept No")
# ws.write("D1","Salary")

# print("CSV file created")
# wb.close()

# wb = xlsxwriter.Workbook("D:\\Python\\MyOwnPractices\\python\\Week5\\XML\\ano.xlsx")
# ws = wb.add_worksheet()

# row = 1
# column = 0
# ws.write("A1","Emp Name")
# ws.write("B1", "Emp No")
# ws.write("C1", "Dept No")
# ws.write("D1","Salary")
# content = ["Viva", "Ronaldo", "Run", "Down", "The", "Wing", "Hear United","Sing"]  

# for i in content:
#     ws.write(row,column,i)
#     row +=1
    
# wb.close()

# wb = xlsxwriter.Workbook("D:\\Python\\MyOwnPractices\\python\\Week5\\XML\\score.xlsx")
# ws = wb.add_worksheet()

# ws.write("A1","Emp Name")
# ws.write("B1", "Emp No")
# ws.write("C1", "Dept No")
# ws.write("D1","Salary")

# scores = ( 
#     ['Ronaldo', 1000], 
#     ['Messi',   100], 
#     ['Neymar',  300], 
#     ['Mbappe',    50], 
# ) 
# row = 1
# column = 0

# for name, score in (scores):
#     ws.write(row,column,name)
#     ws.write(row,column+1,score)
#     row +=1
    
# wb.close()

loc = ("D:\\Python\\MyOwnPractices\\python\\Week5\\XML\\score.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0,0)

for i in range(0,sheet.nrows):
    print(sheet.cell_value(i,0))
