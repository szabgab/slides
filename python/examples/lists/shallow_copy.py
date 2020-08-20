x = ['apple', ['cat', 'dog'], 'banana']
print(x)        # ['apple', ['cat', 'dog'], 'banana']
print(x[0])     # apple
print(x[1][0])  # cat

y = x[:]

x[0] = 'kiwi'
x[1][0] = 'mouse'

print(x)    # ['kiwi', ['mouse', 'dog'], 'banana']
print(y)    # ['apple', ['mouse', 'dog'], 'banana']