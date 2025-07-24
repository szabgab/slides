# Argparse argument with default and optional value


* nargs
* const

* Instead of `default` we use the `const` parameter here
* We tell argparse that the value of the parameter is optional by `nargs='?'`

{% embed include file="src/examples/argparse/argument_with_optional_value.py" %}

```
$ python argument_with_optional_value.py
None
```

```
$ python argument_with_optional_value.py --level
10
```

```
$ python argument_with_optional_value.py --level 20
20
```



