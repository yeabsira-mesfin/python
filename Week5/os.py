import os
import shutil
# drt = "D:\\Python\\MyOwnPractices\\python\\Week5\\TestOne"

# os.mkdir(drt)
# print(f"{os.path.basename(drt)} is created")

# newdrti = input("Please enter the directory name you want: ")
# newdrt = f"D:\\Python\\MyOwnPractices\\python\\Week5\\{newdrti}"
# os.rename(drt,newdrt)
# print(f"{os.path.basename(newdrt)} is created: ")
# print(os.getcwd())
# drt = "D:\\Python\\MyOwnPractices\\python\\Week5\\TestOne"
# os.rmdir(drt)
# print(f"{os.path.basename(drt)} is removed")
# t = open("D:\\Python\\MyOwnPractices\\python\\Week5\\TestOne\\test1.txt","w")
# t2 = "D:\\Python\\MyOwnPractices\\python\\Week5\\TestOne\\test1.txt"
# print(f"{os.path.basename(t2)} is created")
removed = "D:\\Python\\MyOwnPractices\\python\\Week5\\TestOne"
shutil.rmtree(removed)
print(f"{os.path.basename(removed)} is removed")
