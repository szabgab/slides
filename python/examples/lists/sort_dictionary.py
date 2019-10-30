scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
}

print(scores) # {'Miu': 88, 'Foo': 10, 'Bar': 34}

sorted_names = sorted(scores)
print(sorted_names)  # ['Bar', 'Foo', 'Miu']
for s in sorted_names:
    print("{}  {}".format(s, scores[s]))

# sort the values, but we cannot get the keys back!
print(sorted(scores.values())) # [10, 34, 88]

print('')

# sort using a lambda expression
sorted_names = sorted(scores, key=lambda x: scores[x])
for k in sorted_names:
    print("{} : {}".format(k, scores[k]))

# Foo : 10
# Bar : 34
# Miu : 88

print('')

# sort the keys according to the values:
sorted_names = sorted(scores, key=scores.__getitem__)
for k in sorted_names:
    print("{} : {}".format(k, scores[k]))

# Foo : 10
# Bar : 34
# Miu : 88
