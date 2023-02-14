n = int(input())

print(*[i for i in range(1, n+1) if i % 3 == 0 and i % 4 == 0], sep=", ")
