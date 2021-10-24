import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} N")

def pascal(rows):
    row = []
    for current in range(0, rows):
        if row == []:
            next_row = [1]
        else:
            next_row = []
            temp_row = [0] + row + [0]
            for ix in range(len(temp_row)-1):
                next_row.append(temp_row[ix]+temp_row[ix+1])
        print(next_row)
        row = next_row

pascal(int(sys.argv[1]))
