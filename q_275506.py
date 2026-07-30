# https://quera.org/problemset/275506

# input
n = int(input())
pages = list(map(int, input().split()))

# algorithm
total_pages = sum(pages)

for p in pages:
    if p % 2 == 1:
        total_pages += 1