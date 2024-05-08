# 10. Write a Python program to check whether an 
# element exists within a tuple.

t11 = (77,88,57,67,33,84,24,52,51,69,20,55,25)

find = int(input("Search for element - "))
found = False

for idx in t11:
    if idx == find:
        found = True
        break

if found == True:
    print(f"{find} exists in the list")
else:
    print(f"{find} does not exists in the list")

# Search for element - 55
# 55 exists in the list