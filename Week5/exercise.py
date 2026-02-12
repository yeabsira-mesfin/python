import sys
# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\student.txt","w") as f:

#     name = input("What is your name? ")

#     age = int(input("What is your age? "))

#     f.write(f"{name} \n")

#     f.write(str(age))

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\student.txt","r") as f:

#     print(f.read())

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\log.txt","a") as f:

#     message= input("Please enter your message: ")

#     f.write(message)
    

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\log.txt","r") as f:

#     print(len(f.readlines()))

# cf = "y"

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\marks.txt","w") as f:

#     f.write("Name   roll_num   marks \n")

#     while cf == "y":

#         name = input("What is your name? ")

#         roll_num = int(input("What is your roll number? "))

#         marks = int(input("What is your mark? "))
        

#         f.write(f"""{name}  {str(roll_num)}  {marks} \n""")

#         # f.write(f"{str(roll_num)} \n")

#         # f.write(f"{marks} \n \n")

#         cf = input("Do you wanna continue? (y/n)")

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\marks.txt","r") as f:

#     print(f.read())

# def update_line(filename,line_number,new_text):

#     f = open(filename,"w")
    
#     print()

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\marks.txt","r") as f:

#     lines = f.readlines()

#     print(lines[2])
def update_line(file_name, line_num, text):
    new_num = line_num - 1
    with open(file_name,"w+") as f:
        for i in range(10):
            f.write(f"This is line {i} \n")
    
        f.seek(0) 
        
        lines = f.readlines()
        # print(len(lines))
        f.seek(0)
        if line_num < len(f.readlines()):
            replaced = lines[new_num] = f"{text} \n"
        else:
            print("The number is out of index")
            sys.exit(0)
        f.seek(0)
        f.writelines(lines)
        f.seek(0)
        print(f.read())
    return

replaced = int(input("Please enter the line you would like to replace: "))
update_line("D:\\Python\\MyOwnPractices\\python\\Week5\\replace.txt",replaced,"This is the new replacment")
    
        

# with open("D:\\Python\\MyOwnPractices\\python\\Week5\\replace.txt","r") as f:

#      print(f.read())