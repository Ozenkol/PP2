def isPal(str):
    return list(str) == list(reversed(str))


str = input()
print(isPal(str))
