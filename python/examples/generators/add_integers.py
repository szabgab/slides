from series import integers

def mysum(nums):
    print(nums)
    total = 0
    for n in nums:
        total += n
    return total

n3 = integers(3)
n7 = integers(7)
d = ( mysum(p) for p in zip(n3, n7) )

print("start")
for i in d:
    print(i)
    if i >= 20:
        break
