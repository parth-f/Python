# 1. Given a string of odd length greater than 7, return a new string made of the middle three characters
# of a given String
# Given:
# str1 = "RakeshzipPetabb"
# Output
# zip
# str2 = "JazzbonAyxx"
# Output
# Bon

str1 = 'RakeshzipPetabb'
str2 = 'JazzbonAyxx'


strmid = len(str1)//2
print(str1[strmid-1],str1[strmid],str1[strmid+1],sep="")

# zip
# bon
