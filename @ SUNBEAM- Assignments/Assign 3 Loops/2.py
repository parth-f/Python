# 2) Write a program that accepts a list from user and 
#    print the alternate element of list.

user_in = list(input("Enter a list - "))

# print(user_in)
for n in range(0,len(user_in),2):
    print(user_in[n],end="")