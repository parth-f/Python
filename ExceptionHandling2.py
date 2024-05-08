# 2. Write a Python program that prompts the user to input an integer and 
#    raises a ValueError exception if the input is not a valid integer

try :
    val = int(input("Enter a num - "))
except ValueError:
    print("\nEnter a Numbers not a Character")