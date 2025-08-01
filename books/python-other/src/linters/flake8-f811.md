# F811 - redefinition of unused

* flake8

{% embed include file="src/examples/linters/importer.py" %}

```
$ flake8 importer.py
importer.py:4:1: F811 redefinition of unused 'datetime' from line 2
```


