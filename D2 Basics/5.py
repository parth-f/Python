# Q4.    A school has following rules for grading system:  
# a.    Below 25 - F  
# b.    25 to 45 - E  
# c.    45 to 50 - D  
# d.    50 to 60 - C  
# e.    60 to 80 - B  
# f.    Above 80 - A  
# Ask users to enter marks and print the corresponding grade.  

Marks = int(input("Enter Marks - "))

if(Marks>=80):
    print(f"{Marks} you get a A")
elif(80>Marks>=60):
    print(f"{Marks} you get a B")
elif(60>Marks>=50):
    print(f"{Marks} you get a C")
elif(50>Marks>=45):
    print(f"{Marks} you get a D")
elif(45>Marks>=25):
    print(f"{Marks} you get a E")
else:
    print(f"{Marks} you get a F, and you are fail")

# Output =============

# Enter Marks - 24
# 24 you get a F, and you are fail
# Enter Marks - 89
# 89 you get a A
# Enter Marks - 73
# 73 you get a B
# Enter Marks - 56
# 56 you get a C

