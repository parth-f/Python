# 7.    Accept 20 numbers from user and display sum of 
# only even numbers.
sum = 0
for idx in range(20):

    user_input = int(input(f"Enter no. {idx+1}: "))

    if( user_input%2 == 0 ):
        sum += user_input
    elif( user_input%2 != 0 ):
        continue

print("Sum of Even no. is ",sum)