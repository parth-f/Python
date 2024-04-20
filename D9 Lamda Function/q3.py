# Q Given list of strings, sort all the strings by last 
# character of that string. . Use lambda function and 
# normal function both.

list_of_s = ["Today","is","a","day","to","play","soccer"]

print(sorted(list_of_s, key=(lambda s : s[-1])))
