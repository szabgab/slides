import sys

file_a = 'map_string_to_len.py'
file_b = 'map_row_to_length.py'

def compare(row_a, row_b):
    a = row_a.find(' ')
    b = row_b.find(' ')
    return a < b

with open(file_a) as fh_a, open(file_b) as fh_b:
    results = map(compare, fh_a, fh_b)
    print(results)
    print(sys.getsizeof(results))

    truth = list(results)
    print(truth)
    print(sys.getsizeof(truth))
