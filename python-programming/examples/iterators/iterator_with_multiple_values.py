class Counter():
   def __init__(self):
       self.count = 0

   def __iter__(self):
       return self

   def __next__(self):
       self.count += 1
       if self.count > 5:
           raise StopIteration
       return self.count, self.count ** 2

for cnt, sqr in Counter():
   print(f"{cnt}  {sqr}")

