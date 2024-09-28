# 6) Write a program that rotates the element of a list so 
# that the element at the first index moves to the second 
# index, the element in the second index moves to the third 
# index, etc., and the element in the last index moves to 
# the first index

places = ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]
days = ['Sunday','Monday','Tuesday','Wednesday']

def first2last(lst):
    last = lst[-1]
    i = len(lst) - 1
    for l in lst[::-1]:
        if i != 0:
            lst[i] = lst[i-1]
        i -= 1
    lst[0] = last

    return lst
        
print(first2last(places))
# out > ['DUBAI', 'DELHI', 'LONDON', 'PARIS', 'NEW YORK']

print(first2last(days))
# out > ['Wednesday', 'Sunday', 'Monday', 'Tuesday']
