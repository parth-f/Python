# 3.    Modify the above question Q1 to allow student to sit if 
# he/she has medical cause. Ask user if he/she has medical cause 
# or not ( 'Y' or 'N' ) and print accordingly.  

total_classes = int(input("Total Classes - "))
attended_classes = int(input("Attended Classes - "))
attended_perc = attended_classes / total_classes * 100


print(round(attended_perc,1,),"%")


if (attended_perc>=75):
    print("You are allowed to sit in the Exam")
else:
    medi_cause = (input("Is there a medical reason for less attendance? (Press 'Y' or 'N') - ")).upper()
    if(medi_cause=='Y'):
        print("Submit the Medical Certificate, and then you are allowed in Exam")
    else:
        print("You are not allowed to sit in the Exam")


# Output ------------------------------------------

# Total Classes - 89
# Attended Classes - 53
# 59.6 %
# Is there a medical reason for less attendance? 
# (Press 'Y' or 'N') - n
# You are not allowed to sit in the Exam

# Total Classes - 90
# Attended Classes - 64
# 71.1 %
# Is there a medical reason for less attendance? (Press 'Y' or 'N') - y
# Submit the Medical Certificate, and then you are allowed in Exam

