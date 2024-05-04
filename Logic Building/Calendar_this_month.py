# WAP to print calender for a month. Take how many days 
# are there in month and starting day of the month as input

# Ex. input no of days : 30  starting day of month : Thursday
# Ouput :: Day wise Calender  ( just like June 2022 month)

which_day = int(input("1 - Sun | 2 - Mon | 3 - Tue | 4 - Wed | 5 - Thu | 6 - Fri | 7 - Sat | :- "))
total_days = int(input("\nEnter no. of days in mouth - "))

print("")

weekdays = (which_day-1)
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat",end="\n\n") # Prints Days of Months
print(" \t"*weekdays,end="") # Prints Spaces Before the Date Starts

for date in range(1,total_days+1): # Prints the Mouth Starting from that Day

    print(date,"\t",end="") # Prints the date 
    weekdays += 1
    
    if(weekdays==7): # Week Counter restart
        print("\n") # new line
        weekdays = 0

# Output ----
    
# 1 - Sun | 2 - Mon | 3 - Tue | 4 - Wed | 5 - Thu | 6 - Fri | 7 - Sat | :- 5

# Enter no. of days in mouth - 30

# Sun     Mon     Tue     Wed     Thu     Fri     Sat

#                                 1       2       3

# 4       5       6       7       8       9       10

# 11      12      13      14      15      16      17

# 18      19      20      21      22      23      24

# 25      26      27      28      29      30