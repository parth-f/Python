# 3. Generate a new set with all items from both sets by removing 
# numbers which are in both sets.
# set1 = {10, 20, 30, 40, 50,25}
# set2 = {30, 40, 50, 60, 70,100}
# o/p : order is not important
# {70, 10, 20, 60,25,100}

set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}

new_set = (set1 | set2) - (set1 & set2)
print(new_set)

# {100, 70, 10, 20, 25, 60}