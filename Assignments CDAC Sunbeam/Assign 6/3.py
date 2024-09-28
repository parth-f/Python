# 3) Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string

mystr = input("Enter a string : ")

# * uppercase 
out = 0
for a in mystr:
    if a == a.upper() and a != ' ':
        out += 1
print("The number of uppercase letters in the string : "+ str(out))

# *lowercase 
out = 0
for b in mystr:
    if b == b.lower() and a != ' ':
        out +=1
print("The number of lowercase letters in the string : "+ str(out))

# *digits
out = 0
for c in mystr:
    if c.isnumeric() == True:
        out += 1
print("The number of digits in the string : "+ str(out))

# *whitespace 
out = 0
for d in mystr:
    if d == ' ' or d == '\n':
        out += 1
print("The number of whitespace characters in the string : "+ str(out))

# input: 
# Enter a string : How are you doing Raj 2day 5pm

# output:
# The number of uppercase letters in the string : 4
# The number of lowercase letters in the string : 28
# The number of digits in the string : 2
# The number of whitespace characters in the string : 6