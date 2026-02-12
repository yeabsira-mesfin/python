listm= [3,3,4,8, 9, 9, 92]
mult_items = 1
for i in range(len(listm)):
    mult_items *= listm[i]
print(f"The multiplication of all the elements of {listm} is {mult_items}")