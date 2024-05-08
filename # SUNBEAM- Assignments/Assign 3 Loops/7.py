# 7) Write a function filter_long_words() that takes a list of words and 
#    an integer len and returns the list of words that are longer than len.


def filter_long_words(ulist :list, lent: int):

    rl = list()
    for n in ulist:
        if len(n) >= lent:
            rl.append(n)

    return rl

ull = ["how","word","are","you","okay"]

print("Got the long char back - ", filter_long_words(ull,4))