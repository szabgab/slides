import openpyxl
import random
from openpyxl.chart import BarChart, Series, Reference

wb = openpyxl.Workbook()
ws = wb.active

randomList1 = []
randomList2 = []
randomList3 = []
randomList4 = []

for i in range(0,12):
    randomList1.append(random.randint(0,100))
    randomList2.append(random.randint(0, 100))
    randomList3.append(random.randint(0, 100))
    randomList4.append(random.randint(0, 100))
randomList1.insert(0,"Bananas")
randomList2.insert(0,"Pears")
randomList3.insert(0,"Apples")
randomList4.insert(0,"Kiwis")

print(f"""Random number list1: {randomList1}
        Random number list2: {randomList2}
        Random number list3: {randomList3}
        Random number list4: {randomList4}""")

months = ['Fruit','Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

rows = [
    months,
    randomList1,
    randomList2,
    randomList3,
    randomList4,
]

for row in rows:
    ws.append(row)

chart1 = BarChart()
chart1.type = "col"
chart1.style = 12
chart1.title = "Fruit Count per Month"
chart1.y_axis.title = 'Fruit Number'
chart1.x_axis.title = 'Fruit Type'

data = Reference(ws, min_col=2, min_row=1, max_row=5, max_col=13)
cats = Reference(ws, min_col=1, min_row=2, max_row=5)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
chart1.shape = 4
ws.add_chart(chart1, "A11")

wb.save("row_10.xlsx")