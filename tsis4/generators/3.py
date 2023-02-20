n = int(input())

print(*[i for i in range(0, n+1) if i % 3 == 0 and i % 4 == 0], sep=", ")

###########################################################################


def filter_number(limit):
    i = 0
    while i <= limit:
        if i%3 == 0 and i%4 == 0:
            yield i
        i += 1


n = int(input())
print(*list(filter_number(n)), sep=', ')
