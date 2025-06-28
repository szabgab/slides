students = [
    ('John', 'A', 2),
    ('Zoro', 'C', 1),
    ('Dave', 'B', 3),
]
print(students)
  # [('John', 'A', 2), ('Zoro', 'C', 1), ('Dave', 'B', 3)]

print(sorted(students))
  # [('Dave', 'B', 3), ('John', 'A', 2), ('Zoro', 'C', 1)]
  # sort by the first element of each tuple

print(sorted(students, key=lambda s : s[1]))
  # [('John', 'A', 2), ('Dave', 'B', 3), ('Zoro', 'C', 1)]
  # sort by the 2nd element of the tuples (index 1)

print(sorted(students, key=lambda s : s[2]))
  # [('Zoro', 'C', 1), ('John', 'A', 2), ('Dave', 'B', 3)]
  # sort by the 3rd element of the tuples (index 2)


from operator import itemgetter
print(sorted(students, key=itemgetter(2)))
  # [('Zoro', 'C', 1), ('John', 'A', 2), ('Dave', 'B', 3)]
  # maybe this is more simple than the lambda version
  # and probably faster
