from functools import reduce

grades = [
    {
        'subject': 'math',
        'grade': 97,
    },
    {
        'subject': 'chemistry',
        'grade': 60,
    },
    {
        'subject': 'grammar',
        'grade': 75,
    }
]

print(reduce(lambda x,y: x+y, map(lambda s: s['grade'], grades))) # 232

print(reduce(lambda acc,y: acc+y['grade'], grades, 0)) #232
