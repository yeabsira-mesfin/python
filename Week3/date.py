# import time
# import calendar
from datetime import *
# import datetime
# from time import *
# # localtime = time.localtime(time.time())
# # print(localtime)

# formatedtime = asctime(localtime(time()))
# print(formatedtime)
# formated_date =  datetime.datetime.now()
# print(f"""
#      The formatted date is {formated_date}
#      The year is  {datetime.date.today().strftime("%Y")}
#      The month is {datetime.date.today().strftime("%B")}
#      The week number of the year is {datetime.date.today().strftime("%W")}
#      The day of the year is {datetime.date.today().strftime("%w")}
#      The week is {datetime.date.today().strftime("%j")}
#      The day is {datetime.date.today().strftime("%d")}
#      The day is {datetime.date.today().strftime("%A")}""")

# """
# yy-mm-dd format
# """

# print(f"""
#       Current date and time: {datetime.datetime.now()}
#       yy-mm-dd fromat {datetime.date.today().strftime("%Y-%m-%d")}
#       dd-mm-yy fromat {datetime.date.today().strftime("%d-%m-%Y")}
#       """)
# t = time.localtime()  
# print (time.asctime(t))

# calendar.prcal(2026)

## monthly calendar
# monthc = calendar.month(2026,7)
# print(f""" This month calendar:: 
#       {monthc} """)

# y = int(input("Enter the year and will tell you if it's leap year or not: "))
# if calendar.isleap(y):
#     print(f"{y} is leap year")
# else:
#     print(f"{y} is not a leap year.")
# if (y %4 == 0 and y%100!=0) or y %400 == 0:
#     print(f"{y} is leap year")
# else:
#     print(f"{y} is not a leap year")

# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# print(calendar.month(yy,mm))

d0 = date(1999,7,6)
d1 = date(2026,1,30)

diff = d1-d0
diffy = d0.year - d1.year

print(diff)
print(f"""
      {diffy}
      """)