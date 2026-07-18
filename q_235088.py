# https://quera.org/problemset/235088

n = int(input())
l, r = map(int, input().split())

days = (n + r - 1) // r

if days * l <= n <= days * r:
    print(days)
else:
    print(-1)
