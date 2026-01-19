
continue_calculation = 'yes'

while continue_calculation.lower().strip() == 'yes':
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
    reminder = num1 % num2 if num2 != 0 else "undefined (cannot divide by zero)"
    exponent = num1 ** num2 
    print(f"The sum of {num1} and {num2} is: {sum}")
    print(f"The difference when {num2} is subtracted from {num1} is: {difference}")
    print(f"The product of {num1} and {num2} is: {product}")
    print(f"The quotient when {num1} is divided by {num2} is: {quotient}")
    print(f"The remainder when {num1} is divided by {num2} is: {reminder}")
    print(f"{num1} raised to the power of {num2} is: {exponent}")
    continue_calculation = input("Do you want to perform another calculation? (yes/no): ")