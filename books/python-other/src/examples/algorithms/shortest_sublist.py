def shortest(numbers, limit):
    '''
    >>> shortest([], 7)
    -1
    >>> shortest([2, 3], 7)
    -1
    >>> shortest([2, 3], 0)
    0
    >>> shortest([], 0)
    0
    >>> shortest([7, 3], 7)
    1
    >>> shortest([4, 7, 3], 7)
    1
    >>> shortest([1, 23, 1, 1, 10, 11, 12], 30)
    3
    >>> shortest([1, 23, 1, 1, 10, 11, 12], 24)
    2
    >>> shortest([1, 10, 11, 40], 30)
    1
    '''
    if limit == 0:
        return 0
    length = None
    start = 0
    end = -1
    total = 0
    while True:
        #start < len(numbers) and end <= len(numbers) and start < end:
        if total >= limit:
            if length is None:
                length = 1 + end-start
            else:
                length = min(length, 1 + end-start)

            total -= numbers[start]
            start += 1
            if start > end:
                break
        else:
            end += 1
            if end >= len(numbers):
                break
            total += numbers[end]

    return -1 if length is None else length


# To verify run
# pytest --doctest-modules shortest_sublist.py
