# 1) Concatenate two lists in the following order by using list comprehension 
# Input:- 
# list1 = ["Hello ", "take "] 
# list2 = ["Dear", "Sir"] 
# Output:- 
# [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1 = ["Hello ", "take "] 
list2 = ["Dear", "Sir"] 

com_list = list()

for n in list1:
    for m in list2:
        com_list.append(str(n+m))

print(com_list)

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']