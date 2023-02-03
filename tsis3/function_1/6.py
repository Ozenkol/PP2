def reverse_list(list):
    res = []
    i = len(list)-1
    while i >= 0:
        res.append(list[i])
        i = i-1
    return res


list = list(map(str, input().split()))

print(*reverse_list(list))

