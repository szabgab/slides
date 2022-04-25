categories_list = ['animals', 'vegetables', 'fruits']

categories_dict = {cat:[] for cat in categories_list}
print(categories_dict)
categories_dict['animals'].append('cat')
print(categories_dict)

