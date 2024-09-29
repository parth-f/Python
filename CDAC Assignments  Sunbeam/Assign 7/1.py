# 1) Write a version of a palindrome recognizer that also accepts phrase 
# palindromes such as 
# "Go hanga salami I'm a lasagna hog.",
# "Was it a rat I saw?", "Step on no pets", 
# "Sit on a potato pan, Otis", 
# "Lisa Bonet ate no basil", 
# "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation 
# "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usually ignored

enter_str = (input("Enter a string : ")).lower()

enter_str = "".join(v for v in enter_str if v.isalpha())

palindrome = True

for i in range(int(len(enter_str)/2)):
    if (enter_str[i] == enter_str[int(len(enter_str))-1-i]):
        continue
    else:
        palindrome = False

if palindrome == True:
    print("Its is a palindrome")
else:
    print("Its is not a palindrome")
    