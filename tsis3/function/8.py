def spy_game(nums):
    mystr = ''.join(nums)
    return mystr.find("007")


nums = list(map(str, input()))

print(bool(spy_game(nums)))