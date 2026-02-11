import os

old_path = "D:\\Python\\MyOwnPractices\\python\\Week5\\yeab.txt"
file_name = input("Please put your desired file name")
new_path = f"D:\\Python\\MyOwnPractices\\python\\Week5\\{file_name}.txt"

os.rename(old_path, new_path)

print(f"Renamed {os.path.basename(old_path)} → {os.path.basename(new_path)}")
