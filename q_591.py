# https://quera.org/problemset/591

# input
n = int(input())

# algotithem + output
print('*' * n, end="\n")

for i in range(n - 2):
    print('*' + ' ' * (n - 2) + '*')

print('*' * n)
