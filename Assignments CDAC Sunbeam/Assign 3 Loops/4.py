# 4) Write a program to find index of element ‘e’ in 
# given vowels list [’a’, ’e’, ’i’, ’o’, ’i’, ’u’]

vowels = ['a','e','i','o','u']

for i, v in enumerate(vowels):
    if v == 'e':
        print(f"We found 'e' at index {i} in vowels")
           
