# 3) Replace single element ‘b’ in given 
#    list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

l1 = ['a','b','c','d','e']

for i,v in enumerate(l1):
    if v == 'b':
        l1.remove('b') 
        l1.insert(i,[1,2,3])
        # l1.insert(i,2)
        # l1.insert(i,1)   
        break

print(l1)