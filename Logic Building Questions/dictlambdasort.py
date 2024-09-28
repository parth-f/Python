d1 = {"hello":4,"world":3,"how":2,"are":1,"you":0}
print(d1)

print("")

d2 = dict(sorted(d1.items(),key=lambda x:x[0])) # key
print(d2)
d2 = dict(sorted(d1.items(),key=lambda x:x[0],reverse=True)) # key reversed 
print(d2)

print("")

d2 = dict(sorted(d1.items(),key=lambda x:x[1])) # values
print(d2)
d2 = dict(sorted(d1.items(),key=lambda x:x[1],reverse=True)) # values reveresed
print(d2)