# 5. create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1
# and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Given:
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX

s1 = "Abc"
s2 = "Xyz"


for n in range(0,len(s1)):
    print(s1[n],s2[-(n+1)],sep="",end="")

# AzbycX
