# 3) Write a Python program to count the elements in a 
# list until an element is a tuple. 
# Sample input : list = [10, 20, 30, (40,50), 60] 
# Sample output = 3

list1 = [10, 20, 30, (40,50), 60]
for i,v in enumerate(list1):
    if str(type(v)) == "<class 'tuple'>":
        print(f"Found tuple at {i} index")