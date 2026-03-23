
def operation():
    cf = "yes"
    while cf == "yes":
        result = 0
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        operand = int(input(f"""
                Please select the operan you would like to select from the below:
                1: Sum
                2: Difference
                3: Product
                4: Qutotient
                5: Power
                """))
        if operand == 1:
            result = num1 + num2
        elif operand == 2:
            result = num1 - num2
        elif operand == 3:
            result = num1*num2
        elif operand == 4:
         try:
                result = num1/num2
         except ZeroDivisionError:
                result = ZeroDivisionError
        elif operand == 5:
            result = num1**num2
        else:
          print("Please enter two numbers!")
        if result == ZeroDivisionError:
            print("You can't divide a number by zero")
        else:
            print(f"The result is {result}")
        cf = input("Do you wanna continue? (yes/no)")
    return 
        
operation()

