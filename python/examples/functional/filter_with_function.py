numbers = [1, 3, 27, 10, 38]
def big(n):
    return n > 10

big_numbers = filter(big, numbers)
print(big_numbers)
print(list(big_numbers))
