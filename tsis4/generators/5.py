def generator(limit):
    i = limit
    while i >= 0:
        yield i
        i -= 1


n = int(input())

print(*list(generator(n)), sep=', ')
