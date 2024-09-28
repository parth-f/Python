# 1) Write a menu Driven Program To Calculate the Parameter and 
# Area of different Shapes(Circle,Square,Rectangle) using 
# functions

def circle(cal):
    radius = int(input("Enter the radius : "))
    if cal == 1: # parameter 
        return 2*(22/7)*radius
    else: # area
        return (22/7)*pow(radius,2)

def sqr(cal):
    side = int(input("Enter len of sides : "))
    if cal == 1: # paramter
        return 4*side
    else:
        return pow(side,2)

def rectangle(cal):
    height = int(input("Enter the height : "))
    width = int(input("Enter the width : "))

    if cal == 1: # parameter
        return 2*height + 2*width 
    else : # area
        return height*width
    
def cal_some():
    shape = int(input("""Shapes
    1. Circle 
    2. Sqaure 
    3. Rectangle \n"""\
    "Select the shape : "))
    print("-----------")

    area_or_parameter = int(input("""Calculate
    1. Parameter
    2. Area \n"""\
    "Select calculation : "))
    print("-----------")

    if area_or_parameter in [1,2]:
        if shape == 1:
            out = circle(area_or_parameter);
        elif shape == 2:
            out = sqr(area_or_parameter)
        elif shape== 3:
            out = rectangle(area_or_parameter)
        else : 
            print("wrong input try again")
    else : 
        print("Wrong input try again ")

    print("-----------")
    print("Value "+str(out))
