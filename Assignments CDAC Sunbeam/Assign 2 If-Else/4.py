# 4) Write a program that will calculate the price for a quantity entered from 
#   the keyboard, given that the unit price is Rs 5 and there is a discount of 
#   10 percent for quantities over 30 and a 15 percent discount for quantities over 50.


qty = int(input("Enter the quantity - "))

price = 5

def cnt_discount(qty,price=price):
    if qty >= 50:
        final_price = ( qty*price ) - (( qty * price ) / 100 * 15)
        return final_price
    
    elif 50 > qty >= 30:
        final_price = ( qty*price ) - (( qty * price ) / 100 * 10)
        return final_price
    
    else:
        final_price = qty * price
        return final_price

v = cnt_discount(qty)
print("Final Price including Discount",v)
