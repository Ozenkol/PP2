n = int(input())
print(*[i for i in range(1, n+1) if i % 2 == 0], sep=", ")
