# continue_function = 'y'
# while continue_function:
#     name = input('Please enter your name so that I can reverse it: ')
#     print(name[::-1])
#     continue_function = input('Do you wanna do it again? (y/n)')
s=input("Enter any string")
l=s.split(" ") # string into list
l.reverse()
l.sort()
s1=" ".join(l) # list into string
print(s1)

