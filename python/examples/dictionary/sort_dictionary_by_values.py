scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
   'Abc' : 34,
}

# sort using a lambda expression
sorted_names = sorted(scores, key=lambda x: scores[x])

print(sorted_names) # ["Foo", "Bar", "Abc", "Miu"]

for k in sorted_names:
    print("{} : {}".format(k, scores[k]))

# Foo : 10
# Bar : 34
# Abc : 34
# Miu : 88

