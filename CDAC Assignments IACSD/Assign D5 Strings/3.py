# 3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each input
# String

# Given:
# s1 = "America"
# s2 = "Japan"
# Expected Output:
# AJrpan

s1="America"
s2="Japan"


print(s1[0],s2[0],s1[(int(len(s1)//2))],s2[(int(len(s2)//2))],s1[-1],s2[-1],sep="")

# AJrpan

