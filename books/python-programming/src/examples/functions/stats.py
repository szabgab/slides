def stats(*numbers):
   total = 0

   average = None  # there might be better solutions here!
   minx = None
   maxx = None

   for val in numbers:
       total += val
       if minx == None:
           minx = maxx = val
       if minx > val:
           minx = val
       if maxx < val:
           maxx = val

   if len(numbers):
       average = total / len(numbers)


   return total, average, minx, maxx


ttl, avr, smallest, largest = stats(3, 5, 4)

print(ttl)
print(avr)
print(smallest)
print(largest)

