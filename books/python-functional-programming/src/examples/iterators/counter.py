class Counter():
   def __init__(self):
       self.count = 0

   def __iter__(self):
       return self

   def __next__(self):
       self.count += 1
       if self.count > 3:
           raise StopIteration
       return self.count
