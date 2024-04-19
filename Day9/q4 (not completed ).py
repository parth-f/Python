# Q Given list of employees. This list may contain repetitions. 
# Find all unique employee names and print them as per order of 
# second character in that name. Use lambda function and normal function both.

emp = ["rahul","sammer","chetan","rahul","tina","sammer"]

def unique_sort(l :list):
    s = set(l)
    print(s,type(s))
    l = list(s)
    print(l,type(l))
    print(sorted(l, key=(lambda x: x[-2])))
    return l
    
# unique_sort(emp)

print(sorted(emp, key=(lambda s : s)))
l2 = unique_sort(emp)
print(sorted(l2, key=(lambda s : s)))

