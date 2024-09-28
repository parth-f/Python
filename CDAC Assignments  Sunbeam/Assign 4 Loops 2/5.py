# 5).Write a function find_longest_word() that takes a 
#    list of words and returns the length of the longest one.


mylist = ['41','DROND','Sunbeam', '13','ZARA']
maxlen  = 0
x = None
for i,v in enumerate(mylist):
    if len(v)>maxlen:
        maxlen=len(v)
        x = i
print(mylist[x])