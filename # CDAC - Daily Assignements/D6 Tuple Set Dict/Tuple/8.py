import copy 
# 8. Write a Python program to create the colon of a tuple.


t8 = (32,"rahul","takhur",4,"new")

sc_t8 = copy.copy(t8)
dc_t8 = copy.deepcopy(t8)

print(t8,sc_t8,dc_t8)

print(id(t8[1]),id(sc_t8[1]),id(dc_t8[1]))

print("is t8 shallow copy sc_t8 - ", t8[1] is sc_t8[2])
print("is t8 deep copy dc_t8 - ", t8[1] is dc_t8[1])