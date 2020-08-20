words = "ab:cd::ef".split(':')
print(words)   # ['ab', 'cd', '', 'ef']

# special case: split by spaces
names = "foo   bar baz".split()
print(names)   # ['foo', 'bar', 'baz']

# special case: split to characters
chars = list("ab cd")
print(chars)   # ['a', 'b', ' ', 'c', 'd']
