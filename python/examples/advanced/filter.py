numbers = [1, 3, 27, 10, 38]

reduced = filter(lambda n: n > 10, numbers)
print(reduced)       # <filter object at 0x7fcc257b99b0>
print(list(reduced)) # [27, 38]
