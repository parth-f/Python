# Q WA function to take list as parameter and print all numbers of given 
#   list which are divisible by 11

def div_by_11(list_in :list):
    div11_save = list()
    for l in list_in:
        if l % 11 == 0 :
            div11_save.append(l)
    return div11_save
            
l1 = [3,42,44,13,11,44,89,99]
out = div_by_11(l1)

print(out)