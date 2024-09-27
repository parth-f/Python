# 5) Write a program to read 6 numbers and create a dictionary having 
# keys EVEN and ODD. Dictionary's value should be stored in list. Your 
# dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

# l1 = [2,52,5,3,7,3]
l1 = [8,1,10,64,5,9]

my_dict = {'EVEN':[],'ODD':[]}

for x in l1:
    if x % 2 == 0: # EVEN
        my_dict['EVEN'].append(x)
    elif x % 2 != 0: # ODD
        my_dict['ODD'].append(x)
    else:
        pass

print(my_dict)