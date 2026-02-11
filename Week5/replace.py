def create_file(file_name):
    import os
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            for i in range(10):
                f.write(f"This is line {i+1}\n")

def replace_line(file_name, line_num, text):

    with open(file_name, 'r') as f:
        lines = f.readlines()
    
   
    # if 0 < line_num <= len(lines):
    lines[line_num - 3] = text + "\n"
    # else:
    #     print("Invalid line number")
    #     return


    with open(file_name, 'w') as f:
        f.writelines(lines)

   
    with open(file_name, 'r') as f:
        print(f.read())


if __name__=="__main__":
    file_path = "D:\\Python\\MyOwnPractices\\python\\Week5\\data4.txt"
    create_file(file_path)  

    lineno = int(input("Enter line number: "))
    text = input("Enter any string: ")
    replace_line(file_path, lineno, text)
