# 5) Define a function overlapping() that takes two lists and returns 
#    True if they have at least one member in common, False otherwise.

def overlappiing(list1 :list, list2 :list):
    
    for n in list1:
        for m in list2:
            if n == m:
                return True
                break
    return False
    
l1 = [22,7]
l2 = [5,8]

print( overlappiing(l1, l2) )