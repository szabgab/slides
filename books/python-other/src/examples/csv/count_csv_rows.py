import csv
import sys
from collections import defaultdict

def check_rows(filename):
    rows = []
    widthes = defaultdict(int)
    with open(filename) as fh:
        rd = csv.reader(fh, delimiter=';')
        for row in rd:
            width = len(row)
            rows.append(width)
            widthes[width] += 1

    #print(widthes)
    if len(widthes.keys()) > 1:
        print("Not all the rows have the same number of cells")
        cell_counts = sorted(widthes.keys(), key=lambda x: widthes[x], reverse=True)
        print(f"Most common number of cells is {cell_counts[0]} with {widthes[ cell_counts[0] ]} rows")
        for count in cell_counts[1:]:
            print(f"  Cells: {count}")
            print(f"  Rows:")
            for row, cells in enumerate(rows):
                if cells == count:
                    print(f"    {row}")
    else:
        values = list(widthes.values())
        print(f"All rows have the same number of cells: {values[0]}")

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

check_rows(filename)


