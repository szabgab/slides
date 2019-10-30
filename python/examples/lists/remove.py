names = ['abc', 'def', 'qqrq', 'moo', 'def']
print(names)                # ['abc', 'def', 'qqrq', 'moo', 'def']

print(names.remove('def'))  # None
print(names)                # ['abc', 'qqrq', 'moo', 'def']

print(names.remove('zorg'))
   # Traceback (most recent call last):
   #   File "examples/lists/remove.py", line 9, in <module>
   #     print(names.remove('zorg'))  # None
   # ValueError: list.remove(x): x not in list
