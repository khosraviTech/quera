# https://quera.org/problemset/2529

# input
names = list()
n = int(input())
for i in range(n):
    names.append(input())

# algorithm
names_dict = dict()

for i in names:
    names_dict.update({i: len(set(i))})

# output
print(max(names_dict.values()))
