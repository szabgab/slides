def iterative_bubble_sort(data):
    data = data[:]
    for end in (range(len(data)-1, 0, -1)):
        for i in range(end):
            if data[i] < data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data

old = [1, 5, 2, 4, 8]
new = iterative_bubble_sort(old)
print(old)
print(new)
