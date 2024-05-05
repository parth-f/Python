# 1. Add a list of elements to a given set
# Given:
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red","Yellow","orange"]

list1 = list()
set1 = set()

for m in ["Yellow","Orange","Black"]:
    set1.add(m)

print(set1,type(set1))

for n in ["Blue","Green","Red","Yellow","orange"]:
    list1.append(n)

print(list1,type(list1))