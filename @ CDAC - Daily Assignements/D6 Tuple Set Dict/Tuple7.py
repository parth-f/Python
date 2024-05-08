# 7. Take two integer values in a & b. Swap their values using tuple, 
# using temparary variable and without tuple and without temparary variable.
# Ex. a=10 b=23
# After swapping a=23 b=10


a = 10
b = 23

print("a =",a,"b =",b)

new = a,b    # packing in tuple
b,a = new    # unpacking of tuple

print("a =",a,"b =",b)

# a = 10 b = 23
# a = 23 b = 10

# print(type(new))   # tuple