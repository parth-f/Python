# 5)Calculate the sum and average of the digits present 
# in a string 
# Str1="Python83737@#8496"


Str1="Python83737@#8496"

def sum_str_digit(str):
    sum = 0

    for s in str:
        if s.isnumeric() == True:
            sum += int(s)
    return sum

out = sum_str_digit(Str1)
print(out)
