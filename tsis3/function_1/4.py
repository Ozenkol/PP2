def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def filter_prime(list):
    res=[]
    for x in list:
        if is_prime(x)==1:
            res.append(x)

    return res



mylist = list(map(int, input().split()))

print(filter_prime(mylist))
