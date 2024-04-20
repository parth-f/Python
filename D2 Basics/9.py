# 1.    Accept 10 integers from user  and print 
# their average value on the screen

sum_num=0
for n in range(10):
    sum_num+= int(input(f"Enter int no.{n+1} - "))
print(f"The avg value of all 10 input is {sum_num/10}")

# Output ===========================
# Enter int no.1 - 87
# Enter int no.2 - 52
# Enter int no.3 - 2
# Enter int no.4 - 6
# Enter int no.5 - 3
# Enter int no.6 - 6
# Enter int no.7 - 3
# Enter int no.8 - 3
# Enter int no.9 - 6
# Enter int no.10 - 3
# The avg value of all 10 input is 17.1