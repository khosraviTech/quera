# https://quera.org/problemset/218361

# input
row_1=list(input().split(' '))
row_2=list(input().split(' '))

# algorithem
counter=0

for i in range(8):
    if(row_1[i]=='1' and row_1[i]==row_2[i]):
        counter+=1

# output
print(counter)