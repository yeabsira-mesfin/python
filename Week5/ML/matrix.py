import numpy as np
from functools import reduce

# x = np.arange(2,11).reshape(3,3)
# y = x.transpose()
# print(x)
# print(y)
# z = np.arange(45, 60)  # [45, 46, 47]
# print(reduce(lambda x, y: x * y, z))

# x = np.zeros(20)
# print(x)
# print("Update sixth value 11")
# x[6] = 11
# print(x)

# x = np.arange(12,38)
# print("Original array: ")
# print(x)
# print("Reverse array: ")
# x = x[::-1]
# print(x)

# x = [10,20,30]
# print("Original array: ")
# print(x)
# x = np.append(x,[[40,50,60],[70,80,90]])
# print("After append values to the end of the array: ")
# print(x)

# x = np.array([10,10,20,20,30,30,40,50,50,40,7,12,21,29])
# print(f"""
#       Original array 
#       {x}
#       """)
# x = np.unique(x)
# print(f"""
#       Unique elements
#       {x}
#       """)
# x = np.array([[1, 1], [2, 3]])
# print(x)
# print(np.unique(x))
# x = [1,2,3,4,5]
# y = [4,5,6,7,8,9]

# print(f"""
#       The original arrays 
#       {x}
#       {y}
      
#       Unique values in x but not in y
#       {np.setdiff1d(x,y)}
      
#       Unique values in y not in x 
#       {np.setdiff1d(y,x)}
      
#       """)

# x = np.arange(2,14)
# print(f"Original array: {x}")

# y = np.arange(2,14).reshape(3,4)

# print(f"""
# 3 columns and 4 rows
# {y}
#       """)

# z = np.arange(2,14).reshape(4,3)

# print(f"""
# 4 columns and 3 rows
# {z}

#       """)
# a = np.arange(8).reshape(2,2,2)

# print(f"""
# 3D Array
# {a}

#       """)

# y = np.arange(8)
# print(f"""
# Original vector
# {y}      
# """)
# print(f"""
# Array without the first and last element
# {y[1:-1]}
# """)

a = np.array([100,200,1,2,4,5,6,6,7,7,500])
per = np.percentile(a,100)
print(per)