scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
}

print(scores) # {'Miu': 88, 'Foo': 10, 'Bar': 34}

sorted_names = sorted(scores) # "sort dictionary" sorts the keys
print(sorted_names)  # ['Bar', 'Foo', 'Miu']

sorted_keys = sorted(scores.keys())
print(sorted_keys)  # ['Bar', 'Foo', 'Miu']



