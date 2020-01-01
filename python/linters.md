# Linters
{id: python-linters}

## Static Code Analyzis - Linters
{id: linters}

* PEP8
* Flake8
* Pylint



## PEP8
{id: pep8}

```
pip install pep8
```

* [pep8](https://pep8.readthedocs.io/en/release-1.7.x/intro.html)
* [pep8](https://pypi.org/project/pytest-pep8/)



## F811 - redefinition of unused
{id: flake8-f811}
![](examples/linters/importer.py)

```
$ flake8 importer.py
importer.py:4:1: F811 redefinition of unused 'datetime' from line 2
```


## Warn when Redefining functions
{id: warn-when-redefining-functions}
![](examples/linters/redef.py)
![](examples/linters/redef.out)





