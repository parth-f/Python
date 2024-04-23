# 2. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

## a. Find out how many students are in the list
print("Num of students =", len( list(people.keys()) ) )

# output > Num of students = 4

## b. Change Lisa’s favourite colour
people['Lisa']='Green'
print("Lisa fav Color is",people['Lisa'])

# output > Lisa fav Color is Green

## c. Remove 'Jenny' and her favourite colour
del people['Jenny']
print(people)

# output > {'Arham': 'Blue', 'Lisa': 'Green', 'Vinod': 'Purple'}

























# l={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
# print(l.keys())
# x = list(l.keys())
# print(len(x))
# l['Lisa']='green'
# print(l)
# del l['Jenny']
# print(l)
# y="".join(l)

# print(l)



