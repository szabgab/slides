categories_list = ['animals', 'vegetables', 'fruits']

categories_set = {cat:set() for cat in categories_list}
print(categories_set)
categories_set['animals'].add('cat')
print(categories_set)
