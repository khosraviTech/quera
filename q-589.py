# https://quera.org/problemset/589
# input
n = int(input())

# algorithem
def fact(n):
    if(n==1):
        return 1
    else:
        return n*(fact(n-1))
    
# output
print(fact(n))