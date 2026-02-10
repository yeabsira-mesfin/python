f=open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "w")
sname = input("Please enter your name: ")
sno = int(input("Please enter your sno: "))
mark = input("Please enter your mark: ")
s = sname +"\n"+ str(sno) + "\n" + mark
f.write(s)
print("File created :)")
f.close()
f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data.txt", "r")
print(f"""The contents of the file:
      
      {f.read()}
      
      """)
f.close()