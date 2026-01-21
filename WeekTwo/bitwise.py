
continue_checking = 'y'

while continue_checking == 'y':
    num = int(input("Please enter an integer: and will check if its even or odd using bitwise operation: "))
    if num & 1 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    print("===============================")
    continue_checking = input("Please enter y if you want to check another number: ")