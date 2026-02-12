
def string_function():
    continue_function = input("Please enter y if you wanna see the functions: ")
    while continue_function == 'y':
       
        name = input("Please enter your name and let me put it in different cases: ")
        charr = name[1]
        print(f"The length: {len(name)}")
        print(f"To upper: {name.upper()}")
        print(f"To lower: {name.lower()}")
        print(f"Is upper function: {name.isupper()}")
        print(f"Is lower function: {name.islower()}")
        print(f"Count function: {name.count(name)}")
        print(f"Find function: {name.find('e')}")
        print(f"Title function: {name.title()}")
        print(f"Right justified: {name.rjust(20,'*')}")
        print(f"Left justified: {name.ljust(20,'*')}")
        print(f"Center function: {name.center(30,'*')}")
        
        print(f"Remove empty spaces: {name.strip()}")
        continue_function = input("Do you wanna do this again? (y/n)")

string_function()