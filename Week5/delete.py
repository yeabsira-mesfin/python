import os
pathn = "D:\\Python\\MyOwnPractices\\python\\Week5\\delete.txt"
os.remove(pathn)
print(f"{os.path.basename(pathn)} is deleted")