f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "a")
s1 = (input("Please enter anyk string: "))
# binary_text = s1.encode("utf-8")
f.write(s1)
f.close()


f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "rb")
print(f.read())
f.close()