continue_function = 'y'
while continue_function == 'y':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    # max_num = num1 if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 else num2 if num2 > num3 and num2 > num4 and num2 > num5 else num3 if num3 > num4 and num3 > num5 else num4 if num4 > num5 else num5
    entered_numbers = [num1,num2,num3,num4,num5]
    print(f"The maximum value is {max(entered_numbers)}")
    print(f"The minimum value is {min(entered_numbers)}")
    continue_function = input("Do you want to check another numbers? (y/n)")



