# Q Sort all the numbers in a list in descending order using lambda function
# sorted(l1, key=(lambda x:-x))

l1 = [10,4209,84,9,7,824,4]

print(sorted(l1, key=(lambda x : -x )))

# [4209, 824, 84, 10, 9, 7, 4]

