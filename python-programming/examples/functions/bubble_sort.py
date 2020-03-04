

def recursive_bubble_sort(data):
    data = data[:]
    if len(data) == 1:
        return data

    last = data.pop()
    sorted_data = recursive_bubble_sort(data)
    for i in range(len(sorted_data)):
        if last > sorted_data[i]:
            sorted_data.insert(i, last)
            break
    else:
        sorted_data.append(last)
    return sorted_data

def iterative_bubble_sort(data):
    data = data[:]
    for end in (range(len(data)-1, 0, -1)):
        for i in range(end):
            if data[i] < data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


old = [1, 5, 2, 4, 8]
new1 = recursive_bubble_sort(old)
new2 = iterative_bubble_sort(old)
print(old)
print(new1)
print(new2)
