# Q8. Write a program to take marks of 3 subjects from a student. Calculate total in variable name 'total'.
# Note: Don't use sum as variable name, it is built in function in python)

total=0


for i in range(3):
    total += int(input(f"Enter Marks of Sub {i+1} - "))

print("Total Marks = ",total)


# Enter Marks of Sub 1 - 90
# Enter Marks of Sub 2 - 87
# Enter Marks of Sub 3 - 68
# Total Marks =  245