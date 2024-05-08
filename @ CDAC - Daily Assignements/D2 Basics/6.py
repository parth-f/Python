# 7. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
#          	Unit                                	Price    
# First 100 units                                   	no charge  
# Next 100 units                                    	Rs 5 per unit  
# After 200 units                                   	Rs 10 per unit  
# (For example if input unit is 350 than total bill amount is Rs2000)  

unit = int(input("Enter the amount of units consumed - "))


if(unit>=200):
    bill = (unit%200)*10 + 100 * 5 + 0;
elif(unit>=100):
    bill = (unit%100)*5 + 0;
else:
    bill = 0

print("bill is",bill)


# Output =================
# Enter the amount of units consumed - 350
# bill is 2000
