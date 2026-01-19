continue_function = 'y'
while continue_function.lower() == 'y':
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    max = num1 if num1 > num2 else num2
    min = num1 if num1 < num2 else num2
    print(f"The maximum number between {num1} and {num2} is: {max}")
    print(f"The minimum number between {num1} and {num2} is: {min}")
    continue_function = input("Do you want to check another pair of numbers? (y/n):")

"""
This is multiline comment 


so easy right?

Just ignore meeh

"""