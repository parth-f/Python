# WAP to print numbers between 1 to 100 which are divisible by 3, 5 and by both
# ( total 3 list of numbers to be printed)

div_by_3 = list()
div_by_5 = list()
div_by_3_and_5 = list()

for n in range(1,101):
    if(n%3==0):
        div_by_3.append(n)
    if(n%5==0):
        div_by_5.append(n)

for n in div_by_3:
    if(n%5==0):
        div_by_3_and_5.append(n)

print("Divisible by 3 - ",div_by_3)
print("Divisible by 5 - ",div_by_5)
print("Div by 3 and 5 - ",div_by_3_and_5)

# Divisible by 3 -  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
# Divisible by 5 -  [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# Div by 3 and 5 -  [15, 30, 45, 60, 75, 90]