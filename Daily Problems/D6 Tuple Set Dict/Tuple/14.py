# 14. Write a Python program to find the 
#     index of an item in a tuple.

t14 = ("India","is","my","country","and","all","indians","are","my","brother","and","sisters")

i=0
for value in t14:
    if( value == "indians"):
        print(f"index {i} has a value of {value}, hence found")
    i+=1

# index 6 has a value of indians, hence found