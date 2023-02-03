def unique_list(list):
    res=[]
    for i in list:
        if i not in res:
            res.append(i)
    return res


list = list(input().split())

print(unique_list(list))
