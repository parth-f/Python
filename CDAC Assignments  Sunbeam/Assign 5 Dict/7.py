# 7) Write a program in Python to read a string from the keyboard. 
# Replace each ‘this’ word with ‘that word’ in this String. 
# Example: this is me and this is my python program. 
# Output: That is me and That is my python program

my_str = input("Enter a string \n")

str_list = my_str.lower().split()

for i,val in enumerate(str_list):
    if val == 'this':
        str_list[i] = 'That'

final_str = " ".join(str_list)

print(final_str)

# input  : This is not my name this is my surname
# output : That is not my name That is my surname