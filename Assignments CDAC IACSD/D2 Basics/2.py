
# 1.    A student will not be allowed to sit in exam if his/her 
# attendance is less than 75%.  Take following input from user Number 
# of classes held Number of classes attended. And print percentage of 
# class attended Is student is allowed to sit in exam or not.  

total_classes = int(input("Total Classes - "))
attended_classes = int(input("Attended Classes - "))
attended_perc = attended_classes / total_classes * 100

print(round(attended_perc,1,),"%")

if (attended_perc>=75):
    print("You are allowed to sit in the Exam")
else:
    print("You are not allowed to sit in the Exam")

# Total Classes - 89
# Attended Classes - 58
# 65.2 %
# You are not allowed to sit in the Exam