list1 = ['Math', 1, 2, 5, 1999, 'Biology']
list2 = ['pyhics ','is', 'my','favourite']
list3 = ['a','n',' ','favourite']

print(f"List1[0]: {list1[0]}")
print(f"List2[1]: {list2[1]}")
print(f"List2[2]: {list2[2]}")
print(f"List3[3]: {list3[3]}")

# upating lists

list1[0] = 'Programming'
print(f"List1[0]: {list1[0]}")
print(f"List2[1]: {list2[1]}")
print(f"List2[2]: {list2[2]}")
print(f"List3[3]: {list3[3]}")

# deleting lists

del list1[0]
print(f"List1[0]: {list1[0]}")
print(f"List2[1]: {list2[1]}")
print(f"List2[2]: {list2[2]}")
print(f"List3[3]: {list3[3]}")

# Basic descriptions

list4=list1 + list2
print(list4)
print(len(list4))

list5 = ['Holla'] * 4
print(list5)

print('Holla' in list5)


# list operations

list6 = ['Ethiopia', 'Viva Ronaldo', 'Neymar']
list7 = [4,56,3234,322,76,44444]

print(max(list7))
print(min(list7))
print(sorted(list6))
list7.append(2009)
print("Updated list", list7)
list6.insert(0,'Dorgu')
print(list6)
list6.reverse()
print(list6)
list7.remove(3234)
print(list7)
list7.pop(3)
print(list7)