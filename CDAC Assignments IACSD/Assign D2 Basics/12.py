line = int(input("Enter the line of star - "))
for n in range( line - 1 , -1, -1):


    print(" " * (line - n - 1), end = "")
    print("10"*n , end = "1\n")





# Output --------------------

# Enter the line of star - 5
# 101010101
#  1010101
#   10101
#    101
#     1
