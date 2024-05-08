# 2) Write a Python Program to find the repeated item of a 
#    tuple(Take a value from user which you want to find)

t1 = (1,42,'jg',890,"two",5,'jg')

s1 = list()

for i,n in enumerate(t1):
    for j,m in enumerate(t1):
        
        if i == j:
            continue
        if m == n:
            s1.append(n)

print(s1)
print(type(s1))