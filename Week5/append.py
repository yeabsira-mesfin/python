# f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "a")
# s1 = (input("Please enter anyk string: "))
# # binary_text = s1.encode("utf-8")
# f.write(s1)
# f.close()


# f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "rb")
# print(f.read())
# f.close()
def main():
    f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "w+")
    for i in range(10):
        f.write(f"This is line {i} \n")
    f.seek(0)
    # f = open("D:\\Python\\MyOwnPractices\\python\\Week5\\data3.txt", "r")
    contents = f.read()
    print(contents)
    f.close()

    
if __name__ == "__main__":
    main()