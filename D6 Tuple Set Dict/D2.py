# 2. Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# a. Find out how many students are in the list
# b. Change Lisa’s favourite colour
# c. Remove 'Jenny' and her favourite colour

l={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(l.keys())
x = list(l.keys())
print(len(x))
l['Lisa']='green'
print(l)
del l['Jenny']
print(l)
y="".join(l)

print(l)



