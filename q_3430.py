#https://quera.org/problemset/3430
#input

word=input()

#algorithem
for i in range(len(word)):
    
    #output
    print(word[i] * (i + 1) + word[i + 1:])

