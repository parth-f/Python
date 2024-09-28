# 7) Write a NumPy program to create an array with the 
# values 1, 7, 13, 105 determine the size of the memory 
# occupied by the array.


import sys
import numpy as np

arr = np.array([1,7,13,105])

print(sys.getsizeof(arr))
