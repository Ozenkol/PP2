n = int(input())
print(*[i for i in range(0, n+1) if i % 2 == 0], sep=", ")


#######################################################


def filter_generator(limit):
    i = 0
    while i <= limit:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input())
print(*list(filter_generator(n)), sep=', ')
