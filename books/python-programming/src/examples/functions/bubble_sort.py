
def bubble_sort(*values):
    values = list(values)
    for ix in range(len(values)-1):
        for jx in range(len(values)-1-ix):
            if values[jx] > values[jx+1]:
                values[jx], values[jx+1] = values[jx+1], values[jx]
    return values

print(bubble_sort(1, 2, 3))
print(bubble_sort(3, 2, 1))
print(bubble_sort(10, 9, 8, 7, 6, 5, 4, 3, 2, 1))

