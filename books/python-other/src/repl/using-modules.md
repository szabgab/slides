# Using Modules

* import
* sys
* version
* executable


Python has lots of standard (and not standard) modules. You can load one of them using the
`import` keyword. Once loaded, you can use functions from the module
or access its objects. For example the `sys` module has a `sys.version`
and a `sys.executable` variable.



```
>>> import sys
>>> sys.version
'2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]'
```

```
>>> sys.executable
'c:\\Python27\\python.exe'
```

You can also load specific object directly into your code.


```
>>> from sys import executable
>>> executable
'c:\\Python27\\python.exe'
```


To quit the interpreter call the `exit()` function.



```
>>> exit
Use exit() or Ctrl-Z plus Return to exit
```


The `import` binds the word sys to whatever it loaded from the file.

