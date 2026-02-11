import shutil
import os
source = "D:\\Python\\MyOwnPractices\\python\\Week5\\original.txt"
with open(source, "w") as f:
    f.write("I wrote evertything here :/ ")
destination = "D:\\Python\\MyOwnPractices\\python\\Week5\\copy.txt"

shutil.copy(source,destination)
print(f"{os.path.basename(source)} is copied to {os.path.basename(destination)}")