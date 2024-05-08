# 6. To display the cube of the number upto given an integer. 
# If the given integer is 5, then display cube of 1 to 4. # range(1,5)

n = int(input("Enter num - "))

for i in range(1,n):
    print(i,"^2 = ",i**2,sep="")



# Output --------

# 1^2 = 1
# 2^2 = 4
# 3^2 = 9
# 5^2 = 25
# 6^2 = 36
# 7^2 = 49
# 8^2 = 64
# 9^2 = 81
# 10^2 = 100