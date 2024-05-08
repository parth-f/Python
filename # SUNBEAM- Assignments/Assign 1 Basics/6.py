# 6] Write a Python Program Get age input from user and check if user is eligible for voting

age = int(input("Input your age - "))

if age>= 18:
    print(f"your age is {age}, so you are allowed to vote")
else:
    print(f"your age {age} is less than 18 so your are not allowed to vote")