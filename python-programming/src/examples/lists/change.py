fruits = ['apple', 'banana', 'peach', 'strawberry']
print(fruits)      # ['apple', 'banana', 'peach', 'strawberry']
fruits[0] = 'orange'
print(fruits)      # ['orange', 'banana', 'peach', 'strawberry']

print(fruits[1:3]) # ['banana', 'peach']
fruits[1:3] = ['grape', 'kiwi']
print(fruits)      #  ['orange', 'grape', 'kiwi', 'strawberry']

print(fruits[1:3]) # ['grape', 'kiwi']
fruits[1:3] = ['mango']
print(fruits)      #  ['orange', 'mango', 'strawberry']

print(fruits[1:2]) # ['mango']
fruits[1:2] = ["banana", "peach"]
print(fruits)      # ['orange', 'banana', 'peach', 'strawberry']

print(fruits[1:1]) # []
fruits[1:1] = ['apple', 'pineapple']
print(fruits)      # ['orange', 'apple', 'pineapple', 'banana', 'peach', 'strawberry']
