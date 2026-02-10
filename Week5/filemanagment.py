# f=open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "w")
# sname = input("Please enter your name: ")
# sno = int(input("Please enter your sno: "))
# mark = input("Please enter your mark: ")
# s = sname +"\n"+ str(sno) + "\n" + mark
# f.write(s)
# print("File created :)")
# f.close()
# f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "r")
# print(f"""The contents of the file:
      
#       {f.read()}
      
#       """)
# f.close()

f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "w")
f.write("sname sno mark \n")
choice = "y"
while(choice=="y"):
    sname = input("Please enter your name: ")
    sno = int(input("Please enter your sno: "))
    mark = input("Please enter your mark: ")
    s = sname + " "+str(sno) + " "+ mark + "\n"
    f.write(s)
    choice = input("Do you want to continue? (y/n): ")

print("File created :)")
f.close()
f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "r")
# print(f"""
#       The contents of the file:
     
#       {f.read()}
#       """)

print("The files create are: ")
print(f.read())
f.close()
