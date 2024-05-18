x = 8
y = 0

# print(x / y)  

try:
    print(x / y)
except ZeroDivisionError:
    print(f"The Y is 0 and {x} can't be divided by it because maths")