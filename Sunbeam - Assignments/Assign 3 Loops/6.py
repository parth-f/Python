# 6) Find and display the largest number of a list without using built-in 
# function max(). Your program should ask the user to input values in 
# list from keyboard.

user_list = input("Enter a number of list seperated by commas - ").split(",")

def maxx(user_list):

    max = int(user_list[0])
    for v in user_list:
        if max < int(v):
            max = int(v)
    return max

print( maxx(user_list) )