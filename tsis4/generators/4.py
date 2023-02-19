a, b = map(int, input().split())
print(*[i**2 for i in range(a, b+1)], sep=' ')

#################################################


def filter_number(a, b):
    while a <= b:
        yield a**2
        a += 1


a, b = map(int, input().split())

for i in filter_number(a, b):
    print(i)
