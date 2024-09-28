# 9. Write a Python program to find repeated items in a tuple.

t9 = (4,2,1,5,3,2,4)

set_t9 = set(t9)
print(t9)

for n in set_t9:
    c = t9.count(n)
    if c > 1:
        print(n ,"repeated x",c,"times")

# (4, 2, 1, 5, 3, 2, 4)
# 2 repeated x 2 times
# 4 repeated x 2 times