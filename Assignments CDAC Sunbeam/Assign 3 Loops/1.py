# 1) Using for loop, write and run a Python program to 
#    find factorial from 0 to 10

fact = 1

for n in range(10,0,-1):
    fact = fact * n

print("Factorial -",fact)