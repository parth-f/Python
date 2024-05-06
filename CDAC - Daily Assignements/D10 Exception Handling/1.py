bad_var = 2
try:
    var = bad_var
    if var == 2:
        raise Exception
except Exception as e:
    # print('Sorry. /This file dosent not exist')
    print("error!")
else:
    print(var)
finally:
    print("Exceting finally")


# Exception Hnalding 

try:
    pass
except:
    pass
else:
    pass
finally:
    pass