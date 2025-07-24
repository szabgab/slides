import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} N")

def get_next_row(row):
    if row == []:
        next_row = [1]
    else:
        next_row = []
        temp_row = [0] + row + [0]
        for ix in range(len(temp_row)-1):
            next_row.append(temp_row[ix]+temp_row[ix+1])
    return next_row

def get_triangle(rows):
    triangle = []
    row = []
    for current in range(0, rows):
        row = get_next_row(row)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(row)

triangle = get_triangle(int(sys.argv[1]))
print_triangle(triangle)
