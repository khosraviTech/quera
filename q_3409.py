# https://quera.org/problemset/3409

# input
n: int = int(input())

# n=5:
    # 1 2 3 4 5
    # 2 4 6 8 10
    # 3 6 9 12 15
    # 4 8 12 16 20
    # 5 10 15 20 25

# algorithm
horizontal: list[int] = []  # 1  2 3 4 5
vertical: list[int] = []    # 1  2 3 4 5

for i in range(1, n + 1):  # init
    horizontal.append(i)
    vertical.append(i)


