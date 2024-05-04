# Q WA function to take a number as parameter and  print True if 
#   given number is even else print False

def check_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False

num = int(input("Enter a num - "))
print( check_even(num) )
