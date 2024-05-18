# 4). Write a method in python to display the elements of list 
# thrice if it is a number and display the element terminated 
# with ‘#’ if it is not a number. 
# Hint-: Use InBuilt Function isdigit() 
# Refer below as a input:mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]

mylist = ['41','DROND','Sunbeam', '13','ZARA']
for i,v in enumerate(mylist):
    maxlen  = 0
    x = None
    if len(v)>maxlen:
        maxlen=len(v)
        x = i
print( x)