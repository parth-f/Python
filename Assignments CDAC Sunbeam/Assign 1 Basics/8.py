# 8] Write a program that prompts the user to input number of calls and calculate the 
# monthly telephone bills as per the following rule: 
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls. 
# Plus Rs. 0.50 per call for next 50 calls. 
# Plus Rs. 0.40 per call for any call beyond 200 calls.

num_call = int(input("Enter the no. of calls - "))

bill = 0

if num_call > 200:
    bill += (num_call-200)*0.40 + 50 * 0.50 + 50 * 0.60 + 200
elif 200 >= num_call > 150:
    bill += (num_call-150)*0.50 + 50*0.60 + 200
elif 150 >= num_call > 100:
    bill += (num_call-100)*0.60 + 200
else:
    bill += 200

print(bill,"for",num_call)