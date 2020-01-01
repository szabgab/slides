data = {
    'a': [2, 3, 93, 18],
    'b': [27, 81, 11, 35],
    'c': [32, 105, 1],
}

def calc(numbers):
    total  = 0
    for v in numbers:
        total += v
    return total, total / len(numbers)

total = {}
avg   = {}
for name, numbers in data.items():
   total[name], avg[name] = calc(numbers)
   print("sum of {}: {} average of {}: {}".format(name, total[name], name, avg[name]))

