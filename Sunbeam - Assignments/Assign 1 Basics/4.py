# 4] Write a program to accept three integer numbers and find its average.

user_in1 = int(input("Enter 1st int num - "))
user_in2 = int(input("Enter 2nd int num - "))
user_in3 = int(input("Enter 3rd int num - "))

l = [user_in1,user_in2,user_in3]

def fun_avg(nums :list):
    
    sum = 0
    for n in nums:
        sum += n
    
    return sum / len(nums)

print(f"avg of {user_in1}, {user_in2}, {user_in3} = ",round(fun_avg(l),2))

# Enter 1st int num - 4
# Enter 2nd int num - 5
# Enter 3rd int num - 2
# avg of 4, 5, 2 =  3.67
