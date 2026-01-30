# try:
#     num1 = int(input("Enter your fist number: "))
#     num2 = int(input("Enter your second number:"))
#     divison = num1/num2
#     print(f"The quotioent value is {divison}")
# except ZeroDivisionError:
#     print("Divide by zero Error occurs")
# finally:
#     print("Thank you!")
    
try:
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    division = num1/num2
    print(f"The quotient is {division}")
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)
finally:
    print("Thank you!")