#https://quera.org/problemset/3430
#input

word=input()

#algorithem
for i in range(1,len(word)+1):
    print(word[i] * (i + 1) + word[i + 1:])

