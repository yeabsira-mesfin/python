from pprint import pprint
def sum(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y != 0:
        return x/y
    else:
        return print("Denomenator can't be 0")
def exp(x,y):
    return x**y
cf = 'y'
while cf == 'y':
    print(f""" Select the operation you want.
           1. Add.
           2. Subtract.
           3, Multiply.
           4. Division.
           5. Exponent""")
    
    operation = int(input("Enter the operation you want: "))
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    if operation == 1:
        print(f"""The addition of {num1} and {num2} is:""", sum(num1,num2))
    elif operation == 2:
        print(f"""The subtraction of {num1} and {num2} is:""", sub(num1,num2))
    elif operation == 3:
        print(f"""The multiplication of {num1} and {num2} is:""", mul(num1,num2))
    elif operation == 4:
        print(f"""The division of {num1} and {num2} is:""", div(num1,num2))
    elif operation == 5:
        print(f"""The exponent of {num1} to {num2} is:""", exp(num1,num2))
    else:
        print("You didn't enter the right choice.")
    cf = input("Do you wanna try again? (y/n): ")
    

