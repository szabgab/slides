fruits = ['orange', 'mango', 'strawberry']

print(fruits[1]) # mango
fruits[1] = ["banana", "peach"]
print(fruits)    # ['orange', ['banana', 'peach'], 'strawberry']
print(fruits[1]) # ['banana', 'peach']
print(fruits[2]) # strawberry

print(fruits[1][0]) # banana

