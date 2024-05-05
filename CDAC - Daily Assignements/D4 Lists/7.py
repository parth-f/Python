# 7. Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1 = [10, 20, [300, 400,[300, [5000, 6000],400], 500], 30, 40]

def find_list(list):

    found = False
    
    for idx, elm in enumerate(list):

        if found == True:
            return 

        if str(type(elm)) == "<class 'list'>":
            list = list[idx]
            find_list(list)
            continue
        # print(elm)

        if(elm == after):
            list.insert(idx+1,e)
            found = True
            return 

 
print(list1)
print("")
after = int(input("enter after which no. - "))
e = int(input("Enter the num you wanna append - "))
print("")
find_list(list1)
print(list1)