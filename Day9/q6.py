
# Q. Take comma separated numbers as input from the user. 
# Split it in list of strings. Now convert every string in 
# this list to float using map function

val = "49,492,4249,59024,95"

list = (val.split(","))

res = map(float, list)
print(list)
l=[]
for num in res:
    print(num)
    l.append(num)

print(l)


# short cut --------------------

# input_str = "1, 34, 55.5, 77.8, 23.345"
# list_no_str=input_str.split(",")
# print([ num for num in map(float, list_no_str)])
# print([ num for num in map(float, input_str.split(","))])