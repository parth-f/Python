# Ask user number of terms to be generated of a series.
# generate numbers for the following series and find its addition
# [9 + 99 + 999 + 9999+……..]

user_num = int(input("Enter a num - "))
sum = 0

print("[",end="")
for n in range(user_num):
    print("9"*(n+1),end=" + ")
    sum += (int("9"*(n+1)))
print("]",end="")

print("")
print(sum)