# Q1. Write a Python program to create a Vehicle class with max_speed and 
#     mileage instance attributes. Write a python program to Create a child 
#     class Bus that will inherit all of the variables and methods of the 
#     Vehicle class

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
class Bus(Vehicle):
    
    