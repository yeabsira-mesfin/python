def calc():
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
    
    continue_function = 'y'
    while continue_function == 'y':
        print(f"The sum of {num1} and {num2} is {num1+num2}")
        print(f"The difference of {num1} and {num2} is {num1-num2}")
        print(f"The multiplication of {num1} and {num2} is {num1*num2}")
        if num2 != 0:
            print(f"The division of {num1} and {num2} is {num1/num2}")
        else: 
            print("You can't divide a number by 0")
        continue_function = input("Do you wanna do another calculation?(y/n)")

calc()