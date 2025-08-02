# Lists

```python
fruits = ['apple', 'banana', 'peach', 'pear']
fruits[2]
fruits[1:3]
fruits[::2]
fruits[:]

len(fruits)

import copy
copy.copy(fruits)     # shallow copy
copy.deepcopy(fruits)

element in some_list
if element in some_list:
    print('in')

fruits.index(sub)  # return location or raises Exception

fruits.insert(location, anothe_fruit)
fruits.append(another_fruit)
fruits.remove(some_fruit)   # remove by value
fruits.pop(location)        # remove by location
list()

fruits.sort()
sorted(fruits)
```


