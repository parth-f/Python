# 6. Take a sentence as input from user. Every word is seperated
#    by space. Print all unique words from the sentence.

user_input = input("Enter names with ',' as a seperator - ")

names = set(user_input.split(", "))

print(names)

# Enter names with ',' as a seperator - Rahul, Sachin, Pravin, Chaitanya, Shivani
# {' Sachin', ' Chaitanya', ' Pravin', 'Rahul', ' Shivani'}