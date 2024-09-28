# 4. Write a Python program that prompts the user to input two numbers and 
#    raises a TypeError exception if the inputs are not numerical.

try:
    a = input("Enter value of a - ")
    b = input("Enter value of b - ")
    a / b
except TypeError:
    print(f"'a' = {a} which has type and 'b' = {b} which has type ")
