# https://quera.org/problemset/3409

# input
n: int = int(input())

# n=5:
    # 1 2 3 4 5
    # 2 4 6 8 10
    # 3 6 9 12 15
    # 4 8 12 16 20intel
    # 5 10 15 20 25

# algorithm
horizontal: list[int] = []  # 1  2 3 4 5
vertical: list[int] = []    # 1  2 3 4 5

for i in range(1, n + 1):  # init
    horizontal.append(i)
    vertical.append(i)

for i in range(1, len(horizontal) + 1):  # first line
    if i == len(horizontal):
        print(i)
        break
    print(i,'',end='')

for v in range(2, len(vertical) + 1): # 2 3 4 5
    for h in horizontal:# 1  2 3 4 5
        if h == len(horizontal):
                print(h*v)
                break 
        print(h*v,'',end='')
