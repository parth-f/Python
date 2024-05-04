# 5.    Given a number count the total number of digits in a 
# number and also find sum of digits of the number.

num = input("Enter a num  - ")
sum = 0
print("Count of Num - ",len(num))

for n in num:
    sum += int(n)
print("Sum of Digits - ",sum)

# Enter a num  - 429842
# Count of Num -  6
# Sum of Digits -  29