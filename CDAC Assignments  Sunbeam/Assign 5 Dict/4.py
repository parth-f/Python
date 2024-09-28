#  4) Write a program in Python to find out the frequency of each 
#     number in stored in a list using a python dictionary. 

# Example 
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4] 
# Output ={1: 1, 2: 3, 3: 1, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 1, 23: 1}

List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4] 

my_dict = {}
for v in set(List1) : my_dict[v]=0

for v in List1:
    if v in list(my_dict.keys()):
        my_dict[v] += 1

print(my_dict)