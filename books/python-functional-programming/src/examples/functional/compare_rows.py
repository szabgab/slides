import sys
if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILE FILE")

file_a, file_b = sys.argv[1:]

def compare(row_a, row_b):
    a = row_a.find(' ')
    b = row_b.find(' ')
    return a < b

with open(file_a) as fh_a, open(file_b) as fh_b:
    results = map(compare, fh_a, fh_b)
    print(results)

    for res in results:
        print(res)
