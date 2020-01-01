from itertools import groupby

def groupby_even_odd(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    gb = groupby(items, f)
    print(gb)
    for k, items in gb:
        print('{}: {}'.format(k, ','.join(map(str, items))))

groupby_even_odd([1, 3, 4, 5, 6, 8, 9, 11])


