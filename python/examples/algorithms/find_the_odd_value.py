def find_odd(values):
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
    '''
    if len(values) % 2 == 0:
        raise Exception("Number of elements must not be divisible by 2")
    start = 0
    end = len(values) - 1
    while True:
        if end - start < 2:
            return start
        if start > end:
            raise Exception("We have a problem")

        middle = start + int((end-start)/2)
        middle -= middle % 2
        if middle < 0:
            middle += 2
        #return middle
        if values[middle] == values[middle+1]:
            #return 'a'
            start = middle+2
        else:
            #return 'b'
            end = middle


# To verify run
# pytest --doctest-modules find_the_odd_value.py
