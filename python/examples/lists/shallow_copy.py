fruits = ['apple', ['banana', 'peach'], 'kiwi']
print(fruits)        # ['apple', ['banana', 'peach'], 'kiwi']
print(fruits[0])     # apple
print(fruits[1][0])  # banana

salad = fruits[:]

fruits[0] = 'orange'
fruits[1][0] = 'mango'

print(fruits)  # ['orange', ['mango', 'peach'], 'kiwi']
print(salad)   # ['apple', ['mango', 'peach'], 'kiwi']

