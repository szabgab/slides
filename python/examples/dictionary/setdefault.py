
grades = {}
# print(grades['basic'])              # KeyError: 'basic'
print(grades.get('python'))           # None
print(grades.get('python', 'snake'))  # snake
print(grades)                         # {}

print(grades.setdefault('perl'))      # None
print(grades)                         # {'perl': None}

print(grades.setdefault('python', 'snake')) # 'snake'
print(grades)                         # {'perl': None, 'python': 'snake'}

