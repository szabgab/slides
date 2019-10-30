a_queue = ['Foo', 'Bar']
print(a_queue)   # ['Foo', 'Bar']

a_queue.append('Moo')
print(a_queue)   # ['Foo', 'Bar', 'Moo']

first = a_queue.pop(0)
print(first)     # 'Foo'
print(a_queue)   # ['Bar', 'Moo']
