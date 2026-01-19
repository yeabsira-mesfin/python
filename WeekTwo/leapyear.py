continue_calculation = 'y'
while continue_calculation.lower() == 'y':
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year%100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    continue_calculation = input("Do you want to check another year? (y/n): ")
