scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
}

# sort using a lambda expression
sorted_names = sorted(scores, key=lambda x: scores[x])

print(sorted_names) # ["Foo", "Bar", "Miu"]

for k in sorted_names:
    print("{} : {}".format(k, scores[k]))

# Foo : 10
# Bar : 34
# Miu : 88



