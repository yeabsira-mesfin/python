numbers = [1,2,3,4,5]

my_iterator = iter(numbers)
try:
    print(f"{next(my_iterator)}")
    print(f"{next(my_iterator)}")
    print(f"{next(my_iterator)}")
    print(f"{next(my_iterator)}")
    print(f"{next(my_iterator)}")
    print(f"{next(my_iterator)}")
except StopIteration:
    print(f"{StopIteration} has happend.")
# print(f"{next(my_iterator)}")
# print(f"{next(my_iterator)}")
# print(f"{next(my_iterator)}")
# print(f"{next(my_iterator)}")
# print(f"{next(my_iterator)}")
# print(f"{next(my_iterator)}")

for i in numbers:
    print(numbers[i-1])

print("TEST")
    
