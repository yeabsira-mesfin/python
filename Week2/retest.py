import re
continue_function = 'y'
 
# while continue_function == 'y':
#     password = input("Enter your password and I will tell you if it's valid or invalid: ")
#     if re.fullmatch('[a-z0-9A-Z._]+@[a-zA-z]+\\.[a-z]+', password) != None:
#         print(f"Your password{password} is valid")
#     else:
#         print(f"Your password{password} is invalid")
#     continue_function = input("Do you wanna try again (y/n): ")
# print(re.findall('colou?r', "color colour colouur"))
# print(re.findall('colou*r', 'color, colour, colouur colouuur'))
# print(re.findall(r"hello?", "helloo, hello , siuu"))

while continue_function == 'y':
    phonenum = input("Please enter your phone number and will let you know if it\\'s valid or not:")
    # phone_valid = re.fullmatch(r"\d{3}-?\d{3}-?\d{4}", phonenum)
    phone_valid1 = re.fullmatch(r"\d{10}|\d{3}\s*\d{3}\s*\d{4}|\d{3}\-\d{3}\-\d{4}|\(\d{3}\)\d{3}-\d{4}",phonenum)
    

    if phone_valid1 != None:
        print("Your phone number is valid")
    else:
        print("Your phone number is not valid")
    continue_function = input("Do you wanna try another number? (y/n)")
                                               