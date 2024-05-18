# 5. Take a sentence as input from user. Every word is seperated by space. 
# a. Create a word_count dictionary which will have unique words and their count. 

# b. create suffix_count dictionary which will contain count of words ending with 's', 'es', 'ed', 'y', 'en' , etc.

# c. create dictionary word_length_count which will store length of word and count.
# Ex. 
# input_sent= 'CDAC is in Pune'
# There are 2 words of length 4 and 2 words of length 2 so,
# word_length_count = {2:2, 4:2}

u_sentence = input("Enter a sentence - ")

u_list = u_sentence.split(" ")
u_dict = dict(u_list)

# for el in u_dict:
#     c = 0
#     for n in u_list:
#         if el == n:
#             c += 1
#     print(el,c)

print(u_sentence,"\n",u_list,sep="")