scores = {
   'Foo' : 10,
   'Bar' : 34,
   'Miu' : 88,
   'Abc' : 34,
}

print(scores) # {'Miu': 88, 'Foo': 10, 'Bar': 34, 'Abc': 34}

sorted_names = sorted(scores) # "sort dictionary" sorts the keys
print(sorted_names)  # ['Bar', 'Foo', 'Miu', 'Abc']

sorted_keys = sorted(scores.keys())
print(sorted_keys)  # ['Abc', 'Bar', 'Foo', 'Miu']



