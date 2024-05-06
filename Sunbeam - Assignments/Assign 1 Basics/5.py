# 5] Write a Python function to find the maximum of three numbers.

a = 502
b = 2542
c = 529

def which_big(a,b,c):
    big = a
    
    if big < b:
        big = b
    if big < c:
        big = c

    return big

print(which_big(a,b,c))
