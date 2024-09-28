l1 = [14,5]

idx = int(input("Enter index check - "))
try:
    print(l1[idx])
except IndexError:
    print(f"The Index that you have given {idx} is out of bound, last index = {len(l1)-1}")