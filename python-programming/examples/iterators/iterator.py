class Counter():
   def __init__(self):
       self.count = 0

   def __iter__(self):
       return self

   def __next__(self):
       self.count += 1
       return self.count

for c in Counter():
   print(c)
   if c > 10:
       break
