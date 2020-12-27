numbers = [1, 3, 27, 10, 38]
def big(n):
    return n > 10

big_numbers = []
for num in numbers:
    if big(num):
        big_numbers.append(num)
print(big_numbers)
