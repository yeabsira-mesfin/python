import os
drt = "D:\\Python\\MyOwnPractices\\python\\Week5\\test"

# os.mkdir(drt)
# print(f"{os.path.basename(drt)} is created")

newdrti = input("Please enter the directory name you want: ")
newdrt = f"D:\\Python\\MyOwnPractices\\python\\Week5\\{newdrti}"
os.rename(drt,newdrt)
print(f"{os.path.basename(newdrt)} is created: ")