import openpyxl
import sys

if len(sys.argv) !=2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

in_file = sys.argv[1]

wb = openpyxl.load_workbook(filename = in_file)
for ws in wb.worksheets:
    print(ws.title)

ws = wb.worksheets[0]
print(ws['A1'].value)
