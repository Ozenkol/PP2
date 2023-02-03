def from_gram_to_ounces(grams):
    return grams*28.3495231


def from_fahrenheit_to_c(f):
    c = (5 / 9)*(f-32)
    return c


def solve(numheads, numlegs):
    return int((numlegs-2*numheads)/2), int(numheads-(numlegs-2*numheads)/2)


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


def reverse_list(list):
    res = []
    i = len(list)-1
    while i >= 0:
        res.append(list[i])
        i = i-1
    return res


def has_33(nums):
    mystr = ''.join(nums)
    return mystr.find("33")


def spy_game(nums):
    mystr = ''.join(nums)
    return mystr.find("007")


def sphere_volume(radius):
    return (4*3.14*radius**2)/3


def unique_list(list):
    res=[]
    for i in list:
        if i not in res:
            res.append(i)
    return res


def is_palyndrome(string):
    return string == string[::-1]


def histogram(nums):
    for i in nums:
        print("*"*i)

