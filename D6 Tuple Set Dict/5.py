# 5. Copy element 44 and 55 from the following tuple into a new tuple
# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
# tuple2: (44, 55)

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[-3:-1]

print(tuple1)
print(tuple2)

# (11, 22, 33, 44, 55, 66)
# (44, 55)