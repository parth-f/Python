# Create a pascal triangle

old = [1,1]
new = list()

stop = 3

for s in range(0,stop):
    l = list()
    new = old
    for i in range(0,len(old)):
        new.insert(len(old)//2, old[i] + old[i+1])

print(new)