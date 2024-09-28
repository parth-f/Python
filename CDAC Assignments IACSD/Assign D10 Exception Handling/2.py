# 2. Write a Python program that prompts the user to input an 
#    integer and raises a ValueError exception if the input is 
#    not a valid integer.

try :
    u_in = int(input("Enter a num - "))
except ValueError:
    print("Entered input is not a number, please try again ")
else:
    print(u_in,"a good number")
finally:
    print("done")