# try:
#     num1 = int(input("Enter your fist number: "))
#     num2 = int(input("Enter your second number:"))
#     divison = num1/num2
#     print(f"The quotioent value is {divison}")
# except ZeroDivisionError:
#     print("Divide by zero Error occurs")
# finally:
#     print("Thank you!")
    
# try:
#     num1 = int(input("Please enter your first number: "))
#     num2 = int(input("Please enter your second number: "))
#     division = num1/num2
#     print(f"The quotient is {division}")
# except ZeroDivisionError as msg:
#     print(msg)
# except ValueError as msg:
#     print(msg)
# finally:
#     print("Thank you!")

# try:
#     fh = open("d:\\Python\MyOwnPractices\\python\\WeekThree\\exceptionhandling.py")
#     fh.write("This is my test file for exeption handling")
# except Exception as msg:
#     print(msg)

# try:
#     fh = open("d:\\Python\MyOwnPractices\\python\\WeekThree\\exceptionhandling.py", "r")
#     fh.write("This is my test file for exception handling!!")
# except IOError:
#     print("Error: can't find file or read data")
# else:
#     print("Written content in the fil successfully")

# def test(i):
#     list1 = [1,2,3,4,5]
#     try:
#         if list1 >= 1:
#             return list1[i]
#     except TypeError:
#         print("Dealing with TypeError")
#     except IndexError:
#         print("Dealing with IndexError")
#     except:
#         print("I don't know")
#     finally:
#         print("This is the end!")
# if __name__ == "__main__":
#     print(test(5))

def test(i):
    list1 = [1,2,3,4,5]
    try:
        if i >=1:
            return list1[i]
    except Exception as msg:
        print(msg)
        
print(test(5))