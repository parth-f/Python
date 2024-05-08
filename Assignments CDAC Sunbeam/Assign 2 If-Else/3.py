# 3) Write a Python function to calculate the factorial of a number (a nonnegative integer). 
#    The function accepts the number as an argument

def factorial_u(num :int):
    if num == 0:
        return 1
    return num*(factorial_u(num-1))

u_in = int(input("Enter a num to get its factorial - "))
print( factorial_u(u_in) )