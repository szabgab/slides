# deep copy list


{% embed include file="src/examples/modules/copy_list.py" %}

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
```

{% embed include file="src/examples/modules/shallow_copy_list.py" %}

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


{% embed include file="src/examples/modules/deep_copy_list.py" %}

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Joe', 'email': 'joe@examples.com'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


