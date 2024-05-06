# 3] Write a program to accept a 4 digit number and 
# a. Display face value of each decimal digit 
# b. Display place value of each decimal digit 
# c. Display no in reverse order by changing decimal place values 
# If user enters a 4 digit number 9361 output should be 
#       a. 9 3 6 1 
#       b. 9361 = 9 000 + 300 + 60 + 9 
#       c. 1639


fd_num = input("Enter a four digit num - ")

# a.
for n in fd_num:
    print(n," ",end="")
print("")

# b.
print(fd_num,"= ",end="")
flen = len(fd_num)
for i,n in enumerate(fd_num):

    if(flen-1 == i):
        print(n,"0"*(flen-i-1)," ",sep="",end="")
        break
    print(n,"0"*(flen-i-1)," + ",sep="",end="")

print("")

# c. 
print(fd_num[::-1])