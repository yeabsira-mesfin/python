with open("D:\\Python\\MyOwnPractices\\python\\Week5\\data6", "w") as f:
    f.write("Today feels great! \n")
    f.write("Today feels really great! \n")
    f.write("Today feels really really great! \n")
    print(f"Inside with statment is file closed? {f.closed}")
print(f"How about outside with statment is file closed? {f.closed}")
    