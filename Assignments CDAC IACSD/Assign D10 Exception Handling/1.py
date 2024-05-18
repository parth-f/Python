x = int(input("Enter x - "))
y = int(input("Enter y - "))

try :
    print( x / y )
except ZeroDivisionError:
    print(f"x = {x} and y = {y} . but we can't divide any number by zero Cause Maths")



