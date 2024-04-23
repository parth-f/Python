# 1. Reverse the following tuple
# aTuple = (10, 20, 30, 40, 50,60)
# Expected output:
# (60,50, 40, 30, 20, 10)

# Ans
#   Tupples value can't be changed it can be reassigned a new tuple
#   or object reference to be exact so following is the solution 

aTuple = (10, 20, 30, 40, 50, 60)
print(aTuple,type(aTuple))

aTuple_list = list(aTuple)   # Temp Var to switch val 
aTuple_list.sort(reverse=True)

aTuple = tuple(aTuple_list)
print(aTuple,type(aTuple))

# (10, 20, 30, 40, 50, 60) <class 'tuple'>
# (60, 50, 40, 30, 20, 10) <class 'tuple'>