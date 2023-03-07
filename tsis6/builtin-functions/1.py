def product(nums):
  res=1
  for number in nums:
    res = res*number
  return res
    

list = list(map(int, input().split()))

print(product(list))
