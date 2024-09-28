# Operator Overloading make a Point Class

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"{self.x}.{self.y}"
    
    def __add__(self, v):
        above_point = self.x + v.x
        below_point = float(f"0.{self.y}") + float(f"0.{v.y}")
        return above_point + below_point
    
p1 = Point(0,52)
p2 = Point(4,49)

print(p1 + p2)