# WAP to print all leap years between 2000 to 2100. Apply all 
# conditions of checking leap year ( (divisible by 4 and not 
# divisible by 100) OR (divisible by 400))

year = int(input("Enter a year to check if its a leap year - "))

def check_leap(year :int):
    if(year%4==0): # leap year unless div by 100
        if(year%100==0): # not a leap year unless div by 400
            if(year%400==0): # leap year if div by 400
                return True
            else:
                return False
        else:
            return True
    return False

if(check_leap(year)==True):
    print(f"{year} is a leap year ")
else:
    print(f"{year} is a not leap year ")

