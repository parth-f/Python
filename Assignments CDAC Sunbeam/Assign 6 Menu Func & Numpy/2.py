# 2) Display following menu and write required function for it 
# A. Display characters from even position 
# B. Display characters from odd position 
# C. Display length of a string 
# D. Add a at the end of string length times

str = input("Enter a string : ")

opt = input("""Select a option from below
A. Display characters from even position 
B. Display characters from odd position 
C. Display length of a string 
D. Add a at the end of string length times
input > """)



if opt == 'A':
    print(str[::2])
elif opt == 'B':
    print(str[1::2])
elif opt == 'C': 
    print(len(str))
elif opt == 'D':
    str = str + " " + len(str)*'a'
    print(str)
else:
    print("Wrong Input")
    
# Enter a string : how are you
# Select a option from below
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times
# input > D
# how are you aaaaaaaaaaa

