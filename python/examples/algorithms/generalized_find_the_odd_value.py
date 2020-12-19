def find_odd(values, size=2):
    '''
    >>> find_odd(['c'])
    0
    >>> find_odd(['c', 'x', 'x'])
    0
    >>> find_odd(['x', 'x', 'c'])
    2
    >>> find_odd(['x', 'x', 'c', 'y', 'y'])
    2
    >>> find_odd(['a', 'a', 'b', 'b', 'd', 'd', 'x', 'x', 'c', 'y', 'y'])
    8
    >>> find_odd(['a', 'a', 'c', 'b', 'b', 'd', 'd', 'x', 'x', 'y', 'y'])
    2

    >>> find_odd(['c'], 3)
    0
    >>> find_odd(['c', 'd'], 3)
    0
    >>> find_odd(['c', 'x', 'x', 'x'], 3)
    0
    >>> find_odd(['c', 'd', 'x', 'x', 'x'], 3)
    0
    >>> find_odd(['x', 'x', 'x', 'c', 'd'], 3)
    3
    >>> find_odd(['x', 'x', 'x', 'c', 'd', 'y', 'y', 'y'], 3)
    3
    >>> find_odd(['a', 'a', 'a', 'b', 'b', 'b', 'd', 'd', 'd', 'x', 'x', 'x', 'c', 'y', 'y', 'y'], 3)
    12
    >>> find_odd(['a', 'a', 'a', 'b', 'b', 'b', 'd', 'd', 'd', 'x', 'x', 'x', 'c', 'q', 'y', 'y', 'y'], 3)
    12
    >>> find_odd(['a', 'a', 'a', 'c', 'b', 'b', 'b', 'd', 'd', 'd', 'x', 'x', 'x', 'y', 'y', 'y'], 3)
    3
    >>> find_odd(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'z', 'd', 'd', 'd', 'x', 'x', 'x', 'y', 'y', 'y'], 3)
    6
    '''
    if len(values) % size == 0:
        raise Exception(f"Number of elements must not be divisible by {size}")
    start = 0
    end = len(values) - 1
    while True:
        if end - start < size:
            return start
        if start > end:
            raise Exception("We have a problem")

        middle = start + int((end-start)/size)
        middle -= middle % size
        if middle < 0:
            middle += size
        #return middle
        if all(map(lambda val: values[middle] == val, values[middle+1:middle+size])):
            #return f'a {middle}'
            start = middle+size
        else:
            end = middle


# To verify run
# pytest --doctest-modules generalized_find_the_odd_value.py
