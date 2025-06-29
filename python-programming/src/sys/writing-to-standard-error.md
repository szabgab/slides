# Writing to standard error (stderr)

* stdout
* stderr
* write

{% embed include file="src/examples/sys/stderr.py" %}


Redirection (Works on Linux/Mac/Windows):

```
python stderr.py > out.txt  2> err.txt
python stderr.py > all.txt 2>&1

python stderr.py 2> /dev/null            # On Linux and OSX
python stderr.py 2> nul                  # On Windows
```


