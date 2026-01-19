continue_calculation = 'y'
while continue_calculation.lower() == 'y':
    number = int(input("Enter a number to check if it's odd or even:"))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    continue_calculation = input("Do you want to check another number? (y/n): ")