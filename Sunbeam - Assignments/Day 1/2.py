# 2] Write a Python Program to Convert Celsius To Fahrenheit vice versa. 
# fahrenheit = (celsius * 1.8) + 32

def con_fahrenheit(temp):
    return (temp * 1.8) + 32

print(con_fahrenheit(int(input("Enter a Temp in Celcuis to convert to Fahrenhite - "))))