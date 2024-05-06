# 2)The marks obtained by a student in 3 different subjects are input by the user. 
# Your program should calculate the average of subjects and display the grade. 
# The student gets a grade as per the following rules: 

# Average Grade 
# 90-100 A 
# 80-89 B 
# 70-79 C 
# 60-69 D 
# 0-59 F

def cal_grade(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 80 <= marks < 90:
        return "B"
    elif 70 <= marks < 80:
        return "C"
    elif 60 <= marks < 70:
        return "D"
    elif 0 <= marks < 60:
        return "F"
    
sub1 = int(input("Enter marks in sub1 - "))
sub2 = int(input("Enter marks in sub2 - "))
sub3 = int(input("Enter marks in sub3 - "))

print(f"Grade in Sub1 is {cal_grade(sub1)} with marks {sub1}")
print(f"Grade in Sub2 is {cal_grade(sub2)} with marks {sub2}")
print(f"Grade in Sub3 is {cal_grade(sub3)} with marks {sub3}")

# Enter marks in sub1 - 42
# Enter marks in sub2 - 70
# Enter marks in sub3 - 97
# Grade in Sub1 is F with marks 42
# Grade in Sub2 is C with marks 70
# Grade in Sub3 is A with marks 97