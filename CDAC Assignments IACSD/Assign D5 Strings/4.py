
# 4. Given an input string with the combination of the 
# lower and upper case, arrange characters in such a way 
# that all lowercase letters should come first.

# SOLUSTION > 1 -----------------------------------

# str = input("Enter a name - ")
# strlist = list(string1)

# strlist.sort(reverse=True)
# string1 = "".join(strlist)

# print(string1)

# Enter a name - gfbaGFDAdcCeEB
# gfedcbaGFEDCBA

# SOLUSTION > 2 -------------------------------------

Without using sort is done below
str = input("Enter a name - ")
smallstr = ""
bigstr = ""


for n in range(len(str)):
   
    char_val = ord(str[n])


    if( ord("a") <= char_val <= ord("z") ):
        smallstr += "".join(str[n])


    elif( ord("A") <= char_val <= ord("Z")):
        bigstr += "".join(str[n])


print(smallstr,bigstr,sep="")

# Enter a name - lgaeGEagaeGEEGAEGEAWGAgeij
# lgaeagaegeijGEGEEGAEGEAWGA

