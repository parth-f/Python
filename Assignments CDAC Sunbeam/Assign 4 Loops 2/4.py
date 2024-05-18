# 4). Write a method in python to display the elements of list 
#     thrice if it is a number and display the element terminated 
#     with ‘#’ if it is not a number. 
#     Hint-: Use InBuilt Function isdigit() 
#     Refer below as a input:mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]

mylist = ["41","DROND","Sunbeam", "13","ZARA"]



def  newDSprint(l :list):  
    x = len(l)  
    newl = []
    for n in l:

        if n.isdigit():
            newl.append(f"{n}#")
            print()
        else:
            newl.append(f"{n*3}")
    del l
    l = newl
    del newl
    print(l)

newDSprint(mylist)