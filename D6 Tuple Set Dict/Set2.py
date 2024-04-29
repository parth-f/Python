# 2. display common elements from the given set
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# 1st solution ----------------

# for n in set1:
#     for m in set2:
#         if n == m:
#             print(n)

# 2nd Solution -----------------

# common_elements = set1.intersection(set2)
# print("Common elements:", common_elements)

# 3rd Solutino -----------------

common_elements = set1 & set2
print(common_elements)