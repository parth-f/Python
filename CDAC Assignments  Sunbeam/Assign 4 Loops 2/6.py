# 6). Define a procedure histogram() that takes a list of integers and 
#     prints a histogram to the screen. For example, histogram([4, 9, 7]) 
#     should print the following: 

#     **** 
#     ********* 
#     *******

def histogram(l :list):
    for n in l:
        print("*"*n)
    
histogram([4,9,7])