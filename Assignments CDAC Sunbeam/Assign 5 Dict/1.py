# 1) Given a dictionary of students and their favourite colours: 
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
# A. Find out how many students are in the list 
# B. Change Lisa’s favourite colour 
# C. Remove 'Jenny' and her favourite colour 
# D. Sort and print students and their favourite colours alphabetically by name

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'} 

# A. Find out how many students are in the list 
print("A. Number of Students in the list = "+str(len(list(people.values()))))

# B. Change Lisa’s favourite colour 
people['Lisa'] = 'Zebra'
print("B. Lisa Fav Color = "+people['Lisa'])

# C. Remove 'Jenny' and her favourite colour 
del people['Jenny']
print("C. Remove Jenny = " + str(people))

# D. Sort and print students and their favourite colours alphabetically by name
color_sort = dict(sorted(people.items(), key=lambda item:item[1], reverse=False))
print("D. Sort on Color = " + str(color_sort))
