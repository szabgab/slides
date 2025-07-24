names = ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']
print(names)                # ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']

print(names.remove('Kim'))  # None
print(names)                # ['Joe', 'Jane', 'Bob', 'Kim']

print(names.remove('George'))
   # Traceback (most recent call last):
   #   File "examples/lists/remove.py", line 9, in <module>
   #     print(names.remove('George'))  # None
   # ValueError: list.remove(x): x not in list
