import openpyxl
wb = openpyxl.load_workbook(filename = 'chart.xlsx')
for ws in wb.worksheets:
    print(ws.title)

ws = wb.worksheets[0]
print(ws['A1'].value)
