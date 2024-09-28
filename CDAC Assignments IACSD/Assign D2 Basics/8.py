# 9.    Write a program to check whether an years is leap year or not the year is leap if it satisfies following condition  
# •    It the year is divisible by 100 o If it is divisible by 100, then it should also be divisible by 400 then it is leap year  
# •    otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year.  

year = int(input("Enter a year "))

if(year%4==0):
    if(year%100==0):
        print(f"Not a leap year {year}/100")
    else:
        print(f"{year} is a leap year")
else:
    print("Not a leap year - {year}")

# Enter a year 2025
# Not a leap year - 2025
# Enter a year 2024
# 2024 is a leap year
# Enter a year 2400
# Not a leap year 2400/100
