import sys
# print(f"This is the name of the script: {sys.argv[0]}")
# print(f"Number of arguments: {len(sys.argv)}")
# print(f"The arguments are: {str(sys.argv)}")
# a = sys.argv[1]
# b = sys.argv[2]
# sum = int(a) + int(b)
# print(f"The sum is: {sum}")
sum = 0
print(f"This is the name of the script:", sys.argv[0])
print(f"The arguments are: {str(sys.argv)}")

print(f"Number of arguments: {len(sys.argv)-1}")
for i in range(1, len(sys.argv)):
    sum = sum+int(sys.argv[i])
    print(sys.argv[i])
print(f"The sum of the argments is {sum}")