# https://quera.org/problemset/66864

# input
k: int = int(input())

# algorithm
number: str = ""

for i in range(1, k + 1):
    number += str(i)

# output
print(number[k - 1])

