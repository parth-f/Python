#  WAP to convert given integer to binary, hex and octal format

user_in = int(input("Enter a num - "))

print("")
print("","Value","Py Value",sep="\t")
print("","-----","--------",sep="\t")
print("bin - ",(str(bin(user_in)))[2:],bin(user_in),sep="\t")
print("oct - ",(str(oct(user_in)))[2:],oct(user_in),sep="\t")
print("hex - ",(str(hex(user_in)))[2:],hex(user_in),sep="\t")



# Enter a num - 14

#         Value   Py Value
#         -----   --------
# bin -   1110    0b1110
# oct -   16      0o16
# hex -   e       0xe