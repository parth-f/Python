# Q3. WAP to take following from user, 
# roll no : should be int : store in a variable
# percentage marks : should be float: store in a variable
# Any complex number : should be a complex number : store in a variable
# name of student: should be a string : store in a variable

# Print values of all four variables

rollno = int(input("Enter your rollno - "))
percentage = float(input("Enter your Percentage - "))
complexNum = complex(int(input("Enter a Complex Num (Real Part) - ")), int(input("Enter a Complex Num (Imaginery Part) - ")))
name = input("Enter your Name - ")

print(rollno,name,percentage,complexNum)

# Enter your rollno - 4
# Enter your Percentage - 2
# Enter a Complex Num (Real Part) - 4
# Enter a Complex Num (Imaginery Part) - 2
# Enter your Name - Parth
# 4 Parth 2.0 (4+2j)

# print(isinstance(complexNum,complex))
