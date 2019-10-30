a = [2, 3, 93, 18]
b = [27, 81, 11, 35]
c = [32, 105, 1]

def calc(numbers):
    total  = 0
    for v in numbers:
        total += v
    return total, total / len(numbers)

total_a, avg_a = calc(a)
print("sum of a: {} average of a: {}".format(total_a, avg_a))

total_b, avg_b = calc(b)
print("sum of b: {} average of b: {}".format(total_b, avg_b))


total_c, avg_c = calc(c)
print("sum of c: {} average of c: {}".format(total_c, avg_c))
