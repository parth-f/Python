# 6) Write a function translate() that will translate a text into 
# "rövarspråket" (Swedish for "robber's language"). That is, double
#  every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string 

s = 'this is fun'
# "tothohisos isos fofunon".

con = ['a','e','i','o','u']

for v in s:
    if v == ' ':
        print(' ',end='')
    elif v in con:
        print(v,end='')
    elif v not in con:
        print(v+'o'+v,end='')
        print('',end='')
    
# output : "tothohisos isos fofunon".