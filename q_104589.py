# https://quera.org/problemset/104589

# input
n: int = int(input())

# algorithm
lst: list[int] = []

for i in range(2, n + 1):
    if n % i == 0:
        lst.append(n // i)
        
# output
print(max(lst))
