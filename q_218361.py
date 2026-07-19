# https://quera.org/problemset/218361

# input
row_1=list(int(input().split(' ')))
row_2=list(int(input().split(' ')))

# algorithem
counter=0

for i in row_1:
    if(row_1[i]==1 and row_1[i]==row_2[0]):
        counter+=1
