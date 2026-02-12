import re
# print(re.search("cat", "the cat is here with me.")) this one searches all
# print(re.findall("[abc]", "apple")) # this one searches of any match from the bracket.
# print(re.findall("[abc]", "cab")) 
# print(re.findall("[^abc]", "cab wont be here")) # this one matches every word except cab

# print(re.findall("[a-z]", "THERE IS A sMALL LETTER HeRe."))

# print(re.findall("[A-Z]", "there is a BIG LETTER hErE."))

print(re.findall("[a-zA-Z0-9]", "this WILL _ print everything."))

# print(re.findall("[0-9]", "Room 29 is open."))

# print(re.findall("[a-zA-Z0-9]", "This finDS 12"))

# print(re.findall("[^a-z0-9]", "This wont show the number5 and SMall @ letter."))

# print(re.findall("[\s]", "This wont show the space 1"))
# print(re.findall("[\S]", "This wont show the space 1"))
# print(re.findall("[\D]", "Digi8"))
continue_function = 'y'
while continue_function == 'y':
    email = input("Please enter your email and will tell you if it's valid or not: ")

    if re.fullmatch('[a-zA-Z0-9._]+@[a-zA-Z]+\\.[a-zA-Z]+',email):  
        print(f"Your email {email} is valid.")
    else:
        print(f"Your email {email} is invalid.")
    continue_function = input("Do you wanna continue checking? (y/n)")