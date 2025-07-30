# Add README file (setup.py)

In the setup.py add the following function:


```
def readme():
    with open('README.rst') as f:
        return f.read()
```


and in the setup() call include the following parameter:



```
      long_description=readme(),
```

This will display the README file when called at


```
$ python setup.py --long-description
```

