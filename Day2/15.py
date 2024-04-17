# 4. Take integer inputs from user until he/she presses q 
# ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.

product = 1
cnt = 0

while(True):

    cnt+=1
    user_in = input("Enter a num - ")
    if(user_in=="q"):
        break
    else:
        product *= int(user_in)
    print("Press 'q' to quit, ",end="")

print("")
print("Product of all",product,"Avg of all",product/cnt,sep=" ")





# Output =======================

# Enter a num - 4
# Press 'q' to quit, Enter a num - 2
# Press 'q' to quit, Enter a num - 5
# Press 'q' to quit, Enter a num - q

# Product of all 40 Avg of all 10.0

