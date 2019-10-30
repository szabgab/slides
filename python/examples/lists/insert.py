words = ['apple', 'banana', 'cat']
print(words)  # ['apple', 'banana', 'cat']

words.insert(2, 'zebra')
print(words)  # ['apple', 'banana', 'zebra', 'cat']

words.insert(0, 'dog')
print(words)  # ['dog', 'apple', 'banana', 'zebra', 'cat']

words.insert(len(words), 'olifant')
print(words)  # ['dog', 'apple', 'banana', 'zebra', 'cat', 'olifant']

