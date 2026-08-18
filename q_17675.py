# https://quera.org/problemset/17675

# input
n = int(input())

# algorithm
fib = [1, 2]

while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])

fib_set = set(fib)

answer = ""

for i in range(1, n + 1):
    if i in fib_set:
        answer += "+"
    else:
        answer += "-"
        
# output
print(answer)