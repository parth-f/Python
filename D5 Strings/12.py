# 12. You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w
# Example .
# String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
# Width: 4
# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

str1 = input("Enter a string to wrap - ")


wrap_len=int(input("What length should i wrap - "))
wrap_count = 0


for n in range(len(str1)):


    if(wrap_count <= (wrap_len - 1)):
        print(str1[n],end="",sep="")
    elif(wrap_count > (wrap_len - 1)):
        print("\n",str1[n],end="",sep="")
        wrap_count=0
    wrap_count+=1

# Output
# Enter a string to wrap - ABCDEFGHIJKLMNOPQRSTUVWXYZ
# What length should i wrap - 4
# ABCD
# EFGH
# IJKL
# MNOP
# QRST
# UVWX
# YZ
