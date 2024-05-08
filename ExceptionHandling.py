# 1. Write a Python program to handle a ZeroDivisionError 
#    exception when dividing a number by zero.

in1 = int(input("Enter value of x - "))

class WrongOperator(Exception):
    "Raised when the Operator input is Provided Wrong by the User"
    pass
try:
    opp = input("Enter opperations - (+) (-) (*) (/) - ")
    if opp != "+" and opp != "-" and opp != "*" and opp != "/":
        raise WrongOperator
except WrongOperator:
    print("The Operator is Wrong please Try again")
    

in2 = int(input("Enter value of y - "))

def addd(x,y):
    return x + y 

def subb(x,y):
    return x - y 

def multt(x,y):
    return x * y

def divv(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return f"The Y is 0 and {x} can't be divided by it because maths"

match(opp):
    case "+":
        print(addd(in1,in2))
    case "-":
        print(subb(in1,in2))
    case "*":
        print(multt(in1,in2))
    case "/":
        print(divv(in1,in2))