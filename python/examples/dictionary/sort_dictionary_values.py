scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
}

# sort the values, but we cannot get the keys back!
sorted_values = sorted(scores.values())
print(sorted_values) # [10, 34, 88]
