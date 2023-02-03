def has_33(nums):
    mystr = ''.join(nums)
    return mystr.find("33")


nums = list(map(str, input().split()))

print(bool(has_33(nums=nums)))
