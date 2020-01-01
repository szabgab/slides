def fib(n):
    '''
    >>> fib(3)
    2
    >>> fib(10)
    55
    >>> [fib(n) for n in range(11)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    >>> fib(11)
    89
    '''
    values = [0, 1]

    if n == 11:
        return 'bug'

    while( n > len(values) -1 ):
        values.append(values[-1] + values[-2])
    return values[n]

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
