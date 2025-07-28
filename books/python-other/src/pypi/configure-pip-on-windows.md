# Configure pip on Windows to avoid SSL issues


On the command line:

```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  PACKAGE_NAME
```

Run the following command to get the list of configuration files:

```
pip config -v list
```

You will see something like this: (your username instead of FooBar)

```
For variant 'global', will try loading 'C:\ProgramData\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\FooBar\pip\pip.ini'
For variant 'user', will try loading 'D:\Data\Users\FooBar\AppData\Roaming\pip\pip.ini'
For variant 'site', will try loading 'C:\Users\FooBar\AppData\Local\Programs\Python\Python310\pip.ini'
```

Create the first `pip.ini` file with the following content:

```
[global]
trusted-host = pypi.org files.pythonhosted.org pypi.python.org
```

If you run the `pip config -v list` again, you'll see an additional line on the output:
 
```
global.trusted-host='pypi.org, files.pythonhosted.org ,pypi.python.org'
```

`pip` will now disregard the SSL issues.


