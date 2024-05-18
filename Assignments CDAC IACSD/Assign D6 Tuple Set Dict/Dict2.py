# 2. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

## a. Find out how many students are in the list
## b. Change Lisa’s favourite colour
## c. Remove 'Jenny' and her favourite colour

print("Num of students =", len( list(people.keys()) ) )
# a. output > Num of students = 4

people['Lisa']='Green'
print("Lisa fav Color is",people['Lisa'])
# b. output > Lisa fav Color is Green

del people['Jenny']
print(people)
# c. output > {'Arham': 'Blue', 'Lisa': 'Green', 'Vinod': 'Purple'}

























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



