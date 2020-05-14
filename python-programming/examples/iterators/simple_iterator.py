from collections.abc import Iterator, Iterable

class Counter():
   def __init__(self):
       self.count = 0

   def __iter__(self):
       return self

   def __next__(self):
       self.count += 1
       if self.count > 5:
           raise StopIteration
       return self.count

for c in Counter():
   print(c)


print()
cnt = Counter()
print(cnt.__class__.__name__)
print(issubclass(cnt.__class__, Iterator))
print(issubclass(cnt.__class__, Iterable))
