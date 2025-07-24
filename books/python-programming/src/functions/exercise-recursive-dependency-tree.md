# Exercise: recursive dependency tree


* Create a file called **recursive_dependency_tree.py**

Give a bunch of files that has list of requirement in them.
Process them recursively and print the resulting full list of requirements

{% embed include file="src/examples/functions/dependencies/a.txt" %}
{% embed include file="src/examples/functions/dependencies/b.txt" %}
{% embed include file="src/examples/functions/dependencies/c.txt" %}

```
$ python traversing_dependency_tree.py a

Processing a
Processing b
Processing e
Processing d
Processing c
Processing f
Processing g
Processing d
```


