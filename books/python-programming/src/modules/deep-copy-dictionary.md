# deep copy dictionary

{% embed include file="src/examples/modules/copy_dictionary.py" %}

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
```

* [deepcopy](https://docs.python.org/library/copy.html#copy.deepcopy" %}


{% embed include file="src/examples/modules/deep_copy_dictionary.py" %}

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 70, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George']}
```


