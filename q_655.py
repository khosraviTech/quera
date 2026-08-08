# https://quera.org/problemset/655

# input
n = int(input())


# algorithm
for _ in range(n):
    movie = input()
    words = movie.split()

    result = []

    for word in words:
        word = word[0].upper() + word[1:].lower()
        result.append(word)
