a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))

print("Sum is:", a + b)
print("Difference is:", a - b)
print("Product is:", a * b)

if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("They are equal")