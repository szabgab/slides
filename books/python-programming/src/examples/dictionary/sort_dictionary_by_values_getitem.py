scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
   'Abc' : 34,
}

# sort the keys according to the values:
sorted_names = sorted(scores, key=scores.__getitem__)

print(sorted_names) # ["Foo", "Bar", "Miu", "Abc"]

for k in sorted_names:
    print("{} : {}".format(k, scores[k]))

# Foo : 10
# Bar : 34
# Abc : 34
# Miu : 88
