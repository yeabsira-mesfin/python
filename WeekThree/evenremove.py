list1 = [2, 5, 6, 7, 8, 9, 10]
list2 = []

for i in range(len(list1)):
    if list1[i] % 2 != 0:
        list2.append(list1[i])

print(list2)
