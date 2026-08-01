# https://quera.org/problemset/282

# input
n: int = int(input())

# algorithm
divisors:list[int]=[]

for i in range(1,n):
    if n% i ==0:
        divisors.append(i)

# output
if sum(divisors)==n:
    print('YES')      
else:
    print('NO')