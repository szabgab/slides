import matplotlib.pyplot as plt

cases = {
    'success': 38,
    'failure': 7,
    'skipped': 3,
    'xfailed': 8,
    'xpassed': 4,
}

explode = (0, 0.1, 0.1, 0.1, 0.1)
labels = cases.keys()
sizes = cases.values()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.tight_layout()
plt.show()
#plt.savefig('pie_for_tests.png')

