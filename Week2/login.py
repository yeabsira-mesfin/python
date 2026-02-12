continue_function = 'y'
while continue_function == 'y':
    User_name = input("Please enter your name: ")
    Pswd = input("Please enter your password: ")
    if User_name == 'Bryan' and Pswd == 'Bruno':
        print(f"{User_name} welcome!")
    else:
        print("Incorrect user name or password.")
    continue_function = input("Do you wanna verify again? (y/n): ")