# 3. Sort and print students and their favourite colours alphabetically by name

people={'Arham':'Blue','Lisa':'Green','Vinod':'Purple','Jenny':'Pink'}
print("Unsorted list - ",people)

sorted_people = sorted(list(people.keys()))
people2 = dict()

for p in sorted_people:
    for keyy,vall in people.items(): 
        if p == keyy:
            people2[keyy] = vall
            
people = people2
print("Sorted list   - ",people)

# Unsorted list -  {'Arham': 'Blue', 'Lisa': 'Green', 'Vinod': 'Purple', 'Jenny': 'Pink'}
# Sorted list   -  {'Arham': 'Blue', 'Jenny': 'Pink', 'Lisa': 'Green', 'Vinod': 'Purple'}