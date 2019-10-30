n = 50

nums = range(2, n)
for i in range(2, 1+int(n ** 0.5)):
    nums = filter(lambda x: x == i or x % i, nums)

print(nums)
