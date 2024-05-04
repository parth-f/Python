# Q WA function to take string as parameter
#   Check if string is palindrome or not
#   If palindrome return 1
#   if not palindrome return 0

def check_palindrome(str1 :str):
    if str1 == str1[::-1]:
        return 1
    else: 
        return 0

str1 = input("Enter a Palindrome - ")
print(check_palindrome(str1))