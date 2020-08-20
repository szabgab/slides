fruits = ['apple', 'banana', 'peach', 'strawberry']
print(fruits)    # ['apple', 'banana', 'peach', 'strawberry']
fruits[0] = 'orange'
print(fruits)    # ['orange', 'banana', 'peach', 'strawberry']


fruits[1:3] = ['grape', 'kiwi']
print(fruits)    #  ['orange', 'grape', 'kiwi', 'strawberry']

fruits[1:3] = ['mango']
print(fruits)    #  ['orange', 'mango', 'strawberry']

fruits[1:2] = ["banana", "peach"]
print(fruits)    # ['orange', 'banana', 'peach', 'strawberry']
