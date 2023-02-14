a, b = map(int, input().split())



print(*[i**2 for i in range(a, b+1)], sep=' ')
