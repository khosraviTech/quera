# https://quera.org/problemset/108665

#input
word = input()

#algorithem
char_list=["a","e","i","o","u"]

char_counter=0

for i in word:
    if i in char_list:
        char_counter+=1
if(char_counter>0):
    print(2**char_counter)
else:
    print(1)    