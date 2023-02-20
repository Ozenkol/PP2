def square_generator(limit):
    i = 1
    while i**2 <= limit:
        yield i**2
        i += 1


N = int(input())
print(*list(square_generator(N)), sep=', ')
