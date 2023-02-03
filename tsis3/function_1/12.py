def histogram(nums):
    for i in nums:
        print("*"*i)


list = list(map(int, input().split()))

histogram(list)