# WAP that accepts three integers from the user and return true if two or 
# more of them (integers ) have the same rightmost digit. The integers are 
# non-negative

user_in1 = input("Enter a num 1 - ")
user_in2 = input("Enter a num 2 - ")
user_in3 = input("Enter a num 3 - ")

if(user_in1[-1]==user_in2[-1]==user_in3[-1]):
    print(f"Same Last Digit {user_in2[-1]}")
else:
    print("Not the Same Last Digit")