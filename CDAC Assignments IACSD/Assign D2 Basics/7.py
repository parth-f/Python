# 8.  Write a program to check whether the last digit of a number 
# ( entered by user ) is divisible by 3 or not.  

num = input("Enter a number - ")


if( int(num[len(num)-1]) % 3 == 0 ):
    print("Last Digit is divisible by 3")
else:
    print("Last Digit is not divisible by 3")

# Output =========================
# Enter a number - 8996  
# Last Digit is divisible by 3
# Enter a number - 9842
# Last Digit is not divisible by 3
