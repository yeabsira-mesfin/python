from functools import reduce
list1 = [10, 2, 3] 
list2 = [3, 2, 4]

print(reduce((lambda x, y: x * y),list1))
print(reduce((lambda x, y: x+y), list2))